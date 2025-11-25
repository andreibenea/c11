from . import (
    c11,
    hallway_ground,
    hallway_upper,
    j23,
    overseer_office,
    security_office,
    vault_door_room,
)

SCENES = {
    "c11": c11.c11,
    "hallway_ground": hallway_ground.hallway_ground,
    "hallway_upper": hallway_upper.hallway_upper,
    "j23": j23.j23,
    "overseer_office": overseer_office.overseer_office,
    "security_office": security_office.security_office,
    "vault_door_room": vault_door_room.vault_door_room,
}
