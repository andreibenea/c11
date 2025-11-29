from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from player import Player
    from event_emitter import Output

import sys
from commands import COMMANDS
from dialogues import DIALOGUES


class Game:
    def __init__(
        self, player: "Player", world, output: "Output", allow_exit: bool = True
    ):
        # ------------------------------[ INITIALIZATION ]------------------------------
        # Constructs the Game object by linking the active player, world model, and
        # output emitter. Sets core runtime flags and determines the starting scene
        # based on the player's initial location. Prepares dialogue and hint tracking.
        # --------------------------------------------------------------------------------
        self.player = player
        self.world = world
        self.output = output
        self.running = True
        self.current_scene_id = player.scene_id
        self.scene_dialogues = {}
        self.scene_hints = []
        self.allow_exit = allow_exit

    def run(self):
        # ------------------------------[ GAME LOOP ]------------------------------
        # Initializes the first scene display, then enters the primary input cycle.
        # Continuously reads and sanitizes player commands, ignoring empty input,
        # and routes valid entries to the command handler for processing.
        # -------------------------------------------------------------------------
        self.output.emit(self.describe_current_scene(), "scene")
        while self.running:
            raw = input("> ").strip().lower()
            if not raw:
                continue
            self.handle_command(raw)

    def change_scene(self, scene_id: str):
        # ---------------------------[ SCENE TRANSITION ]---------------------------
        # Updates the player's current scene, then emits the narrative description
        # of the new location. Handles the visual shift between areas in the world.
        # ----------------------------------------------------------------------------
        self.current_scene_id = scene_id
        self.output.emit(self.describe_current_scene(), "scene")

    def describe_current_scene(self) -> str:
        # -------------------------[ SCENE DESCRIPTION ]-------------------------
        # Retrieves the active scene from the world model and returns its
        # narrative text block. This function does not print or emit output;
        # it only provides the description for the caller to display.
        # -----------------------------------------------------------------------
        scene = self.world.get_scene(self.current_scene_id)
        return scene["description"]

    def handle_command(self, raw_input: str):
        # -------------------------[ COMMAND ROUTER ]-------------------------
        # Parses raw player input, resolves verbs and targets, applies
        # modifiers, and directs execution to the appropriate game actions
        # or dialogue pathways depending on the current game state.
        # --------------------------------------------------------------------
        try:
            verb, raw_args = raw_input.split(maxsplit=1)
        except:
            verb, raw_args = raw_input, None
        self.output.emit(f"verb: {verb}", "debug")
        if self.player.in_dialog:
            self.output.emit("PLAYER IN DIALOG MODE", "debug")
            self.determine_response(verb)
            return
        if verb not in COMMANDS:
            self.output.emit(
                "I don't understand that command. Type 'help' to see what you can do.",
                "system",
            )
            return
        self.output.emit(f"modifiers: {COMMANDS[verb]["modifiers"]}", "debug")
        self.output.emit(f"raw args: {raw_args}", "debug")
        try:
            args = raw_args.split()
            target = None
        except:
            args = None
            target = None
        self.output.emit(f"args: {args}", "debug")
        self.scene = self.world.get_scene(self.current_scene_id)
        self.scene_items = self.scene["objects"]
        self.scene_npcs = self.world.get_scene_npcs(self.current_scene_id)
        self.output.emit(f"scene NPCs: {self.scene_npcs}", "debug")
        self.output.emit(f"scene objects: {self.scene_items.keys()}", "debug")

        if not args:
            self.output.emit(f"command has no args", "debug")
            return self.execute_command(COMMANDS[verb]["default_action"])
        if args:
            for arg in args:
                self.output.emit(f"ARG: {arg}", "debug")
                if arg == "around":
                    self.output.emit("RUNNING MODIFIED LOOK COMMAND", "debug")
                    return self.execute_command(COMMANDS[verb]["modifiers"][arg])
                if arg in self.scene_items:
                    self.output.emit(f"is item: {arg in self.scene_items}", "debug")
                    target = arg
                    if self.scene_items[arg]["can_talk"]:
                        self.dialog_id_base = f"{target}_{self.player.scene_id}"
                        self.scene_dialogues[self.dialog_id_base] = DIALOGUES[
                            self.dialog_id_base
                        ]
                        self.dialog_intro = self.scene_dialogues[self.dialog_id_base][
                            "intro"
                        ]
                        self.dialog_intro_dialogue = self.scene_dialogues[
                            self.dialog_id_base
                        ]["intro_dialogue"]
                        self.dialog_options = self.scene_dialogues[self.dialog_id_base][
                            "options"
                        ]
                        self.dialog_count = 1
                    break
                else:
                    for exit in self.scene["exits"]:
                        if arg == self.scene["exits"][exit]["destination"]:
                            self.output.emit(
                                f"target is destination: {self.scene["exits"][exit]["destination"]}",
                                "debug",
                            )
                            target = arg
                            break
                    for npc in self.scene_npcs:
                        if arg == npc.id:
                            self.output.emit(
                                f"is item: {arg in self.scene_items}", "debug"
                            )
                            self.output.emit(f"is npc: {arg == npc.id}", "debug")
                            target = arg
                            self.dialog_id_base = f"{target}_{self.player.scene_id}"
                            self.scene_dialogues[self.dialog_id_base] = DIALOGUES[
                                self.dialog_id_base
                            ]
                            self.dialog_intro = self.scene_dialogues[
                                self.dialog_id_base
                            ]["intro"]
                            self.dialog_intro_dialogue = self.scene_dialogues[
                                self.dialog_id_base
                            ]["intro_dialogue"]
                            self.dialog_options = self.scene_dialogues[
                                self.dialog_id_base
                            ]["options"]
                            self.dialog_count = 1
                            break
            if target is None:
                return self.output.emit(
                    "You can't seem to find that here. If it should be, check your spelling and try again.",
                    "system",
                )
        self.output.emit(f"target: {target}", "debug")
        if len(args) < COMMANDS[verb]["min_args"]:
            return self.output.emit(
                "You haven't given enough information to do that.", "system"
            )
        if len(args) > COMMANDS[verb]["max_args"]:
            return self.output.emit(
                "That's a bit much at once. Try a simpler command.", "system"
            )
        for arg in args:
            self.output.emit(f"arg: {arg}", "debug")
            if arg in COMMANDS[verb]["modifiers"]:
                return self.execute_command(COMMANDS[verb]["modifiers"][arg], target)
        return self.execute_command(COMMANDS[verb]["default_action"], target)

    def determine_response(self, option):
        # -------------------[ DIALOGUE RESPONSE LOGIC ]-------------------
        # Interprets numeric replies, routes outcomes, updates dialogue
        # state, and triggers world effects such as door unlock events.
        # -----------------------------------------------------------------
        if option == "help":
            return self.execute_command(option)
        if option == "quit":
            return self._end_game()
        try:
            option = int(option)
            self.output.emit(f"DIALOG OPTIONS: {self.dialog_options}", "debug")
            if option in self.dialog_options:
                self.output.emit(self.dialog_options[option]["npc"], "dialogue_npc")
                if self.dialog_options[option]["outcome"] == "go_next":
                    self.dialog_count += 1
                    self.dialog_id = f"{self.dialog_id_base}_{self.dialog_count}"
                    self.scene_dialogues[self.dialog_id] = DIALOGUES[self.dialog_id]
                    self.dialog_intro = self.scene_dialogues[self.dialog_id]["intro"]
                    self.dialog_intro_dialogue = self.scene_dialogues[
                        self.dialog_id_base
                    ]["intro_dialogue"]
                    self.dialog_options = self.scene_dialogues[self.dialog_id][
                        "options"
                    ]
                    self.output.emit(f"DIALOG ID: {self.dialog_id}", "debug")
                    lines = self.player.talk(self)
                    for line in lines:
                        self.output.emit(line, "dialogue_pc")
                    return
                if self.dialog_options[option]["outcome"] == "good":
                    self.output.emit("THIS IS THE GOOD OUTCOME BEING HIT", "debug")
                    for exit in self.scene["exits"]:
                        if self.scene["exits"][exit]["unlocked_via"] == self.talking_to:
                            self.scene["exits"][exit]["status"] = "unlocked"
                            self.output.emit(
                                self.scene["exits"][exit]["on_unlock"], "event"
                            )
                            self.player.in_dialog = not self.player.in_dialog
                            return
                    return self.output.emit(
                        "You feel like something should have changed... but nothing happens.",
                        "system",
                    )
                if self.dialog_options[option]["outcome"] == "neutral":
                    self.player.in_dialog = not self.player.in_dialog
                    return self.output.emit("Nothing seems to happen.", "system")
                if self.dialog_options[option]["outcome"] == "bad":
                    self.output.emit(
                        "The moment the words leave your mouth, you know you've made a mistake.",
                        "system",
                    )
                    self.output.emit("Everything goes dark.", "system")
                    if self.allow_exit:
                        raise SystemExit()
                    return self._end_game()
                else:
                    self.player.in_dialog = not self.player.in_dialog
                    return self.output.emit(
                        self.dialog_options[option]["npc"], "dialogue_pc"
                    )
            return self.output.emit(
                "Invalid reply.. check your input and try again!", "system"
            )
        except ValueError:
            self.output.emit("Cannot convert to INT!", "debug")
            return self.output.emit(
                "That's not a valid choice. Type the number of your reply.", "system"
            )

    def execute_command(
        self,
        cmd: str,
        target: str | None = None,
    ):
        # -----------------------[ COMMAND EXECUTION ]-----------------------
        # Dispatches parsed commands to their respective handlers, performs
        # object and exit interactions, manages movement, inventory actions,
        # and routes dialogue initiation when appropriate.
        # -------------------------------------------------------------------
        match cmd:
            case "help":
                return self.output.emit(
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

Keep commands simple: one verb plus a target or modifier.""",
                    "help",
                )
            case "examine":
                if not target:
                    return self.output.emit(
                        "What exactly are you trying to examine?", "system"
                    )
                for npc in self.scene_npcs:
                    if target == npc.id:
                        return self.output.emit(npc.description)
                if target in self.scene["exits"]:
                    if self.scene["exits"][target]["status"] == "locked":
                        self.output.emit(
                            self.scene["exits"][target]["description_locked"]
                        )
                    else:
                        self.output.emit(
                            self.scene["exits"][target]["description_unlocked"]
                        )
                    self.output.emit("This looks like the way out of this room.")
                    self.output.emit(
                        f"It should lead to '{self.scene['exits'][target]['destination']}'."
                    )
                    return
                if target in self.scene_items:
                    if self.scene_items[target]["kind"] == "hint":
                        if (
                            self.scene_items[target]["dialog_id"]
                            not in self.scene_hints
                        ):
                            self.scene_hints.append(
                                self.scene_items[target]["dialog_id"]
                            )
                        return self.output.emit(
                            self.scene["objects"][target]["description"], "hint"
                        )
                    return self.output.emit(
                        self.scene["objects"][target]["description"]
                    )
                return self.output.emit(
                    "You can't seem to find that here. If it should be, check your spelling and try again.",
                    "system",
                )
            case "look_around":
                self.output.emit("You take a slow look around the room...")
                self.output.emit(
                    f"A few things stand out to you. They might be worth examining more closely:"
                )
                self.output.emit(", ".join(self.scene_items.keys()))
                for npc in self.scene_npcs:
                    self.output.emit(f"You see {npc.name} standing there.")
            case "use":
                if not target:
                    return self.output.emit("Use what, exactly?", "system")
                for npc in self.scene_npcs:
                    if target == npc.id:
                        return self.output.emit(
                            "You can't use a person. Maybe try talking to them instead."
                        )
                if target in self.scene["exits"]:
                    if self.scene["exits"][target]["status"] == "locked":
                        return self.output.emit(
                            self.scene["exits"][target]["description_locked"]
                        )
                    self.player.move_to(self.scene["exits"][target]["destination"])
                    self.change_scene(self.scene["exits"][target]["destination"])
                    return
                if target in self.scene_items:
                    if self.scene_items[target]["kind"] == "hint":
                        if (
                            self.scene_items[target]["dialog_id"]
                            not in self.scene_hints
                        ):
                            self.scene_hints.append(
                                self.scene_items[target]["dialog_id"]
                            )
                        return self.output.emit(
                            self.scene["objects"][target]["description"], "hint"
                        )
                    if self.scene["objects"][target]["kind"] == "scenery":
                        return self.output.emit(
                            "That isn't something you can really use.", "system"
                        )
                    if self.scene["objects"][target]["can_take"]:
                        if self.scene_items[target]["needs_item"]:
                            return self.output.emit(
                                f"You'll need a '{self.scene_items[target]['needs_item']}' before you can use the {target}.\n"
                                "It might be worth holding onto for later..."
                            )
                        return self.output.emit(
                            "This might be useful later. You should probably take it with you."
                        )
                    elif self.scene["objects"][target]["can_talk"]:
                        self.output.emit(
                            "THIS IS A TALKING OBJECT LIKE THE INTERCOM (MAYBE TERMINAL)",
                            "debug",
                        )
                        self.player.in_dialog = not self.player.in_dialog
                        self.talking_to = target
                        self.output.emit(f"{self.dialog_intro}")
                        self.output.emit(
                            f"{self.dialog_intro_dialogue}", "dialogue_npc"
                        )
                        lines = self.player.talk(self)
                        for line in lines:
                            self.output.emit(line, "choice")
                        return
                return self.output.emit(
                    "You fumble around, but there's nothing like that here to use."
                )
            case "take":
                if not target:
                    return self.output.emit("What are you trying to pick up?", "system")
                for npc in self.scene_npcs:
                    if target == npc.id:
                        return self.output.emit(
                            "You can't pick them up. That's... not how this works."
                        )
                if target in self.scene_items:
                    if self.scene_items[target]["can_take"]:
                        self.player.add_item_to_inventory(self.scene["objects"][target])
                        self.output.emit(
                            f"The {target.lower()} was added to your inventory!",
                            "event",
                        )
                        del self.scene_items[target]
                        return
                    if self.scene_items[target]["kind"] == "hint":
                        if (
                            self.scene_items[target]["dialog_id"]
                            not in self.scene_hints
                        ):
                            self.scene_hints.append(
                                self.scene_items[target]["dialog_id"]
                            )
                        return self.output.emit(
                            self.scene_items[target]["description"], "hint"
                        )
                return self.output.emit("You can't pick that up.", "system")
            case "talk":
                if not target:
                    return self.output.emit("Who are you trying to talk to?", "system")
                for npc in self.scene_npcs:
                    if (
                        target.lower() == str(npc.id).lower()
                        or target.lower() == str(npc.name).lower()
                    ):
                        self.player.in_dialog = not self.player.in_dialog
                        self.talking_to = npc.id
                        lines = self.player.talk(self)
                        for line in lines:
                            self.output.emit(line, "choice")
                        return
                if target in self.scene_items:
                    if self.scene_items[target]["can_talk"]:
                        self.player.in_dialog = not self.player.in_dialog
                        self.talking_to = target
                        self.output.emit(self.dialog_intro)
                        self.output.emit(self.dialog_intro_dialogue, "dialogue_npc")
                        lines = self.player.talk(self)
                        for line in lines:
                            self.output.emit(line, "choice")
                        return
                self.output.emit("There's no one like that here to talk to.", "system")
            case "exit_room":
                if not target:
                    return self.output.emit("Go where, exactly?", "system")
                for exit in self.scene["exits"]:
                    if self.scene["exits"][exit]["destination"] == target:
                        if self.scene["exits"][exit]["status"] == "locked":
                            return self.output.emit(
                                f"The door leading to {self.scene['exits'][exit]['destination']} is locked tight.",
                                "system",
                            )
                        self.player.move_to(target)
                        self.change_scene(target)
                        return
                return self.output.emit("You can't get there from here.", "system")
            case "exit_game":
                if self.allow_exit:
                    raise SystemExit()
                return self._end_game()

    def _end_game(self):
        """Common end-of-game behavior: no exceptions, just events/flags."""
        # Only emit these once if you like; but this is fine for now.
        self.output.emit("GAME OVER.", "system")
        self.output.emit("Refresh the page to play again.", "system")
        self.output.emit("", "game_over")  # sentinel for the browser
        self.running = False
