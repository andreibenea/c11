# 📘 C-Eleven  
*A terminal-based Python adventure game*

C-Eleven is a **command-driven text adventure** built entirely in Python.  
The game loads scenes, objects, and NPC dialogue dynamically using a modular architecture that makes it easy to expand or modify the story.

This repository contains the **standalone Python CLI version** of the game.

---

## 🚀 Features

- **Modular scene architecture** – each room is defined in its own file  
- **Dialogue / NPC system** – structured dialogue trees with branching conversation  
- **Command interpreter** – all player actions processed through a unified system  
- **Extensible engine** – add rooms, commands, NPCs, and interactions without engine changes  
- **World loader** – scenes are registered and connected via `world.py`


---

## 📂 Project Structure
```
C-ELEVEN/
├── commands.py
├── event_emitter.py
├── game.py
├── handler.py
├── main.py
├── npc.py
├── player.py
├── world.py
│
├── dialogues/
│   ├── __init__.py
│   ├── intercom_c11.py
│   ├── juno_j23.py
│   ├── juno_j23_2.py
│   ├── juno_j23_3.py
│
└── scenes/
    ├── __init__.py
    ├── c11.py
    ├── hallway_ground.py
    ├── hallway_upper.py
    ├── j23.py
    ├── overseer_office.py
    ├── security_office.py
    ├── vault_door_room.py
```
---

## ▶️ Running the Game

### 1. Navigate to the project folder  
`cd c-eleven`

### 2. Launch the game  
`python3 main.py`

### 3. Start playing  
The game will display the current scene and wait for input.

Example commands:

- `look`  
- `inspect bed`  
- `talk security`  
- `go hallway`  
- `use console`  
- `help`

---

## 🧩 How the Game Works

### Scenes

Each module inside `/scenes/` defines:

- a room description  
- objects available for interaction  
- exits to other rooms  
- optional scripted events  

### Dialogues

NPC conversations in `/dialogues/` include:

- player dialogue choices  
- NPC responses  
- branching outcomes  

### Engine

`game.py` is responsible for:

- parsing player input  
- executing commands  
- advancing dialogue  
- handling scene transitions  
- emitting events  
- running the main game loop  

### World Builder

`world.py` registers all scenes and defines the starting location.  
The world layout is fully expandable by adding new modules.

---

## 🛠️ Extending the Game

You can expand the game by modifying or adding:

- `/scenes/*.py` — new rooms, objects, or events  
- `/dialogues/*.py` — new NPCs and dialogue trees  
- `commands.py` — new player commands  
- `world.py` — updates to the world map  

The engine is modular — **adding content never requires modifying core systems**.

---

## 📄 License

This project is for educational and portfolio use.  
Feel free to modify or extend it.






