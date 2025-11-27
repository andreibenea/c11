class NonPlayerCharacter:
    def __init__(self, id: str, name: str, scene_id: str, dialog_id=None):
        self.id = id
        self.name = name
        self.scene_id = scene_id
        self.dialog_id = dialog_id
        self.type = "npc"

    def talk(self, intro: str, potential_replies: dict):
        lines = [intro]
        i = 1
        for reply_key in potential_replies:
            line = f"{i}. {potential_replies[reply_key][self.type]}"
            lines.append(line)
            i += 1
        return lines
