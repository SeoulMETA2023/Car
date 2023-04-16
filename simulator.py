import pygame

from the_algorithm import path_search

DISPLAY_SIZE = (1100, 700)

pygame.init()
display = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Car navigation system simulator")
clock = pygame.time.Clock()


class Node:
    def __init__(self, pos: tuple[int, int], connected_nodes: list[int]):
        self.pos = pos
        self.connected_nodes = connected_nodes


def get_node_map(node_map: dict[int: Node]):
    return {node_n: node.connected_nodes for node_n, node in node_map.items()}


def get_cost_map(node_map: dict[int: Node]):
    cost_map = {}
    for node1_n, node1 in node_map.items():
        for node2_n in node1.connected_nodes:
            node2 = node_map[node2_n]
            cost_map[get_cost_map_key(node1_n, node2_n)] = get_cost(node1, node2)
    return cost_map


def get_cost_map_key(node1: int, node2: int):
    if node1 > node2:
        return f"{node2}-{node1}"
    return f"{node1}-{node2}"


def get_cost(node1: Node, node2: Node):
    n1 = node1.pos
    n2 = node2.pos
    return ((n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2) ** 0.5


school_image = pygame.image.load("school.png")

nodes = {
    0: Node((647, 558), [1, 13]),
    1: Node((334, 561), [0, 2]),
    2: Node((341, 601), [1, 3]),
    3: Node((281, 602), [2, 4]),
    4: Node((283, 438), [3, 5]),
    5: Node((277, 331), [4, 6, 21]),
    6: Node((455, 339), [5, 7]),
    7: Node((456, 392), [6, 8]),
    8: Node((620, 385), [7, 14]),
    9: Node((801, 389), [14, 10]),
    10: Node((935, 391), [9, 11]),
    11: Node((967, 430), [10, 12]),
    12: Node((969, 494), [11, 13]),
    13: Node((967, 555), [12, 0]),
    14: Node((727, 387), [8, 9, 15]),
    15: Node((712, 274), [14, 16]),
    16: Node((734, 191), [15, 17]),
    17: Node((603, 183), [16, 18]),
    18: Node((477, 183), [17, 19]),
    19: Node((446, 288), [18, 20]),
    20: Node((354, 299), [19, 21]),
    21: Node((316, 308), [20, 5])
}

node_map = get_node_map(nodes)
cost_map = get_cost_map(nodes)
print(node_map)
print(cost_map)

font = pygame.font.SysFont("arial", 20, True, False)

start = 1
end = 4
paths = path_search(start, end, node_map, cost_map)
print(paths)

n = 0

running = True
while running:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    display.fill((255, 255, 255))
    display.blit(school_image, (
    (DISPLAY_SIZE[0] / 2) - (school_image.get_width() / 2), (DISPLAY_SIZE[1] / 2) - (school_image.get_height() / 2)))

    for start_node in nodes.values():
        for end_node_n in start_node.connected_nodes:
            end_node = nodes[end_node_n]
            pygame.draw.line(display, (255, 255, 255), start_node.pos, end_node.pos, 12)
            pygame.draw.line(display, (0, 0, 0), start_node.pos, end_node.pos, 8)

    for node in nodes.values():
        pygame.draw.circle(display, (255, 255, 255), node.pos, 17)
        pygame.draw.circle(display, (0, 0, 0), node.pos, 14)

    for path, _ in paths:
        for i in range(1, len(path)):
            pygame.draw.circle(display, (0, 80, 0), nodes[path[i - 1]].pos, 10)
            pygame.draw.circle(display, (0, 80, 0), nodes[path[i]].pos, 10)
            pygame.draw.line(display, (0, 80, 0), nodes[path[i - 1]].pos, nodes[path[i]].pos, 10)

    path = paths[n][0]
    for i in range(1, len(path)):
        pygame.draw.circle(display, (0, 230, 0), nodes[path[i - 1]].pos, 10)
        pygame.draw.circle(display, (0, 230, 0), nodes[path[i]].pos, 10)
        pygame.draw.line(display, (0, 230, 0), nodes[path[i - 1]].pos, nodes[path[i]].pos, 10)

    for node_n, node in nodes.items():
        node_pos = node.pos
        if ((mouse_pos[0] - node_pos[0]) ** 2 + (mouse_pos[1] - node_pos[1]) ** 2) ** 0.5 <= 40:
            text_image = font.render(str(node_n), True, (255, 255, 255))
            display.blit(text_image, (
                node_pos[0] - (text_image.get_width() / 2), (node_pos[1] - (text_image.get_height() / 2))))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(f"POS: {event.pos}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                n += 1 if n < len(paths) - 1 else 0
            if event.key == pygame.K_LEFT:
                n -= 1 if 0 < n else 0
    pygame.display.update()

pygame.quit()
