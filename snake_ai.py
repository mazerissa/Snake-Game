DIRECTIONS = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def get_next_move(snake_segments, food_position):
    head_x, head_y = snake_segments[0]
    food_x, food_y = food_position

    options = ["up", "down", "left", "right"]

    def distance_after_move(direction):
        dx, dy = DIRECTIONS[direction]
        new_head = (head_x + dx, head_y + dy)
        return abs(new_head[0] - food_x) + abs(new_head[1] - food_y)

    options.sort(key=distance_after_move)


    for direction in options:
        dx, dy = DIRECTIONS[direction]
        new_head = (head_x + dx, head_y + dy)

        if abs(new_head[0]) > 280 or abs(new_head[1]) > 280:
            continue

        if new_head in snake_segments:
            continue

        return direction  

    return "up" 
