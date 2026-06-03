class User:

    def __init__(
        self,
        id=None,
        full_name=None,
        email=None,
        password_hash=None,
        created_at=None
    ):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at