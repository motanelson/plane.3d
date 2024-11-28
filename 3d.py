import pygame
import sys

# Inicialização do pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de Paisagem de Avião")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configurações do cenário
horizon_y = 50  # Altura inicial da linha do horizonte
triangle_width = 200  # Largura do triângulo (pista)
triangle_x = WIDTH // 2 - triangle_width // 2  # Posição inicial no eixo X
triangle_color = WHITE
triangle_speed = 5
vertical_speed = 5

# Função principal
def main():
    global horizon_y, triangle_x

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação com teclas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and horizon_y < HEIGHT - 100:  # Mover horizonte para baixo
            horizon_y += vertical_speed
        if keys[pygame.K_UP] and horizon_y > 50:  # Mover horizonte para cima
            horizon_y -= vertical_speed
        if keys[pygame.K_LEFT] and triangle_x > 0:  # Mover triângulo para a esquerda
            triangle_x -= triangle_speed
        if keys[pygame.K_RIGHT] and triangle_x < WIDTH - triangle_width:  # Mover triângulo para a direita
            triangle_x += triangle_speed

        # Desenhar na tela
        WINDOW.fill(BLACK)

        # Desenhar linha do horizonte
        pygame.draw.line(WINDOW, WHITE, (0, horizon_y), (WIDTH, horizon_y), 2)

        # Desenhar triângulo
        triangle_points = [
            (triangle_x + triangle_width // 2, horizon_y ),  # Base inferior (centro)
            (triangle_x - triangle_width, HEIGHT),  # Ponta do triângulo (no horizonte)
            (triangle_x + triangle_width*2, HEIGHT),  # Base direita
           
        ]
        pygame.draw.polygon(WINDOW, triangle_color, triangle_points)

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

