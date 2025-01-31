import os
import fitz
from PyPDF2 import PdfReader, PdfWriter

from common.models.data_model import Data


class PDFProcessor:
    @staticmethod
    def _get_file_name(file_path):
        return os.path.basename(file_path)

    @staticmethod
    def _get_page_count(file_path):
        pdf_document = fitz.open(file_path)
        page_count = pdf_document.page_count
        pdf_document.close()
        return page_count

    @staticmethod
    def process_data(file_path):
        return Data(
            pdf_name=PDFProcessor._get_file_name(file_path),
            page_count=PDFProcessor._get_page_count(file_path),
        )

    @staticmethod
    def mergePdfs(pdfFiles, outputFile, add_blank_page):
        writer = PdfWriter()

        for pdf_file in pdfFiles:
            reader = PdfReader(pdf_file)

            # Add pages from the current PDF to the writer
            for page in reader.pages:
                writer.add_page(page)

            # If the user opted to add blank pages and the PDF has an odd number of pages
            if add_blank_page and len(reader.pages) % 2 != 0:
                writer.add_blank_page()

        # Save the merged PDF
        outputFile = outputFile
        with open(outputFile, "wb") as output:
            writer.write(output)

        print(f"Merged PDF saved as {outputFile}")
