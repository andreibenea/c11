from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game


class NonPlayerCharacter:
    def __init__(self, id: str, name: str, description:str, scene_id: str, dialog_id=None):
        self.id = id
        self.name = name
        self.description = description
        self.scene_id = scene_id
        self.dialog_id = dialog_id
        self.type = "npc"

    def talk(self, game: "Game"):
        lines = []
        dialog_hint = f"{game.talking_to}_{self.scene_id}"
        i = 1
        for reply_key in game.dialog_options:
            if dialog_hint in game.scene_hints:
                if game.dialog_options[reply_key]["outcome"] == "good":
                    line = f"{i}. [HINT] {game.dialog_options[reply_key][self.type]}"
                else:
                    line = f"{i}. {game.dialog_options[reply_key][self.type]}"
            else:
                line = f"{i}. {game.dialog_options[reply_key][self.type]}"
            lines.append(line)
            i += 1
        return lines
