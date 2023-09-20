#!/usr/bin/env python3
""" This is the filter_datum module

This module contains a function filter_datum that returns
an obfuscated log message.
"""

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    This function takes a list of field names to be obfuscated (redacted)
    within a log message. It uses regular expressions to identify the fields
    and replaces their values with a redaction string. The fields in the log
    message are assumed to be separated by a specified separator.

    Parameters:
    - fields (list of str): The names of the fields to be obfuscated.
      e.g., ["password", "date_of_birth"]

    - redaction (str): The string to replace the field values with.
      e.g., "xxx"

    - message (str): The log message containing key-value pairs of fields.
      e.g., "name=John;password=123;date_of_birth=01/01/1990;"

    - separator (str): The character that separates each key-value pair in
    the message.
      e.g., ";"

    Returns:
    - str: The log message with the specified fields obfuscated.
      e.g., "name=John;password=xxx;date_of_birth=xxx;"

    Example:
    >>> filter_datum(["password", "date_of_birth"], "xxx",
    "name=John;password=123;date_of_birth=01/01/1990;", ";")
    "name=John;password=xxx;date_of_birth=xxx;"
    """
    return re.sub(f'({"|".join(fields)})=([^;{separator}]*)',
                  lambda m: f"{m.group(1)}={redaction}", message)
