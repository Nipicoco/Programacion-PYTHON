#codigo terminado, usaremos random y time para los clocks y la def mover
import pygame
from pygame.locals import *
import time
import random
#tamano del snake en si
TAMANO = 40

#usaremos la clase manzana para cargar la imagen de nuestra carpeta
class Manzana:
    def __init__(self, pantalla1):
        self.pantalla1 = pantalla1
        self.imagen = pygame.image.load("resources/manzana2.jpg").convert()
        self.x = 120
        self.y = 120

    def dibujar(self):
        self.pantalla1.blit(self.imagen, (self.x, self.y))
        pygame.display.flip()

    def mover(self):
        self.x = random.randint(1,24)*TAMANO
        self.y = random.randint(1,19)*TAMANO

class Snake:
    def __init__(self, pantalla1):
        self.pantalla1 = pantalla1
        self.imagen = pygame.image.load("resources/azusa1.jpg").convert()
        self.direccion = 'abajo'

        self.largo = 1
        self.x = [40]
        self.y = [40]

    def mover_izq(self):
        self.direccion = 'izquierda'

    def mover_der(self):
        self.direccion = 'derecha'

    def mover_arriba(self):
        self.direccion = 'arriba'

    def mover_abajo(self):
        self.direccion = 'abajo'

    def actualizar(self):
        # ACTUALIZAR CUERPO DE SANEK
        for i in range(self.largo-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # ACTUALIZAR CABEZA
        if self.direccion == 'izquierda':
            self.x[0] -= TAMANO
        if self.direccion == 'derecha':
            self.x[0] += TAMANO
        if self.direccion == 'arriba':
            self.y[0] -= TAMANO
        if self.direccion == 'abajo':
            self.y[0] += TAMANO

        self.dibujar()

    def dibujar(self):
        for i in range(self.largo):
            self.pantalla1.blit(self.imagen, (self.x[i], self.y[i]))

        pygame.display.flip()

    def aumentar_largo(self):
        self.largo += 1
        self.x.append(-1)
        self.y.append(-1)

class Juego:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake de rodrigo y Nicolas")

        pygame.mixer.init()
        self.play_background_music()

        self.superficie = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.superficie)
        self.snake.dibujar()
        self.manzanita = Manzana(self.superficie)
        self.manzanita.dibujar()

    def play_background_music(self):
        pygame.mixer.music.load('resources/kiminosei.mp3')
        pygame.mixer.music.play(-1, 0)

    def reproducir_sonido(self, nombre_sonido):
        if nombre_sonido == "crash":
            sound = pygame.mixer.Sound("resources/oof.mp3")
        elif nombre_sonido == 'ding':
            sound = pygame.mixer.Sound("resources/noice.mp3")

        pygame.mixer.Sound.play(sound)
        # pygame.mixer.music.stop()


    def resetear(self):
        self.snake = Snake(self.superficie)
        self.manzanita = Manzana(self.superficie)


    def colision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + TAMANO:
            if y1 >= y2 and y1 < y2 + TAMANO:
                return True
        return False

    def fondo_conversion(self):
        bg = pygame.image.load("resources/fondo1.jpg")
        self.superficie.blit(bg, (0,0))

    def jugar(self):
        self.fondo_conversion()
        self.snake.actualizar()
        self.manzanita.dibujar()
        self.mostrar_puntaje()
        pygame.display.flip()

        # snake come manzanita 
        for i in range(self.snake.largo):
            if self.colision(self.snake.x[i], self.snake.y[i], self.manzanita.x, self.manzanita.y):
                self.reproducir_sonido("ding")
                self.snake.aumentar_largo()
                self.manzanita.mover()

        # snake colisiona consigo mismo
        for i in range(3, self.snake.largo):
            if self.colision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.reproducir_sonido('crash')
                raise "Colision detectada"

        # snake colisiona con los bordes
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.reproducir_sonido('crash')
            raise "Choque con los bordes"

    def mostrar_puntaje(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Puntaje: {self.snake.largo}",True,(200,200,200))
        self.superficie.blit(score,(850,10))

    def mostrar_muerte(self):
        self.fondo_conversion()
        font = pygame.font.SysFont('arial', 30)
        linea1 = font.render(f"Juego terminado, tu puntaje es de: {self.snake.largo}", True, (0, 0, 0))
        self.superficie.blit(linea1, (200, 300))
        linea2 = font.render("Para jugar denuevo, apretar enter, para terminar, escape!", True, (0, 0, 0))
        self.superficie.blit(linea2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def ejecutars(self):
        ejecutandose = True
        pausado = False

        while ejecutandose:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        ejecutandose = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pausado = False

                    if not pausado:
                        if event.key == K_LEFT:
                            self.snake.mover_izq()

                        if event.key == K_RIGHT:
                            self.snake.mover_der()

                        if event.key == K_UP:
                            self.snake.mover_arriba()

                        if event.key == K_DOWN:
                            self.snake.mover_abajo()

                elif event.type == QUIT:
                    ejecutandose = False
            try:

                if not pausado:
                    self.jugar()

            except Exception as e:
                self.mostrar_muerte()
                pausado = True
                self.resetear()

            time.sleep(.1)

if __name__ == '__main__':
    game = Juego()
    game.ejecutars()