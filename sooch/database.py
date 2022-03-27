from enum import Enum


class Scopes(Enum):
    NONE = 0
    PLAYER_RAW = 1
    PLAYER_FULL = 2
    SERVER_ONLY = 3
    PLAYER_RAW_AND_SERVER = 4
    PLAYER_AND_SERVER = 5


def load_contexts(scopes):
    if scopes == Scopes.NONE:
        return {}
    elif scopes == Scopes.PLAYER_ONLY:
        return {}
    elif scopes == Scopes.SERVER_ONLY:
        return {}
    else:
        return {}
