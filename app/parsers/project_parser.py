import re


class ProjectParser:

    @staticmethod
    def extract_projects(
        project_section
    ):

        projects = []

        lines = (
            project_section.splitlines()
        )

        for line in lines:

            line = line.strip()

            if (
                line.startswith("–")
                or
                line.startswith("-")
            ):

                project_name = (
                    line.replace(
                        "–",
                        ""
                    )
                    .replace(
                        "-",
                        ""
                    )
                    .strip()
                )

                projects.append(
                    project_name
                )

        return projects