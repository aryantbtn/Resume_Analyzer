from app.database.mysql_connection import Database


class ResumeRepository:

    @staticmethod
    def get_resume_by_hash(file_hash):

        conn = Database.get_connection()

        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT *
        FROM resumes
        WHERE file_hash = %s
        """

        cursor.execute(
            query,
            (file_hash,)
        )

        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def save_resume(
        user_id,
        original_filename,
        stored_filename,
        file_hash
    ):

        conn = Database.get_connection()

        cursor = conn.cursor()

        query = """
        INSERT INTO resumes
        (
            user_id,
            original_filename,
            stored_filename,
            file_hash
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        """

        cursor.execute(
            query,
            (
                user_id,
                original_filename,
                stored_filename,
                file_hash
            )
        )

        resume_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return resume_id