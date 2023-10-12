"""
Terminal prompt endowed with persistent memory that echoes last choices
made and provide them as default.
"""

__version__ = "0.0.1-beta"

from InquirerPy import inquirer
from trapdoor import Trapdoor


class EchoPrompt:
    def __init__(self, store_name):
        self.history = Trapdoor(store_name)

    def prompt_choice(self, name, choices):
        res = inquirer.select(
            message=name.replace("_", " ").title(),
            choices=choices,
            default=self.history.get(name),
        ).execute()
        if res:
            self.history.set(name, res)
        return res
