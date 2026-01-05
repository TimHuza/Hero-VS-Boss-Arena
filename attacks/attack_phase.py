from attacks.attack1 import attack1_main
from attacks.attack2 import attack2_main
from attacks.attack3 import attack3_main
from attacks.attack4 import attack4_main

class AttackPhase:
    def __init__(self):
        self.attacks = [attack1_main, attack2_main, attack3_main, attack4_main]
        self.current_attack_index = 0
        self.finished = False
        self.game_over = False

    def update(self, player, screen):
        if self.current_attack_index >= len(self.attacks):
            self.finished = True
            return

        attack = self.attacks[self.current_attack_index]
        result = attack(player, screen)

        if result == "GAME_OVER":
            self.game_over = True
            self.finished = True
        elif result is True:
            self.current_attack_index += 1