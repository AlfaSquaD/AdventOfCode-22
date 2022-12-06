INPUT_FILE = 'input.txt'

def isAllUnique(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return False
    return True

def main():
    with open(INPUT_FILE) as f:
        data = f.read()

    sliding_window = 4

    windows = [data[i:i+sliding_window] for i in range(len(data)-sliding_window)]

    for i in range(len(windows)):
        if isAllUnique(windows[i]):
            # print the last characters index
            print(i+sliding_window)
            break



if __name__ == '__main__':
    main()