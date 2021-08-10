from core import Input, Screen, Game, pg, np
from spritesheet import Spritesheet

# pg = pygame
# np = numpy

square_position = np.array(Screen.size // 2)


while Game.run:
    Game.update()

    if Game.input["type": pg.QUIT]:
        Game.run = False

    if Game.input["type": pg.KEYDOWN, "key": pg.K_q]:
        print("Hello world!")

    if Game.input["type": pg.KEYDOWN, "key": pg.K_ESCAPE]:
        Game.run = False

    if Game.input["type": pg.KEYDOWN, "key": pg.K_UP]:
        square_position = square_position - (0, 10)
    if Game.input["type": pg.KEYDOWN, "key": pg.K_DOWN]:
        square_position = square_position + (0, 10)

    if Game.input["type": pg.KEYDOWN, "key": pg.K_LEFT]:
        square_position = square_position - (10, 0)
    if Game.input["type": pg.KEYDOWN, "key": pg.K_RIGHT]:
        square_position = square_position + (10, 0)

    Screen.screen.fill((0, 0, 0))

    pg.draw.rect(Screen.screen, (255, 255, 255), (square_position, (10, 10)))

    pg.display.update()
    Game.clock.tick(Game.fps)

pg.quit()
