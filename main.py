import pygame
import random

def generate_food():
    x_rand = random.randrange(100, 600, 10)
    y_rand = random.randrange(100, 400, 10)
    return x_rand, y_rand

def game_not_over(snake):
    head = snake[0]
    tail = snake[1:]
    for parts in tail:
        if head == parts:
            return False
    return True

def game_loop():
        white = (255, 255, 255)
        green = (0, 255, 0)
        game = pygame
        game.init()
        window_size = (800, 600)
        window = game.display.set_mode(window_size)
        game.display.set_caption("Snakey game")
        x = 400
        y = 300
        w = 10
        h = 10
        vel = 10
        hit = False
        food_x, food_y = generate_food()
        food = [food_x, food_y, w, h]
        head = [x, y, w, h]
        snakey = [head]
        key_pressed = {"up" : True, "down" : False, "left" : False, "right" : False}
        current_way = "up"
        old_way = "up"
        game_is_not_over = True
        points = 0
        game_speed = 100
        while game_is_not_over:
            value = 0
            for event in game.event.get():
                if event.type == game.KEYDOWN:
                    print("Key pressed")
                    print(event.key)
                    if event.key == game.K_UP:
                        if key_pressed["down"] == True:
                            pass
                        else:
                            for keys in key_pressed:
                                key_pressed[keys] = False
                            key_pressed["up"] = True
                            break
                    if event.key == game.K_DOWN:
                        if key_pressed["up"] == True:
                            pass
                        else:
                            for keys in key_pressed:
                                key_pressed[keys] = False
                            key_pressed["down"] = True
                            break
                    if event.key == game.K_LEFT:
                        if key_pressed["right"] == True:
                            pass
                        else:
                            for keys in key_pressed:
                                key_pressed[keys] = False
                            key_pressed["left"] = True
                            break
                    if event.key == game.K_RIGHT:
                        if key_pressed["left"] == True:
                            pass
                        else:
                            for keys in key_pressed:
                                key_pressed[keys] = False
                            key_pressed["right"] = True
                            break
            if key_pressed["up"]:
                if y > 0:
                    y -= vel
                else:
                    y = 600 - vel
            if key_pressed["down"]:
                if y <= 600 - vel:
                    y += vel
                else:
                    y = 0
            if key_pressed["left"]:
                if x > 0:
                    x -= vel
                else:
                    x = 800 - vel
            if key_pressed["right"]:
                if x <= 800 - vel:
                    x += vel
                else:
                    x = 0
            game.time.delay(game_speed)
            window.fill(green)
            new_head = [x, y, w, h]
            game_is_not_over = game_not_over(snakey)
            snakey.pop()
            snakey.insert(0, new_head)
            for tails in snakey:
                game.draw.rect(window, 0, tails)
            if hit != True:
                game.draw.rect(window, 0, food)
            else:
                points += 1
                if game_speed > 20:
                    game_speed -= 10
                food_x, food_y = generate_food()
                food = [food_x, food_y, w, h]
                snakey.insert(len(snakey), _tail)
                print(snakey)
                hit = False
            if snakey[0] == food:
                if len(snakey) == 1:
                    _tail = snakey[0]
                else:
                    _tail = snakey[len(snakey) - 1]
                    print(_tail)
                hit = True
                print("HIT")
            game.display.update()
            game_is_not_over = game_not_over(snakey)
        window.fill(white)
        font = game.font.Font('freesansbold.ttf', 32)
        text = font.render("Points: {}".format(int(points)), True, green, white)
        rect = text.get_rect(center=(400,300))
        window.blit(text, rect)
        game.display.update()
        while True:
            for event in game.event.get():
                if event.type == game.KEYDOWN:
                    game.quit()
                    break

def main():
    game_loop()

if __name__ == '__main__':
    main()
