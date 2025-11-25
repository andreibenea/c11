hallway_upper = {
    "id": "hallway_upper",
    "name": "Upper Floor Hallway",
    "description": (
        "A quieter upper corridor with reinforced doors. Placards indicate the Security Office "
        "and the Overseer's Office."
    ),
    "objects": {
        "door": {
            "kind": "actionable",
            "description": "A standard sliding Vault door. The status light glows green - it's unlocked.",
            "description_unlocked": "A standard sliding Vault door. The status light glows green - it's unlocked.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {
        "stairs_down": "hallway_ground",
        "security_office": "security_office",
        "overseer_office": "overseer_office",
    },
    "flags": {"door_locked": False},
}
