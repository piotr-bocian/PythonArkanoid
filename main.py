import sys
import pygame
import csv
from Classes.Level import Level
from Classes.Game import Game
from Classes.MenuElements.Menu import Menu
from Classes.MenuElements.HallOfFame import HallOfFame
from Classes.MenuElements.Options import Options
from Classes.MenuElements.EndGameScreen import EndGameScreen

menu = Menu([320, 270])
hof = HallOfFame()
options = Options([320, 270])
pygame.init()
screen = pygame.display.set_mode((1280, 720))
end_screen = EndGameScreen(0,0)
running = True

def update_load_file(output):
    with open('data/load.csv', 'w+') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(output)
        f_object.close()

def load_game():
    with open('data/load.csv', newline='') as f:
        reader = csv.reader(f)
        game_data = list(reader)
        f.close()
        return game_data

def play(game, i, points = 0, pattern = None):
    game.points = points
    game.levels.clear()
    while not game.finished and not game.paused:
        game.levels.append(Level(len(i),3))
        recent = game.levels[len(game.levels) - 1]
        if pattern:
            recent.bricks.pattern = pattern
            recent.bricks.create_bricks_from_pattern()
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(180, 0, 1100, 720), width=2)
            recent.paddle.draw(screen)
            recent.ball.draw(screen)
            pygame.display.flip()
            recent.lscreen.display(screen)
            pattern = None
        else:
            recent.level_setup(screen)
        recent.game_loop(screen)
        if recent.cleared:
            game.points += recent.points
            i.append("0")
        if recent.lost:
            game.finished = True
        if recent.saved:
            game.paused = True



while running:
    screen.fill((0, 0, 0))
    if menu.run_display:
        menu.draw_menu(screen)
        menu.draw_cursor(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    menu.move_cursor_down()
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    menu.move_cursor_up()
                elif event.key == pygame.K_RETURN or pygame.K_SPACE:
                    if menu.state == 0:
                        menu.run_display = False
                        i = ['0']
                        game = Game()
                        while not game.finished and not game.paused:
                            play(game, i)
                        if game.paused:
                            menu.run_display = True
                            output = [len(i), game.points,game.levels[-1].bricks.pattern]
                            update_load_file(output)
                        if game.finished:
                            end_screen.update(game.points, len(i))
                            end_screen.run_display = True
                    elif menu.state == 1:
                        menu.run_display = False
                        data = load_game()
                        i = ["0"]*int(data[0][0])
                        pattern = eval(data[0][2])
                        game = Game()
                        while not game.finished and not game.paused:
                            play(game, i, int(data[0][1]),pattern)
                        if game.paused:
                            menu.run_display = True
                            output = [len(i), game.points, game.levels[-1].bricks.pattern]
                            update_load_file(output)
                        if game.finished:
                            end_screen.update(game.points, len(i))
                            end_screen.run_display = True
                    elif menu.state == 2:
                        menu.run_display = False
                        options.run_display = True
                    elif menu.state == 3:
                        menu.run_display = False
                        hof.run_display = True
                    elif menu.state == 4:
                        sys.exit(0)

    elif hof.run_display:
        hof.draw_hof(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or pygame.K_SPACE:
                    menu.run_display = True
                    hof.run_display = False
    elif options.run_display:
        options.draw_hof(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or pygame.K_SPACE:
                    menu.run_display = True
                    hof.run_display = False

    elif end_screen.run_display:
        end_screen.draw_eog(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = end_screen.name[:-1]
                elif event.key == pygame.K_RETURN:
                    output = [end_screen.name,end_screen.score]
                    with open('Classes/MenuElements/hof.csv', 'a', newline='') as f_object:
                        writer_object = csv.writer(f_object)
                        writer_object.writerow(output)
                        f_object.close()
                    end_screen.run_display = False
                    menu.run_display = True
                else:
                    end_screen.name += event.unicode


    pygame.display.flip()
