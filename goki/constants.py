"""Module containting constant definitions for GOBLIN KING (GOKI)."""

# Standard Imports
from collections import namedtuple
from pathlib import Path
from typing import Final, List
# Third Party Imports
# Local Imports
from goki.menu import Menu

Database = namedtuple('Database', 'name path_obj')


# DATABASES
# Directories
DATABASE_DIR: Final[Path] = Path.cwd().joinpath('goki', 'databases')  # Database directory
EQUIPMENT_DIR: Final[Path] = DATABASE_DIR.joinpath('equipment')  # Database/Equipment directory
# Equipment/Clothing
EQUIP_CLOTHING_DB: Final[Database] = Database('Equipment', EQUIPMENT_DIR.joinpath('clothing.db'))
# Equipment/Food
EQUIP_FOOD_DB: Final[Database] = Database('Equipment', EQUIPMENT_DIR.joinpath('food.db'))
# Equipment Database List
EQUIP_DB_LIST: Final[List[Database]] = [EQUIP_CLOTHING_DB, EQUIP_FOOD_DB]

# MENUS
MAIN_MENU: Final = Menu('GOBLIN KING', {1: 'Randomize equipment', 2: 'Randomize a character',
                                        999: 'EXIT'})
