class World:
    def __init__(self, scenes: dict, npcs: dict):
        self.scenes = scenes
        self.npcs = npcs

    def get_scene(self, scene_id: str):
        return self.scenes[scene_id]

    def get_scene_npcs(self, scene_id: str) -> list[object]:
        return [npc for npc in self.npcs.values() if npc.scene_id == scene_id]

    def move_npc(self, npc: object, scene_id: str):
        npc.scene_id = scene_id
