"""Define top-level GOBLIN KING (GOKI) functionality."""

# Standard Imports
# Third Party Imports
# Local Imports
from goki.constants import EQUIP_FOOD_DB, MAIN_MENU
from goki.menu import get_choice
from goki.misc import print_exception
from goki.rando import rando_db_entries, rando_db_entry


def main() -> int:
    """GOBLIN KING (GOKI) entry point.

    Returns:
        0 on successful usage.
        1 on bad environment (e.g., missing/corrupt database, bug)
        2 on bad user input (e.g., invalid input)
        3 on unspecified error (e.g., ?!?!?!)
    """
    # LOCAL VARIABLES
    ret_val = 0          # Return value: 0 success, 1 bad env, 2 bad input
    clear_screen = True  # Controls whether get_choice() clears the screen
    user_input = 0       # Main menu user choice

    # MENU
    while ret_val == 0:
        # Main Menu
        try:
            user_input = get_choice(MAIN_MENU, choice_type=int, return_choice=True,
                                    clear_screen=clear_screen)
        except (TypeError, ValueError) as err:
            print_exception(err)
            ret_val = 1
        except RuntimeError as err:
            print_exception(err)
            ret_val = 2
        except Exception as err:
            print_exception(err)
            ret_val = 3
        finally:
            if ret_val != 0:
                break

        # User Selection
        try:
            # 1: Randomize Equipment
            if user_input == 1:
                print(f'One item: {rando_db_entry(EQUIP_FOOD_DB.path_obj)}')
                print(f'Ten items:{rando_db_entries(EQUIP_FOOD_DB.path_obj, 10)}')
                clear_screen = False  # Don't clear the results
            # 2: Randomize Character
            elif user_input == 2:
                print_exception(NotImplementedError('The "randomize character" feature is not done.'))
            # 999: Exit
            elif user_input == 999:
                break
            else:
                ret_val = 3  # How did we get here?!
        except (TypeError, ValueError, FileNotFoundError, LookupError) as err:
            print_exception(err)
            ret_val = 1
        except Exception as err:
            print_exception(err)
            ret_val = 3

    # DONE
    return ret_val
