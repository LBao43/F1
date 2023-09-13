import pygame

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
screen = pygame.display.set_mode((800, 600))

# Thiết lập tiêu đề của cửa sổ
pygame.display.set_caption("Game đơn giản")

# Khởi tạo màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Khởi tạo vị trí ban đầu của nhân vật
x = 400
y = 300

# Vòng lặp chính của game
running = True
while running:
    # Xử lý các sự kiện trong game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình bằng màu đen
    screen.fill(BLACK)

    # Vẽ nhân vật trên màn hình
    pygame.draw.circle(screen, WHITE, (x, y), 50)

    # Cập nhật vị trí của nhân vật khi người chơi di chuyển chuột
    x, y = pygame.mouse.get_pos()

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc Pygame khi thoát game
pygame.quit()