# MUSIC CREDIT: Kevin Macleod - 8bit Dungeon (No copyright), https://youtu.be/tM5d0G0vue0
# All graphics designed on or retrieved from https://www.canva.com

import pygame
import sys
from mastermind.constants import *
from mastermind.board import *
from mastermind.game import *

pygame.init()

def main():
    setup()
    game_loop()
    end_game()

def setup():
    board = Board()
    pygame.display.set_caption('Mastermind, implemented by Virgilio Viernes')
    board.play_music()
    board.draw_board(WINDOW)
    
def game_loop():
    game = Game()
    run = True
    attempt = game.get_attempt()
    dificulty = game.get_difficulty()
    while run and attempt <= 10:
        pygame.time.Clock().tick(FPS)
        submitted_guess = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_xpos, mouse_ypos = event.pos[0], event.pos[1]

                if 925 < mouse_ypos < 975:                                          # Player move: Draw color on board
                    if 200 < mouse_xpos < 250:
                        game.place_color('red')
                    elif 250 < mouse_xpos < 300:
                        game.place_color('yellow')
                    elif 300 < mouse_xpos < 350:
                        game.place_color('blue')
                    elif 350 < mouse_xpos < 400:
                        game.place_color('purple')
                    elif 150 < mouse_xpos < 200 and difficulty != "Easy":
                        game.place_color('orange')     
                    elif 400 < mouse_xpos < 450 and difficulty != "Easy":
                        game.place_color('green')     
                    elif 100 < mouse_xpos < 150 and difficulty == "Hard":
                        game.place_color('navy')           
                    elif 450 < mouse_xpos < 500 and difficulty == "Hard":
                        game.place_color('pink')        

                current_row = game.get_board()[attempt - 1]                         # Player move: Submit guess
                if len(current_row) == 4:
                    game.draw_submit_button()
                    if 100 < mouse_xpos < 150 and 800 - 50 * (attempt - 1) < mouse_ypos < 800 - 50 * (attempt - 1) + 50:
                        game.submit_guess()
                        submitted_guess = True
                        game.increment_attempt()
                        attempt = game.get_attempt()
    
                if submitted_guess is True:                                         # Player move: Check guess against secret code
                    current_guess = game.get_board()[attempt - 2]
                    game.set_current_guess(current_guess)
                    game.give_clue()
                    game_is_over = game.check_code_to_win()
                    if game_is_over is True:
                        game.show_answer()
                        run = False
                
                if 50 < mouse_xpos < 100 and 200 < mouse_ypos < 250:                # BUTTON FUNCTION: Redo guesses on current row
                    game.redo_guess()
    
                if 200 < mouse_xpos < 250 and 200 < mouse_ypos < 250:               # BUTTON FUNCTION: Toggle music on or off
                    game.toggle_music()
                
                if 500 < mouse_xpos < 550 and 200 < mouse_ypos < 250:               # BUTTON FUNCTION: Start new game  
                    pygame.init()
                    main()
        pygame.display.update()

def end_game():
    print("Game Over")
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
   main()






