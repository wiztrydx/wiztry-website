# WizTry株式会社 公式サイト

Astro 5製の静的コーポレートサイト。ホスティングはCloudflare Pages（予定）、ドメインは wiztrydx.com。

## 更新の運用

**このサイトの更新はAI社員（Claude）経由で行う。** 「ブログ記事を書いて」「実績ロゴを追加して」等を依頼すれば、編集→ビルド→デプロイまで実行される。

- 数字・社名・掲載ロゴなどの共通データ: `src/data/site.ts`
- ブログ記事: `src/content/blog/*.md`（frontmatter: title / description / pubDate / tag / thumb）
- ページ本体: `src/pages/`
- デザインシステム: `src/styles/global.css`（ネイビー×クリーン。色はCSS変数）
- 全ページ共通の枠: `src/layouts/Base.astro`
- ページ仕様・コピーの正本: `SPEC.md`

## コマンド

```sh
npm run dev      # 開発サーバー (localhost:4321)
npm run build    # 本番ビルド → dist/
npm run preview  # ビルド結果の確認
```

## 画像生成のルール（2026-07-10 代表指示）

生成モデルの優先順位は **①GPT-Image-2 → ②Nano Banana 2（gemini-3.1-flash-image）→ ③Nano Banana Pro（gemini-3-pro-image）**。上位が失敗したときのみ下位へフォールバックする。実装は `tools/imagegen.py`（全生成スクリプトはこれを経由すること）。

- APIキー: `~/.config/wiztry/image-gen.env`（OPENAI_API_KEY / GEMINI_API_KEY）
- サムネ生成: `tools/gen_thumbs.py` ＋ `tools/thumbs_config.json`（mainの `|` は改行位置指定）
- 文字入り生成は**必ず目視で誤字チェック**し、NGならそのslugだけ再生成する

## 素材

- `public/logos/` — WizTryロゴ（黒/白抜き）、ファビコン用マーク
- `public/clients/` — クライアント企業ロゴ19社（掲載許可はDrive「WizTry ホームページ/ロゴデータ/ロゴ一覧シート」で管理）
- `public/photos/` — 研修・セミナー・オフィス写真（Drive「写真素材」「SNS用写真・動画素材」から選別・WebP化済み）
- 元データ: `assets-raw/`（git管理外）

## お問い合わせフォーム

FormSubmit.co を使用し info@wiztrydx.com へ送信される。**初回送信時にFormSubmitからアクティベーションメールが届くので、リンクを1回クリックして有効化が必要。**

## 注意事項

- 「No.1」等の最上級表現は景表法対応のため使用しない（数字ベースの表現を使う）
- 実績数字（累計90社以上・満足度4.8）の出典は代表確認（2026-07-10）。更新時は `src/data/site.ts` を修正
