---
title: "3Dルームツアー動画の作り方｜Claude Code×Blender全手順"
description: "図面1枚と見本の画像から、Claude Codeが無料の3DソフトBlenderを動かして3Dルームツアー動画を作る全手順を解説。プロンプト12本の全文、導入と安全設定、リアルにする4つのコツ、不動産で使うときのルールまでまとめました。"
pubDate: 2026-11-02T12:00:00
tag: "AIエージェント"
thumb: "/thumbs/claude-code-blender-3d-roomtour.webp"
---

「3DやCGをやってみたいけれど、Blenderは難しそう」。そう思っている方に、先に結論をお伝えします。Blenderの操作を覚えなくても、Claude Codeに日本語で頼むだけで、部屋の中を歩くような3Dルームツアー動画が作れます。

元にしたのは、図面1枚と雰囲気の見本の画像4枚、それに補足のメモだけです。この記事では、10月28日に公開した動画の内容をもとに、導入から書き出しまでの全手順と、実際に使ったプロンプト12本の全文をまとめました。

- 費用：Blender、MCP for Blender（AIとBlenderをつなぐ道具）、素材のPoly Havenは無料です。Claude Codeだけ有料プランが要ります
- コツ：いきなり作らせず、段階ごとに確かめます。一番効くのは光です
- 仕事で使うなら：CGであることをはっきり書き、広さや窓の外の景色は実物どおりにします

<div style="position:relative;width:100%;aspect-ratio:16/9;margin:1.5em 0;">
<iframe src="https://www.youtube-nocookie.com/embed/dZPFTSyPFeg" title="【Claude Code×Blender】3Dルームツアー動画 完全攻略｜図面と写真からリアルなルームツアー動画を作る全手順" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:8px;" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## まず完成品をご覧ください

下の映像は、カメラで撮っていません。
Claude Codeが無料の3Dソフト「Blender」を動かして部屋を組み立て、書き出した3DのCG映像です。Blenderの操作は不要で、日本語で頼むだけです。

<video controls playsinline preload="none" poster="/blog/claude-code-blender-3d-roomtour/demo-poster.webp" style="width:100%;height:auto;border-radius:8px;margin:1.5em 0;"><source src="/videos/blog/claude-code-blender-3d-roomtour/demo.mp4" type="video/mp4"></video>

※この映像はカメラで撮ったものではなく、Blenderで作った3DのCGです。部屋は架空のもので、図面と見本の画像はAIが作りました。動画で使った家具・床・空の素材はPoly Havenのものです。Poly Havenの素材はCC0といって、クレジットなしで仕事にも使える条件で公開されています。

部屋は、幅10.8メートル、奥行き6メートル、天井の高さ3メートルのリビングダイニング。架空の海辺のヴィラという設定です。30.5秒の映像の書き出しには、7時間14分かかりました。

ここまで聞くと難しそうに感じるかもしれませんが、作り方は4ステップだけです。

![3Dルームツアーの作り方は材料・組み立て・リアルにする・書き出しの4ステップ](/blog/claude-code-blender-3d-roomtour/diagram-3-overview.webp)

## BlenderとMCPを、ひとことで言うと

### Blenderは、パソコンの中の撮影スタジオ

Blenderは無料の3Dソフトで、映画やゲーム、建築のCGにも使われています。たとえて言うなら、パソコンの中の撮影スタジオです。

スタジオの中に壁や家具を置き、床や壁紙を貼り、照明とカメラの位置を決めます。Blenderからの書き出しが、そのまま撮影です。

![Blenderはパソコンの中の撮影スタジオというたとえのイラスト](/blog/claude-code-blender-3d-roomtour/diagram-4-studio.webp)

### Blender MCPは、AIが使うリモコン

Blenderの操作を覚えるのは、確かに大変です。ただ、AIに動かしてもらえば、その操作を覚えなくて大丈夫です。

つなぐのに使うのがBlender MCPです。AIがBlenderを動かすためのリモコンだと思ってください。MCPは、AIとソフトをつなぐ接続口のような意味です。今の正式な名前は「MCP for Blender」で、有志が作っている無料の道具です。

![Claude CodeからMCPというリモコンでBlenderを動かすイラスト](/blog/claude-code-blender-3d-roomtour/diagram-5-remote.webp)

あなたが日本語で頼み、Claude CodeがMCPを通してBlenderに伝え、できたものをあなたが見て直す。この繰り返しで、スタジオができていきます。

### 動画生成AIではなくBlenderを使う理由

動画生成AIは、手軽でハイクオリティです。ただ、部屋の動画に使うと、部屋の形や家具の位置が毎回微妙に変わることがよくあります。

Blenderで作るCGは、寸法どおりに作れて、形がどのコマでも同じです。カメラは何度でも撮り直せて、まったく同じ部屋で昼と夜を比べたり、床や家具の色違いを作ったりできます。

![動画生成AIと3DのCGの違いの比較](/blog/claude-code-blender-3d-roomtour/diagram-6-compare.webp)

なので、部屋の形が毎回正しいことが大事な不動産やリフォームの動画には、こちらのやり方が向いているかなと思います。どちらが上という話ではなく、向き不向きです。

## 必要なものと費用

| 何を | 中身 | 費用 |
|---|---|---|
| パソコン | 動画はMacBook Pro（M4 Pro・メモリ24GB） | 手持ちのもの |
| Blender | 今の最新は5.2.3 LTS（長期サポート版・10月22日公開） | 無料 |
| Claude Code | Claudeのデスクトップアプリの「Code」タブ | Pro以上 |
| MCP for Blender | AIとBlenderをつなぐ有志版の道具 | 無料 |
| Poly Haven | 家具・床・空の素材サイト（CC0） | 無料 |

Macの方は1点だけ確認してください。Blender 5以降はApple Silicon（M1以降のチップ）の機種（macOS 13以降）だけで動きます。Intelの機種は4.5 LTSを使います。メモリは最低8GB、公式の推奨は32GBです。

Claudeの料金は、日本から[料金ページ](https://claude.com/ja-jp/pricing)を開いた表示でProが月22ドル、年払いなら月18ドル相当（年220ドル）、Maxは月110ドル、Ultraは月220ドルです。無料プランではClaude Codeを使えません。チャットなどと同じ利用枠を使うので、長い作業ほど多く消費します。残りは設定の「使用状況」で見られます。（いずれも日本の消費税10%込みの表示です。上限に達すると、リセットを待つか上のプランに移ります）

## 導入編：やることは5つ

![導入でやることは5つの一覧](/blog/claude-code-blender-3d-roomtour/diagram-7-setup-five.webp)

### ① Blenderを入れる

[公式サイト](https://www.blender.org/download/)からダウンロードします。Mac版は330MBです。ファイルを開いて、Blenderをアプリケーションへドラッグし、初回は「開く」を押します。Windowsの方は、公式サイトのWindows用を入れてください。

開くと、真ん中に箱が1つ置かれています。これが撮影スタジオの初期の状態です。

### ② 操作画面を日本語にする

最初は英語なので、Edit の Preferences を開き、Interface の中の Language で日本語を選びます。

ここで1つだけ。「新規データ」のチェックだけはオフにしておいてください。AIが作っていくものの名前は、英語のままの方がAIとの相性がいいからです。

### ③ Claude Code側からつなぐ

こういう設定は難しそうに見えますが、準備はClaude Codeに頼むだけです。デスクトップに「内見動画」フォルダを作り、Claude Codeでそのフォルダを選んで開きます。そこに次のプロンプトを貼ります。

<details open style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト1：Blender MCPを使えるようにする（uvの確認・登録・アドオン・利用データの送信を止める）（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">Claude Code から Blender を操作できるように、有志版の「MCP for Blender」（パッケージ名 mcp-for-blender）をセットアップしてください。

【やってほしいこと】
1. 道具の確認：Pythonのパッケージを動かす道具「uv」が入っているか確かめる。無ければ、公式の方法（Macは Homebrew の「brew install uv」）で入れる。「pip install uv」は使わない
2. Claude Code への登録：「claude mcp add」で、名前「blender」、起動コマンド「uvx mcp-for-blender」を、どのフォルダでも使える形（スコープは user）で登録する。登録するときに、利用データの送信を止める環境変数「DISABLE_TELEMETRY=true」を、このサーバーに付ける
   （例：claude mcp add --env DISABLE_TELEMETRY=true --transport stdio --scope user blender -- uvx mcp-for-blender。--env のすぐ後に名前を置くと、名前まで環境変数として読まれてしまうので、間に --transport stdio を入れる。書式は、今の Claude Code のヘルプで確かめてから実行して）
   claude コマンドが見つからないときは、別に入れずに止まって私に伝えてください。私がOKしたら、設定ファイル ~/.claude.json の mcpServers に同じ内容（環境変数を含む）を追記します
3. Blender側のアドオン：「uvx mcp-for-blender install-addon」で、Blender用のアドオンを入れる
4. 最後に、私がBlenderで押すボタンを、順番に、画面の言葉で教える。それから「Claude Code を新しいセッションで開き直すと、Blenderの道具が使えるようになる」ことも伝える

【材料の場所】
・Blender は、すでにこのMacの「アプリケーション」に入っています
・公式の説明（README）：https://github.com/ahujasid/mcp-for-blender

【気をつけてほしいこと】
・私はパソコンに詳しくありません。何を入れるのか、なぜ必要なのかを、中学生にも分かる言葉で先に説明してから進めてください
・管理者パスワードが必要な操作（Homebrew 自体のインストールなど）や、パソコンの設定を変える操作は、勝手に進めずに止まって、私がやることを教えてください。パスワードは聞かないでください
・ネット上のスクリプトをそのまま実行する一括セットアップ（curl … | sh や、setup コマンド）は使わないでください。1つずつ進めてください
・Blender の開発者側の公式MCP（Blender Lab）は、今回は入れません。有志版と同じ通信口（ポート9876）を使うので、2つを同時に有効にしないでください

【進め方】
・まず、やることの一覧と、パソコンに起きる変更を説明してから始めてください
・各ステップが終わるごとに、結果を1行で報告してください
・最後に、登録できたか（claude mcp list。使えないときは設定ファイルの中身）と、利用データの送信を止める設定が入っているかを確かめて、結果を教えてください</pre>

</details>

中身は4つです。必要な道具が入っているかの確認、リモコン（MCP）の登録、Blender側の受け口になるアドオンの追加、そして利用記録の送信を止める設定です。

コマンドは基本的にAIが打ちます。ただしHomebrewが入っていないMacなど、管理者パスワードが要る作業は、AIが止まって手順を教えるので、自分でターミナルに打ちます。パスワードは、ターミナルの枠をクリックしてから入力してください。チャット欄には打たないでください。

### ④ Blender側でスイッチを入れる

終わるとAIが押すボタンを教えてくれます。やることは次のとおりです。あなたがBlenderで押すのは、これで全部です。

1. 「編集」→「プリファレンス」→「アドオン」を開き、検索欄に「MCP」と打って出てきた「MCP for Blender」にチェックを入れる。出てこなければBlenderを開き直す
2. 3Dの画面でキーボードの N を押し、右に出る「MCP for Blender」のタブを開く
3. 「Connected on port 9876」と出ていれば、つながっています。出ていなければ「Connect to MCP server」を押す
4. 同じタブの「Poly Haven」にチェックを入れる。無料の素材サイトから家具や床を持ってこられるようになります

Poly Havenのチェックはファイルごとの設定で、初めはオフです。新しいファイルを作ったら、入れ直してください。

### ⑤ つながったか試す

Claude Codeで新しいセッション（新しい会話）を開き、次のプロンプトを貼ります。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト2：つながったか試す（中を見る→箱を消して椅子を1脚→画面を見せる）（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">Blenderの中を見て、何があるか教えてください。
そのあと、真ん中の箱（Cube）を消して、木の椅子を1脚、床の上に置いてください。椅子は Poly Haven の素材から探して読み込んでください。
最後に、椅子が画面に大きく映るように寄ってから、Blenderの画面（ビューポート）を画像で見せてください。

【気をつけてほしいこと】
・Blender の画面に実際に出ているかを、画像で確かめてから「できました」と言ってください
・Blender とつながっていない場合は、作り始めずに、「つながっていません。Blender側で◯◯を押してください」と教えてください
・素材のダウンロード中は Blender が止まったように見えますが、待ってください

【進め方】
・作業は1つずつ。箱を消したら1回、椅子を置いたら1回、画面の画像を見せてください</pre>

</details>

AIがBlenderの中を見て、箱を消し、素材サイトから椅子を探して置きます。Blenderに椅子が出てきたら、準備は完了です。この間、私はBlenderに一切触っていません。

## AIに任せる前に知っておく安全の話

便利な道具ですが、ここは飛ばさないでください。[MCP for Blenderの公式の説明](https://github.com/ahujasid/mcp-for-blender)に書かれていることを4つにまとめます。

![AIに任せる前の安全4点](/blog/claude-code-blender-3d-roomtour/diagram-8-safety.webp)

1. AIはBlenderの中で、どんなプログラムでも実行できます。Blenderの中といっても、安全モードで止めない限り、パソコンのファイルの読み書き、別のプログラムの起動、ネット接続まで届きます。使う前に保存し、顧客情報や機密資料の入ったパソコンでは使わないでください。Claude Codeの確認をすべて省く設定（画面の表示は「権限をバイパス」）にもしないでください
2. 何もしないと、匿名の利用記録が送られる仕組みです。中身はランダムなID、使った道具の名前、成功したか、時間、版、OSなどです。研究やAIの学習に使われることもあると書かれています。止める設定 DISABLE_TELEMETRY=true をプロンプト1に入れてあります
3. プロンプト、コード、画面の画像、シーンの中身は、同意しない限り送られません。会話の最初に同意を聞かれることがありますが、断って大丈夫です
4. もっと慎重に使いたいときは安全モードがあります。BLENDER_MCP_SAFE_MODE=1 を設定すると、ファイルの直接操作、別のプログラムの起動、ネット接続を含むコードを止めます。モデリングや描画、保存はそのまま使えます

もう1つ。Blenderの受け口には認証がないので、自分のパソコンの中だけで使い、外から入れるようにしないでください。

なお、Blenderの開発者側（Blender Lab）が出している公式のMCPもあります。公式ページに素材連携の説明はなく、動画では有志版を使っています。[公式のページ](https://www.blender.org/lab/mcp-server/)には、AIが作ったコードを安全策なしで実行するので、仮想マシンか機密情報のない環境で使うよう書かれています。同じ通信口を使うことがあるので、2つを同時に有効にしないでください。

お客様の図面や写真を使うときは、先に本人の許可を取ってください。Proなどの個人プランでは、会話やコーディングの内容をモデルの学習に使うかどうかを、[プライバシー設定](https://www.anthropic.com/news/updates-to-our-consumer-terms)で自分で選びます。設定を確かめてから使ってください。

## 材料編：図面・写真・メモの3つ

セットアップが終わったら、材料です。使うのは3つだけです。

### ① 図面

寸法が入っていれば、手描きでも大丈夫です。今回は架空の海辺のヴィラの図面を用意しました。

![架空の部屋の図面1枚と、AIが作った雰囲気の見本の画像4枚](/blog/claude-code-blender-3d-roomtour/diagram-9-materials.webp)

ここで注意点です。公開されている物件の間取り図や写真を、勝手にダウンロードして使わないでください。自分の物件か、許可をもらった物件か、架空の間取りで作ります。理由はこのあとのルールの章で説明します。

### ② 写真

1部屋に6枚くらいが目安です。部屋の4つの角から反対の角に向けて4枚、窓まわり、床と壁のアップです。

![写真の撮り方。部屋の四隅から4枚、窓まわり、床と壁のアップ](/blog/claude-code-blender-3d-roomtour/diagram-10-photos.webp)

本物の写真があるのが一番です。今回は架空の部屋なので、写真の代わりに画像生成AIで見本の画像を4枚作りました。

### ③ メモ1枚

図面に書いていないことを書きます。天井の高さ、窓の高さと大きさ、窓の下の端が床から何cmか、ドアの高さ、床の素材、壁の色、窓の向きです。窓の向きは光の入り方に効きます。

### フォルダを作る

先ほどの「内見動画」フォルダの中に、「図面」「写真」「メモ」「完成」の4つのフォルダを作って材料を入れます。フォルダ名はこのままで大丈夫です。プロンプトの【 】の中だけ、自分の部屋に合わせて書きかえてください。写真は撮った順に 01.jpg、02.jpg と名前を付けます。

## いきなり作らせない

材料が揃ったら作り始めたくなりますが、いきなり作り始めないのがコツです。まずAIと打ち合わせをします。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト3：材料を全部読んで、寸法表を作る。分からない所は先に質問（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">「内見動画」フォルダの材料を全部読んで、この部屋の寸法表を作ってください。まだ3Dは作らないでください。

【やってほしいこと】
・「図面」「写真」「メモ」フォルダの中身を全部読む
・部屋の縦・横・天井の高さ、壁の位置、窓とドアの位置・幅・高さ・床からの高さ、床と壁の素材と色、窓の向き、写真に写っている家具の一覧を、1つの表（寸法表）にまとめる
・寸法表は「内見動画/寸法表.md」に保存する（これが、このあとの作業の正本になります）
・手描きの図面なら、寸法表の数字できれいな平面図の画像も1枚作って、「内見動画/図面/清書.png」に保存する

【材料の場所】
・図面：内見動画/図面（寸法の単位は【cm】）
・写真：内見動画/写真（撮った位置と向きは【ファイル名の順に、部屋の4つの角から時計回り。5枚目が窓、6枚目が床と壁のアップ】）
・メモ：内見動画/メモ

【気をつけてほしいこと】
・図面の数字は、画像からの読み取りだと「おおよそ」になります。読み取った数字には「図面の記載」か「推定」のどちらかを必ず付けて、推定は私に確認してください
・写真から推定した大きさは、推定と分かるように書く
・分からない所を、勝手に決めない

【進め方】
・材料を読んだら、まず、分からない所・あいまいな所を質問の一覧にして、私に聞いてください（例：天井の高さ、窓の下の端の高さ、ドアの高さ、家具の大きさ）
・私の答えを寸法表に反映して、確定版を見せてから、次へ進んでください</pre>

</details>

するとAIから質問が返ってきます。天井の高さはどれくらいですか。窓の下の端は床から何センチありますか。渡した材料から判断できなかった所を聞いてきます。

![AIが作る前に天井の高さなどを質問してくるイラスト](/blog/claude-code-blender-3d-roomtour/diagram-11-ask-first.webp)

作る前に細かい部分を質問させる。頼み方では、これが一番重要なコツです。分からないまま作らせると、後で全部やり直しになります。逆を返せば、作る前に質問を出し切っておけば、手戻りは減らせます。

## 実践編：貼って、待って、確かめる

ここからやることはずっと同じです。Claudeに指示を貼り、待って、できたものを確かめる。作るのは全部AIで、私たちの仕事は確かめることだけです。

3DのCGは、AIにとってもパソコンにとっても重たい処理です。なので一気に完成品を出させず、要所要所で段階的に確認します。

![部屋の形から本番の書き出しまで段階で確かめる階段の図](/blog/claude-code-blender-3d-roomtour/diagram-12-stairs.webp)

### 手順① 部屋の形だけを作る

図面をもとに、色のない部屋を作らせます。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト4：色のない部屋を作って、真上から図面と照合する（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">寸法表どおりに、色のない部屋を作ってください。壁・床・天井と、窓とドアの穴だけです。

【やってほしいこと】
・新しいBlenderのファイルを「内見動画/完成/部屋.blend」として保存してから始める
・寸法表（内見動画/寸法表.md）の数字で、壁の厚さも含めて作る。単位はメートルで、実寸どおり
・色や素材はまだ付けない。家具もまだ置かない
・できたら、真上から見た画像（平面図と同じ向き）を描いて、図面の画像と半透明で重ねた「照合画像」を作って見せる

【材料の場所】
・寸法表：内見動画/寸法表.md
・図面：内見動画/図面

【気をつけてほしいこと】
・図面が正本です。「だいたい合っている」ではなく、壁の位置・窓とドアの位置のずれを、数字（cm）で出してください
・作業の前に保存。途中も節目で保存

【進め方】
・計画（どの順番で何を作るか）を先に見せてから、作り始める
・できたら、照合画像と、ずれの一覧（場所・何cm）を見せる。私が「直して」と言った所だけ直す
・Blenderの画面に実際に出ているかを、画像で確かめてから報告する</pre>

</details>

AIが真上から見た画像を図面と重ねてくれます。確かめるのは図面とのズレです。今回はズレが0か所でした。

<img src="/blog/claude-code-blender-3d-roomtour/diagram-13-overlay.webp" alt="図面と3Dを重ねた照合画像。ずれ1cm以上は0か所" loading="lazy" style="display:block;width:100%;max-width:560px;height:auto;margin:1.5em auto;border-radius:8px;">

### 手順② 家具を置く

プロンプト5を貼る前に、Poly Havenのチェックを入れ直してください。AIが無料の素材サイトから家具を探し、図面の位置に置きます。終わったら、家具の位置と向きが図面どおりかを目で確かめます。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト5：写真の家具を一覧にして、素材で同じ位置に置く（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">写真に写っている家具を一覧にして、Poly Haven の素材から近いものを探して、写真と同じ位置に置いてください。

【やってほしいこと】
・写真から、家具と大きな物（ソファ、テーブル、棚、カーテン、照明器具など）を一覧にする（名前・だいたいの大きさ・置いてある場所）
・一覧を私に見せて、OKをもらってから、Poly Haven で近い素材を探して読み込む
・床・壁・天井にも、写真に近い素材（Poly Haven のテクスチャ）を貼る。木目やタイルは、実物の大きさで
・置いたら、人の目の高さ（約150cm）から見た画像を2〜3枚見せる

【材料の場所】
・写真：内見動画/写真
・寸法表：内見動画/寸法表.md
・Blenderのファイル：内見動画/完成/部屋.blend

【気をつけてほしいこと】
・家具の形をゼロから作らないでください（素材を使う）。近い素材が無いときは、候補を3つ（うち1つは箱に素材を貼る簡単な形）出して、私に選ばせる
・素材の大きさは 1k か 2k で（重くなるので）。ダウンロード中は Blender が止まったように見えても、待つ
・家具が床にめり込んだり、浮いたりしないように、底面を床に合わせる
・家具を置く前に、「家具なし」の状態を別の名前で保存しておく（内見動画/完成/部屋_家具なし.blend）

【進め方】
・一覧 → 私のOK → 読み込み → 画像、の順。全部置いてから、画像で見せてよい</pre>

</details>

### 手順③ カメラを決めて、下書きの動画を作る

AIが人の目の高さで歩くカメラの通り道を決めて、下書きの動画を作ります。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト6：人の目線のカメラで、下書きの内見動画（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">人の目線で部屋の中をゆっくり歩く、下書きの内見動画を作ってください。

【やってほしいこと】
・カメラは、人の目の高さ（約150cm）、自然な広角
・動きは、ドアから入って部屋を一周するイメージで、【20〜30】秒
・一度に一つの動き（進む、止まる、ゆっくり曲がる）。急な動きは入れない
・まずは速い描き方（ビューポートの描画＝Playblast）で、下書きを書き出す。フルHD
・保存先：内見動画/完成/下書き_01.mp4

【材料の場所】
・Blenderのファイル：内見動画/完成/部屋.blend

【気をつけてほしいこと】
・カメラが壁や家具を通り抜けないか、通り道を数字で確かめる（カメラの位置と、壁・家具との距離）
・下書きなので、画質より「動きと通り道」の確認が目的です

【進め方】
・カメラの通り道を、言葉と、真上から見た図で先に見せて、OKをもらってから書き出す
・書き出したら、最初・真ん中・最後の3コマの画像と、動画のファイルの場所を教える</pre>

</details>

![下書きの段階のカメラの通り道を真上から見た図](/blog/claude-code-blender-3d-roomtour/diagram-14-camera-path.webp)

上の図は、下書きの段階のカメラの通り道です。確かめるのは、壁の中をすり抜けていないか、動きが速すぎないかです。

この時点の映像は、まだCGっぽくてクオリティは全然低いです。でも、それで構いません。まず図面どおりの下書きを作り、クオリティはこの先で上げます。

## まるで本物にする4つのコツ

![まるで本物にする4つのコツの一覧](/blog/claude-code-blender-3d-roomtour/diagram-15-four-tips.webp)

### コツ① 光を決める

4つの中で、特に効くのがこれです。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト7：光を決める（空の光・照明の色・明るさ）（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">光を決めてください。窓から入る空の光、部屋の照明、明るさの3つです。

【やってほしいこと】
・窓からの光：Poly Haven の HDRI（空をぐるっと撮った写真）を使う。時間帯は【昼・晴れ】。窓の向き（【南】）に太陽の方向を合わせる
・部屋の照明：写真と同じ色（【電球色／昼白色】）。照明器具の位置は写真どおり
・明るさ：白い壁が白く見える明るさに。白飛びしない。暗い所が真っ黒にならない
・できたら、同じカメラで「光を入れる前」と「後」の画像を1枚ずつ見せる

【材料の場所】
・写真（照明の色と、光の入り方の見本）：内見動画/写真
・メモ（窓の向き）：内見動画/メモ

【気をつけてほしいこと】
・HDRI は 2k までの大きさで
・明るすぎる光だと、色が白く飛んで見えることがあります。色が変だと思ったら、数値（露出・光の強さ）を見て確かめる

【進め方】
・設定の案（使うHDRIの名前・照明の色・明るさの数値）を先に見せてから、実行する</pre>

</details>

AIが窓の外の空と部屋の照明を調整します。光が変わるだけで、ここまで変わります。

![光を決める前と後の比較。CGの部屋](/blog/claude-code-blender-3d-roomtour/diagram-16-light.webp)

屋外の空の光と、部屋の光をちゃんと揃える。リアルにするときに一番気をつける点かなと思います。

### コツ② 別のAIに採点させる

AIが見本と同じ角度で1枚作り、別のAI（もう1体のClaude）がそれを採点して、違う所を3つ挙げて直します。これを最大3回、自分で繰り返させます。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト8：写真と同じ角度で試し描き→並べて違いを直す（採点は別のAI）（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">写真と同じ角度で試しに描いて、写真と見比べて、違う所を直してください。採点は、別のAIにお願いします。

【やってほしいこと】
・写真【01.jpg】と同じ位置・高さ・向き・画角にカメラを置いて、1枚描く（下書きの画質でよい）
・写真と、描いた画像を左右に並べた、1枚の比較画像を作る
・比較画像を、この作業をしていない別のAI（サブエージェント）に渡して、「本物の写真にどれくらい近いか」を10点満点で採点させ、違う所を3つ、具体的に挙げさせる（例：窓枠が太い、床の木目が大きい、壁が明るすぎる）
・3つを直して、もう一度描いて、採点してもらう。8点以上になるまで、最大【3】回くり返す

【材料の場所】
・写真：内見動画/写真
・Blenderのファイル：内見動画/完成/部屋.blend

【気をつけてほしいこと】
・採点は、作った本人（あなた）ではなく、別のAIにさせてください。自分で採点しない
・直すのは「違う所3つ」だけ。ほかを勝手に変えない
・寸法表や図面を変えるような直しは、私に確認してから

【進め方】
・比較画像と点数、違う所3つを、毎回私にも見せてください
・8点以上になったら、同じ要領で、別の写真【02.jpg】でも1回確かめる</pre>

</details>

採点は作った本人ではなく、別のAIにさせるのがコツです。今回も、回を重ねるごとに見た目が良くなっていきました。

![見本の画像と、直す前、直し1回目、直し3回目のCGの比較](/blog/claude-code-blender-3d-roomtour/diagram-17-scoring.webp)

左上の見本の画像はAIが作ったものです。残りの3枚がBlenderで作ったCGです。

### コツ③ あえて完璧すぎないようにする

完璧に作りすぎると、かえってリアリティがなくなります。床のムラ、角の丸み、カーテンのたわみ、小物を足してもらいます。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト9：完璧すぎないように仕上げる（実物の大きさの木目・ムラ・角・小物）（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">「完璧すぎる」所をなくして、本物の部屋らしくしてください。

【やってほしいこと】
・床の木目（または床材）は実物の大きさで。少しのムラ・つや・小さな傷を足す
・壁と家具の角に、わずかな丸みを付ける
・カーテンは少したるませる。クッションは少しへこませる
・生活感の小物を少しだけ（本・コップ・観葉植物など、Poly Haven の素材で3〜5点）。散らかさない
・できたら、同じカメラで「前」と「後」、それと小物と床のアップを見せる

【材料の場所】
・写真（実物の木目の大きさや、物の置き方の見本）：内見動画/写真
・Blenderのファイル：内見動画/完成/部屋.blend

【気をつけてほしいこと】
・お客さんに見せる部屋です。汚れ・散らかりは、やりすぎない。「新築のモデルルームに、人が1日住んだくらい」が目安
・私物を特定できる物（写真・郵便物・文字が読める物）は置かない
・寸法は変えない

【進め方】
・足す物と変える所の一覧を先に見せて、OKをもらってから実行する</pre>

</details>

仕上げの前と後を並べると、こうなります。

![完璧すぎない仕上げの前と後、小物のアップ。CGの部屋](/blog/claude-code-blender-3d-roomtour/diagram-18-imperfect.webp)

### コツ④ チェック表を作らせて、数字で検査する

家具のめり込みや浮き、通り道の幅、カメラの変な動きを、AIに数字で検証させて直します。見た目で「問題なし」と言わせないのがポイントです。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト10：めり込み・浮き・通り道・壁抜けを数字で検査して直す（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">部屋の中を数字で検査して、おかしい所を全部直してください。見た目で「問題なし」と答えないでください。

【やってほしいこと】
次の4つを、Pythonで数字を出して検査する
1. めり込み：家具どうし、家具と壁・床が重なっていないか（重なりの大きさ cm）
2. 浮き：家具の底が床から離れていないか（すき間 cm）
3. 通り道：人が歩く所の幅が【60】cm以上あるか
4. カメラ：内見動画のカメラの通り道が、全コマで壁・家具・天井から【30】cm以上離れているか
結果を表（場所・何が・数字・直し方）にして見せてから、直す。直したら、もう一度同じ検査をして、0件になったことを確かめる

【材料の場所】
・Blenderのファイル：内見動画/完成/部屋.blend
・寸法表：内見動画/寸法表.md

【気をつけてほしいこと】
・検査は数字で。画像を見て「大丈夫そう」は、検査ではありません
・直すときに、寸法表の数字（部屋の形）は変えない。家具の位置と大きさで直す
・1cm未満の差は「許容」として、表に残してよい

【進め方】
・検査の結果の表 → 私のOK → 直す → 再検査、の順
・見つかった数と直した数を、最後に1行で報告する</pre>

</details>

今回は4か所おかしい所が見つかり、AIに直させると0か所になりました。

![数字の検査で見つかった4か所と直した結果](/blog/claude-code-blender-3d-roomtour/diagram-19-inspection.webp)

## 本番の書き出しは、寝ている間に

ここまで積み重ねてから、最後に本番の書き出しです。いきなり書き出すと、全然違うものができたときに最初からやり直しになります。

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト11：3コマ試して時間を見積もり、本番を書き出す（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">本番の描き方（Cycles）で、まず3コマだけ試して、時間を見積もってから、内見動画を書き出してください。

【やってほしいこと】
・描き方を Cycles にする。GPU（Metal）を使う。ノイズ除去をオンにする
・最初・真ん中・最後の3コマを、本番の設定で描いて、1コマの時間を測る
・平均×コマ数で全体の時間を見積もって、私に見せる（例：1コマ◯分×◯コマ＝約◯時間）
・私がOKしたら、書き出しを始める。保存先：内見動画/完成/内見動画_本番.mp4（フルHD）
・設定（サンプル数・解像度・時間の上限など）は、見積もりと一緒に表で見せる

【材料の場所】
・Blenderのファイル：内見動画/完成/部屋.blend

【気をつけてほしいこと】
・見積もりが【3】時間を超えるなら、始める前に、画質を少し落として時間を半分にする案も出してください
・書き出しの前に、Blenderのファイルを保存
・書き出し中は、ほかの作業をBlenderに頼まない（止まるので）
・長い書き出しは、接続の待ち時間切れを避けるためBlenderの別プロセスで実行し、止まっても続きから再開できるよう連番画像で書き出してから動画にしてください

【進め方】
・3コマの画像と見積もりを見せる → 私のOK → 書き出し → 終わったら、動画の場所と、実際にかかった時間を報告</pre>

</details>

3D動画の書き出しは、本当に数時間以上かかります。今回は30.5秒の映像に7時間14分かかりました。計算すると1コマあたり約36秒です。できれば寝ている間に書き出すのがおすすめです。MacBookは電源につなぎ、ふたを開けたまま、スリープしない設定にしてから始めてください。

![完成した3Dルームツアー動画から抜いた4コマ。CGの部屋](/blog/claude-code-blender-3d-roomtour/diagram-20-demo-grid.webp)

作業ごとの待ち時間も書いておきます。今回の部屋とパソコンでの目安で、動画の手順カードに出したものと同じです。

| 作業 | 待つ時間 | 確かめること |
|---|---|---|
| 部屋の形 | 約3分 | 図面とのズレ |
| 家具 | 約6分 | 位置と向き |
| カメラ（下書き） | 約10〜20分 | 下書きの動画 |
| 光 | 約4分 | 光の前と後 |
| 見比べ | 約15分 | 点数と違う所3つ |
| 完璧すぎない仕上げ | 約2分 | アップの画像 |
| 数字で検査 | 約2分 | 検査の表 |
| 本番の書き出し | 7時間14分 | 完成した動画 |

## 一度作った部屋は、一言で何パターンも作れる

ここからが嬉しいところです。「時間帯を夜にして」と言えば同じ部屋の夜の動画ができ、家具やカメラワークを入れ替えた動画も、SNS用の縦型動画も作れます。これが3DのCG動画の一番のメリットです。指示は一言ですが、本番の書き出しはパターンごとにまた数時間かかります。

![同じ部屋の作り分け。夜、床の色違い、家具なし、縦型](/blog/claude-code-blender-3d-roomtour/diagram-21-variants.webp)

<details style="margin:1.2em 0;border:1px solid #dbe3ee;border-radius:8px;background:#f7f9fc;padding:.7em 1em;">
<summary style="cursor:pointer;font-weight:700;">プロンプト12：作り分け（昼夜・床の色・家具の有無・縦の動画）（全文）</summary>

<pre style="white-space:pre-wrap;word-break:break-word;font-family:inherit;font-size:.92em;line-height:1.7;margin:.8em 0 .2em;background:none;color:inherit;padding:0;">今の部屋を元に、次の4パターンを作り分けてください。元のファイルは変えないでください。

【やってほしいこと】
1. 夜：空の光を夕方〜夜にして、部屋の照明だけが点いた状態
2. 床の色違い：床を【ウォルナット（濃い茶色）】に
3. 家具なし：部屋.blend を別名（部屋_空室.blend）で複製し、家具だけを消す。光・床・壁・カメラはそのまま
4. 縦の動画：同じカメラの通り道で、縦長（1080×1920）
それぞれ、まず下書きの画質で1枚ずつ画像を見せて、私がOKしたものだけ、本番の設定で書き出す
保存先：内見動画/完成/パターン_夜.mp4 など、名前で分かるように

【材料の場所】
・Blenderのファイル：内見動画/完成/部屋.blend

【気をつけてほしいこと】
・元のファイル（部屋.blend）は上書きしない。パターンごとに別の名前で保存
・部屋の形・寸法は変えない。変えるのは、光・素材・家具・カメラだけ
・縦の動画は、カメラの画角を縦向きに合わせて、天井と床が切れないか確かめる

【進め方】
・4つの下書きの画像 → 私が選ぶ → 本番の見積もり（プロンプト11と同じやり方） → 書き出し</pre>

</details>

## 仕事ではどう使えるか

まず取り組みやすく効果が見えやすいのは、リフォームや工務店の提案です。作る前の完成イメージや、床や壁の色違いをお客様に見せられます。

![リフォームの提案で完成イメージと色違いを見せるイラスト](/blog/claude-code-blender-3d-roomtour/diagram-22-reform.webp)

不動産なら、空室に家具を置いたイメージや、完成前の物件のイメージです。店舗やオフィスなら、内装やレイアウトの提案にも使えると思います。ただし、不動産で使うにはルールがあります。

## 不動産・住宅で使うときのルール

ここは丁寧に書きます。基準になるのは[不動産の表示に関する公正競争規約](https://www.rftc.jp/koseikyosokiyaku/)と、その施行規則です。不動産会社の広告についての業界のルールです。最新の変更は、規約が2024年10月1日、施行規則が2022年9月1日です。

![仕事で使うときの4つのルール](/blog/claude-code-blender-3d-roomtour/diagram-23-rules.webp)

### ① 画面に「CGです」とはっきり書く

施行規則の第9条第23号で、建物のCGや完成予想図は、その旨を明示して使うことになっています。

### ② 広さ・間取り・窓の外の景色は実物どおりに

規約の第23条第1項第42号は、CGや動画で物件の規模や形、構造を事実と違えて見せること、実際より良いと思わせることを禁じています。第43号は眺めや景色についての同じ決まりです。わざとでなくても、実物よりよく見えるおそれがあれば問題になります。

「イメージです」と書けば許される、というわけではありません。[首都圏の協議会の事例](https://www.sfkoutori.or.jp/jireikoukoku/hutohyoji-kinshi/)では、写真の電柱や電線をCGで消した表示は、注記があっても不当表示にあたるとされています。

間取りの言葉にも決まりがあります。畳数で書くなら1畳は1.62平方メートル以上、建築基準法で居室と認められない部分は「納戸」などと書きます（施行規則 第9条第16号・第17号）。

### ③ CGの家具は「価格に含まれません」と書く

条文に家具の定めはありませんが、価格に含まれると誤解されないよう書いておくと安心です。大手の不動産会社も、次のような注記を入れています。

> ※この画像は、実際の室内にCGによる家具等を配置したものです。家具等は販売価格に含まれません。（[三井のリハウス](https://www.rehouse.co.jp/buy/panorama/homestaging/)）

### ④ 図面と写真は、自分のものか許可をもらったものだけ

物件サイトの間取り図や写真を無断で使うと、そのサイトの利用規約に反するおそれがあり、著作権の問題にもなりえます。[SUUMOの利用規約](https://cdn.p.recruit.co.jp/terms/suu-t-1003/index.html)の第2条第1項は私的利用の範囲を超える使用を、[LIFULL HOME'Sの利用規約](https://www.homes.co.jp/kiyaku/)の第6条は無断の改変や公開を禁じています。

### そのほかに気をつけること

- 工事が終わる前の物件は、建築確認などを受けた後でないと広告を始められません（規約 第5条。宅地建物取引業法 第33条にも同じ趣旨の決まりがあります）。完成イメージの動画も同じです
- 不動産会社から頼まれて作る制作会社にも、規約の趣旨に沿った制作の努力が求められています（第3条）
- 不動産会社でなくても、[景品表示法の優良誤認](https://www.caa.go.jp/policies/policy/representation/fair_labeling/representation_regulation/misleading_representation/)（実際より良いと誤解させる表示）は事業者全般が対象です。リフォーム会社や家具店の完成イメージにも関わることがあります
- YouTubeに載せるときは、本物らしく見える映像に「AI の使用」の開示が求められる場合があります。写実的なCGも対象になりうるので、[YouTubeのヘルプ](https://support.google.com/youtube/answer/14328491?hl=ja)を見て設定してください
- 素材はCC0のものを使います。Poly Haven以外の素材サイトには、クレジットが要るものや商用で使えないものがあります

正直なところ、個別の広告が問題ないかの判断は私にはできかねます。広告に使う前に、加盟している協議会や専門家に確認してください。

## よくある質問

### つながりません

順番に3つ見ます。Blender側のタブに「Connected on port 9876」と出ているか。Claude Codeを新しいセッションで開き直したか（登録の直後は、新しいセッションからしか使えません）。会話の中で /mcp と打つと、つながっているかが見られます。

### Blenderが固まります

ほとんどは素材をダウンロードしている時間で、待てば動きます。素材は「1kか2kの大きさで」と頼むと軽くなります。書き出し中はBlenderにほかの作業を頼まないでください。

### 寸法がずれます

[Claudeの公式の説明](https://platform.claude.com/docs/en/build-with-claude/vision)にも、画像から読み取る位置は「おおよそ」と書かれています。「図面が正本。真上から見た画像を図面と重ねて、ずれを数字（cm）で出して」と頼んでください。最後は人が確かめます。

### AIが「作りました」と言うのに、画面に何もありません

MCPを使わずに作ったつもりになっていた、という報告が出ています。「Blenderの画面を画像で見せて、本当に出ているか確かめて」と頼んでください。プロンプト2と4には、この確認を入れてあります。

### 書き出しが遅いです

プロンプト11のとおり、3コマだけ試して時間を測ります。1回目は準備で数分余計にかかることがあります。

10月26日に仮の部屋で試したときは、1回目の準備に約3分かかりました。2回目からの1コマは、本番の描き方（Cycles）が25.8秒、速い描き方（EEVEE）が6.0秒でした。

### Windowsでもできますか

MCP for Blenderの公式の説明にはWindowsの入れ方も書かれていて、Blenderも公式にWindows版があります。プロンプト1の「brew install uv」と「このMacの「アプリケーション」」、プロンプト11の「GPU（Metal）」を、お使いのWindowsに合わせて書きかえてください。ただ、私が試したのはMacだけです。

### 費用はどれくらいかかりますか

道具と素材は無料で、かかるのはClaudeのプランだけです。Proで足りるかは測っていません。小さい部屋から試してください。

## 始め方3ステップ

![明日からの3ステップ](/blog/claude-code-blender-3d-roomtour/diagram-24-three-steps.webp)

1. Blenderを入れて、プロンプト1でつなぐ。プロンプト2で椅子が出たら成功です
2. 自分の部屋を6枚撮って、メモを1枚書く。図面は手描きの寸法メモで大丈夫です
3. プロンプト3〜6で、下書きの動画まで作る。「まるで本物」にするのは、そのあとのプロンプト7〜10です

最初は自分の部屋1つ、または架空の1部屋で練習してみてください。

## 注意点のおさらい

- 作業の前に保存します。パスワードやAPIキーはチャットに貼りません
- 版と料金は2026年11月2日時点です。Blenderは次の5.3がベータ版の段階で、公開されると画面が変わることがあります。MCP for Blenderは2.2.6（10月28日）が最新で、動画を作った時点の2.2.4から上がっています
- 図面の読み取りは「おおよそ」です。数字は人が確かめます
- 仕事で使うときは、CGの明示と実物どおりを守ります

## 研修と導入支援のご相談

WizTryでは、企業向けの生成AI研修と導入支援を行っています。2025年度の研修・セミナーの登壇は年間300回以上で、累計90社以上（2026年7月時点）を支援してきました。ご相談はお問い合わせからお願いします。

- 研修や導入支援について：[サービス](/service/)
- ご相談：[お問い合わせ](/contact/)

なお、この動画の編集もAIが行いました。やり方は[Claude CodeでAI動画編集の完全攻略](https://youtu.be/49OIGpNKVhA)でお話ししています。
