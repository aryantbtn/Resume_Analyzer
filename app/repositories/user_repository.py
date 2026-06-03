from app.database.mysql_connection import Database


class UserRepository:

    @staticmethod
    def get_user_by_email(email):

        connection = Database.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT *
        FROM users
        WHERE email = %s
        """

        cursor.execute(query, (email,))

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user

    @staticmethod
    def create_user(
        full_name,
        email,
        password_hash
    ):

        connection = Database.get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO users
        (
            full_name,
            email,
            password_hash
        )
        VALUES
        (
            %s,
            %s,
            %s
        )
        """

        cursor.execute(
            query,
            (
                full_name,
                email,
                password_hash
            )
        )

        user_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return user_id