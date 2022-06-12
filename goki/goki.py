"""Define top-level GOBLIN KING (GOKI) functionality."""

# Standard Imports
# Third Party Imports
# Local Imports
from goki.constants import MAIN_MENU
from goki.menu import get_choice
from goki.misc import print_exception


def main() -> int:
    """GOBLIN KING (GOKI) entry point.

    Returns:
        0 on successful usage.
        1 on bad environment (e.g., missing/corrupt database, bug)
        2 on bad user input (e.g., invalid input)
        3 on unspecified error (e.g., ?!?!?!)
    """
    # LOCAL VARIABLES
    ret_val = 0     # Return value: 0 success, 1 bad env, 2 bad input
    user_input = 0  # Main menu user choice

    # MENU
    while ret_val == 0:
        # Main Menu
        try:
            user_input = get_choice(MAIN_MENU, choice_type=int, return_choice=True)
        except (TypeError, ValueError) as err:
            print_exception(err)
            ret_val = 1
        except RuntimeError as err:
            print_exception(err)
            ret_val = 2
        except Exception as err:
            print_exception(err)
            ret_val = 3
        else:
            print(f'User chose {user_input} which is of type {type(user_input)}')  # DEBUGGING
        finally:
            if ret_val != 0:
                break

        # User Selection
        # 1: Randomize Equipment
        if user_input == 1:
            print_exception(NotImplementedError('The "randomize equipment" feature is not done.'))
        # 2: Randomize Character
        elif user_input == 2:
            print_exception(NotImplementedError('The "randomize character" feature is not done.'))
        # 999: Exit
        elif user_input == 999:
            break
        else:
            ret_val = 3  # How did we get here?!

    # DONE
    return ret_val
