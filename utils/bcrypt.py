import bcrypt

# Method for password encryption
def hash_password(password):
    salt = bcrypt.gensalt(10)
    encrypted_pass = bcrypt.hashpw(password.encode('utf-8'), salt)

    # password with hash algorithm with salt 10
    return encrypted_pass.decode('utf-8')
