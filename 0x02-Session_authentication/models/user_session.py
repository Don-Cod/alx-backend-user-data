#!/usr/bin/env python3
"""User sessionHandle _module.
"""
from models.base import Base


class UserSession(Base):
    """user_session_class.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """Initializes session instance.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
