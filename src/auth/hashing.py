from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
