import PyPDF2
import os

def get_pdf_page_count(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "rb") as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    num_pages = len(pdf_reader.pages)
                    print(f"{filename}: {num_pages} pages")
            except PyPDF2.errors.PdfReadError as e:
                print(f"Error reading {filename}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing the PDF files (leave empty for current folder): ").strip()
    if not folder_path:
        folder_path = os.getcwd()
    get_pdf_page_count(folder_path)
