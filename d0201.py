from functools import reduce
from itertools import combinations
from operator import mul

def read_file(file_name: str) -> list[int]:
    instruction = []
    with open(file_name) as f:
        for line in f:
            instruction.extend(map(int, line.split("x")))
    return instruction

def parse_instruction(instr: list[int]) -> tuple[list[int], list[int]]:
    surface_areas = []
    ribbon_lengths = []
    for i in range(0, len(instr), 3):
        surface_areas.append(calculate_surface_area(instr[i:i+3]))
        ribbon_lengths.append(calculate_ribbon(instr[i:i+3]))
    return surface_areas, ribbon_lengths

def calculate_surface_area(dimensions) -> int:
    combos = combinations(dimensions, 2)
    surface_areas = [combo[0] * combo[1] * 2 for combo in combos]
    return sum(surface_areas, min(surface_areas)//2)

def calculate_ribbon(dimensions) -> int:
    return sum(sorted(dimensions)[0:2])*2 + reduce(mul, dimensions, 1)

def main() -> None:
    instruction = read_file("d2_input.txt")
    # print(instruction)
    # print(list(combinations([1,2,3], 2)))
    results = parse_instruction(instruction)
    print(sum(results[0]), sum(results[1]))

if __name__ == "__main__":
    main()
