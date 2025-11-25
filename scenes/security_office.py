security_office = {
    "id": "security_office",
    "name": "Security Office",
    "description": (
        "The Security Office is lined with monitors and weapon lockers. Normally it's staffed, "
        "but at times it can be eerily empty."
    ),
    "objects": {
        "consoles": {
            "kind": "scenery",
            "description": "Banks of consoles show camera feeds from across the Vault.",
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "lockers": {
            "kind": "scenery",
            "description": "Heavy-duty lockers used for storing equipment and personal gear.",
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "pipboy_cradle": {
            "kind": "scenery",
            "description": (
                "An empty Pip-Boy cradle with a faint outline where one usually rests."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
    },
    "exits": {"hallway": "hallway_upper"},
    "flags": {"occupied": True, "pipboy_available": False, "door_locked": False},
}
