import os

from app.parsers.pdf_parser import (
    PDFParser
)

from app.parsers.section_parser import (
    SectionParser
)


class ParsingService:

    @staticmethod
    def parse_resume(
        stored_filename
    ):

        file_path = os.path.join(
            "app",
            "uploads",
            stored_filename
        )

        full_text = (
            PDFParser.extract_text(
                file_path
            )
        )

        parsed_data = {

            "name":
                SectionParser.extract_name(
                    full_text
                ),

            "email":
                SectionParser.extract_email(
                    full_text
                ),

            "phone":
                SectionParser.extract_phone(
                    full_text
                )
        }

        return (
            full_text,
            parsed_data
        )