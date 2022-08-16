from operator import add

vec_map = {"<":(-1,0), "^":(0,1), ">":(1,0), "v":(0,-1)}

def read_file(file_name: str) -> str:
    with open(file_name) as f:
        return f.readline()

def question_1(instr: str) -> set[tuple[int, int]]:
    locations = [(0,0)]
    for i in instr:
        vec = vec_map[i]
        locations.append(tuple(map(add,locations[-1], vec)))
    return set(locations)

def question_2(instr: str) -> tuple[int, int]:
    locations_1 = [(0,0)]
    locations_2 = locations_1.copy()
    for i in range(0, len(instr), 2):
        vec = vec_map[instr[i]]
        vec2 = vec_map[instr[i+1]]
        locations_1.append(tuple(map(add,locations_1[-1], vec)))
        locations_2.append(tuple(map(add,locations_2[-1], vec2)))
    return set(locations_1), set(locations_2)


def main() -> None:
    instruction = read_file("d3_input.txt")
    results_1: set = question_1(instruction)
    results_2: list[set] = question_2(instruction)
    print(len(results_1))
    print(len(results_2[0].union(results_2[1])))

if __name__ == "__main__":
    main()
