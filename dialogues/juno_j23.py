juno_j23 = {
    "npc_id": "juno",
    "intro": (
        "Juno freezes mid-pace as you step into the room. Relief flashes across her face.\n"
    ),
    "intro_dialogue": '"You actually made it. Good. I wasn’t sure the note would get past Security."',
    "options": {
        1: {
            "player": "What happened to me? C-11 was locked down and my Pip-Boy is gone.",
            "npc": (
                '"Then you haven’t heard anything."\n'
                "She shuts the door, lowers her voice.\n\n"
                '"Something’s wrong in the Vault. The Overseer locked down the trainee wing, '
                "Security started ‘collecting’ Pip-Boys, and anyone who complains gets rerouted "
                'to Medical and doesn’t come back the same shift."\n\n'
                '"You were flagged in the system. That’s why the lockdown hit your room."'
            ),
            "outcome": "go_next",  # leads to juno_j23_2
        },
        2: {
            "player": "Your note said I’m in danger. Why?",
            "npc": (
                '"Because someone put your name on a list."\n'
                "Her jaw tightens.\n"
                "\"Security marked you as a 'containment risk'. That means monitoring, isolation, "
                "and eventually relocation. Your Pip-Boy wasn’t stolen. They took it—probably "
                'to stop you from accessing restricted logs."\n\n'
                '"If you want out, you need to stay ahead of whatever they think you saw."'
            ),
            "outcome": "go_next",
        },
    },
}
