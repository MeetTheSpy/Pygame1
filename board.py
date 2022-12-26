import pygame


class Board:
    def __init__(self, width, height, a=True):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, 'white',
                                 ((self.left + j * self.cell_size, self.top + i * self.cell_size),
                                 (self.cell_size, self.cell_size)), 1)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Соединяй точки')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    board = Board(5, 5)
    board.set_view(100, 100, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()