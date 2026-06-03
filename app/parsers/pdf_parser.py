import fitz


class PDFParser:

    @staticmethod
    def extract_text(
        file_path: str
    ):

        document = fitz.open(
            file_path
        )

        full_text = ""

        for page in document:

            full_text += (
                page.get_text()
                + "\n"
            )

        document.close()

        return full_text