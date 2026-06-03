import re


class SectionParser:

    @staticmethod
    def extract_email(text):

        pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

        match = re.search(
            pattern,
            text
        )

        return (
            match.group(0)
            if match
            else None
        )

    @staticmethod
    def extract_phone(text):

        pattern = r'(\+?\d[\d\s\-]{8,15})'

        match = re.search(
            pattern,
            text
        )

        return (
            match.group(0).strip()
            if match
            else None
        )

    @staticmethod
    def extract_name(text):

        lines = text.splitlines()

        for line in lines:

            line = line.strip()

            if len(line) > 3:

                return line

        return None