INPUT_FILE = "input.txt"

def checkFullOverlap(section1:tuple, section2:tuple):
    if section1[0] >= section2[0] and section1[1] <= section2[1]:
        return True
    elif section1[0] <= section2[0] and section1[1] >= section2[1]:
        return True
    return False



def main():
    with open(INPUT_FILE, 'r') as f:
        data = f.readlines()
    
    total = 0

    while data:
        line = data.pop().replace('\n', '')
        sections = line.split(',')
        sections = [tuple(map(int, section.split('-'))) for section in sections]
        if checkFullOverlap(sections[0], sections[1]):
            total += 1
    print(total)

if __name__ == "__main__":
    main()
