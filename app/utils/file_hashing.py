import hashlib


class FileHasher:

    @staticmethod
    def generate_hash(file_bytes):

        return hashlib.sha256(
            file_bytes
        ).hexdigest()