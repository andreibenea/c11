juno_j23_2 = {
    "npc_id": "juno",
    "intro": ("Juno checks the corridor again before speaking.\n"),
    "intro_dialogue": "\"All right. If you're still with me, here's the actual picture.\"",
    "options": {
        1: {
            "player": "Fine. Tell me what I need to do.",
            "npc": (
                '"Step one: get your Pip-Boy back. Without it, the Vault door terminal '
                "won’t even show you the evacuation keys. I saw it logged into the "
                "Security Office for 'calibration'.\"\n\n"
                '"Step two: trigger a Vault-wide security alert. The door only opens if '
                "the system thinks you're an active response unit during an incident.\""
            ),
            "outcome": "go_next",  # leads to juno_j23_3
        },
        2: {
            "player": "And Security? They're already suspicious of me.",
            "npc": (
                '"Exactly why you need the alert."\n\n'
                "\"If the system tags you as a response asset, guards won't question you—"
                "they’ll be too busy chasing the 'breach' the Overseer's terminal reports.\"\n\n"
                '"Once the bulletin goes out, walking into the Security Office won’t get you shot—'
                'they’ll just hand you your Pip-Boy to clear their queue."'
            ),
            "outcome": "go_next",
        },
    },
}
