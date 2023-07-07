"""
This module is used in conjunction with solve_mazes.py to perform an A* 
search algorithm to solve a given maze.
"""

import heapq


def a_star_algorithm(maze: list,
                     start: tuple[int, int],
                     end: tuple[int, int]) -> tuple[list[tuple[int, int]], int]:
    """
    This function implements the A* search algorithm to solve a maze.

    Args:
        maze (list): A list of lists representing the maze.
        start (tuple[int, int]): A tuple representing coordinates of the starting 
        position in the maze.
        end (tuple[int, int]): A tuple representing coordinates of the ending position in the maze.

    Returns:
        tuple[list[tuple[int, int]], int]: A tuple containing the path through the maze as a list 
        of coordinates, and the number of nodes explored by the algorithm.
    """
    # Define a helper heuristic function to calculate the manhattan distance.
    def heuristic(node):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

    # Create a priority queue heap with a single tuple containing the heuristic value,
    #  cost, starting node, and path.
    heap = [(heuristic(start), 0, start, [start])]
    # Create an empty set to keep track of visited nodes.
    visited = set()
    # Initialize a counter to keep track of the number of nodes visited.
    node_count = 0

    # Loop while there are nodes in the heap.
    while heap:
        # Pop the node with the lowest cost so far from the heap.
        _, cost, node, path = heapq.heappop(heap)
        # If the popped node is the end node, return the path and the number of nodes visited.
        if node == end:
            return path, node_count

        # If the node has not been visited, mark it as visited and increment the node count.
        if node not in visited:
            visited.add(node)
            node_count += 1

            # Get the row and column of the node.
            row, col = node

            # Find the valid neighbors of the current node.
            neighbors = [(row-1, col), (row+1, col),
                         (row, col-1), (row, col+1)]

            for neighbor in neighbors:
                n_row, n_col = neighbor

                # If the neighbor is a valid move, add it to the heap.
                if maze[n_row][n_col] == "-":
                    heapq.heappush(heap, (cost + 1 + heuristic(neighbor),
                                          cost + 1, neighbor,
                                          path + [neighbor]))
    # If there is no path to the end node, return an empty path and the number of nodes visited.
    return [], node_count
