import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt(10)
    encrypted_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return encrypted_pass.decode('utf-8')