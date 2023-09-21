#!/usr/bin/env python3
""" Auth module for handling authentication
"""
from typing import List, TypeVar
from flask import request


User = TypeVar('User')


class Auth():
    """ Auth class to manage API Authentication
    This class serves as a template for all authentication systems.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to determine if a given path requires authentication.
        Args:
            path (str): The path from the request.
            excluded_paths (List[str]): List of excluded paths
            from authentication.

        Returns:
            bool: Always returns `False`. This behavior will change
            in the future.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to fetch the value of the authorization header.
        Args:
            request (flask.Request, optional): The request object from Flask.
            Defaults to None.

        Returns:
            str: Always returns `None`.
            This behavior will change in the future.
        """
        return None

    def current_user(self, request=None) -> User:
        """ Method to fetch the current user.
        Args:
            request (flask.Request, optional): The request object from Flask.
            Defaults to None.

        Returns:
            User: Always returns `None`.
            This behavior will change in the future.
        """
        return None
