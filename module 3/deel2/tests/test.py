import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bloons Tower Defense 6")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Tower class
class Tower(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=pos)
        self.range = 100  # Range of the tower
        self.damage = 1   # Damage per shot

    def update(self):
        pass

    def attack(self, target):
        target.health -= self.damage
        if target.health <= 0:
            target.kill()
            return 1  # Cash earned from destroying balloon
        return 0  # No cash earned yet

# Balloon class
class Balloon(pygame.sprite.Sprite):
    def __init__(self, path, target):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.path = path
        self.index = 0
        self.progress = 0.0  # Progress along the path (0.0 to 1.0)
        self.rect.center = self.path[0]
        self.target = target
        self.health = 3  # Health of the balloon

    def update(self):
        if self.progress >= 1.0:
            self.target.hp -= 1
            self.kill()
            return 0  # No cash earned for reaching the end
        else:
            self.progress += 0.005  # Adjust this value to change the speed
            self.rect.centerx = self.path_point(self.progress)[0]
            self.rect.centery = self.path_point(self.progress)[1]
            return 0  # No cash earned while moving

    def path_point(self, progress):
        index = min(int(progress * (len(self.path) - 1)), len(self.path) - 2)
        start_point = self.path[index]
        end_point = self.path[index + 1]
        return (start_point[0] + (end_point[0] - start_point[0]) * (progress * (len(self.path) - 1) - index),
                start_point[1] + (end_point[1] - start_point[1]) * (progress * (len(self.path) - 1) - index))

# Target class
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 20))
        self.hp = 100
        self.cash = 20  # Starting cash

    def draw_health_bar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x - 20, self.rect.y - 30, 40, 10))
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x - 20, self.rect.y - 30, self.hp * 0.4, 10))
        font = pygame.font.Font(None, 24)
        cash_text = font.render(f"Cash: {self.cash}", True, YELLOW)
        screen.blit(cash_text, (10, 10))

# Define the path (letter Z shape)
path = [(100, 100), (700, 100), (100, 300), (700, 500)]

# Convert path points to pygame.Rect objects
path_rects = [pygame.Rect(point[0] - 5, point[1] - 5, 10, 10) for point in path]

# Group for all sprites
all_sprites = pygame.sprite.Group()
towers = pygame.sprite.Group()
balloons = pygame.sprite.Group()

# Create target
target = Target()
all_sprites.add(target)

# Game loop
running = True
clock = pygame.time.Clock()

# Balloon settings
balloon_limit = 5  # Max number of balloons
balloon_spawn_delay = 60  # Delay between spawning balloons
balloon_spawn_timer = balloon_spawn_delay

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                overlapping = False
                for sprite in all_sprites:
                    if isinstance(sprite, Tower) and sprite.rect.collidepoint(mouse_pos):
                        overlapping = True
                        break
                if not overlapping and not any(rect.collidepoint(mouse_pos) for rect in path_rects):
                    if target.cash >= 10:
                        tower = Tower(mouse_pos)
                        towers.add(tower)
                        all_sprites.add(tower)
                        target.cash -= 10

    # Update
    all_sprites.update()

    # Spawn balloons
    if balloon_spawn_timer <= 0 and len(balloons) < balloon_limit:
        balloon = Balloon(path, target)
        all_sprites.add(balloon)
        balloons.add(balloon)
        balloon_spawn_timer = balloon_spawn_delay
    else:
        balloon_spawn_timer -= 1

    # Check for collision between towers and balloons
    for tower in towers:
        for balloon in balloons:
            distance = math.sqrt((tower.rect.centerx - balloon.rect.centerx) ** 2 +
                                 (tower.rect.centery - balloon.rect.centery) ** 2)
            if distance < tower.range:
                target.cash += tower.attack(balloon)

    # Draw
    screen.fill(WHITE)
    pygame.draw.lines(screen, BLACK, False, path, 3)  # Draw the path
    all_sprites.draw(screen)
    target.draw_health_bar(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
