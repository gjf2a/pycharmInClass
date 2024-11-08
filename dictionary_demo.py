from typing import List, Dict, Tuple

grade_points = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0
}

def gpa_2(grades: List[str]) -> float:
    total_points = 0.0
    for grade in grades:
        total_points += grade_points[grade]
    return total_points / len(grades)

def gpa_1(grades: List[str]) -> float:
    total_points = 0.0
    for grade in grades:
        if grade == 'A':
            total_points += 4
        elif grade == 'B':
            total_points += 3
        elif grade == 'C':
            total_points += 2
        elif grade == 'D':
            total_points += 1
    return total_points / len(grades)

def gpa_3(grades: List[str], grade_point_filename: str) -> float:
    with open(grade_point_filename) as file_input:
        grade_points = {}
        for line in file_input:
            grade, point = line.split()
            grade_points[grade] = float(point)

        total_points = 0.0
        for grade in grades:
            total_points += grade_points[grade]
        return total_points / len(grades)

def set_up_battleship_grid() -> Dict[Tuple[int,int], bool]:
    ships = {}
    done = False
    while not done:
        coords = input("Enter x and y of ship location, separated by a space\nenter 'quit' to end: ")
        if coords == 'quit':
            done = True
        else:
            x, y = coords.split()
            x = int(x)
            y = int(y)
            ships[(x, y)] = True
    return ships


def get_grid_dimensions(grid: Dict[Tuple[int,int], bool]) -> Tuple[int, int, int, int]:
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for (x, y) in grid:
        if min_x is None or x < min_x:
            min_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_x is None or x > max_x:
            max_x = x
        if max_y is None or y > max_y:
            max_y = y
    return (min_x, min_y, max_x, max_y)


def print_grid(grid: Dict[Tuple[int,int], bool]):
    min_x, min_y, max_x, max_y = get_grid_dimensions(grid)
    for row in range(min_y, max_y + 1):
        row_str = ""
        for col in range(min_x, max_x + 1):
            if (col, row) in grid:
                row_str += 'S'
            else:
                row_str += '.'
        print(row_str)
