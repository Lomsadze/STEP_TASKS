def fibonacci_of(range_max):
    if range_max in {0, 1}:
        return range_max

    return fibonacci_of(range_max - 1) + fibonacci_of(range_max - 2)


class Fibonacci:
    def __init__(self, range_min, range_max):
        self.lst = None
        self.range_min = range_min
        self.range_max = range_max

    def get_list(self):
        self.lst = [fibonacci_of(n) for n in range(self.range_max)]

        return self.lst

    def create_file(self):
        lst = self.lst
        numbers = []

        for number in lst:
            numbers.append(str(number) + ", ")

        with open("fibonacci.txt", "w+") as file:
            file.writelines(numbers)

        return lst


result = Fibonacci(1, 15)

fibonacci_list = result.get_list()
create_file = result.create_file()
