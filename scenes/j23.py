j23 = {
    "id": "j23",
    "name": "Quarters J-23",
    "description": (
        "Juno's quarters are small but organized—tools, notes, and schematics stacked in careful piles. "
        "Her bunk is neatly made, but she's nowhere to be seen."
    ),
    "objects": {
        "bunk": {
            "id": "bunk",
            "kind": "scenery",
            "description": "A neatly made bunk with a folded jumpsuit at the foot.",
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "workbench": {
            "id": "workbench",
            "kind": "scenery",
            "description": (
                "Juno's workbench is cluttered with tools and ventilation schematics for Vault 656."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "note": {
            "id": "note",
            "kind": "actionable",
            "description": (
                "A hastily written note from Juno mentioning strange log entries tied to your ID "
                "and a meeting point near the Overseer's office."
            ),
            "can_take": True,
            "can_talk": False,
            "is_exit": False,
        },
        "door": {
            "id": "door",
            "kind": "actionable",
            "description": (
                "A standard sliding Vault door. The status light glows green - it's unlocked."
            ),
            "description_unlocked": (
                "A standard sliding Vault door. The status light glows green - it's unlocked."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {
        "door": {
            "destination": "hallway_ground",
            "status": "unlocked",  # locked | unlocked | jammed | sealed
            "unlocked_via": None,  # what unlocks it (intercom, event, etc.)
            "required_item": None,  # if item needed to pass
            "unlock_on_use": False,  # if using auto-unlocks
            "description_locked": (
                "A standard sliding Vault door. The status light glows red — locked from the outside."
            ),
            "description_unlocked": (
                "A standard sliding Vault door. The status light glows green - it's unlocked."
            ),
            "on_attempt": None,  # optional callback/event
            "on_unlock": None,  # optional callback/event
        }
    },
    "flags": {},
}
