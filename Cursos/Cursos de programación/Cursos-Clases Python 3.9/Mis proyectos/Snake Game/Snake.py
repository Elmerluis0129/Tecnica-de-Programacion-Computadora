#Game made whit Inex's Tutorial
import sys
import pygame
import random
import tkinter as tk
from tkinter import messagebox as mBox

Height    = 500
Width     = 500 
Black     = (0, 0, 0)
Red       = (255, 0, 0)
Purple    = (100, 0, 255)
Yellow    = (255, 236, 0)
DarkGreen = (40, 100, 3)
Green     = (45, 150, 10)
Orange    = (255, 159, 3)
Grid_size = 20 
Dificult  = 20
Normal    = 10
Easy      = 4

main_image = pygame.image.load("Snake.jpg")
paused_image = pygame.image.load("Paused.jpg")


class Snake: #Serpiente
    def __init__(self):
        self.velocity = 20 #Velocidad
        self.length = 1 #longitud
        self.snake_body = [[220, 220]] #Cuerpo
        self.actual_movements = random.choice(["right", "left", "down", "up"]) #Movimiento actual
        self.best_score = 1 #Mejor record
        self.temp_score = 1 #Record temporal

    def move_snake(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN: #Sirve para identificar cuando presionen una flecha.
                if event.key == pygame.K_LEFT:#Flecha izquierda
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.actual_movements = "left"
                elif event.key == pygame.K_RIGHT:#Flecha derecha
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.actual_movements = "right"
                elif event.key == pygame.K_UP:#Flecha arriba
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.actual_movements = "up"
                elif event.key == pygame.K_DOWN:#Flecha abajo
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue
                    self.actual_movements = "down"

                if event.key == pygame.K_p:
                    pause_game(window)
        self.snake_movements(window)

    def snake_movements(self, window): #Movimientos de la serpiente
        if self.actual_movements == "right":
            temp = self.snake_body[0][0] + self.velocity
            x = self.check_bounds(temp, "max_limit")
            self.update_snake(x, "X", window)

        if self.actual_movements == "left":
            temp = self.snake_body[0][0] - self.velocity
            x = self.check_bounds(temp, "min_limit")
            self.update_snake(x, "X", window)

        if self.actual_movements == "up":
            temp = self.snake_body[0][1] - self.velocity
            y = self.check_bounds(temp, "min_limit")
            self.update_snake(y, "Y", window)

        if self.actual_movements == "down":
            temp = self.snake_body[0][1] + self.velocity
            y = self.check_bounds(temp, "max_limit")
            self.update_snake(y, "Y", window)

    def update_snake(self, value, key, window):
        if key == "X":
            self.snake_body.insert(0, [value, self.snake_body[0][1]])
            self.snake_body.pop()
            self.draw_snake(window)
        else:
            self.snake_body.insert(0, [self.snake_body[0][0], value])
            self.snake_body.pop()
            self.draw_snake(window)
            
    def draw_snake(self, window): #Creamos la serpiente
        for idx, body in enumerate(self.snake_body):
            if idx == 0: 
                pygame.draw.rect(window, DarkGreen, [body[0], body[1], 20, 20]) #Cabeza de la serpiente
                continue

            pygame.draw.rect(window, Green, [body[0], body[1], 20, 20]) #Cuerpo de la serpiente

        self.check_error(window)

    def check_valid_movement(self, next_move): #Con esto impedimos que haga un movimiento contrario al movimiento actual
        if next_move == "right" and self.actual_movements == "left": #Si va hacia la izquierda, no permite ir hacia la derecha
            return True
        if next_move == "left" and self.actual_movements == "right": #Si va hacia la derecha, no permite ir hacia la izquierda
            return True
        if next_move == "up" and self.actual_movements == "down": #Si va hacia abajo, no permite ir hacia arriba
            return True
        if next_move == "down" and self.actual_movements == "up": #Si va hacia arriba, no permite ir hacia abajo
            return True

    def check_bounds(self, value_to_chcek, limit): #Limites, para que aparezca del otro lado si llega al limite
        if limit == "max_limit":
            if value_to_chcek > 480:
                return 0
            else:
                return value_to_chcek

        else:
            if value_to_chcek < 0:
                return 480
            else:
                return value_to_chcek

    def get_snake_head(self): #Cabeza de la serpiente
        return self.snake_body[0]

    def grow_snake(self, value, window): #Crecimiento de la serpiente
        self.snake_body.insert(0, list(value))
        self.draw_snake(window)

    def check_error(self, window): #Si choca con el cuerpo pierde
        if self.get_snake_head() in self.snake_body[2:]:
            self.reset()

    def reset(self): #Reinicio de la serpiente al perder 
        message(self.length)
        self.snake_body = [[220, 220]]
        self.actual_movements = random.choice(["right", "left", "up", "down"])

        if self.length > self.temp_score:
            self.temp_score = self.length
            self.best_score = self.length

        self.length = 1

def message(score): #Mensaje
    root = tk.Tk()
    root.withdraw()
    mBox.showerror("YOU LOST", f"Your score was: {score}") #Mensaje que muestra al perder
    try:
        root.destroy()
    except:
        pass

class Food: #Comida de  la serpiente
    def __init__(self):
        self.food_position = (0, 0) #Posicion de la comida
        self.random_position()

    def random_position(self): #Posicion random de la comida
        self.food_position = (random.randrange(0, 480, 20), random.randrange(0, 480, 20)) #Que aparezca random del 0 al 480

    def draw_food(self, window): #Creacion de la comida
        pygame.draw.rect(window, Red, [self.food_position[0], self.food_position[1], 20, 20]) #Creamos la comida
        #Comidas Troll
        #   pygame.draw.rect(window, Red, [self.food_position[1], self.food_position[0], 20, 20]) #Comida Troll(En caso de que quieras poner el juego más dificil)
        #pygame.draw.rect(window, Red, [self.food_position[0], self.food_position[0], 20, 20]) #Comida Troll(En caso de que quieras poner el juego más dificil)
        #pygame.draw.rect(window, Red, [self.food_position[1], self.food_position[1], 20, 20]) #Comida Troll(En caso de que quieras poner el juego más dificil)

class Block:
    def __init__(self):
        self.block_position = (0, 0)
        self.random_position()

    def random_position(self): #Ubicacion random de los bloques
        self.block_position = [(random.randrange(0, 480, 20), random.randrange(0, 480, 20)) for i in range(Normal)]#Creacion de bloques en ubicaciones random (Dificultad)

    def draw_block(self, window): #Dibujar los bloques
        for i, value in enumerate(self.block_position):
            pygame.draw.rect(window, Black, [value[0], value[1], 20, 20])


def check_food(snake, food, window): #Aqui es para que le cresca la cola a la serpiente por cada comida que se coma
    if tuple(snake.get_snake_head()) == food.food_position:
        snake.grow_snake(food.food_position, window)
        food.random_position()
        food.draw_food(window)

        snake.length += 1

        if snake.length > snake.best_score: #Mejor record, para que siga subiendo si la longitud de la serpiente es mayor
            snake.best_score += 1

def check_block(snake, block): #Aqui reiniciamos la serpiente si choca con un bloque negro
    if tuple(snake.get_snake_head()) in block.block_position:
        block.random_position
        snake.reset()

#class Difficulty:
    #def __init__(self):
        #self.Dificult = 20
        #self.Normal   = 10
        #self.Easy     = 5

    def nivel(self, dificultad):
        pass

def draw_grid(window): #Funcion para pintar y dibujar la ventana, como las lineas
    window.fill(Orange) #Damos color de fondo a la ventana
    x = 0
    y = 0
    for i in range(Width): #Ciclo para dibujar linea por linea
        x += Grid_size #Aumentamos
        y += Grid_size #Aumentamos

        pygame.draw.line(window, Black, (x, 0), (x, Width)) #Dibujamos las lineas Horizontales
        pygame.draw.line(window, Black, (0, y), (Height, y)) #Dibujamos las lineas verticales

def start_menu(start, window):
    window.blit(main_image, (0, 0)) #Aqui mostramos la imagen en nuestra ventana
    pygame.display.update() #Actualizamos la ventana
    for event in pygame.event.get(): #Capturamos caulquier evento
        if event.type == pygame.QUIT: #Si se ejecuta esto, el usuario quiere cerrar el juego
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN: 
            if event.key: #Si se presiona  una tecla
                return False  #devuelve False

    return True

def pause_game(window):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Si se ejecuta esto, el usuario quiere cerrar el juego
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()

        window.blit(paused_image, (0, 0))
        pygame.display.update()

def main():
    pygame.init() #Creamos un objeto de pygame
    window = pygame.display.set_mode((Height, Width)) #Creamos la ventana 500 x 500
    pygame.display.set_caption("Snake") #Le ponemos nombre a la ventana

    
    clock = pygame.time.Clock() #Tiempo
    snake = Snake() #Serpiente
    food = Food() #Comida
    block = Block() #Bloques

    game_font = pygame.font.SysFont("Bell MT", 26) #Tipo de lentra y tamano
    start = True

    while True:
        clock.tick(11) #Para que nuestro juego no vaya tan rapido
        
        while start:
            start = start_menu(start, window)

        draw_grid(window) #Llamamos la funcion para que dibuje la ventana y las lineas
        snake.move_snake(window) #Se llama a la función que se encarga de los movimientos de la serpiente
        check_block(snake, block)
        check_food(snake, food, window) #Se llama a la función que reinicia la serpiente si choca con su cuerpo

        #Score - Best Score
        score = game_font.render(f"Score: {snake.length}", True, Black) #Creacion de record
        window.blit(score, (1, 4))
        best_score = game_font.render(f"Best Score {snake.best_score}", True, Black) #Creacion de mejor record
        window.blit(best_score, (1, 24))

        block.draw_block(window) #Se dibujan los bloques

        if food.food_position in block.block_position: #Aquí evitamos que la comida quede en la posición de un bloque negro
            food.random_position()

        food.draw_food(window) #Se dibuja la comida
        pygame.display.update() #Se actualiza la ventana


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo. Por favor, espere...")
        exit()
