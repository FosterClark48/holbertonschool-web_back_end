#!/usr/bin/env python3
""" BasicAuth method """
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class to manage basic authentication """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extracts the Base64 encoded part of an Authorization header. """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes a Base64 encoded Authorization header. """
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None

        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extracts user email and password from a Base64 decoded value """
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)
        # Argument '1' ensures only the first ':' is used for splitting
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on email and password """
        if (user_email is None or type(user_email) is not str or
                user_pwd is None or type(user_pwd) is not str):
            return None

        # Try fetching users w/ provided email
        users = User.search({'email': user_email})

        # Check if any user was found w/ given email
        if not users:
            return None

        # Assuming the email is unique and we get a single user back
        user = users[0]

        # Verify password for fetched user
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the User instance for a request """

        # 1. Get the Authorization header
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        # 2. Extract the Base64 part of the Authorization header
        base64_header = self.extract_base64_authorization_header(auth_header)
        if not base64_header:
            return None

        # 3. Decode the Base64 string
        decoded_header = self.decode_base64_authorization_header(
            base64_header)
        if not decoded_header:
            return None

        # 4. Extract user email and password from the decoded string
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        if not user_email or not user_pwd:
            return None

        # 5. Fetch the User object using the email and password
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
