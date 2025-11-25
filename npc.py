class NonPlayerCharacter:
    def __init__(self, id: str, name: str, scene_id: str, dialog_id=None):
        self.id = id
        self.name = name
        self.scene_id = scene_id
        self.dialog_id = dialog_id
        self.type = "npc"

    def talk(self, intro: str, potential_replies: dict):
        i = 1
        print(intro)
        for reply in potential_replies:
            print(f"{i}. {potential_replies[reply][self.type]}")
            i += 1
