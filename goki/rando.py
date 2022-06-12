"""Randomize things."""

# Standard Imports
from pathlib import Path
from typing import List
import random
# Third Party Imports
# Local Imports


def rando_db_entry(db_file: Path) -> str:
    """Randomize an entry from a GOKI database.

    Returns a random, non-empty, entry from db_file.

    Args:
        db_file: Path object to a newline-delimited, non-empty database.

    Raises:
        TypeError: db_file is not a Path object.
        FileNotFoundError: db_file does not exist.
        LookupError: db_file does not contain valid entries.
        OSError: db_file exists but is not a file.

    Returns:
        Random entry from db_file on success.
    """
    # LOCAL VARIABLES
    db_entries = _get_db_entries(db_file)  # Database entries
    entry = random.choice(db_entries)      # Database entry to return

    # DONE
    print(f'rando_db_entry({str(db_file)}) returning {entry}')
    return entry


def rando_db_entries(db_file: Path, num_entries: int) -> List[str]:
    """Randomize multiple entries from a GOKI database.

    Returns a list of random, non-empty, unique entries from db_file.

    Args:
        db_file: Path object to a newline-delimited, non-empty database.
        num_entries: Number of unique entries to randomize.

    Raises:
        FileNotFoundError: db_file does not exist.
        LookupError: db_file does not contain valid entries.
        RuntimeError: db_file does not contain at least num_entries of entries, or failed
            processing.
        TypeError: Bad data type.
        ValueError: Invalid value in num_entries.

    Returns:
        List of random, unique entries from db_file on success.
    """
    # LOCAL VARIABLES
    db_entries = []  # Database entries
    entry_list = []  # Random selections to return
    temp_entry = ''  # Temporary random selection

    # INPUT VALIDATION
    # _get_db_entries() validates db_file
    [db_entries.append(entry) for entry in _get_db_entries(db_file) if entry not in db_entries]
    if not isinstance(num_entries, int):
        raise TypeError(f'num_entries must be of type int instead of {type(num_entries)}')
    if num_entries < 1:
        raise ValueError(f'num_entries must be greater than 0')
    if num_entries > len(db_entries):
        raise RuntimeError(f'The {str(db_file)} only contains {len(db_entries)} which is not '
                           f'enough to randomize {num_entries} entries.')

    # DO IT
    while True:
        temp_entry = random.choice(db_entries)
        if temp_entry not in entry_list:
            entry_list.append(temp_entry)
            db_entries.remove(temp_entry)
        else:
            raise RuntimeError(f'How did we get here?!  Was {temp_entry} somehow non-unique '
                               f'in source {db_entries} and destination {entry_list}?!')
        if len(entry_list) == num_entries:
            break  # Done

    # DONE
    return entry_list


def _get_db_entries(db_file: Path) -> List[str]:
    """Read database entries.

    Returns a list of valid database entries read from db_file.

    Args:
        db_file: Path object to a newline-delimited, non-empty database.

    Raises:
        FileNotFoundError: db_file does not exist.
        LookupError: db_file does not contain valid entries.
        OSError: param exists but is not a file.
        TypeError: db_file is not a Path object.

    Returns:
        Random entry from db_file on success.
    """
    # LOCAL VARIABLES
    db_entries = []  # Database entries

    # INPUT VALIDATION
    _validate_path_file(db_file, 'db_file')

    # READ DB
    with open(db_file, 'r') as in_file:
        db_entries = [entry.lower() for entry in in_file.read().split() if entry]
    if not db_entries:
        raise LookupError(f'{str(db_file)} did not contain any valid database entries')

    # DONE
    return db_entries


def _validate_path_file(param: Path, param_name: str) -> None:
    """Validate that a Path object exists as a file.

    Args:
        param: Path object to validate.
        param_name: Original name of the parameter being validated.

    Raises:
        FileNotFoundError: param does not exist.
        OSError: param exists but is not a file.
        TypeError: path_obj is not a Path object.
    """
    if not isinstance(param, Path):
        raise TypeError(f'{param_name} must be of type Path instead of {type(param)}')
    if not param.exists():
        raise FileNotFoundError(f'Unable to locate {str(param)}')
    if not param.is_file():
        raise OSError(f'{str(param)} is not a file')
