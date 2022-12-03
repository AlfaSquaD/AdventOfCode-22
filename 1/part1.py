INPUT_FILE = 'input.txt'

def main():
    max_sum = 0
    with open(INPUT_FILE, 'r') as f:
        _currentSum = 0
        while True:
            line = f.readline()
            if not line:
                break
            elif line == '\n':
                if _currentSum > max_sum:
                    max_sum = _currentSum
                _currentSum = 0
                continue
            else:
                _currentSum += int(line)

    print(max_sum)

if __name__ == '__main__':
    main()

            

    