import os
from jwt import decode
from fastapi import Depends, Header, HTTPException
from fastapi.params import Depends, Depends
from fastapi import HTTPException
from src.config.database import Session, get_db
from enums.http_enum import HttpStatus


def auth_token(authorization):
    AUTH = os.getenv('JWT_SECRET') or 'ADMIN'
    if not authorization or not authorization.startswith('Bearer '):
        raise HTTPException(HttpStatus.UNAUTHORIZED, detail='Fail of authorization of token')

    token = authorization.split(' ')[1]
    payload = decode(token, AUTH, algorithms=['HS256'])
    return payload.get('user')