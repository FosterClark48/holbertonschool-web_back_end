#!/usr/bin/env python3
""" BasicAuth method """
from api.v1.auth.auth import Auth


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
