#!/usr/bin/env python3
""" Auth module """
import bcrypt
from uuid import uuid4
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user with the given email and password """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            # if no user is found w/ email, create one
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates if login credentials are correct """
        try:
            user = self._db.find_user_by(email=email)
            hashed_pwd = user.hashed_password
            return bcrypt.checkpw(password.encode('utf-8'), hashed_pwd)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Finds user corresponding w/ email and creates session id """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str):
        """ Get the user from a session id """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Takes a user ID and sets its session ID to None """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """This function receives a password string and returns its hashed version
    as bytes. The returned bytes are a salted hash of the input password.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """ Generates UUID and returns it as a string """
    return str(uuid4())
