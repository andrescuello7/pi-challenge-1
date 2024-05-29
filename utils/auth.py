import os
from jwt import decode
from fastapi import HTTPException

# Validation JWT in case expired [ UserModel or 401 ]


def auth_token(authorization):
    if not authorization or not authorization.startswith('Bearer '):
        # JWT expired return error 401
        raise HTTPException(
            401, detail='Fail of authorization of token')

    hash_token = authorization.split(' ')[1]
    result = decode(hash_token, os.getenv(
        'JWT_SECRET'), algorithms=['HS256'])

    # Return object user with dates of schema UserModel
    return result.get('user')
