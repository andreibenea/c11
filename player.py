from npc import NonPlayerCharacter


class Player(NonPlayerCharacter):
    def __init__(self, name, description, scene_id):
        super().__init__(
            id="player",
            name=name,
            description=description,
            scene_id=scene_id,
            dialog_id=None,
        )
        self.inventory = []
        self.type = "player"
        self.in_dialog = False

    def move_to(self, new_scene_id: str):
        self.scene_id = new_scene_id

    def add_item_to_inventory(self, item: dict):
        self.inventory.append(item)
