import requests

url = "https://adventofcode.com/2024/day/4/input"

headers = {
    "Cookie": ""
}
response = requests.get(url, headers=headers)
lines = response.text.splitlines()

WORD = "XMAS"

DIRECTIONS = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1), # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1),   # down-right
]

def in_bounds(row, col):
    return 0 <= row < len(lines) and 0 <= col < len(lines[row])

def check_direction(row, col, d_row, d_col):
    for idx, ch in enumerate(WORD):
        r = row + d_row * idx
        c = col + d_col * idx
        if not in_bounds(r, c) or lines[r][c] != ch:
            return False
    return True

def check_adjacent(row, col):
    if lines[row][col] != WORD[0]:
        return 0
    count = 0
    for d_row, d_col in DIRECTIONS:
        if check_direction(row, col, d_row, d_col):
            count += 1
    return count

def count_xmas():
    total = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == WORD[0]:
                total += check_adjacent(row, col)
    return total

print(count_xmas())