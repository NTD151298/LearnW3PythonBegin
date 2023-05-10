import pygame
import time
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập cửa sổ game
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Tạo một mặt phẳng game
game_surface = pygame.Surface((window_width, window_height))

# Tạo đơn vị LinhBo1
LinhBo1 = pygame.Surface((20, 20))
LinhBo1.fill((255, 0, 0))
LinhBo1_health = 100
LinhBo1_damage = 10
LinhBo1_range = 1
LinhBo1_attack_speed = 1
LinhBo1_move_speed = 2
LinhBo1_pos = [100, 100]

# Tạo đơn vị LinhBo2
LinhBo2 = pygame.Surface((20, 20))
LinhBo2.fill((0, 0, 255))
LinhBo2_health = 100
LinhBo2_damage = 10
LinhBo2_range = 1
LinhBo2_attack_speed = 1
LinhBo2_move_speed = 2
LinhBo2_pos = [400, 400]

def draw_linhbo(linhbo, position):
    game_surface.blit(linhbo, position)

# Vẽ đơn vị LinhBo1
draw_linhbo(LinhBo1, LinhBo1_pos)

# Vẽ đơn vị LinhBo2
draw_linhbo(LinhBo2, LinhBo2_pos)

# Hàm di chuyển đơn vị
def move_unit(unit_pos, target_pos, move_speed):
    # Tính toán khoảng cách giữa đơn vị và mục tiêu
    distance = ((target_pos[0]-unit_pos[0])**2 + (target_pos[1]-unit_pos[1])**2)**0.5
    
    # Nếu khoảng cách nhỏ hơn tốc độ di chuyển, đơn vị sẽ di chuyển đến mục tiêu
    if distance < move_speed:
        unit_pos[0] = target_pos[0]
        unit_pos[1] = target_pos[1]
    else:
        # Tính toán hướng di chuyển
        dx = (target_pos[0] - unit_pos[0]) / distance
        dy = (target_pos[1] - unit_pos[1]) / distance
        unit_pos[0] += dx * move_speed
        unit_pos[1] += dy * move_speed

# Hàm xử lý va chạm giữa 2 đơn vị
def collide(unit1_pos, unit2_pos):
    distance = ((unit1_pos[0]-unit2_pos[0])**2 + (unit1_pos[1]-unit2_pos[1])**2)**0.5
    return distance < 20  # 20 là bán kính của đơn vị

# Vòng lặp game
start_time = time.time()
while time.time() - start_time < 100:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

   

