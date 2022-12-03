INPUT_FILE = "input.txt"

PRIORITY = {}

for i in range(26):
    PRIORITY[chr(ord('a') + i)] = i + 1
    PRIORITY[chr(ord('A') + i)] = i + 27

def main():
    with open(INPUT_FILE) as f:
        data = f.readlines()
    
    total = 0

    while data:
        sharedItems = set()
        lines = [data.pop().replace('\n', '') for _ in range(3)]
        sharedItems = set(lines[0]) & set(lines[1]) & set(lines[2])

        for item in sharedItems:
            total += PRIORITY[item]
    
    print(total)

if __name__ == "__main__":
    main()
            