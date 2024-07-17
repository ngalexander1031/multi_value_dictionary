Requirements:
Python 3.8.10
pytest 8.2.2

Usage:
To run this application, please execute 'python mvd.py'

Overview
The Multi-Value Dictionary application provides a set of commands to interact with an in-memory dictionary:

KEYS: List all keys in the dictionary.
> KEYS

MEMBERS: List all members for a given key.
> MEMBERS key

ADD: Add a member to a key.
> ADD key member

REMOVE: Remove a member from a key.
> REMOVE key member

REMOVEALL: Remove all members from a key.
> REMOVEALL key

CLEAR: Clear all keys and members from the dictionary.
> CLEAR

KEYEXISTS: Check if a key exists.
> KEYEXISTS key

MEMBEREXISTS: Check if a member exists within a key.
> MEMBEREXISTS key member

ALLMEMBERS: List all members in the dictionary.
> ALLMEMBERS

ITEMS: List all keys and their members in the dictionary.
> ITEMS

HISTORY: Returns the up to the last 10 most recent calls.
> HISTORY

HELP: Provide aid to those that need help.
> HELP

EXIT: Exits program.
> EXIT

Tests:
Unit tests are provided to ensure the functionality of MVD.
To run tests, use 'pytest test_mvd.py'