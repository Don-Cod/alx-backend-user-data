#!/usr/bin/env python3
"""Encrypting passwords Modules
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes password through random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks password formed from given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
