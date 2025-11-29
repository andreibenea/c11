COMMANDS = {
    "help": {
        "default_action": "help",
        "modifiers": {},  # no sub-actions
        "min_args": 0,
        "max_args": 0,
    },
    "info": {
        "default_action": "help",
        "modifiers": {},
        "min_args": 0,
        "max_args": 0,
    },
    "look": {
        "default_action": "examine",
        # e.g. "look around", "look around for a bit"
        "modifiers": {
            "around": "look_around",
        },
        "min_args": 0,
        "max_args": 10,  # high ceiling since you allow natural phrases
    },
    "examine": {
        "default_action": "examine",
        "modifiers": {},
        "min_args": 1,
        "max_args": 10,
    },
    "inspect": {
        "default_action": "examine",
        "modifiers": {},
        "min_args": 1,
        "max_args": 10,
    },
    "use": {
        "default_action": "use",
        "modifiers": {},
        "min_args": 1,
        "max_args": 10,
    },
    "take": {
        "default_action": "take",
        "modifiers": {},
        "min_args": 1,
        "max_args": 10,
    },
    "pick": {
        "default_action": "take",  # "pick <thing>" behaves like "take <thing>"
        "modifiers": {
            "up": "take",  # "pick up <thing>"
        },
        "min_args": 1,
        "max_args": 10,
    },
    "talk": {
        "default_action": "talk",
        "modifiers": {},
        "min_args": 1,
        "max_args": 10,
    },
    "go": {
        "default_action": "exit_room",
        "modifiers": {
            "to": "exit_room",  # "pick up <thing>"
        },
        "min_args": 1,
        "max_args": 10,
    },
    "exit": {
        # default behavior = leave room through an exit
        "default_action": "exit_room",
        "modifiers": {
            "game": "exit_game",  # "exit game", "exit the game now"
            "room": "exit_room",  # explicit form: "exit room"
        },
        "min_args": 0,
        "max_args": 10,
    },
    "quit": {
        # treat "quit" like "exit"
        "default_action": "exit_game",
        "modifiers": {
            "game": "exit_game",
        },
        "min_args": 0,
        "max_args": 10,
    },
}
