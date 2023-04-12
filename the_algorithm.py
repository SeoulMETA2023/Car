""""
author: Piop2

path finging algorithm for self-driving car navigation system

TEST MAP
#####################
# 1 # 2 # 3 # 4 # 5 #
#12 ############# 6 #
#11 #10 # 9 # 8 # 7 #
#####################
"""


def path_search(
    start: int, 
    end: int, 
    map_tree: dict[int:list[int]], 
    path: list[int] = []
) -> list[list[int]]:
    if not path:
        path = [start]
    next_nodes = list(set(map_tree[path[-1]]) - set(path))
    if not next_nodes:
        return [[]]

    all_paths = []
    for node in next_nodes:
        new_path = path + [node]
        if node == end:
            all_paths.append(new_path)
            break

        for next_path in path_search(start, end, map_tree, new_path):
            if not next_path:
                continue

            all_paths.append(next_path)

    return all_paths


if __name__ == "__main__":
    test_map = {
        1: [12, 2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4, 6],
        6: [5, 7],
        7: [6, 8],
        8: [7, 9],
        9: [8, 10],
        10: [9, 11],
        11: [10, 12],
        12: [11, 1],
    }
    routes = path_search(start=9, end=4, map_tree=test_map)
    sorted_routes = sorted(routes, key=len)
    print(sorted_routes)
