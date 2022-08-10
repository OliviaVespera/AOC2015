LEVEL_MAP = {"(":1, ")": -1}

def read_file(file_name) -> str:
    with open(file_name) as f:
        instruction = f.read()
    return instruction

def parse_instruction(instr) -> tuple[int, int]:
    level = 0
    basement = 0
    for i, j in enumerate(instr, start=1):
        level += LEVEL_MAP[j]
        if level < 0 and basement == 0:
            basement = i
    return level, basement

def main() -> None:
    instruction = read_file("d1_input.txt")
    level, basement = parse_instruction(instruction)
    print(level, basement)

if __name__ == "__main__":
    main()
