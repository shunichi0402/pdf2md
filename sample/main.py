import sys
import pdf2md as a2f

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ./sample/main.py <pdf_file_path> <output_path>")
        sys.exit(1)
    
    print("PDFからテキストを抽出中...")
    md_text = a2f.convert(sys.argv[1])

    print(f"Markdownファイルを保存中...")
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"Markdownファイルを保存しました: {sys.argv[2]}")
