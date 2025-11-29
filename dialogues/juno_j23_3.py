juno_j23_3 = {
    "npc_id": "juno",
    "intro": '"Last part. And this is the dangerous one."',
    "intro_dialogue": None,
    "options": {
        1: {
            "player": "How do I trigger the alert without getting executed by the Overseer?",
            "npc": (
                '"You won’t ask him. You’ll use his terminal."\n\n'
                '"He pretends everything is biometric, but he still keeps a paper fallback '
                "password in his office—old Vault-Tec habits. Check under the console housing, "
                'inside the side maintenance hatch, or behind those motivational plaques he loves."\n\n'
                '"Once you have the password, log in, mark yourself as a confirmed incident, '
                'and push a full Response Team alert."'
            ),
            "outcome": "lore",
        },
        2: {
            "player": "Anything else before I try cracking open the Vault door?",
            "npc": (
                '"Yeah. Two things."\n\n'
                '"One: don’t touch the door terminal without the alert active and your Pip-Boy in hand. '
                'If you input the wrong sequence, the door hard-seals. Forever."\n\n'
                "\"Two: once you're through the door, don’t come back. The Overseer will purge your "
                'access within minutes. Grab everything you need beforehand."'
            ),
            "outcome": "final_hint",
        },
    },
}
