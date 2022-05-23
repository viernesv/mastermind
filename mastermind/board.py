import pygame
from mastermind.constants import *

difficulty = 'Normal'
class Board():
    def __init__(self):
        self.pieces = []
        self.secret = []

        self.set_pieces()

    def draw_board(self, window):
        # load board background
        WINDOW.blit(background, (0, 0))

        # draw game option buttons
        for i in range(len(button_collection)):
            self.draw_item(window, button_collection[i], 50 + 150*i, 200)
        
        # draw pieces on Easy difficulty
        for i in range(len(easy_piece_collection)):
            self.draw_item(window, easy_piece_collection[i], 200 + SQUARE_SIZE*i, 925)
        
        # draw pieces on Normal/Hard difficulty
        if difficulty != 'Easy':
            for i in range(len(normal_piece_collection)):
                self.draw_item(window, normal_piece_collection[i], 150 + SQUARE_SIZE*5*i, 925)
            if difficulty == 'Hard':
                for i in range(len(normal_piece_collection)):
                    self.draw_item(window, hard_piece_collection[i], 100 + SQUARE_SIZE*7*i, 925)

        # draw secret code 
        for i in range(4):
            self.draw_item(window, piecesecret, 175 + SQUARE_SIZE*i, 300)

        # draw submit code section
        for i in range(10):
            self.draw_item(window, submitwaiting, 100, 350 + SQUARE_SIZE*i)

        # draw guess section
        for row in range(10):
            for col in range(4):
                self.draw_item(window, piecewhite, 175  + SQUARE_SIZE*col, 350 + SQUARE_SIZE*row)
        
        #draw clue section
        for row in range(10):
            for col in range(4):
                self.draw_item(window, cluegray, 400  + SQUARE_SIZE/2*col, 350 + SQUARE_SIZE*row)

    def draw_item(self, window, asset, x_pos, y_pos):
        window.blit(asset, (x_pos, y_pos))

    def get_board(self):
        return self.board

    def get_pieces(self):
        return self.pieces
    
    def set_pieces(self):
        if difficulty == 'Easy':
            self.pieces = easy_piece_collection
        elif difficulty == 'Normal':
            self.pieces = normal_piece_collection
        elif difficulty == 'Hard':
            self.pieces = hard_piece_collection
        
    def play_music(self):
        # Starting the mixer
        pygame.mixer.init()
        
        # Loading the song
        pygame.mixer.music.load("assets/music.mp3")
        
        # Start playing the song
        pygame.mixer.music.play(-1)     # argument of -1 loops music


        
