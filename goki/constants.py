"""Module containting constant definitions for GOBLIN KING (GOKI)."""

# Standard Imports
from typing import Final
# Third Party Imports
# Local Imports
from goki.menu import Menu

# MENUS
MAIN_MENU: Final = Menu('GOBLIN KING', {1: 'Randomize equipment', 2: 'Randomize a character',
                                        999: 'EXIT'})
