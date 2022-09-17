if __name__ == '__main__':
    listA = []
    listB = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        listA.append([name, score])
        listB.append(score)

    secondLast = sorted(set(listB))[1]

    for i, j in sorted(listA):
        if j == secondLast:
            print(i)
