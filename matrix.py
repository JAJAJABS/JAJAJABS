import random
import time

# Configuración de los caracteres
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
char_list = list(characters)

# Configuración de los colores
green = "\033[32m"
reset = "\033[0m"

def draw():
    # Dibujar la columna
    for i in range(80):
        char_index = random.randint(0, len(char_list) - 1)
        char = char_list[char_index]
        print(green + char + reset, end="")
    print()

def main():
    while True:
        draw()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
