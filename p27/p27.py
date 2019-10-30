def numberOfWitnesses(lst):
    tallestPerson = 0
    totalWitnesses = 0
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] > tallestPerson:
            totalWitnesses += 1
            tallestPerson = lst[i]
    return totalWitnesses

if __name__ == '__main__':
    listOfPeople = [ 7, 8, 3, 2, 5, 3, 3, 3, 3, 1]
    print(numberOfWitnesses(listOfPeople))
