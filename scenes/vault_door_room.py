vault_door_room = {
    "id": "vault_door_room",
    "name": "Vault Door Antechamber",
    "description": (
        "You stand before the massive gear-shaped Vault Door. Warning lights blink slowly. "
        "A control podium sits nearby, blank where a Pip-Boy interface should be."
    ),
    "objects": {
        "vault_door": {
            "kind": "actionable",
            "description": (
                "The colossal Vault Door is sealed shut. Mechanical locks and massive hinges hold it in place."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        "control_podium": {
            "kind": "scenery",
            "description": (
                "A control podium with a recessed Pip-Boy docking port and a small status display."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "door": {
            "kind": "actionable",
            "description": "A standard sliding Vault door. The status light glows green - it's unlocked.",
            "description_unlocked": "A standard sliding Vault door. The status light glows green - it's unlocked.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {"hallway": "hallway_ground", "outside": "outside"},
    "flags": {
        "vault_unlocked": False,
        "door_locked": False,
    },
}
