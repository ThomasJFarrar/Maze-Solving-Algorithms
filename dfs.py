"""
This module is used in conjunction solve_mazes.py to perform a depth-first 
search algorithm to solve a given maze.
"""


def dfs_algorithm(maze: list, start: tuple[int, int],
                  end: tuple[int, int]) -> tuple[list[tuple[int, int]], int]:
    """
    This function implements the depth-first search algorithm to solve a maze.

    Args:
        maze (list): A list of lists representing the maze.
        start (tuple): A tuple representing coordinates of the starting position in the maze.
        end (tuple): A tuple representing coordinates of the ending position in the maze.

    Returns:
        list: A list representing the final path from start to end.
        int: The number of nodes visited during the search.

    """
    # Create the stack with the starting node and its path.
    stack = [(start, [start])]
    # Create an empty set to keep track of visited nodes.
    visited = set()
    # Initialize a counter to keep track of the number of nodes visited.
    node_count = 0

    # Loop while there are nodes in the stack.
    while stack:
        # Pop the top node and its path from the stack.
        node, path = stack.pop()
        # If the popped node is the ending node, return the path and the number of nodes visited.
        if node == end:
            return path, node_count

        # If the node has not been visited, mark it as visited and increment the node count.
        if node not in visited:
            visited.add(node)
            node_count += 1

            # Get the row and column of the node.
            row, col = node

            # Find the valid neighbors of the current node.
            neighbors = [(row+1, col), (row-1, col),
                         (row, col+1), (row, col-1)]

            for neighbor in neighbors:
                n_row, n_col = neighbor

                # If the neighbor is a valid move, add it to the stack.
                if maze[n_row][n_col] == "-":
                    stack.append((neighbor, path + [neighbor]))

    # If there is no path to the end node, return an empty path and the number of nodes visited.
    return [], node_count
