#!/usr/bin/env python3
""" This is the filter_datum module

This module contains a function filter_datum that returns
an obfuscated log message.
"""

import re
from typing import List
import logging


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    This class inherits from logging.Formatter and redacts specific fields in
    log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize the formatter.

        Args:
            fields (list): List of field names to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log record.

        Args:
            record (logging.LogRecord): The log record.

        Returns:
            str: Formatted log record with specified fields redacted.
        """
        original_msg = logging.Formatter.format(self, record)
        return filter_datum(self.fields,
                            self.REDACTION, original_msg, self.SEPARATOR)
