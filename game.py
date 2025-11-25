from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from player import Player

import sys
from commands import COMMANDS
from dialogues import DIALOGUES


class Game:
    def __init__(self, player: "Player", world):
        # Store references to the active player entity and the world model.
        # Initialize overall game-state toggles.
        # Set current_scene_id based on the player's starting location.
        self.player = player
        self.world = world
        self.running = True
        self.current_scene_id = player.scene_id

    def run(self):
        # Main game loop.
        # 1. Show initial scene description.
        # 2. Continuously read user input.
        # 3. Ignore blank lines.
        # 4. Route input to the command handler.
        print(self.describe_current_scene())
        while self.running:
            raw = input("> ").strip().lower()
            if not raw:
                continue
            self.handle_command(raw)

    def change_scene(self, scene_id: str):
        # Transition the player to a new scene.
        # Updates internal scene pointer and prints the scene's description.
        self.current_scene_id = scene_id
        print(self.describe_current_scene())

    def describe_current_scene(self) -> str:
        # Fetch the active scene's data from the world.
        # Return the textual description of the scene, without printing.
        scene = self.world.get_scene(self.current_scene_id)
        return scene["description"]

    def handle_command(self, raw_input: str):
        # Dispatch logic based on whether the player is in a dialogue state.
        # Later, this should route to the parser and command execution system.
        try:
            verb, raw_args = raw_input.split(maxsplit=1)
        except:
            verb, raw_args = raw_input, None
        print(
            f"""===============================
verb: {verb}"""
        )
        if self.player.in_dialog:
            print("Handle REPLY")
            self.determine_response(verb)
            return
        if verb not in COMMANDS:
            print("BAD COMMAND. verb not in COMMANDS. RETRY")
            return
        print(
            f"""===============================
modifiers: {COMMANDS[verb]["modifiers"]}"""
        )
        print(
            f"""===============================
raw args: {raw_args}"""
        )
        try:
            args = raw_args.split()
            target = None
        except:
            args = None
            target = None
        print(
            f"""===============================
args: {args}"""
        )
        self.scene = self.world.get_scene(self.current_scene_id)
        self.scene_items = self.scene["objects"]
        self.scene_npcs = self.world.get_scene_npcs(self.current_scene_id)
        print(
            f"""===============================
scene NPCs: {self.scene_npcs}"""
        )
        print(
            f"""===============================
scene objects: {self.scene_items.keys()}"""
        )

        if not args:
            print(
                f"""===============================
command has no args"""
            )
            return self.execute_command(COMMANDS[verb]["default_action"])
        if args:
            for arg in args:
                print(
                    f"""===============================
ARG: {arg}"""
                )
                if arg == "around":
                    print(
                        """===============================
RUNNING MODIFIED LOOK COMMAND"""
                    )
                    return self.execute_command(COMMANDS[verb]["modifiers"][arg])
                if arg in self.scene_items:
                    print(f"is item: {arg in self.scene_items}")
                    target = arg
                    if self.scene_items[arg]["can_talk"]:
                        self.dialog_id_base = f"{target}_{self.player.scene_id}"
                        self.dialog_intro = DIALOGUES[self.dialog_id_base]["intro"]
                        self.dialog_options = DIALOGUES[self.dialog_id_base]["options"]
                        self.dialog_count = 1
                    break
                else:
                    for exit in self.scene["exits"]:
                        if arg == self.scene["exits"][exit]["destination"]:
                            print(
                                f"target is destination: {self.scene["exits"][exit]["destination"]}"
                            )
                            target = arg
                            break
                    for npc in self.scene_npcs:
                        if arg == npc.id:
                            print(f"is item: {arg in self.scene_items}")
                            print(f"is npc: {arg == npc.id}")
                            target = arg
                            self.dialog_id_base = f"{target}_{self.player.scene_id}"
                            self.dialog_intro = DIALOGUES[self.dialog_id_base]["intro"]
                            self.dialog_options = DIALOGUES[self.dialog_id_base][
                                "options"
                            ]
                            self.dialog_count = 1
                            break
            if target is None:
                return print(
                    "That didn't work..if your target should be there, check your spelling!"
                )
        print(
            f"""===============================
target: {target}"""
        )
        if len(args) < COMMANDS[verb]["min_args"]:
            print("COMMAND NEEDS MORE ARGUMENTS")
            return
        if len(args) > COMMANDS[verb]["max_args"]:
            print("COMMAND HAS TOO MANY ARGS!")
            return
        for arg in args:
            print(
                f"""===============================
arg: {arg}"""
            )
            if arg in COMMANDS[verb]["modifiers"]:
                return self.execute_command(COMMANDS[verb]["modifiers"][arg], target)
        return self.execute_command(COMMANDS[verb]["default_action"], target)

    def determine_response(self, option):
        try:
            option = int(option)
            print(
                f"""===============================
DIALOG OPTIONS: {self.dialog_options}"""
            )
            if option in self.dialog_options:
                print(self.dialog_options[option]["npc"])
                if self.dialog_options[option]["outcome"] == "go_next":
                    self.dialog_count += 1
                    self.dialog_id = f"{self.dialog_id_base}_{self.dialog_count}"
                    self.dialog_intro = DIALOGUES[self.dialog_id]["intro"]
                    self.dialog_options = DIALOGUES[self.dialog_id]["options"]
                    print(
                        f"""===============================
DIALOG ID: {self.dialog_id}"""
                    )
                    return self.player.talk(self.dialog_intro, self.dialog_options)
                if self.dialog_options[option]["outcome"] == "good":
                    print("THIS IS THE GOOD OUTCOME BEING HIT")
                    for exit in self.scene["exits"]:
                        if self.scene["exits"][exit]["unlocked_via"] == self.talking_to:
                            self.scene["exits"][exit]["status"] = "unlocked"
                            self.player.in_dialog = not self.player.in_dialog
                            return
                    print("OUTCOME GOOD BUT NO MATCH - LINE 183")
                if self.dialog_options[option]["outcome"] == "neutral":
                    self.player.in_dialog = not self.player.in_dialog
                    return print("NOTHING HAPPENED...")
                if self.dialog_options[option]["outcome"] == "bad":
                    print(
                        """===============================
OOPS! YOU SHOULD NOT HAVE SAID THAT!
==============================="""
                    )
                    print(
                        """===============================
GAME OVER
==============================="""
                    )
                    return sys.exit()
                else:
                    self.player.in_dialog = not self.player.in_dialog
                    return print(self.dialog_options[option]["npc"])
            return print("Invalid reply.. check your input and try again!")
        except ValueError:
            print(
                """===============================
CANNOT CONVERT TO INT"""
            )
            return print("Invalid reply.. start over (for now..)!")

    def execute_command(
        self,
        cmd: str,
        target: str | None = None,
    ):
        match cmd:
            case "help":
                return print(
                    """
This is a text adventure. You type commands. The parser pretends to understand them.

Core verbs:
  look          - examine an object (e.g., "look [at] locker")
  look around   - scan the whole room
  examine <x>   - describe an object (same as "look [at] <x>")
  inspect <x>   - synonym for examine
  use <x>       - interact with an object or exit
  take <item>   - pick up an item
  go <location> - move to another room
  talk <npc>    - start dialogue with someone

The parser accepts natural language after the verb.  
Examples:
  "look around for a moment"
  "look at the terminal"
  "go to the hallway"
  "talk to juno"

Keep commands simple: one verb plus a target or modifier."""
                )
            case "examine":
                if not target:
                    return print("What are you trying to examine?")
                if target in self.scene["exits"]:
                    if self.scene["exits"][target]["status"] == "locked":
                        print(self.scene["exits"][target]["description_locked"])
                    else:
                        print(self.scene["exits"][target]["description_unlocked"])
                    print("This seems to be the way out of this room.")
                    print(f"Leads to '{self.scene["exits"][target]["destination"]}'")
                    return

                return print(self.scene["objects"][target]["description"])
            case "look_around":
                print("You take a look around the room...")
                print(f"The following objects catch your attention:")
                print(list(self.scene_items.keys()))
                for npc in self.scene_npcs:
                    print(f"You see {npc.name} standing there.")
            case "use":
                if not target:
                    return print("Use WHAT exactly!?")
                if target in self.scene["exits"]:
                    if self.scene["exits"][target]["status"] == "locked":
                        return print(self.scene["exits"][target]["description_locked"])
                    self.player.move_to(self.scene["exits"][target]["destination"])
                    self.change_scene(self.scene["exits"][target]["destination"])
                    print("IMPLEMENT CHANGE SCENE FUNC AND CALL HERE")
                    return
                if target in self.scene_items:
                    if self.scene["objects"][target]["kind"] == "hint":
                        return print(self.scene["objects"][target]["description"])
                    if self.scene["objects"][target]["kind"] == "scenery":
                        return print("This is not an item you can use!")
                    if self.scene["objects"][target]["can_take"]:
                        if self.scene_items[target]["needs_item"]:
                            return print(
                                f"You'll need to have a(n) '{self.scene_items[target]["needs_item"]}' before you can use this {target}.\n"
                                "It might be worth picking it up for later..."
                            )
                        return print("Seems useful, you should take that with you!")
                    elif self.scene["objects"][target]["can_talk"]:
                        print(
                            """===============================
THIS IS A TALKING OBJECT LIKE THE INTERCOM (MAYBE TERMINAL)"""
                        )
                        self.player.in_dialog = not self.player.in_dialog
                        self.talking_to = target
                        return self.player.talk(self.dialog_intro, self.dialog_options)
                return print("TRYING TO USE SOMETHING THAT'S NOT THERE WON'T WORK")
            case "take":
                if not target:
                    return print("You need to specify WHAT you want to pick up!")
                if self.scene_items[target]["can_take"]:
                    self.player.add_item_to_inventory(self.scene["objects"][target])
                    del self.scene_items[target]
                    return
                if self.scene_items[target]["kind"] == "hint":
                    return print(self.scene_items[target]["description"])
                return print("You cannot pick this up...")
            case "talk":
                if not target:
                    return print("Who do you wanna talk to!?")
                for npc in self.scene_npcs:
                    if (
                        target.lower() == str(npc.id).lower()
                        or target.lower() == str(npc.name).lower()
                    ):
                        self.player.in_dialog = not self.player.in_dialog
                        self.talking_to = npc.id
                        return self.player.talk(self.dialog_intro, self.dialog_options)
                if self.scene_items[target]["can_talk"]:
                    self.player.in_dialog = not self.player.in_dialog
                    self.talking_to = target
                    return self.player.talk(self.dialog_intro, self.dialog_options)
                print("TALK TO THE THING/NPC")
            case "exit_room":
                if not target:
                    return print("Go where exactly?!")
                for exit in self.scene["exits"]:
                    if self.scene["exits"][exit]["destination"] == target:
                        if self.scene["exits"][exit]["status"] == "locked":
                            return print(
                                f"The door leading to {self.scene["exits"][exit]["destination"]} is locked!"
                            )
                        self.player.move_to(target)
                        self.change_scene(target)
                        return
                return print("You cannot travel there from your current location")
            case "exit_game":
                sys.exit()
