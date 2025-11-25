c11 = {
    "id": "c11",
    "name": "Quarters C-11",
    "description": (
        "You wake up groggy on your bed in Vault 123. The room is dim—only the "
        "emergency floor strips glow faint blue. Your left forearm is bare. "
        "Your Pip-Boy is missing. The door is sealed, its status light glowing yellow."
    ),
    "objects": {
        "bed": {
            "id": "bed",
            "kind": "scenery",
            "description": (
                "The bed is a mess—twisted sheets, pillow on the floor. It looks like "
                "someone pulled you out of it rather than waking you."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "locker": {
            "id": "locker",
            "kind": "scenery",
            "description": (
                "The steel locker is slightly ajar. A dent near the handle suggests "
                "it was forced open. Inside, your jumpsuit is folded, but your "
                "belongings box and Pip-Boy cradle are missing."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "floor": {
            "id": "floor",
            "kind": "scenery",
            "description": (
                "A small plastic syringe cap lies on the floor—standard Medbay issue. "
                "You don't remember receiving any treatment."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "desk": {
            "id": "desk",
            "kind": "scenery",
            "description": (
                "A metal desk is bolted to the floor. On top of it sits a dark, unpowered "
                "terminal and a single Vault-Tec holotape."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "terminal": {
            "id": "terminal",
            "kind": "scenery",
            "description": (
                "The terminal's screen is completely dark. With emergency power only, it "
                "won't even attempt to boot."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "holotape": {
            "id": "holotape",
            "kind": "actionable",
            "description": (
                "A Vault-Tec holotape with a worn label. Without your Pip-Boy, there's no "
                "way to read or play whatever's on it."
            ),
            "can_take": True,
            "can_talk": False,
            "needs_item": "pip-boy",
            "is_exit": False,
        },
        "vent": {
            "id": "vent",
            "kind": "scenery",
            "description": (
                "The ventilation grate clicks on and off, cycling air irregularly. "
                "Something in the system is struggling."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "intercom": {
            "id": "intercom",
            "kind": "actionable",
            "description": (
                "A standard Vault intercom used for communication with Security."
            ),
            "can_take": False,
            "can_talk": True,
            "is_exit": False,
            "dialog_id": "intercom_c11",
        },
        "pillow": {
            "id": "pillow",
            "kind": "hint",
            "description": (
                "You pick up the pillow from the floor. The case is slightly unzipped. "
                "Inside the pillowcase, you find a tightly folded note. It reads: "
                "\"You're in danger! Come find me and don't trust anyone!\"\n"
                "You recognize the hurried scribble — it's your friend Juno.\n"
                "You put the pillow back, wondering how or when that information might be useful..."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "door": {
            "id": "door",
            "kind": "actionable",
            "description": (
                "A standard sliding Vault door. The status light glows yellow — local lockdown. "
                "Normally it opens at a touch, but right now it's sealed by an override from outside."
            ),
            "description_unlocked": "A standard sliding Vault door. The status light glows green - it's unlocked.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {
        "door": {
            "destination": "hallway_ground",  # state
            "status": "locked",  # locked | unlocked | jammed | sealed
            "unlocked_via": "intercom",
            "required_item": None,  # item (pip-boy) or None
            "unlock_on_use": False,  # if using it performs unlock
            # descriptions
            "description_locked": (
                "A standard sliding Vault door. The status light glows yellow — local lockdown. "
                "Normally it opens at a touch, but right now it's sealed by an override from outside."
            ),
            "description_unlocked": "A standard sliding Vault door. The status light glows green - it's unlocked.",
            # optional: custom text or event when attempting to open
            "on_attempt": None,
            "on_unlock": None,
        }
    },
    "flags": {},
}
