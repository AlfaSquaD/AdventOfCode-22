INPUT_FILE = "input.txt"

def checkPartialOverlap(section1:tuple, section2:tuple):
    if section2[0] > section1[0]:
        section1, section2 = section2, section1
    if section1[0] <= section2[0] or section1[0] <= section2[1]:
        return True
    
def main():
    with open(INPUT_FILE, 'r') as f:
        data = f.readlines()
    
    total = 0

    while data:
        line = data.pop().replace('\n', '')
        sections = line.split(',')
        sections = [tuple(map(int, section.split('-'))) for section in sections]
        if checkPartialOverlap(sections[0], sections[1]):
            total += 1
    print(total)

if __name__ == "__main__":
    main()
