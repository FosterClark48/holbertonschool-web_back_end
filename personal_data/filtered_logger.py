#!/usr/bin/env python3
"""
filtered_logger Module
======================

This module provides functionality for logging with specific data redaction
capabilities. It is designed to handle various types of Personally
Identifiable Information (PII) by filtering them out or replacing them
with a fixed redaction string when logging.

The module includes:
- A customized logging formatter (`RedactingFormatter`) that can redact
specified fields.
- A function (`get_db`) for obtaining a MySQL database connection.
- A `main` function for retrieving and logging user data from a database
in a redacted format.

Functions:
-----------
- `filter_datum(fields: List[str], redaction: str, message: str,
separator: str) -> str`
    Takes a string message and redacts specific fields.

- `get_logger() -> logging.Logger`
    Returns a logging object that has been configured to use
    the RedactingFormatter.

- `get_db() -> mysql.connector.connection.MySQLConnection`
    Returns a connector to the database.

- `main() -> None`
    Retrieves and logs user data in a redacted format.

Usage:
------
    $ python3 filtered_logger.py

Notes:
------
- Environment variables are used to get the database credentials.
- Only the `main` function should run when the module is executed directly.

Author: Foster
"""

import re
from typing import List, NoReturn
import logging
import os
from mysql.connector.connection import MySQLConnection
import mysql.connector


# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[HOLBERTON] user_data")


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


def get_db() -> MySQLConnection:
    """ Returns a connector to the database """
    # Getting credentials from env variables
    username: str = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password: str = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host: str = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name: str = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    # Establish the database connection
    db: MySQLConnection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )
    return db


def main() -> NoReturn:
    """
    Main function that retrieves all rows from the users table and logs them.
    Connects to the database, executes a SELECT query, and logs the results
    in a redacted format.

    Returns:
        NoReturn: The function returns nothing.
    """
    # Obtain database connection
    db = get_db()

    # Initialize cursor
    cursor = db.cursor()

    # SQL to fetch all rows from the users table
    cursor.execute("SELECT * FROM users;")

    # Loop through each row and log in the specific format
    for row in cursor:
        user_data = {
            "name": row[0],
            "email": row[1],
            "phone": row[2],
            "ssn": row[3],
            "password": row[4],
            "ip": row[5],
            "last_login": row[6],
            "user_agent": row[7]
        }

        # Convert user_data dict to message string
        message = "; ".join(
            [f"{key}={value}" for key, value in user_data.items()]
        )

        # Apply filtering
        redacted_message = filter_datum(["name",
                                         "email",
                                         "phone",
                                         "ssn",
                                         "password"], "***", message, "; ")

        # Log the redacted_message
        logger.info(redacted_message)

    cursor.close()
    db.close()

# Only run main when the module is executed
if __name__ == "__main__":
    main()
