from npc import NonPlayerCharacter
from player import Player
from world import World
from event_emitter import Output
from game import Game
from scenes import SCENES


juno = NonPlayerCharacter(
    "juno",
    "Juno",
    "Juno carries an anxious energy beneath her calm exterior. Her hands are steady, but her thoughts look like they're racing ahead of her words.",
    "j23",
    "juno_j23",
)
security_guard_one = NonPlayerCharacter(
    "security_guard_one",
    "Officer Jason",
    "Dark circles under his eyes betray a long shift. Even so, he keeps a firm grip on protocol, scanning every movement with practiced vigilance.",
    "security_office",
    "intercom_c11",
)
overseer = NonPlayerCharacter(
    "overseer",
    "Overseer Hanson",
    "The Overseer regards you with a controlled, measured calm—every word and gesture precise, as if the entire Vault runs on his breathing.",
    "overseer_office",
    "overseer",
)

npcs = {"juno": juno, "security_guard_one": security_guard_one, "overseer": overseer}


event_emitter = Output()
player = Player("You", "Player", SCENES["c11"]["id"])
world = World(SCENES, npcs)
game = Game(player, world, event_emitter)


game.run()
