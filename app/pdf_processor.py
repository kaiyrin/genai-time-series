import PyPDF2
import os

class PDFProcessor:
    def __init__(self, input_path, output_path):
        self.input_path = "data/raw_pdfs" 
        self.output_path = "data/transcripts"

    def extract_text(self, pdf_file, start_page=0, end_page=None):
        pdf_path = os.path.join(self.input_path, pdf_file)
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                if end_page is None:
                    end_page = len(reader.pages)  # Read until the last page
                text = ""
                for page_number in range(start_page, end_page):
                    page = reader.pages[page_number]
                    text += page.extract_text() + "\n"
                return text
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")
            return None

    def save_text(self, text, output_file):
        output_path = os.path.join(self.output_path, output_file)
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"Extracted text saved to {output_path}")
        except Exception as e:
            print(f"Error saving text to {output_file}: {e}")
