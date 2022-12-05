INPUT_FILE = "input.txt"

import re

DECIMAL_REGEX = re.compile(r"\b\d+\b")


def readStacks(stack_text: list):
    stacks = {}
    for stack in stack_text[:-1]:
        stack = stack.replace('\n', '')
        currentStack = 1
        for i in range(1, len(stack), 4):
            if stack[i] != ' ':
                if currentStack not in stacks:
                    stacks[currentStack] = []
                stacks[currentStack].insert(0, stack[i])
            currentStack += 1
    return stacks


def readInstructions(instruction_text: list):
    instructions = []
    for instruction in instruction_text:
        instruction = instruction.replace('\n', '')
        numbers = DECIMAL_REGEX.findall(instruction)
        if len(numbers) == 3:
            instructions.append(DECIMAL_REGEX.findall(instruction))
        else:
            print("Invalid instruction: {}".format(instruction))
    return instructions


def executeInstructions(count:int, fromStack: int, toStack: int, stacks: dict):
    carry = stacks[fromStack][-count:]
    stacks[fromStack] = stacks[fromStack][:-count]
    stacks[toStack] += carry[::-1]

def main():
    with open(INPUT_FILE, 'r') as f:
        data = f.read()
    sections = data.split('\n\n')
    stacks = readStacks(sections[0].split('\n'))
    instructions = readInstructions(sections[1].split('\n'))
    for instruction in instructions:
        instruction = list(map(int, instruction))
        executeInstructions(instruction[0], instruction[1], instruction[2], stacks)
    keys = list(stacks.keys())
    keys.sort()
    print(''.join([stacks[key][-1] for key in keys]))


if __name__ == "__main__":
    main()