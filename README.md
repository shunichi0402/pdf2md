# pdf2md

## 概要
PDFファイルをMarkdown形式に変換するPythonツールです。PyMuPDFでPDFからテキストを抽出し、OpenAIのChatGPT APIを利用してMarkdownに整形します。

## 使い方
1. ライブラリをgithubからインストールしてください。
```
pip install git+https://github.com/shunichi0402/pdf2md.git
```


2. OpenAI APIキーを環境変数`OPENAI_API_KEY`に設定してください。
3. 必要に応じて`OPENAI_MODEL`も設定できます（デフォルト: gpt-4.1-mini）。


**コード例**
```python
import pdf2md as p2m

md_text = p2m.convert('sample.pdf')
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(md_text)
```

## 必要な環境変数
- `OPENAI_API_KEY`: OpenAIのAPIキー
- `OPENAI_MODEL`: （任意）使用するモデル名（例: gpt-4.1-mini）

## 依存パッケージ
- openai
- pymupdf
