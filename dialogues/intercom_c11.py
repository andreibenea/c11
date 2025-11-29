intercom_c11 = {
    "npc_id": "security_guard_one",
    "intro": (
        "The intercom crackles to life. A tired voice answers:"
    ),
    "intro_dialogue": "Security here. State your ID and what the problem is.",
    "options": {
        1: {
            "player": "This is C-11, reporting for trainee rotation — door's stuck again.",
            "npc": "…Damn maintenance. Always the trainees. Hold on.",
            "outcome": "good",  # door unlocks
        },
        2: {
            "player": (
                "Hey, this is C-11. My Pip-Boy seems defective and I can't open the door."
            ),
            "npc": "…Trainees. Always something. Put in a maintenance ticket!",
            "outcome": "neutral",  # nothing happens
        },
        3: {
            "player": (
                "Someone stole my Pip-Boy and drugged me. I think there's been a security breach."
            ),
            "npc": (
                "\"…Say that again?\"\n"
                "(muffled) C-11 is compromised. Notify Response Team.\n"
                "\"Stay where you are. Help is on the way.\""
            ),
            "outcome": "bad",  # game over
        },
    },
}
