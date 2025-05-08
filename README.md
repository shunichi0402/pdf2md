# pdf2md

## 概要
PDFファイルをMarkdown形式に変換するPythonツールです。PyMuPDFでPDFからテキストを抽出し、OpenAIのChatGPT APIを利用してMarkdownに整形します。

## インストール
1. Python 3.8以上が必要です。
2. 必要なパッケージをインストールします。
   ```bash
   pip install -r requirements.lock
   ```

## 使い方
1. OpenAI APIキーを環境変数`OPENAI_API_KEY`に設定してください。
2. 必要に応じて`OPENAI_MODEL`も設定できます（デフォルト: gpt-4.1-mini）。
3. コマンドラインから以下のように実行します。
   ```bash
   python ./sample/main.py <pdfファイルパス> <出力Markdownパス>
   ```
   例:
   ```bash
   python ./sample/main.py sample.pdf output.md
   ```

## ライブラリとしての使い方
`pdf2md`はPythonコードから直接利用できます。

```python
import pdf2md as p2m

md_text = p2m.convert('sample.pdf')
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(md_text)
```

- `pdf2md.convert(pdf_path: str) -> str` でPDFファイルをMarkdown形式のテキストに変換できます。
- 事前に`OPENAI_API_KEY`などの環境変数を設定してください。

## 必要な環境変数
- `OPENAI_API_KEY`: OpenAIのAPIキー
- `OPENAI_MODEL`: （任意）使用するモデル名（例: gpt-4.1-mini）

## 依存パッケージ
- openai
- pymupdf
