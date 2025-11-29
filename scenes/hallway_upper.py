hallway_upper = {
    "id": "hallway_upper",
    "name": "Upper Floor Hallway",
    "description": (
        "A quieter upper corridor with reinforced doors and thicker wall plating. "
        "Placards indicate the Security Office, the Overseer's Office, and the stairwell "
        "back down to the trainee quarters."
    ),
    "objects": {
        "signs": {
            "id": "signs",
            "kind": "scenery",
            "description": (
                "Metal placards point the way:\n"
                "  • Security Office\n"
                "  • Overseer's Office\n"
                "  • Stairs down to C- and J-wing quarters"
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "stairs_down": {
            "id": "stairs_down",
            "kind": "actionable",
            "description": (
                "A grated metal stairwell leading back down toward the trainee quarters."
            ),
            "description_unlocked": (
                "A grated metal stairwell leading back down toward the trainee quarters."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        "security_door": {
            "id": "security_door",
            "kind": "actionable",
            "description": (
                "A reinforced sliding door marked SECURITY OFFICE. "
                "Its status light glows green — currently unlocked."
            ),
            "description_unlocked": (
                "A reinforced sliding door marked SECURITY OFFICE. "
                "Its status light glows green — currently unlocked."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        "overseer_door": {
            "id": "overseer_door",
            "kind": "actionable",
            "description": (
                "A heavy door with the Overseer's insignia. The status light glows green — unlocked."
            ),
            "description_unlocked": (
                "A heavy door with the Overseer's insignia. The status light glows green — unlocked."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {
        "stairs_down": {
            "destination": "hallway_ground",
            "status": "unlocked",  # locked | unlocked | jammed | sealed
            "unlocked_via": None,
            "required_item": None,
            "unlock_on_use": False,
            "description_locked": (
                "The stairwell access is blocked off — a red status light bars the way."
            ),
            "description_unlocked": (
                "A grated metal stairwell leading back down toward the trainee quarters."
            ),
            "on_attempt": None,
            "on_unlock": None,
        },
        "security_door": {
            "destination": "security_office",
            "status": "unlocked",
            "unlocked_via": None,
            "required_item": None,
            "unlock_on_use": False,
            "description_locked": (
                "The Security Office door is sealed, its status light a hard red."
            ),
            "description_unlocked": (
                "A reinforced sliding door marked SECURITY OFFICE. "
                "Its status light glows green — currently unlocked."
            ),
            "on_attempt": None,
            "on_unlock": None,
        },
        "overseer_door": {
            "destination": "overseer_office",
            "status": "unlocked",
            "unlocked_via": None,
            "required_item": None,
            "unlock_on_use": False,
            "description_locked": (
                "The Overseer's door is sealed tight, status light red and unblinking."
            ),
            "description_unlocked": (
                "A heavy door with the Overseer's insignia. The status light glows green — unlocked."
            ),
            "on_attempt": None,
            "on_unlock": None,
        },
    },
    # Possible global “upper hallway locked” state.
    "flags": {"door_locked": False},
}
