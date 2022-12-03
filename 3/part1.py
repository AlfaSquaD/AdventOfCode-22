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
        line = data.pop()
        # Split the line to half
        line1 = line[:len(line)//2]
        line2 = line[len(line)//2:]

        sharedItems = set(line1) & set(line2)

        for item in sharedItems:
            total += PRIORITY[item]
    
    print(total)

if __name__ == "__main__":
    main()
            