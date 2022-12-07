INPUT_FILE = "input.txt"

DEVICE_SIZE = 70000000

UPDATE_SIZE = 30000000

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory():
    def __init__(self, path):
        self.path = path
        self.totalSize = 0
        self.subDirectories = {}
        self.files = []
        self.upperDirectory : Directory = None
    
    def addSubDirectory(self, directory):
        if directory.path in self.subDirectories:
            raise Exception("Directory already exists")
        self.subDirectories[directory.path] = directory
        directory.upperDirectory = self
    
    def addFile(self, file: File):
        self.files.append(file)
    
    def calculateTotalSize(self):
        self.totalSize = sum(file.size for file in self.files)
        for directory in self.subDirectories.values():
            self.totalSize += directory.calculateTotalSize()
        return self.totalSize
    
    def getDirectory(self, directoryName):
        if directoryName == '.':
            return self
        if directoryName == '/':
            directory = self
            while directory.upperDirectory:
                directory = directory.upperDirectory
            return directory
        if directoryName == '..':
            return self.upperDirectory
        if directoryName in self.subDirectories:
            return self.subDirectories[directoryName]
        raise Exception("Directory not found")
    

class DirectoryCrawler():

    def __init__(self, input:list):
        self.input = input
        self.rootDirectory = Directory('/')
        self.currentDirectory : Directory = self.rootDirectory

    def _changeDirectory(self, directory_name):
        self.currentDirectory = self.currentDirectory.getDirectory(directory_name)

    def _list(self, content): 
        if content.startswith('dir'):
            self.currentDirectory.\
                addSubDirectory(Directory(''.join(content.split(" ")[1:])))
        else :
            self.currentDirectory.\
                addFile(File(''.join(content.split(" ")[1:]), int(content.split(" ")[0])))
    
    def crawl(self):
        while self.input:
            line = self.input.pop(0).strip()
            if line.startswith('$'):
                if 'cd' in line:
                    self._changeDirectory(line.split(" ")[2])
                elif 'ls' in line:
                    while self.input and not self.input[0].startswith('$'):
                        self._list(self.input.pop(0).strip())
    
    def calculateTotalSize(self):
        return self.rootDirectory.calculateTotalSize()


def solution(root: Directory, neededSpace: int, currentMinSize: int = 0):
    directories = root.subDirectories.values()

    for directory in directories:
        if directory.totalSize > neededSpace and directory.totalSize < currentMinSize:
            currentMinSize = directory.totalSize
        currentMinSize = solution(directory, neededSpace, currentMinSize)
           
    return currentMinSize

def main():
    with open(INPUT_FILE) as f:
        input = f.readlines()
    crawler = DirectoryCrawler(input)
    crawler.crawl()
    crawler.calculateTotalSize()

    unusedSpace = DEVICE_SIZE - crawler.calculateTotalSize()

    neededSpace = UPDATE_SIZE - unusedSpace

    print(solution(crawler.rootDirectory, neededSpace, DEVICE_SIZE))

if __name__ == "__main__":
    main()
    
    

    
    
    

