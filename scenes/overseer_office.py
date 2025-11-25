overseer_office = {
    "id": "overseer_office",
    "name": "Overseer's Office",
    "description": (
        "The Overseer's Office overlooks parts of the Vault through thick glass. A large desk dominates "
        "the room, with a secure terminal built into its surface."
    ),
    "objects": {
        "desk": {
            "kind": "scenery",
            "description": "A heavy desk piled with reports and access logs.",
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "overseer_terminal": {
            "kind": "actionable",
            "description": (
                "A secured Overseer terminal with access to system logs and security alerts."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "dialog_id": "overseer_terminal_menu",
        },
    },
    "exits": {"hallway": "hallway_upper"},
    "flags": {"sector7_alert_raised": False, "door_locked": False},
}
