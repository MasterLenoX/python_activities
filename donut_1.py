import pygame
import math

# Initialize Pygame
pygame.init()

# Corrected variable name
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Donut parameters
theta_spacing = 0.05
phi_spacing = 0.03
R1 = 1
R2 = 2
K2 = 5

# Correctly initializing 2D lists
output = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]
zbuffer = [[-10000 for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]


def clear_screen():
    """Clears the screen buffers."""
    for i in range(SCREEN_HEIGHT):
        for j in range(SCREEN_WIDTH):
            output[i][j] = ' '
            zbuffer[i][j] = -1000


def render_frame(A, B):
    """Renders the ASCII donut frame."""
    K1 = SCREEN_WIDTH / 2
    clear_screen()

    cosA, sinA = math.cos(A), math.sin(A)
    cosB, sinB = math.cos(B), math.sin(B)

    for theta in range(0, int(2 * math.pi / theta_spacing)):
        for phi in range(0, int(2 * math.pi / phi_spacing)):
            cosphi = math.cos(phi * phi_spacing)
            sinphi = math.sin(phi * phi_spacing)
            circleX = R2 + R1 * math.cos(theta * theta_spacing)
            circleY = R1 * math.sin(theta * theta_spacing)

            x = circleX * (cosB * cosphi + sinA * sinB * sinphi) - circleY * cosA * sinB
            y = circleX * (sinB * cosphi - sinA * cosB * sinphi) + circleY * cosA * cosB
            z = K2 + cosA * cosphi * sinphi + circleY * sinA
            ooz = 1 / z

            xp = int(SCREEN_WIDTH / 2 + K1 * x * ooz)
            yp = int(SCREEN_HEIGHT / 2 - K1 * y * ooz)

            if 0 <= xp < SCREEN_WIDTH and 0 <= yp < SCREEN_HEIGHT:
                L = (
                    cosphi * math.cos(theta * theta_spacing) * sinB
                    - cosA * math.cos(theta * theta_spacing) * sinphi
                    - sinA * math.sin(theta * theta_spacing)
                    + cosB * (cosA * math.sin(theta * theta_spacing) - math.cos(theta * theta_spacing) * sinA * sinphi)
                )

                if L > 0 and ooz > zbuffer[yp][xp]:
                    zbuffer[yp][xp] = ooz
                    luminanceIndex = int(L * 8)
                    luminanceIndex = min(luminanceIndex, 7)  # Prevent out-of-bounds error
                    output[yp][xp] = ".,-~:;=!*#$@"[luminanceIndex]


def main():
    """Main game loop for the rotating ASCII donut."""
    A, B = 0, 0
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render_frame(A, B)

        # Draw ASCII donut to the screen
        for i in range(SCREEN_HEIGHT):
            for j in range(SCREEN_WIDTH):
                if output[i][j] != ' ':
                    screen.set_at((j, i), (255, 255, 255))

        pygame.display.flip()
        screen.fill((0, 0, 0))
        A += 0.08
        B += 0.08

        clock.tick(60)  # Maintain 60 FPS

    pygame.quit()


if __name__ == "__main__":
    main()
