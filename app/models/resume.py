class Resume:

    def __init__(
        self,
        id=None,
        user_id=None,
        original_filename=None,
        stored_filename=None,
        file_hash=None,
        upload_time=None
    ):

        self.id = id
        self.user_id = user_id
        self.original_filename = original_filename
        self.stored_filename = stored_filename
        self.file_hash = file_hash
        self.upload_time = upload_time