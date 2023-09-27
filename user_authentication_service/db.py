#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import SQLAlchemyError, InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ This method saves the user to the DB """
        user = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(user)
            self.__session.commit()
            return user
        except SQLAlchemyError as e:
            self._session.rollback()
            raise e

    def find_user_by(self, **kwargs) -> User:
        """ Returns first row found in users table as filtered by
        the method's input arguments
        """
        try:
            # return first User obj that matches filter criteria specified
            # by kwargs, show exactly one row of results - one()
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise
