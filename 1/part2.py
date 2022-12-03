import bisect

INPUT_FILE = 'input.txt'

def main():
    max_sum = []
    with open(INPUT_FILE, 'r') as f:
        _currentSum = 0
        while True:
            line = f.readline()
            if not line:
                break
            elif line == '\n':
                if len(max_sum) < 3 or _currentSum > max_sum[0]:
                    bisect.insort(max_sum, _currentSum)
                    max_sum = max_sum[-3:]
                _currentSum = 0
                continue
            else:
                _currentSum += int(line)

    print(sum(max_sum))

if __name__ == '__main__':
    main()

            

    