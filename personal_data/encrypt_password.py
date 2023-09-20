#!/usr/bin/env python3
"""
Encrypt Password Module
=======================

This module provides functionalities for securely hashing passwords,
making use of the bcrypt hashing algorithm to ensure password data
security.
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt and returns a salted, hashed byte string.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
