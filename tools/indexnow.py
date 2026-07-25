#!/usr/bin/env python3
"""IndexNow へURLを送信して、Bing系のインデックスを即時更新させる。

なぜ必要か: ChatGPTの検索グラウンディングはBingのインデックスに強く依存している
（OpenAI公式がBingをサードパーティ検索プロバイダとして明記／実測でも引用の大半がBing上位と一致）。
Googleは自前のクロールで十分速いが、Bing側は放置すると反映が遅い。IndexNowで公開直後に
通知しておくと、ChatGPT・Copilot・Perplexityが最新の内容を拾える状態になる。

キーは自己発行（Bing Webmaster Tools のアカウント不要）。
public/<KEY>.txt に同じ文字列を置くことで所有証明になる。

使い方:
    python3 tools/indexnow.py                # 本番のsitemapから全URLを送信
    python3 tools/indexnow.py <URL> [<URL>…]  # 指定URLだけ送信（記事公開時など）
    python3 tools/indexnow.py --dry-run       # 送信せず対象URLを表示
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request

KEY = "13cedb6977af8923f843dbfdf8bd69a615385400c8cb0edd"
HOST = "wiztrydx.com"
SITEMAP = f"https://{HOST}/sitemap-0.xml"
# api.indexnow.org へ送ると参加検索エンジン（Bing・Yandex・Seznam・Naver等）へ共有される
ENDPOINT = "https://api.indexnow.org/indexnow"
UA = "WizTry-IndexNow/1.0 (+https://wiztrydx.com/)"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as res:
        return res.read()


def urls_from_sitemap() -> list[str]:
    xml = fetch(SITEMAP).decode("utf-8")
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def submit(urls: list[str]) -> int:
    """IndexNowへ一括送信し、HTTPステータスを返す。1リクエスト最大10,000件。"""
    body = json.dumps(
        {"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls},
        ensure_ascii=False,
    ).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            return res.status
    except urllib.error.HTTPError as e:
        # 422 = URLとキーの不一致、403 = キーファイルが見つからない など。原因が分かるよう本文も出す
        print(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}", file=sys.stderr)
        return e.code


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv[1:]

    urls = args or urls_from_sitemap()
    if not urls:
        print("送信対象URLがありません", file=sys.stderr)
        return 1

    print(f"対象 {len(urls)} 件:")
    for u in urls:
        print(f"  {u}")
    if dry:
        print("--dry-run のため送信しません")
        return 0

    status = submit(urls)
    # IndexNowは200（受理）と202（受理・キー検証待ち）をどちらも成功として返す
    if status in (200, 202):
        print(f"送信成功 (HTTP {status}) — {len(urls)} 件")
        return 0
    print(f"送信失敗 (HTTP {status})", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
