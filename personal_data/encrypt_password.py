#!/usr/bin/env python3
"""
Encrypt Password Module
=======================

This module provides functionalities for securely hashing passwords,
making use of the bcrypt hashing algorithm to ensure password data
security.

Functions:
----------
- `hash_password(password: str) -> bytes`:
    Hashes a plain-text password and returns the salted, hashed byte-string.

- `is_valid(hashed_password: bytes, password: str) -> bool`:
    Validates that a plain-text password matches the hashed password.

Dependencies:
-------------
- bcrypt
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
    salt = bcrypt.gensalt()  # Generate a salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against a hashed password using bcrypt.

    Args:
        hashed_password (bytes): The hashed password to compare against.
        password (str): The plain-text password to validate.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
