import pygame

# Dimension for Board components 
WIDTH = 600
HEIGHT = 1000
SQUARE_SIZE = 50
FPS = 30
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))



# draw game option buttons
background = pygame.image.load('assets/background.png')
buttonundo = pygame.image.load('assets/buttonundohover.png')
buttonmusicon = pygame.image.load('assets/buttonmusicon.png')
buttonrestart = pygame.image.load('assets/buttonrestarthover.png')
buttonsettings = pygame.image.load('assets/buttonsettinghover.png')
piecered = pygame.image.load('assets/piecered.png')
pieceorange = pygame.image.load('assets/pieceorange.png')
pieceyellow = pygame.image.load('assets/pieceyellow.png')
piecegreen = pygame.image.load('assets/piecegreen.png')
pieceblue = pygame.image.load('assets/pieceblue.png')
piecenavy = pygame.image.load('assets/piecenavy.png')
piecepurple = pygame.image.load('assets/piecepurple.png')
piecepink = pygame.image.load('assets/piecepink.png')
piecewhite = pygame.image.load('assets/piecewhite.png') 
piecesecret = pygame.image.load('assets/piecesecret.png')
cluegray = pygame.image.load('assets/cluegray.png')
clueblue = pygame.image.load('assets/clueblue.png')
cluepink = pygame.image.load('assets/cluepink.png')
submitwaiting = pygame.image.load('assets/submitwaiting.png') 
submitready = pygame.image.load('assets/submitready.png') 
submitconfirm = pygame.image.load('assets/submitconfirm.png') 


easy_piece_collection = [piecered, pieceyellow, pieceblue, piecepurple] 
normal_piece_collection = [pieceorange, piecegreen]
hard_piece_collection = [piecenavy, piecepink]
button_collection = [buttonundo, buttonmusicon, buttonsettings, buttonrestart]
