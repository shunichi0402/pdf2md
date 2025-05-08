import os
from pdf2md.chatgpt import ask_chatgpt

SYSTEM_PROMPT = """
[タスク]
ユーザーから入力された文章はPDFファイルから読み取られた文章です。
入力された文章をマークダウンに変換してください。
変換する際の注意点と出力形式は以下に示します。

[注意点]
- ユーザーから入力された文章の内容は改変せず、フォーマットのみを整えてください。
- PDFからの変換の影響で不要な改行やスペースが挿入されています。適宜削除してください。
- PDFからの変換の影響で表がテキストに変換されています。適宜表形式に変換してください。
- 図や画像は削除されています。画像のキャプションなどが残っている場合があります。これは`![図n キャプション名]()`のように変換してください。

[出力形式]
- 出力の形式はMarkdown形式で出力してください。
- `実行が完了しました`等のMarkdown形式ではない部分は出力しないでください。
- 一番上位の```等のコードブロックは不要です。素のMarkdownのみ出力してください。

適切な実行を確保するために、出力は常にこの形式に従ってください。
"""
USER_PROMPT_PATH = """
[[plain_txt]]
"""

def convert_pdf_text_to_markdown(pdf_text: str, system_prompt: str = SYSTEM_PROMPT, user_prompt: str = USER_PROMPT_PATH) -> str:
    user_prompt = user_prompt.replace("[[plain_txt]]", pdf_text)

    response = ask_chatgpt(
        prompt=user_prompt,
        system_prompt=system_prompt
    )

    return response