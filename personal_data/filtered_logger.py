#!/usr/bin/env python3
""" filtered_logger.py module

This module contains the RedactingFormatter class for logging, which
inherits from logging.Formatter. It redacts sensitive information
(fields like email, ssn, password, etc.) from the log records.

Classes:
    RedactingFormatter: A logging formatter that redacts sensitive fields.

Functions:
    filter_datum(fields, redaction, message, separator): Obfuscates specific
    fields in a log message.
"""

import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "ssn", "password", "phone")


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


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object named "user_data" configured to log
    messages up to the INFO level and redact PII fields.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger


def get_db():
    """ Returns a connector to the database """
    # Getting credentials from env variables
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    # Establish the database connection
    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )
    return db
