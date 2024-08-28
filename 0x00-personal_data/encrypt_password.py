#!/usr/bin/env python3
"""Module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes tha password using a random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks is tha hashed password was formed from tha given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
