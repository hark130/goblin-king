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
EQUIP_CLOTHING_DB: Final[Database] = Database('Clothing', EQUIPMENT_DIR.joinpath('clothing.db'))
# Equipment/Food
EQUIP_FOOD_DB: Final[Database] = Database('Food', EQUIPMENT_DIR.joinpath('food.db'))
# Equipment/Misc
EQUIP_MISC_DB: Final[Database] = Database('Misc', EQUIPMENT_DIR.joinpath('misc.db'))
# Equipment/Tool
EQUIP_TOOL_DB: Final[Database] = Database('Tool', EQUIPMENT_DIR.joinpath('tool.db'))
# Equipment/Weapon
EQUIP_WEAPON_DB: Final[Database] = Database('Weapon', EQUIPMENT_DIR.joinpath('weapon.db'))
# Equipment Database List
EQUIP_DB_LIST: Final[List[Database]] = [EQUIP_CLOTHING_DB,
                                        EQUIP_FOOD_DB,
                                        EQUIP_MISC_DB,
                                        EQUIP_TOOL_DB,
                                        EQUIP_WEAPON_DB,
                                        ]

# MENUS
MAIN_MENU: Final = Menu('GOBLIN KING', {1: 'Randomize equipment', 2: 'Randomize a character',
                                        999: 'EXIT'})
