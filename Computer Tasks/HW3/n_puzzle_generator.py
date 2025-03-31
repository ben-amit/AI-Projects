import os
import random


def create_domain(filename="domain.pddl"):
    # if os.path.exists(filename):
    #     print(f"{filename} already exists.")
    #     return

    domain_text = """(define (domain puzzle)
  (:requirements :strips)
  (:predicates
    (at ?t ?p)
    (empty ?p)
    (adjacent ?p1 ?p2)
  )

  (:action move
    :parameters
    (?t
    ?from
    ?to)
    :precondition
    (and
      (at ?t ?from)
      (empty ?to)
      (adjacent ?from ?to)
    )
    :effect
    (and
      (not (at ?t ?from))
      (at ?t ?to)
      (not (empty ?to))
      (empty ?from)
    )
  )
)"""
    with open(filename, "w") as file:
        file.write(domain_text)
    print(f"Domain file written to {filename}")


def print_board(board, N):
    print("The randomly generated board is:")
    max_width = len(str(N**2))
    for i in range(N):
        row = board[i * N: (i + 1) * N]
        row_str = " ".join(
            f"{x:>{max_width}}" if x is not None else f"{"X":>{max_width}}" for x in row
        )
        print(row_str)


def generate_adjacent_lines(N):
    adjacent_line = ""
    for row in range(N):
        for col in range(N):
            current_index = row * N + col
            current_pos = f"p{current_index + 1}"
            # Right neighbor
            if col < N - 1:
                right_index = row * N + (col + 1)
                right_pos = f"p{right_index + 1}"
                adjacent_line += f"    (adjacent {current_pos} {right_pos})\n"
                adjacent_line += f"    (adjacent {right_pos} {current_pos})\n\n"
            # Down neighbor
            if row < N - 1:
                down_index = (row + 1) * N + col
                down_pos = f"p{down_index + 1}"
                adjacent_line += f"    (adjacent {current_pos} {down_pos})\n"
                adjacent_line += f"    (adjacent {down_pos} {current_pos})\n\n"
    return adjacent_line


def generate_at_lines(board, N):
    text = ""
    for i, tile in enumerate(board):
        if tile is not None:
            at_line = f"    (at t{tile} p{i + 1})\n"
        else:
            at_line = f"    (empty p{i + 1})\n\n"
        text += at_line
    return text


def create_problem(N, filename="problem.pddl"):
    # if os.path.exists(filename):
    #     print(f"{filename} already exists.")
    #     return

    # Starting config
    board = list(range(1, N**2))
    random.shuffle(board)
    board += [None]
    print_board(board, N)

    # Starting section
    problem_text = "(define (problem puzzle)\n"
    problem_text += f"  (:domain puzzle)\n"

    # Object section
    tile_names, position_names = "", ""
    for i in range(1, N**2 + 1):
        position_names += f"p{i} "
        if i != N**2:
            tile_names += f"t{i} "

    objects_line = "  (:objects\n    " + tile_names + " " + position_names + "\n  )\n\n"
    problem_text += objects_line

    # Init section
    init_line = "  (:init\n"
    problem_text += init_line
    problem_text += generate_at_lines(board, N)

    problem_text += generate_adjacent_lines(N)

    # Goal section
    goal_line = "  )\n\n  (:goal (and\n"
    problem_text += goal_line
    for i in range(1, N**2):
        problem_text += f"    (at t{i} p{i})\n"
    problem_text += f"    (empty p{N**2})\n  ))\n)"

    with open(filename, "w") as f:
        f.write(problem_text)
    print(f"Problem file written to {filename}")


if __name__ == "__main__":
    random.seed(42)
    try:
        N = int(input("Enter the size of the puzzle (N): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit(1)

    print(f"Generating domain.pddl and problem.pddl for a {N} by {N} puzzle...")
    create_domain()
    create_problem(N)

