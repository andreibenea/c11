class Output:
    def __init__(self):
        self.events = []  # list of {"kind": ..., "text": ...}

    def emit(self, text: str, kind: str = "narration"):
        # Store it for whatever front-end we use
        self.events.append({"kind": kind, "text": text})
        # CLI rendering
        if kind == "scene":
            print()
            print(text)
            print()
        elif kind == "system":
            print(f"[INFO] {text}")
        elif kind == "dialogue_npc":
            print(f"[NPC] {text}")
        elif kind == "hint":
            print()
            print(f">>>{text}<<<")
            print()
        elif kind == "event":
            print(f"[EVENT] {text}")
        elif kind == "debug":
            # print(f"[DEBUG] {text}")
            # print("============================")
            pass
        else:
            print(text)
