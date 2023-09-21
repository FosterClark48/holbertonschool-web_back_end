#!/usr/bin/env python3
""" BasicAuth method """
from api.v1.auth.auth import Auth
import base64


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