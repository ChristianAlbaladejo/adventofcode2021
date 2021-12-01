f = open("input.txt", "r")
data = list(map(int, f.readlines()))


def part_1():
    total = 0
    for idx, x in enumerate(data):
        if idx == 0:
            print("(N/A - no previous measurement)")
        elif data[idx - 1] < x:
            print("(increased)")
            total += 1
        else:
            print("(decreased)")

    print("--------")
    print("Total: " + str(total))
    print("--------")
    f.close()


def part_2():
    lastSum = 0
    total = 0
    for idx, x in enumerate(data):
        if idx == 0:
            print("(N/A - no previous measurement)")
        else:
            try:
                number = data[idx] + data[idx + 1] + data[idx + 2]
                if (lastSum > number):
                    print(str(idx) + ": " + str(data[idx]) + "+" + str(data[idx + 1]) + "+" + str(
                        data[idx + 2]) + " = " + str(number) + "(decreased)")
                elif (lastSum < number):
                    total += 1
                    print(str(idx) + ": " + str(data[idx]) + "+" + str(data[idx + 1]) + "+" + str(
                        data[idx + 2]) + " = " + str(number) + "(increased)")
                else:
                    print(str(idx) + ": " + str(data[idx]) + "+" + str(data[idx + 1]) + "+" + str(
                        data[idx + 2]) + " = " + str(number) + " - " + str(lastSum) + "(no change)")
                lastSum = number
            except:
                print("out")
    print("--------")
    print("Total: " + str(total))
    print("--------")
    f.close()


if __name__ == "__main__":
    # part_1()
    part_2()
