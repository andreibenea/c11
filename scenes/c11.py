c11 = {
    "id": "c11",
    "name": "Quarters C-11",
    "description": (
        "You wake with a sour, metallic taste in your mouth and a throbbing ache behind your eyes. "
        "The room is dim — only thin bands of emergency floor lighting pulse in a faint blue rhythm. "
        "Your left forearm is bare. Your Pip-Boy is gone. The door's indicator glows a steady yellow, signaling a local lockdown. "
        "Something is very wrong in Vault 656… and someone wanted you unconscious when it happened."
    ),
    "objects": {
        "bed": {
            "id": "bed",
            "kind": "scenery",
            "description": (
                "The sheets are twisted and half-dragged to the floor, as if someone pulled you out of bed rather than waking you. "
                "The pillow lies several feet away — nothing about this suggests a peaceful rest."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "locker": {
            "id": "locker",
            "kind": "scenery",
            "description": (
                "Your locker sits cracked open, the metal around the latch dented from forced entry. "
                "Inside, your jumpsuit is still neatly folded — but the valuables box and Pip-Boy cradle are missing. "
                "Whoever drugged you wasn't after clothes. They came for your gear."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "floor": {
            "id": "floor",
            "kind": "scenery",
            "description": (
                "A small, sky-blue syringe cap rests near your foot. It's standard Medbay equipment — a sterile cap used for anesthetic injectors. "
                "You don't remember visiting Medbay. You don't remember anything at all before waking here."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "desk": {
            "id": "desk",
            "kind": "scenery",
            "description": (
                "A steel desk is bolted into the floor, as all Vault furniture is. "
                "An unpowered terminal sits dark and lifeless beside a single Vault-Tec holotape. "
                "Without main power, the terminal won't even cough out an error message."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "terminal": {
            "id": "terminal",
            "kind": "scenery",
            "description": (
                "The screen is pitch black. Emergency power bypasses terminal circuits to conserve energy, leaving it completely unresponsive. "
                "Whatever information it holds is locked behind the outage… or sabotage."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "holotape": {
            "id": "holotape",
            "kind": "actionable",
            "description": (
                "A worn Vault-Tec holotape labeled in faded pen. Without your Pip-Boy, there's no way to read the data.\n"
                "It's just a silent, sealed message waiting for the tool that's been stolen from you."
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
                "A ventilation grate hums inconsistently, cycling bursts of air through the room. "
                "The rhythm is irregular, as if part of the environmental system is failing… or being tampered with. It smells faintly of ozone and sterilizer."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "intercom": {
            "id": "intercom",
            "kind": "actionable",
            "description": (
                "A standard Vault intercom panel, scratched from years of use. Through it, Security can monitor and communicate with residents.\n"
                "It's your only link to the outside of this locked room."
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
                "The pillow from the floor is unzipped slightly. Tucked inside the case is a tightly folded note written in hurried strokes:\n"
                "“You're in danger. Come find me. Don't trust anyone.”\n"
                "The handwriting is unmistakable — Juno's. You return the pillow to where it was, pulse quickening. She must've planted this before everything went dark."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "dialog_id": "intercom_c11",
        },
        "door": {
            "id": "door",
            "kind": "actionable",
            "description": (
                "A reinforced sliding Vault door with a glowing yellow status light — local lockdown. "
                "Under normal conditions it would open at a touch. Now it's sealed by an override from the outside."
            ),
            "description_unlocked": "A reinforced sliding Vault door with its status light glowing green. The lockdown has been cleared; the door will open on command.",
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
                "A reinforced sliding Vault door with a glowing yellow status light — local lockdown. "
                "Under normal conditions it would open at a touch. Now it's sealed by an override from the outside."
            ),
            "description_unlocked": "A reinforced sliding Vault door with its status light glowing green. The lockdown has been cleared; the door will open on command.",
            # optional: custom text or event when attempting to open
            "on_attempt": None,
            "on_unlock": "A soft chime sounds as the door's status light shifts from yellow to green.",
        }
    },
    "flags": {},
}
