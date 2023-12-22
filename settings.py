"""Functions to support configuration amongst environments"""
import os
import pathlib

from dotenv import load_dotenv


class Config:
    """Class to get any environment variable passed in"""

    def __init__(self):
        pass

    def __getattr__(self, attr: str):
        variable = os.getenv(attr)
        if variable == "":
            return None
        return variable

    def load(self):
        """Load"""
        load_dotenv(override=True)
        return self


BASE_DIR = pathlib.Path(__file__).parent

HIDDEN_COMMANDS_DIR = BASE_DIR / "hidden_commands"
APPLICATION_COMMANDS_DIR = BASE_DIR / "application_commands"
COGS_DIR = BASE_DIR / "cogs"
