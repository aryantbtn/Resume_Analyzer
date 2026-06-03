class ExperienceParser:

    @staticmethod
    def extract_experience(
        experience_section
    ):

        experiences = []

        lines = (
            experience_section
            .splitlines()
        )

        for line in lines:

            line = line.strip()

            if (
                line.startswith("•")
            ):

                experiences.append(
                    line.replace(
                        "•",
                        ""
                    ).strip()
                )

        return experiences