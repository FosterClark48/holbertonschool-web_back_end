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
            bool: Returns `True` if path needs authentication,
            otherwise `False`.
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Make sure the path has a trailing slash for comparison
        # if path doesnt end with a slash put one on there otherwise leave it
        path = path + '/' if not path.endswith('/') else path

        if path in excluded_paths:
            return False

        return True

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
