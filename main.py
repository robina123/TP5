import random
import arcade
# import arcade.gui
from attack_animation import AttackType, AttackAnimation
from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.

class MyGame(arcade.Window):

    PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
    PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
    COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
    COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
    ATTACK_FRAME_WIDTH = 154 / 2.
    ATTACK_FRAME_HEIGHT = 154 / 2

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.player = None
        self.computer = None
        self.players = None
        self.rock_player = None
        self.paper = None
        self.scissors = None
        self.player_score = 0
        self.computer_score = 0
        self.player_attack_type = {}
        self.computer_attack_type = None
        self.player_attack_chosen = False
        self.player_won_round = 0
        self.draw_round = None
        self.game_state = GameState.NOT_STARTED

    def setup(self):
        self.player = arcade.Sprite('asset/faceBeard.png', 0.5, center_x=self.PLAYER_IMAGE_X, center_y=self.PLAYER_IMAGE_Y)
        self.computer = arcade.Sprite('asset/compy.png', 2.5, center_x=self.COMPUTER_IMAGE_X, center_y=self.COMPUTER_IMAGE_Y)
        self.players = None
        self.type_choice = arcade.SpriteList()
        self.rock_player = arcade.Sprite('asset/srock.png', 0.5, center_x=SCREEN_WIDTH / 4, center_y=SCREEN_HEIGHT / 5)
        self.type_choice.append(self.rock_player)
        self.paper_player = arcade.Sprite('asset/spaper.png', 0.5, center_x=SCREEN_WIDTH / 3, center_y=SCREEN_HEIGHT / 5 )
        self.type_choice.append(self.paper_player)
        self.scissors_player = arcade.Sprite('asset/scissors.png', 0.5, center_x=SCREEN_WIDTH / 6 , center_y=SCREEN_HEIGHT/ 5)
        self.type_choice.append(self.scissors_player)

        self.rock_computer = arcade.Sprite('asset/srock.png', 0.5, center_x=SCREEN_WIDTH / 1.35, center_y=SCREEN_HEIGHT / 5)
        self.paper_computer = arcade.Sprite('asset/spaper.png', 0.5, center_x=SCREEN_WIDTH / 1.35, center_y=SCREEN_HEIGHT / 5)
        self.scissors_computer = arcade.Sprite('asset/scissors.png', 0.5, center_x=SCREEN_WIDTH / 1.35, center_y=SCREEN_HEIGHT / 5)
        self.player_score = 0
        self.computer_score = 0
        self.player_attack_type = {1: AttackType.ROCK, 2: AttackType.PAPER, 3: AttackType.SCISSORS}
        self.computer_attack_type = None
        self.player_attack_chosen = False
        self.player_won_round = 0
        self.draw_round = None
        self.game_state = GameState.NOT_STARTED
    def validate_victory(self):
        """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """

    def draw_possible_attack(self):
        """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
        pass

    def draw_computer_attack(self):
        if self.game_state == GameState.ROUND_ACTIVE and self.player_attack_chosen == True:
            print ("draw computer attack")

    def draw_scores(self):
        """
       Montrer les scores du joueur et de l'ordinateur
       """
        pass

    def draw_instructions(self):
        """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
        pass
    def computer_choice(self):
        return random.choice(list(AttackType))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(SCREEN_TITLE, 0, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2, arcade.color.BLACK_BEAN, 60,width=SCREEN_WIDTH, align="center")
        arcade.draw_text(f"Le score de l'ordinateur est de {self.computer_score}",SCREEN_WIDTH/ 4.1, SCREEN_HEIGHT / 12, arcade.color.BLACK_BEAN, 20, width=SCREEN_WIDTH, align="center")
        arcade.draw_text(f"Votre score est de {self.player_score}", SCREEN_WIDTH / -5, SCREEN_HEIGHT / 12, arcade.color.BLACK_BEAN, 20, width=SCREEN_WIDTH, align="center")
        self.draw_instructions()
        self.player.draw()
        self.computer.draw()
        #self.players.draw()
        self.draw_possible_attack()
        self.draw_scores()


        if self.game_state == GameState.ROUND_ACTIVE:
                self.type_choice.draw()
        elif self.game_state == GameState.ROUND_DONE:
            if self.player_attack_type == AttackType.ROCK:
                self.rock_player.draw()
            elif self.player_attack_type == AttackType.PAPER:
                self.paper_player.draw()
            elif self.player_attack_type == AttackType.SCISSORS:
                self.scissors_player.draw()

        arcade.draw_rectangle_outline(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 5, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.RED, 5)
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 5, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.RED, 5)
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 6, SCREEN_HEIGHT / 5, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.RED, 5)
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 1.35, SCREEN_HEIGHT / 5, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.RED, 5)



    def on_update(self, delta_time):
        if self.player_attack_chosen:
            self.computer_attack_type = self.computer_choice()
            self.game_state = GameState.ROUND_DONE

    def on_key_press(self, key, key_modifiers):
        """hh
       Cette méthode est invoquée à chaque fois que l'usager tape une touche
       sur le clavier.
       Paramètres:
           - key: la touche enfoncée
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

       Pour connaître la liste des touches possibles:
       http://arcade.academy/arcade.key.html
       """
        if self.game_state == GameState.NOT_STARTED:
            self.game_state = GameState.ROUND_ACTIVE

        elif self.game_state == GameState.ROUND_DONE:
            self.game_state = GameState.ROUND_ACTIVE
        elif self.game_state == GameState.GAME_OVER:
            self.game_state = GameState.ROUND_ACTIVE
        print(self.computer_choice())
    def reset_round(self):
        """
       Réinitialiser les variables qui ont été modifiées
       """
        self.computer_attack_type = -1
        self.player_attack_chosen = False
        self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
        self.player_won_round = False
        self.draw_round = False

        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """

        # Test de collision pour le type d'attaque (self.player_attack_type).
        # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True
        if self.game_state == GameState.ROUND_ACTIVE:

            if self.rock_player.collides_with_point((x, y)):
                self.player_attack_type = AttackType.ROCK
                self.player_attack_chosen = True
            elif self.paper_player.collides_with_point((x, y)):
                self.player_attack_type = AttackType.PAPER
                self.player_attack_chosen = True
            elif self.scissors_player.collides_with_point((x, y)):
                self.player_attack_type = AttackType.SCISSORS
                self.player_attack_chosen = True



def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()