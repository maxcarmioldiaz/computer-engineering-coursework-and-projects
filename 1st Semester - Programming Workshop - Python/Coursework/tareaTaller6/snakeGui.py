import pygame
import snake as snk 

TAM = 10
TICK = 15

def main():
    global TICK
    pygame.init()
    snk.init()
    ancho = snk.cols * TAM
    alto = snk.filas * TAM
    window = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    snk.cambiar_direccion("U")
                elif keys[pygame.K_DOWN]:
                    snk.cambiar_direccion("D")
                elif keys[pygame.K_LEFT]:
                    snk.cambiar_direccion("L")
                elif keys[pygame.K_RIGHT]:
                    snk.cambiar_direccion("R")
        window.fill((100, 255, 100))
        for f in range(snk.filas):
            for c in range(snk.cols):
                x = c * TAM
                y = f * TAM
                if snk.matriz[f][c] == snk.MANZANA:
                    pygame.draw.rect(window, (255, 0, 0), (x, y, TAM, TAM))
                elif snk.matriz[f][c] == snk.MANZANA_DORADA:
                    pygame.draw.rect(window, (212, 175, 55), (x, y, TAM, TAM))
                elif snk.matriz[f][c] == snk.VENENO:
                    pygame.draw.rect(window, (0, 100, 0), (x, y, TAM, TAM))
                elif snk.matriz[f][c] > 0:
                    pygame.draw.rect(window, (100, 100, 255), (x, y, TAM, TAM))
        snk.avanzar()
        if snk.death():
            window.fill((40, 40, 40))
            for f in range(snk.filas):
                for c in range(snk.cols):
                    x = c * TAM
                    y = f * TAM
                    if snk.matriz[f][c] > 0:
                        pygame.draw.rect(window, (255, 255, 255), (x, y, TAM, TAM))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_r]:
                        pygame.init()
                        snk.init()
                        
                        
        pygame.display.update()
        TICK += snk.manzanas_comidas
        clock.tick(TICK)

    pygame.quit()

if __name__ == "__main__":
    main()
