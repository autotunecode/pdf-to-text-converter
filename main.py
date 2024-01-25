import PyPDF2
import os
import re

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        # テキストの前処理（改行と空白の削除）
        text = re.sub(r'\n+', '\n', text)  # 連続する改行を1つに置換
        text = re.sub(r'\s+', ' ', text)  # 連続する空白を1つに置換
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

def batch_pdf_to_txt(pdf_dir, txt_dir):
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, filename)
            txt_path = os.path.join(txt_dir, os.path.splitext(filename)[0] + ".txt")
            try:
                pdf_to_txt(pdf_path, txt_path)
            except Exception as e:
                print(f"Error processing {pdf_path}: {e}")

# テスト用のディレクトリパス
pdf_dir = "pdf_files"
txt_dir = "txt_files"

# PDFファイルをテキストファイルに変換
batch_pdf_to_txt(pdf_dir, txt_dir)