import os


class Iterator:
    def __init__(self, type_name: str, dir_name: str):
        self.type_name = type_name
        self.count = 0
        self.dir_name = dir_name
        self.data = os.listdir(os.path.join(dir_name, type_name))
        self.limit = len(self.data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.limit:
            path = os.path.join("dataset", self.type_name, self.data[self.count])
            self.count += 1
            return path
        else:
            raise StopIteration
        

def main() -> None:

    type1 = 'polar_bear'

    name : Iterator = Iterator(type1, 'dataset')

    for i in range(6):
        print(next(name))


if __name__ == "__main__":
    main()