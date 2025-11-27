from npc import NonPlayerCharacter
from player import Player
from world import World
from event_emitter import Output
from game import Game
from scenes import SCENES


juno = NonPlayerCharacter("juno", "Juno", "j23", "juno_j23")
security_guard_one = NonPlayerCharacter("security_guard_one", "Officer Jason", "security_office", "intercom_c11")
overseer = NonPlayerCharacter("overseer", "Overseer Hanson", "overseer_office", "overseer")

npcs = {
    "juno": juno,
    "security_guard_one": security_guard_one,
    "overseer": overseer
}


event_emitter = Output()
player = Player("You", SCENES["c11"]["id"])
world = World(SCENES, npcs)
game = Game(player, world, event_emitter)


game.run()