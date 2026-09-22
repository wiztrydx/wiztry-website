---
title: "Claude Opus 5.5とGPT-6の違い｜仕事別の選び方"
description: "Claude Opus 5.5とGPT-6 Sol・Lunaが同じ日に登場。GPT-6 Astraとの関係、API料金、使える場所、会社の仕事での選び方を整理します。自社の資料を使って比較する3つの手順と、そのまま使える依頼文も紹介します。"
pubDate: 2026-09-23T08:00:00
tag: "AI最新動向"
thumb: "/thumbs/opus-5-5-gpt-6-erabikata.webp"
---

「ClaudeもGPTも新型が出た。結局、会社ではどれを使えばいいの？」。発表が重なると、モデル名を覚えるだけで疲れてしまいます。

結論から言うと、まず比べるべきなのはAIの順位ではなく、自社の仕事を一件終えるまでの手間と費用です。今回はそこまで判断できるよう、発表内容を実務に引き寄せて整理します。

## 同日に出たのは何か。GPT-6は3種類ある

2026年9月22日、AnthropicはClaude Opus 5.5を発表しました。同じ日にOpenAIが発表したのは、GPT-6 Sol（ソル）とGPT-6 Luna（ルナ）です。GPT-6 Astra（アストラ）は9月3日に先行して発表されています。つまり「GPT-6」と一括りにすると、価格も役割も違う3種類が混ざります。[Anthropicの発表](https://www.anthropic.com/claude-opus-5-5)と[OpenAIの9月22日の発表](https://openai.com/index/introducing-gpt-6-sol-and-luna/)で確認できます。

<figure class="blog-diagram blog-diagram--timeline">
  <figcaption><span class="blog-diagram__eyebrow">図解 01｜発表の順番</span><strong>同じ日に出たのは、Opus 5.5 と Sol・Luna</strong></figcaption>
  <ol class="blog-diagram__timeline">
    <li><span class="blog-diagram__date">9月3日</span><div class="blog-diagram__event"><span>OpenAI</span><strong>GPT-6 Astra</strong><small>先に登場した最上位モデル</small></div></li>
    <li><span class="blog-diagram__date">9月22日</span><div class="blog-diagram__launches"><div class="blog-diagram__event"><span>Anthropic</span><strong>Claude Opus 5.5</strong><small>Claudeの新モデル</small></div><div class="blog-diagram__event"><span>OpenAI</span><strong>GPT-6 Sol・Luna</strong><small>GPT-6に加わった2モデル</small></div></div></li>
  </ol>
</figure>

会社の人にたとえるなら、難しい案件を深く考える担当、幅広い仕事を任せる担当、大量の定型作業を素早くこなす担当がいるイメージです。ただし、実際の成果は依頼内容と使う道具にも左右されます。

| モデル | 発表上の位置づけ | 最初に試したい仕事 |
| --- | --- | --- |
| Claude Opus 5.5 | Claudeの高性能モデル。文章や開発、調査など複雑な仕事を想定 | 提案書の論点整理、複数資料の照合、開発作業 |
| GPT-6 Astra | GPT-6の最上位モデル。複雑な仕事を最初から最後まで扱う設計 | 複数のアプリをまたぐ難しい作業、重要資料の作成 |
| GPT-6 Sol | Astraより費用を抑えた、幅広い実務向けのモデル | 資料の下書き、表の分析、日常的な開発作業 |
| GPT-6 Luna | 低価格で大量処理を想定したモデル | 問い合わせの分類、短い要約、定型文の草案 |

この表は公式説明から考えた「試す順番」です。用途ごとの勝敗を実測した結果ではありません。

## 料金は「月額」と「使った分」を分けて見る

普段のClaudeやChatGPTの画面で使う場合は、契約プランと利用上限を確認します。下の数字は、自社のシステムからAIを呼び出す「API」の従量料金です。月額料金とは別物です。単位の「100万トークン」は、AIが処理する文章量を数える単位だと思ってください。

| モデル | 入力100万トークン | 出力100万トークン |
| --- | ---: | ---: |
| Claude Opus 5.5 | 4米ドル | 20米ドル |
| GPT-6 Astra | 10米ドル | 50米ドル |
| GPT-6 Sol | 2米ドル | 10米ドル |
| GPT-6 Luna | 0.10米ドル | 0.50米ドル |

出典は[Claude Opus 5.5の料金表](https://www.anthropic.com/claude-opus-5-5)、[GPT-6 Astraのモデル仕様](https://developers.openai.com/api/docs/models/gpt-6-astra)、[GPT-6 Sol・Lunaの料金表](https://openai.com/index/introducing-gpt-6-sol-and-luna/)です。2026年9月23日時点の標準的なAPI単価で、税金、為替、検索などの道具の料金、割引は含みません。

たとえば「資料を10万トークン読み、回答を2万トークン書く」一回の作業なら、単純計算でOpus 5.5は0.80米ドル、Astraは2.00米ドル、Solは0.40米ドル、Lunaは0.02米ドルです。同じ品質になるという意味ではありません。安いモデルで修正を何度も繰り返せば、時間も費用も増えます。

<figure class="blog-diagram blog-diagram--cost">
  <figcaption><span class="blog-diagram__eyebrow">図解 02｜API料金の計算例</span><strong>入力10万・出力2万トークンなら</strong></figcaption>
  <ol class="blog-diagram__bars">
    <li><span>GPT-6 Astra</span><span class="blog-diagram__track"><i style="width:100%"></i></span><strong>2.00ドル</strong></li>
    <li><span>Claude Opus 5.5</span><span class="blog-diagram__track"><i style="width:40%"></i></span><strong>0.80ドル</strong></li>
    <li><span>GPT-6 Sol</span><span class="blog-diagram__track"><i style="width:20%"></i></span><strong>0.40ドル</strong></li>
    <li><span>GPT-6 Luna</span><span class="blog-diagram__track"><i style="width:1%"></i></span><strong>0.02ドル</strong></li>
  </ol>
  <p class="blog-diagram__note">標準API単価だけの試算です。使える機能や仕上がりの品質を表す図ではありません。</p>
</figure>

Anthropicが説明する「Opus 5より典型的な作業で40％安い」も、入力単価が40％下がったという意味ではありません。単価の引き下げに加え、一件の作業で使う文章量が減ることを含む同社の試算です。

## 点数だけでは決められない理由

両社の発表には性能を示すテスト結果が並びます。ここで気をつけたいのは、同じ「パソコンを操作する仕事」でも、用意された道具、考える時間、安全設定、採点方法が違えば点数も変わることです。各社の発表値を横に並べるだけで、あなたの会社の業務でも同じ順番になるとは言えません。

さらに、AIが「終わりました」と報告しても、元資料の数字が抜けていたり、変更してはいけない箇所まで直していたりします。これは高性能モデルでも起こり得ます。確認すべきは、答えの流暢さより、仕事の完了条件を守ったかどうかです。

正直なところ、公開直後の時点で「どちらが全業務で上」と断言できる材料はありません。なので、私は次のように考えています。公開された点数は候補を絞る材料にして、最終判断は自社の仕事で行うのが確実です。

## 明日からできる、社内での比較3ステップ

まず一点目。いつも発生する仕事を一つ選びます。たとえば「商談メモから、お客様への提案書の骨子を作る」「20件の問い合わせを担当別に仕分ける」です。機密情報は自社の利用規程と契約を確認し、比較用には匿名化した資料を使ってください。

二点目。元資料、依頼文、完成条件をそろえて、使えるモデル二つに同じ仕事を頼みます。提案書なら「元資料にない金額を足さない」「不明点を列挙する」「1ページで読める構成にする」。仕分けなら「分類理由を一行で示す」「判断できないものは保留にする」といった条件です。

<figure class="blog-diagram blog-diagram--workflow">
  <figcaption><span class="blog-diagram__eyebrow">図解 03｜社内での比べ方</span><strong>条件をそろえて、仕事の結果を見る</strong></figcaption>
  <div class="blog-diagram__input"><span>共通の入力</span><strong>同じ資料 ＋ 同じ依頼文 ＋ 同じ完成条件</strong></div>
  <div class="blog-diagram__split" aria-hidden="true">↓</div>
  <div class="blog-diagram__models"><div><span>モデル A</span><strong>仕事を依頼</strong></div><div><span>モデル B</span><strong>同じ仕事を依頼</strong></div></div>
  <div class="blog-diagram__split" aria-hidden="true">↓</div>
  <div class="blog-diagram__review"><strong>人が4項目で確認</strong><div><span>完成度</span><span>手直し</span><span>速さ</span><span>費用</span></div></div>
  <p class="blog-diagram__note">1件だけで決めず、同じ種類の仕事を3件ほど試します。</p>
</figure>

三点目。担当者が次の四つを数えます。

| 確認項目 | 見るもの |
| --- | --- |
| 完成度 | 条件を満たした件数、抜けや誤りの件数 |
| 手直し | 人が修正に使った分数 |
| 速さ | 依頼から、確認できる成果物になるまでの時間 |
| 費用 | API料金、または契約プラン内で使える回数 |

一回だけでは偶然もあります。同じ種類の仕事を3件ほど試し、特に間違えやすい事例を一つ混ぜると差が見えやすくなります。逆を返せば、自社の仕事で差が出なければ、評判のために高いモデルを選ぶ必要はありません。

## そのまま使える比較用の依頼文

下の文の角括弧を埋めて、同じ内容を二つのモデルへ送ってみてください。仕事の目的、資料、完成条件をそろえるだけで、比較の質が上がります。

> あなたに依頼する仕事は［仕事の名前］です。目的は［誰が、何に使うか］です。添付した［資料名］だけを根拠に、［成果物の形式と分量］を作ってください。資料にない事実や数字は補わず、「未確認」と明記してください。完成条件は①［条件1］②［条件2］③［条件3］です。最後に、参照した資料の箇所、未確認事項、人が確認すべき点を短く示してください。

たとえば不動産会社なら、物件資料から紹介文を作る際に、広さや駅からの距離を元資料と照らせる形で出す。製造業なら、点検記録の要約で異常を「問題なし」に丸めない。業種が違っても、見るべきポイントは同じです。

## どれから始めるか

すでにClaudeを使っている会社なら、まずOpus 5.5で、手直しの多い仕事を一つ試すとよいと思います。ChatGPT WorkやCodexを使っている会社なら、日常業務にSol、繰り返しの定型業務にLuna、難しい案件にAstraを当てて比べてください。OpenAIはSolとLunaについて、9月22日時点ではChatGPT WorkとCodexでの提供を案内しており、通常のChatにはまだ提供していないと説明しています。画面にモデルが見えない場合は、提供状況を確認してください。[提供先の公式説明](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

モデルはこれからも入れ替わります。ただ、業務の完成条件と確認方法を一度作れば、次のモデルにもそのまま使えます。まずは一つの仕事で「何分の手直しが減ったか」まで測ってみてください。

自社で試す仕事の選び方から整理したい方は、[熊本の生成AI研修](/kumamoto-ai-training/)や[お問い合わせ](/contact/)をご覧ください。
