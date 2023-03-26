import sys
import random
import pygame
#from skimage.transform import resize
#import matplotlib.pyplot as plt
#import cv2
import numpy as np
def scale(im, nR, nC):
    number_rows = len(im)     # source number of rows
    number_columns = len(im[0])  # source number of columns
    return [[ im[int(number_rows * r / nR)][int(number_columns * c / nC)]
                 for c in range(nC)] for r in range(nR)]

class Jeu:
    # contenir toutes les variables ainsi que les fonctions utiles pour le bon deroulement du jeu

    def __init__(self):
        """:rtype: object"""
        self.ecran = pygame.display.set_mode((800, 600))  # defini la resoultion de la fenetre ,tuple(longueur,largeur)
        pygame.display.set_caption('Jeu Snake')  # attribue un titre a la fenetre
        self.jeu_encours = True

        # creer les variables de position et de direction du serpent 1

        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10

        # creer les variables serpent 2

        self.serpent2_position_x = 200
        self.serpent2_position_y = 200
        self.serpent2_direction_x = 0
        self.serpent2_direction_y = 0
        self.serpent2_corps = 10

        # cree la position pour la pomme

        self.pomme_position_x = random.randrange(120, 680, 10)
        self.pomme_position_y = random.randrange(120, 580, 10)
        self.pomme = 10

        # cree la position pour la banane

        self.banane_position_x = random.randrange(120, 680, 10)
        self.banane_position_y = random.randrange(120, 580, 10)
        self.banane = 10
        # fixer les fps
        self.clock = pygame.time.Clock()

        # creer une liste qui rescence toutes les positions du serpent
        self.positions_serpent = []
        self.positions_serpent2 = []

        # creer la variable en rapport avec la taille du serpent
        self.taille_du_serpent = 1
        self.taille_du_serpent2 = 1

        self.ecran_du_debut = True

        self.image_tete_serpent = pygame.image.load('la_tete_du_serpent.png')
        self.image_tete_serpent2 = pygame.image.load('la_tete_du_serpent.png')

        self.image_pomme = pygame.image.load('pomme.jpg')
        #self.image_pomme_taille = pygame.transform.scale(self.image_pomme, (10,10))
        #self.image_pomme = cv2.imread('pomme.jpg')
        #self.res = cv2.resize(self.image_pomme, dsize=(10, 10), interpolation=cv2.INTER_CUBIC)
        # Charger l'image

        self.image = pygame.image.load('snake-game.jpg')
        # retrecir l'image
        self.image_titre = pygame.transform.scale(self.image, (200, 100))

        # creer la variable score
        self.score = 0
        self.score2 = 0

    def fonction_principale(self):

        # permet de gerer les evenements , d'afficher certains composants du jeu grace au while loop

        while self.ecran_du_debut:

            for evenement in pygame.event.get():  # verifier les evenements lorsque le jeu est en cours
                # print(evenement)
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:

                        self.ecran_du_debut = False

                self.ecran.fill((0, 0, 0))

                self.ecran.blit(self.image_titre, (300, 50, 100, 50))
                # self.creer_message('petite','Snake',(300,300,100,50),(255,255,255))
                self.creer_message('petite', 'Le but du jeu est que le serpent se développe ',
                                   (250, 200, 200, 5), (240, 240, 240))
                self.creer_message('petite', ' pour cela , il a besoin de pomme ,mangez-en autant que possible !!',
                                    (190, 220, 200, 5), (240, 240, 240))
                self.creer_message('moyenne', 'Appuyer sur Enter pour commencer', (200, 450, 200, 5),
                                    (255, 255, 255))

                pygame.display.flip()




        while self.jeu_encours:

            # creer un while loop pour creer l'ecran de debut /events /afficher l'image ...

            for evenement in pygame.event.get():# verifier les evenements lorsque le jeu est en cours
                #print(evenement)
                if evenement.type == pygame.QUIT:
                    sys.exit()

                # creer les evenements qui permettent de bouger le serpent

                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_RIGHT:
                        # lorsque l'on presse la touche 'fleche droite'
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0
                        #print('Droite')

                    if evenement.key == pygame.K_LEFT:
                        # lorsque l'on presse la touche 'fleche gauche'

                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0
                        #print('LEFT')

                    if evenement.key == pygame.K_DOWN:
                        # lorsque l'on presse la touche 'fleche vers le  bas'

                        self.serpent_direction_y = 10
                        self.serpent_direction_x = 0
                        #print('En bas')

                    if evenement.key == pygame.K_UP:
                        # lorsque l'on presse la touche 'fleche vers le haut'

                        self.serpent_direction_y = -10
                        self.serpent_direction_x = 0
                        #print('En haut ')

                    if evenement.key == pygame.K_z:
                        self.serpent2_direction_y = -10
                        self.serpent2_direction_x = 0

                    if evenement.key == pygame.K_s:
                        self.serpent2_direction_y = 10
                        self.serpent2_direction_x = 0

                    if evenement.key == pygame.K_q:
                        self.serpent2_direction_x = -10
                        self.serpent2_direction_y = 0

                    if evenement.key == pygame.K_d:
                        self.serpent2_direction_x = 10
                        self.serpent2_direction_y = 0



            # faire bouger le serpent si il se trouve dans les limites du jeu

            if self.serpent_position_x <= 100 or self.serpent_position_x >= 700 \
                or self.serpent_position_y <= 100 or self.serpent_position_y >= 600 :
                # si la position du serpent depasse les limites alors le jeu s'arrete
                sys.exit()

            if self.serpent2_position_x <= 100 or self.serpent2_position_x >= 700 \
                or self.serpent2_position_y <= 100 or self.serpent2_position_y >= 600 :
                sys.exit()

            self.serpent_mouvement()
            self.serpent2_mouvement()

            # cree la cond si le serpent mange la pomme
            if self.banane_position_y == self.serpent2_position_y and self.serpent2_position_x == self.banane_position_x :

                self.banane_position_x = random.randrange(110,690,10)
                self.banane_position_y = random.randrange(110,590,10)

                self.taille_du_serpent2 += 1
                self.score2 += 1

            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x :

                self.pomme_position_x = random.randrange(110,690,10)
                self.pomme_position_y = random.randrange(110,590,10)

                self.taille_du_serpent += 1
                self.score += 1

            # creer une liste pour les qui stocke la position de la tete du serpent
            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)

            la_tete_du_serpent2 = []
            la_tete_du_serpent2.append(self.serpent2_position_x)
            la_tete_du_serpent2.append(self.serpent2_position_y)

            # append dans la liste des positions du serpent

            self.positions_serpent.append(la_tete_du_serpent)

            self.positions_serpent2.append(la_tete_du_serpent2)

            # cond pour resoudre le probleme des positions du serpent avec la taille du serpent
            if len(self.positions_serpent) > self.taille_du_serpent:

                self.positions_serpent.pop(0)
                print(self.positions_serpent)

            if len(self.positions_serpent2) > self.taille_du_serpent2:

                self.positions_serpent2.pop(0)
                print(self.positions_serpent2)


            self.afficher_les_elements()
            #self.se_mord(la_tete_du_serpent)

            self.creer_message('grande','Snake Game', (320, 10, 100, 50), (255, 255, 255), )
            self.creer_message('grande','player 1 = {} player 2 = {}'.format(str(self.score), str(self.score2)), (250, 50, 50, 50), (255, 255, 255), )

            # afficher les limites
            self.creer_limites()
            self.clock.tick(30)

            pygame.display.flip()# mettre a jour l'ecrand


    # creer une fonction qui permet de creer un rectangle qui representera les limites du jeu (dimension 100,100,600,500),3


    def creer_limites(self):
        # afficher les limites du jeu

        pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)

    def serpent_mouvement(self):

        # faire bouger le serpent

        self.serpent_position_x += self.serpent_direction_x  # faire bouger le serpent a gauche ou a droite
        self.serpent_position_y += self.serpent_direction_y  # faire bouger le serpent en haut ou en bas

    def serpent2_mouvement(self):

        self.serpent2_position_x += self.serpent2_direction_x
        self.serpent2_position_y += self.serpent2_direction_y


    def afficher_les_elements(self):

        self.ecran.fill((0, 0, 0))  # attriubue la couleur noir a l'ecran

        # Afficher le serpent
        pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent_position_x, self.serpent_position_y,
                                                   self.serpent_corps, self.serpent_corps))

        self.ecran.blit(self.image_tete_serpent,(self.serpent_position_x,self.serpent_position_y,
                                                 self.serpent_corps,self.serpent_corps))

        pygame.draw.rect(self.ecran, (0, 255, 255), (self.serpent2_position_x, self.serpent2_position_y,
                                                   self.serpent2_corps, self.serpent2_corps))

        self.ecran.blit(self.image_tete_serpent2, (self.serpent2_position_x, self.serpent2_position_y,
                                                  self.serpent2_corps, self.serpent2_corps))

        # afficher la pomme
        pygame.draw.rect(self.ecran, (255, 0, 0),
                         (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))

        # afficher la banane
        pygame.draw.rect(self.ecran, (255, 255, 0),
                         (self.banane_position_x, self.banane_position_y, self.banane, self.banane))

        self.afficher_Serpent()
        self.afficher_Serpent2()


    def afficher_Serpent(self):
        # afficher les autres parties du serpent

        for partie_du_serpent in self.positions_serpent[:-1]:
            pygame.draw.rect(self.ecran, (0, 255, 0),
                             (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))

    def afficher_Serpent2(self):
        # afficher les autres parties du serpent

        for partie_du_serpent2 in self.positions_serpent2[:-1]:
            pygame.draw.rect(self.ecran, (0, 255, 0),
                             (partie_du_serpent2[0], partie_du_serpent2[1], self.serpent2_corps, self.serpent2_corps))
    #def se_mord(self,tete_serpent):


        # le seprent se mord

     #   for partie_serpent in self.positions_serpent[:-1]:
      #      if partie_serpent == tete_serpent :
       #         sys.exit()
# creer une fonction qui permet d'afficher des messages

    def creer_message(self,font,message,message_rectangle,couleur):

        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)

        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message,True,couleur)

        self.ecran.blit(message,message_rectangle)

if __name__ == '__main__':

    pygame.init()# initie pygame
    Jeu().fonction_principale()
    pygame.quit()# quitte pygame,