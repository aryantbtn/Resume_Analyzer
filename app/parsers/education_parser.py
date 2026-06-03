class EducationParser:

    @staticmethod
    def extract_education(
        education_section
    ):

        education_entries = []

        lines = (
            education_section
            .splitlines()
        )

        for line in lines:

            line = line.strip()

            if (
                "University" in line
                or
                "College" in line
                or
                "Board" in line
            ):

                education_entries.append(
                    line
                )

        return education_entries