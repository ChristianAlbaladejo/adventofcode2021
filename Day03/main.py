f = open("input.txt", "r")


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


def column(matrix, i):
    return [row[i] for row in matrix]


def part_1():
    matrix = []
    gama = ""
    epsilom = ""
    for x in f:
        matrix.append(list(map(int, list(x)[:-1])))

    for i in range(len(matrix[0])):
        num = most_frequent(column(matrix, i))
        gama += str(num)

        if num == 0:
            epsilom += "1"
        else:
            epsilom += "0"

    print(gama, int(gama, 2))
    print(epsilom, int(epsilom, 2))
    print(int(gama, 2) * int(epsilom, 2))

def filter_nums(nums, rating):
    pos = 0
    while len(nums) > 1:
        ones, zero = [], []
        for num in nums:
            if num[pos] == '1':
                ones.append(num)
            else:
                zero.append(num)
        pos += 1
        by_size = sorted((zero, ones), key=len)
        nums = by_size[1] if rating == 'O2' else by_size[0]
    return int(nums[0], 2)


def part_2():
    nums = f.read().splitlines() # list with all numbers
    return print(filter_nums(nums, 'O2') * filter_nums(nums, 'CO2'))



if __name__ == "__main__":
    #part_1()
    part_2()
