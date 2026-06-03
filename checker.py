from app.utils.hashing import PasswordHasher

print("Starting Test...")

hashed = PasswordHasher.hash_password("123456")

print("Hash:", hashed)