"""
This module is used to solve mazes using DFS and A* algorithms and
produce statistics about their performance.
"""
import sys
from os.path import isfile
from time import process_time
from astar import a_star_algorithm
from dfs import dfs_algorithm
from bfs import bfs_algorithm


def read_file(file_name: str) -> list[str]:
    """
    Reads the contents of the maze text file.

    Args:
        file_name (str): The name of the maze file to be read.

    Returns:
        list[str]: A list containing the lines of the maze file.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        maze_lines = file.readlines()
        file.close()
    return maze_lines


def convert_to_list(maze_lines: list[str]) -> list[list[str]]:
    """
    Converts the maze into a 2D list representation.

    Args:
        maze_lines (list[str]): A list containing the lines of the maze file.

    Returns:
        list[list[str]]: A 2D list representation of the maze.
    """
    maze = []
    for line in maze_lines:
        row = []
        # Remove whitespace from the maze.
        for char in line.replace(" ", "").strip():
            if char in ("#", "-"):
                row.append(char)
            else:
                print("Maze contains invalid characters")
                main()
        # Check that the row isn't empty.
        if row:
            maze.append(row)
    return maze


def solve_maze(maze: list[list[str]], algorithm: str) -> tuple[list[tuple[int, int]], int, float]:
    """
    Calls and times the algorithm to execute.

    Args:
        maze (list[list[str]]): A 2D list representation of the maze.
        algorithm (str): The name of the algorithm to be used to solve the maze.

    Returns:
        tuple[list[tuple[int, int]], int, float]: A tuple containing the path through the maze
        as a list of coordinates,
        the number of nodes explored by the algorithm, and the time taken to execute the algorithm.
    """
    # Get the start and end coordinates of the maze.
    start = (0, maze[0].index("-"))
    end = (len(maze)-1, maze[-1].index("-"))
    # Get the number of rows and columns in the maze.
    if algorithm == "dfs":
        # Get the time the algorithm starts.
        start_time = process_time()
        # Call the DFS algorithm.
        path, nodes_explored = dfs_algorithm(maze, start, end)
        # Get the time the algorithm ends.
        end_time = process_time()
    elif algorithm == "astar":
        # Get the time the algorithm starts.
        start_time = process_time()
        # Call the A* algorithm.
        path, nodes_explored = a_star_algorithm(maze, start, end)
        # Get the time the algorithm ends.
        end_time = process_time()
    elif algorithm == "bfs":
        # Get the time the algorithm starts.
        start_time = process_time()
        # Call the BFS algorithm.
        path, nodes_explored = bfs_algorithm(maze, start, end)
        # Get the time the algorithm ends.
        end_time = process_time()
    return path, nodes_explored, end_time - start_time


def write_path_to_file(solution_file: str,
                       maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    """
    Write the maze with the solution path indicated by '@' characters to the given output file.

    Args:
        solution_file (str): The output file path to write to.
        maze (list[list[str]]): A 2D list representation of the maze.
        path (list[tuple[int, int]]): The path through the maze as a list of coordinates.
    """
    with open(solution_file, "w", encoding="utf-8") as file:
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                if (i, j) in path:
                    file.write('@ ')
                else:
                    file.write(cell + ' ')
            file.write('\n')


def main() -> None:
    """
    The main function prompts the user to enter the name of the maze file to solve and
    checks that the file exists. It then prompts the user to choose an algorithm to solve
    the maze and checks that the user entered a valid option. Next, it calls solve_maze
    with the selected algorithm and the maze, and prints statistics about the performance of
    the algorithm, including the path found, the number of nodes explored, and the execution time.
    Finally, it writes the maze to a file, with the solution path included in it.
    """
    # Ask the user for the file name of the maze to solve.
    while True:
        file_name = input("Enter the text file name of the maze to solve: ")
        if isfile(file_name):
            maze_lines = read_file(file_name)
            maze = convert_to_list(maze_lines)
            break
        print("File does not exist")

    # Ask the user which algorithm to run.
    algorithm = None
    while algorithm is None:
        choice = input("Which algorithm would you like to run? 1. DFS or 2. A* or 3. BFS: ")
        if choice in ("1", "DFS", "dfs"):
            algorithm = "dfs"
            path, nodes_explored, duration = solve_maze(maze, algorithm)
        elif choice in ("2", "A*", "a*"):
            algorithm = "astar"
            path, nodes_explored, duration = solve_maze(maze, algorithm)
        elif choice in ("3", "BFS", "bfs"):
            algorithm = "bfs"
            path, nodes_explored, duration = solve_maze(maze, algorithm)
        else:
            print("Invalid option")

    # Get the solution file name and ouput the solution.
    solution_file = "solutions/solution-" + algorithm + "-" + file_name
    # Ask the user whether to output the solution.
    while True:
        choice = input("Would you like to rewrite the maze solution to an output file?\n"
               " (May take longer for larger mazes) Y/N : ")
        if choice in ("Y", "y", "yes", "Yes"):
            write_path_to_file(solution_file, maze, path)
            break
        if choice in ("N", "n", "no", "No"):
            break
        print("Invalid option")

    # Print statistics about the algorithm solving the maze.
    print("====== Stats ======")
    print("Path:           " + "see " + solution_file)
    print("Nodes in Path:  " + str(len(path)))
    print("Nodes explored: " + str(nodes_explored))
    print("Execution time: " + str(duration) + " seconds")
    print("===================")
    input()
    sys.exit()


# Call the main function.
main()
