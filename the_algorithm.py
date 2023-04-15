""""
author: Piop2

path finding algorithm for self-driving car's navigation system

TEST MAP
#####################
# 1 # 2 # 3 # 4 # 5 #
#12 ############# 6 #
#11 #10 # 9 # 8 # 7 #
#####################
"""


def path_search(
        start: int, end: int, node_map: dict[int: list[int]], cost_map: dict[str: int]
) -> list[tuple[list[int], int]]:
    """
    search all path and sort by cost.
    if start node and end node are the same, it will return a path with only the end node.

    :param start: start node number
    :param end: end(target) node number
    :param node_map: node map which value nodes are connected to key node. \
     you must write like this: {node: [node1, node2, ...]}
    :param cost_map: node-to-node distance cost. \
     you must write like this: {"n-N": cost} (n: small node number, N: big node number)
    :return: all path sorted by cost. \
     return like this: [(path1, cost1), (path2, cost2), ...]
    """
    return _cost_sort(
        _search_path(target=end, path=[start], map_nodes=node_map), cost_map=cost_map
    )


def _search_path(
        target: int, path: list[int], map_nodes: dict[int: list[int]]
) -> list[list[int]]:
    if path[0] == target:
        return [path]

    next_nodes = list(set(map_nodes[path[-1]]) - set(path))
    if not next_nodes:
        return [[]]

    all_paths = []
    for node in next_nodes:
        new_path = path + [node]
        if node == target:
            all_paths.append(new_path)
            break

        for next_path in _search_path(
                target=target, path=new_path, map_nodes=map_nodes
        ):
            if not next_path:
                continue

            all_paths.append(next_path)

    return all_paths


def _cost_sort(paths: list[list[int]], cost_map: dict[str:int]):
    def get_path_cost(path: list[int]) -> int:
        # result = 0
        # for i in range(0, len(path) - 2):
        #     result += dict[f"{path[i]}-{path[i + 1]}"]
        # return result
        return sum(
            map(
                lambda x: cost_map[_get_cost_map_key(node1=path[x], node2=path[x + 1])],
                range(0, len(path) - 2),
            )
        )

    path_cost = list(map(lambda x: (x, get_path_cost(x)), paths))

    return sorted(path_cost, key=lambda x: x[1])


def _get_cost_map_key(node1: int, node2: int) -> str:
    if node1 > node2:
        return f"{node2}-{node1}"
    return f"{node1}-{node2}"


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

    test_cost = {
        "1-2": 1,
        "2-3": 1,
        "3-4": 1,
        "4-5": 1,
        "5-6": 1,
        "6-7": 1,
        "7-8": 1,
        "8-9": 1,
        "9-10": 1,
        "10-11": 1,
        "11-12": 1,
        "1-12": 1,
    }

    routes = path_search(start=9, end=4, node_map=test_map, cost_map=test_cost)
    print(routes)
