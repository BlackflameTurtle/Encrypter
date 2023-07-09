import sys

import pygame
from pygame.locals import *
pygame.font.init()

class Acode:
    def __init__(self, message, coded):
        self.title = False
        self.coded = coded
        self.message = message
        self.punctuation = ".,?! "
        self.alphabet = "abcdFGHefgABhijkWXlqyzCDEIJKoκpLMNrstOPQRuvwxSTmnUVYZоеíսһахсԁрӏјąïօզυʝỏḷúżýʐʂ"
        self.new_message = ""
    def encryption(self):
        for i in range(len(self.message)):
            letter = self.alphabet.find(self.message[i])
            if letter > -1:
                self.new_message += self.alphabet[letter + 11]


            if letter <= -1:
                mark = self.punctuation.find(self.message[i])
                self.new_message += self.punctuation[mark]
        print(self.new_message)
    def code_breaking(self):
        for i in range(len(self.coded)):
            letter = self.alphabet.find(self.coded[i])

            if letter > -1:
                self.new_message += self.alphabet[letter - 11]



            if letter <= -1:
                mark = self.punctuation.find(self.coded[i])
                self.new_message += self.punctuation[mark]
        print(self.new_message)


class CCipher:
    def __init__(self, message, shift):
        self.shift = shift
        self.message = message
        self.punctuation = ".,?! "
        self.alphabet = "abcdefghijklmnoκpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.new_message = ""
    def encryption(self):
        for i in range(len(self.message)):
            letter = self.alphabet.find(self.message[i])
            if letter > -1:
                self.new_message += self.alphabet[letter + self.shift]


            if letter <= -1:
                mark = self.punctuation.find(self.message[i])
                self.new_message += self.punctuation[mark]
        print(self.new_message)
    def code_breaking(self):
        for i in range(len(self.message)):
            letter = self.alphabet.find(self.message[i])

            if letter > -1:
                self.new_message += self.alphabet[letter - self.shift]



            if letter <= -1:
                mark = self.punctuation.find(self.message[i])
                self.new_message += self.punctuation[mark]



class App:
    def __init__(self, surface):
        self.ccipher_coding= False
        self.ccipher_decoding = False
        self.acode_coding = False
        self.acode_decoding = False
        self.ccipher_typing = True
        self.surface = surface
        self.user_amessage = ""
        self.user_acipher = ""
        self.user_ccipher = ""
        self.user_shift = 10
        self.ccipher = CCipher(self.user_ccipher, self.user_shift)
        self.acode = Acode
        self.acode(self.user_amessage , self.user_acipher)
        self.lock =  False
        self.color = 255, 255, 255
    def screen(self):
        self.surface.fill((100, 150, 255))

    def buttons_title (self):
        self.title = True
        self.color1 = 255, 255, 255
        self.color2 = 255, 255, 255
        while self.title:

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 190 <= mouse_x <= 315 and 210 <= mouse_y <= 260:
                self.color1 = 250, 150, 0

            elif 590 <= mouse_x <= 690 and 210 <= mouse_y <= 260:
                self.color2 = 250, 150, 0

            else:
                self.color1 = 255, 255, 255
                self.color2 = 255, 255, 255
            if pygame.mouse.get_pressed() != (0,0,0):
                if 190 <= mouse_x <= 315 and 210 <= mouse_y <= 260:
                    self.ccipher_screen()

                elif 590 <= mouse_x <= 690 and 210 <= mouse_y <= 260:
                    self.color2 = 250, 150, 0

            font1 = pygame.font.SysFont("Britannic", 30, bold=False, italic=False)
            line1 = font1.render("Ccipher", True, (0, 0, 0))
            line2 = font1.render("Acode", True, (0,0,0))
            self.surface.fill((100, 150, 255))
            self.surface.blit(line1,(200, 220))
            self.surface.blit(line2, (600, 220))
            pygame.draw.rect(self.surface, (self.color1), (190, 210, 125, 50), 1, 10)
            pygame.draw.rect(self.surface, (self.color2), (590, 210, 100, 50), 1, 10)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        title = False
    def ccipher_screen(self):
        ccipher = True
        self.color1 = 255, 255, 255
        self.color2 = 255, 255, 255
        while ccipher:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 140 <= mouse_x <= (140 + 277) and 160 <= mouse_y <= 210:
                self.color1 = 250, 150, 0

            elif 540 <= mouse_x <= (540 + 277) and 160 <= mouse_y <= 210:
                self.color2 = 250, 150, 0

            else:
                self.color1 = 255, 255, 255
                self.color2 = 255, 255, 255
            if pygame.mouse.get_pressed() != (0, 0, 0):
                if 140 <= mouse_x <= (140 + 277) and 160 <= mouse_y <= 210:
                    ccipher = False
                    self.title = False
                    self.ccipher_coding = True
                    self.ccipher_typing = True

               # elif 540 <= mouse_x <= (540 + 277) and 210 <= mouse_y <= 260:
                #    self.color2 = 250, 150, 0

            font1 = pygame.font.SysFont("Britannic", 30, bold=False, italic=False)
            line1 = font1.render("Ccipher encryption", True, (0, 0, 0))
            line2 = font1.render("Ccipher decryption", True, (0, 0, 0))
            self.surface.fill((100, 150, 255))
            self.surface.blit(line1, (150, 170))
            self.surface.blit(line2, (550, 170))
            pygame.draw.rect(self.surface, (self.color1), (140, 160, 277, 50), 1, 10)
            pygame.draw.rect(self.surface, (self.color2), (540, 160, 277, 50), 1, 10)
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        title = False

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    print(self.user_ccipher)
                    if event.key == K_CAPSLOCK:
                        if not self.lock:
                            self.lock = True
                            print(self.lock)
                            break
                        if self.lock:
                            self.lock = False
                            print(self.lock)
                    if self.ccipher_typing:
                        if event.key == K_a:
                            self.user_ccipher += "a"
                        if event.key == K_b:
                            self.user_ccipher += "b"
                        if event.key == K_c:
                            self.user_ccipher += "c"
                        if event.key == K_d:
                            self.user_ccipher += "d"
                        if event.key == K_e:
                            self.user_ccipher += "e"
                        if event.key == K_f:
                            self.user_ccipher += "f"
                        if event.key == K_g:
                            self.user_ccipher += "g"
                        if event.key == K_h:
                            self.user_ccipher += "h"
                        if event.key == K_i:
                            self.user_ccipher += "i"
                        if event.key == K_j:
                            self.user_ccipher += "j"
                        if event.key == K_k:
                            self.user_ccipher += "k"
                        if event.key == K_l:
                            self.user_ccipher += "l"
                        if event.key == K_m:
                            self.user_ccipher += "m"
                        if event.key == K_n:
                            self.user_ccipher += "n"
                        if event.key == K_o:
                            self.user_ccipher += "o"
                        if event.key == K_p:
                            self.user_ccipher += "p"
                        if event.key == K_q:
                            self.user_ccipher += "q"
                        if event.key == K_r:
                            self.user_ccipher += "r"
                        if event.key == K_s:
                            self.user_ccipher += "s"
                        if event.key == K_t:
                            self.user_ccipher += "t"
                        if event.key == K_u:
                            self.user_ccipher += "u"
                        if event.key == K_v:
                            self.user_ccipher += "v"
                        if event.key == K_w:
                            self.user_ccipher += "w"
                        if event.key == K_x:
                            self.user_ccipher += "x"
                        if event.key == K_y:
                            self.user_ccipher += "y"
                        if event.key == K_z:
                            self.user_ccipher += "z"
                        if event.key == K_SPACE:
                            self.user_ccipher += " "
                        if event.key == K_PERIOD:
                            self.user_ccipher += "."
                        if event.key == K_BACKSPACE:
                            self.user_ccipher = self.user_ccipher[:-1]


            while self.ccipher_coding:
                self.ccipher.encryption()
                self.ccipher_coding = False
            while self.ccipher_decoding:
                self.ccipher.code_breaking()
                self.ccipher_decoding = False
            if self.ccipher_typing:
                self.color = 255, 255, 255
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 790 <= mouse_x <= 880 and 445 <= mouse_y <= 475:
                    self.color = 250, 150, 0
                if 790 <= mouse_x <= 880 and 445 <= mouse_y <= 475:
                    self.ccipher.encryption()
                    
                pygame.draw.rect(self.surface, (255, 255, 255), (20, 70, 860, 360), 0, 10)
                pygame.draw.rect(self.surface, (self.color), (790, 445, 90, 30), 1, 10)




                font1 = pygame.font.SysFont("Britannic", 30, bold=False, italic=False)
                font2 = pygame.font.SysFont("Britannic", 20, bold=False, italic=False)
                line1 = font1.render("Enter the message you wish to encrypt", True, (0, 0, 0))
                line2 = font2.render(self.user_ccipher, True, (0,0,0))
                line3 = font2.render("Encrypt", True, (0,0,0))
                self.surface.blit(line1, (20, 10))
                self.surface.blit(line2, (25, 80))
                self.surface.blit(line3, (800, 450))
                pygame.display.flip()


            self.screen()
            if not self.ccipher_typing:
                pygame.display.flip()










if __name__ == '__main__':
    app = App(pygame.display.set_mode((900, 500)))
    app.buttons_title()
    app.run()


