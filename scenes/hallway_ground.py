hallway_ground = {
    "id": "hallway_ground",
    "name": "Ground Floor Hallway",
    "description": (
        "A long, curved hallway lined with numbered doors and flickering wall lamps. "
        "Signs point toward Security, the Overseer's office upstairs, and the main Vault Door."
    ),
    "objects": {
        "signs": {
            "id": "signs",
            "kind": "scenery",
            "description": (
                "Directional signs point toward Quarters C-11, J-23, Security, the Overseer's office, "
                "and the Vault Door."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "c11door": {
            "id": "c11door",
            "kind": "actionable",
            "description": "The door to Quarters C-11. Your room.",
            "description_unlocked": "The door to Quarters C-11. Your room.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        "j23door": {
            "id": "j23door",
            "kind": "actionable",
            "description": "The door leading to Juno's quarters, J-23.",
            "description_unlocked": "The door leading to Juno's quarters, J-23.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        "vaultdoor": {
            "id": "vaultdoor",
            "kind": "actionable",
            "description": "A heavy bulkhead door leading toward the main Vault Door.",
            "description_unlocked": "A heavy bulkhead door leading toward the main Vault Door.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        "stairwell": {
            "id": "stairwell",
            "kind": "actionable",
            "description": "A metal stairwell leading to the upper floor.",
            "description_unlocked": "A metal stairwell leading to the upper floor.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {
        "c11door": {
            "destination": "c11",
            "status": "unlocked",  # locked | unlocked | jammed | sealed
            "unlocked_via": None,
            "required_item": None,
            "unlock_on_use": False,
            "description_locked": "The door to Quarters C-11. Your room.",
            "description_unlocked": "The door to Quarters C-11. Your room.",
            "on_attempt": None,
            "on_unlock": None,
        },
        "j23door": {
            "destination": "j23",
            "status": "unlocked",
            "unlocked_via": None,
            "required_item": None,
            "unlock_on_use": False,
            "description_locked": "The door leading to Juno's quarters, J-23.",
            "description_unlocked": "The door leading to Juno's quarters, J-23.",
            "on_attempt": None,
            "on_unlock": None,
        },
        "vaultdoor": {
            "destination": "vault_door_room",
            "status": "unlocked",
            "unlocked_via": None,
            "required_item": None,
            "unlock_on_use": False,
            "description_locked": "A heavy bulkhead door leading toward the main Vault Door.",
            "description_unlocked": "A heavy bulkhead door leading toward the main Vault Door.",
            "on_attempt": None,
            "on_unlock": None,
        },
        "stairwell": {
            "destination": "hallway_upper",
            "status": "unlocked",
            "unlocked_via": None,
            "required_item": None,
            "unlock_on_use": False,
            "description_locked": "A metal stairwell leading to the upper floor.",
            "description_unlocked": "A metal stairwell leading to the upper floor.",
            "on_attempt": None,
            "on_unlock": None,
        },
    },
    "flags": {},
}
