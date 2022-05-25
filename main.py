# MUSIC CREDIT: Kevin Macleod - 8bit Dungeon (No copyright), https://youtu.be/tM5d0G0vue0
# All graphics designed on or retrieved from https://www.canva.com
import pygame
import sys
from mastermind.constants import *
from mastermind.board import *
from mastermind.game import *


pygame.init()

def main():
    title_screen()
    game_setup()
    result = game_loop()
    game_end(result)

def title_screen():
    WINDOW.blit(menu, (0, 0))
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_xpos, mouse_ypos = event.pos[0], event.pos[1]
                if 90 < mouse_xpos < 500 and 320 < mouse_ypos < 440:        # play
                        run = False
                elif 90 < mouse_xpos < 500 and 570 < mouse_ypos < 690:       # settings
                        print('B')
                elif 90 < mouse_xpos < 500 and 810 < mouse_ypos < 930:      # quit
                        pygame.quit()
                        sys.exit()
        pygame.display.update()

def game_setup():
    board = Board()
    pygame.display.set_caption('Mastermind, implemented by Virgilio Viernes')
    board.play_music()
    board.draw_board(WINDOW)
    
def game_loop():
    game = Game()
    run = True
    game_is_won = False
    attempt = game.get_attempt()
    difficulty = game.get_difficulty()
    while run and attempt <= MAX_ATTEMPTS:
        pygame.time.Clock().tick(FPS)
        submitted_guess = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_xpos, mouse_ypos = event.pos[0], event.pos[1]

                if 925 < mouse_ypos < 975:                                          # PLAYER MOVE: Draw color on board
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

                current_row = game.get_board()[attempt - 1]                         # PLAYER MOVE: Submit guess
                if len(current_row) == 4:
                    game.draw_submit_button()
                    if 100 < mouse_xpos < 150 and 800 - SQUARE_SIZE * (attempt - 1) < mouse_ypos < 800 - SQUARE_SIZE * (attempt - 1) + SQUARE_SIZE:
                        game.submit_guess()
                        submitted_guess = True
                        game.increment_attempt()
                        attempt = game.get_attempt()
    
                if submitted_guess is True:                                         # PLAYER MOVE: Check guess against secret code
                    current_guess = game.get_board()[attempt - 2]
                    game.set_current_guess(current_guess)
                    game.give_clue()
                    game_is_won = game.check_code_to_win()
                    if game_is_won is True:
                        game.show_answer()
                        run = False
                
                if 50 < mouse_xpos < 100 and 200 < mouse_ypos < 250:                # BUTTON FUNCTION: Go back to start menu
                    pygame.mixer.music.stop()
                    pygame.init()
                    main()
    
                if 275 < mouse_xpos < 325 and 200 < mouse_ypos < 250:               # BUTTON FUNCTION: Toggle music on or off
                    game.toggle_music()
                
                if 500 < mouse_xpos < 550 and 200 < mouse_ypos < 250:               # BUTTON FUNCTION: Redo guesses for current row
                    game.redo_guess()

        pygame.display.update()
        
    if attempt > MAX_ATTEMPTS:
        game.show_answer()
        return game_is_won
    if run is False and game_is_won is True:
        return game_is_won
    elif run is False and game_is_won is False:
        pygame.quit()
        sys.exit()
    
def game_end(result):
    pygame.time.delay(DELAY_TIME)
    if result is True:
        WINDOW.blit(win, (0, 0))
    else:
        WINDOW.blit(lose, (0, 0))
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_xpos, mouse_ypos = event.pos[0], event.pos[1]
                if 90 < mouse_xpos < 500 and 660 < mouse_ypos < 780:        # play again
                    pygame.mixer.music.stop()
                    pygame.init()
                    main()
                elif 90 < mouse_xpos < 500 and 810 < mouse_ypos < 930:      # quit
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
    


if __name__ == "__main__":
   main()






