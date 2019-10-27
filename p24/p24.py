def dominoPosition(initialCondition):
    finalCondition = []
    index = 0
    stringLength = len(initialCondition)
    while index < stringLength:
        character = initialCondition[index]
        if  character == '.':
            finalCondition.append('.')
            index += 1
        elif character == 'R':
            index = rightLeaning(index, stringLength, initialCondition, finalCondition)
        elif character == 'L':
            leftLeaning(index, finalCondition)
            index += 1

    return ''.join(finalCondition)

def rightLeaning(index, initialSequenceLength, initialSequence, finalSequence):
    i = index + 1
    indexOfLeft = index
    while i < initialSequenceLength:
        if initialSequence[i] == '.':
            i += 1
        elif initialSequence[i] == 'R':
            break
        elif initialSequence[i] == 'L':
            indexOfLeft = i
            mod = (indexOfLeft - index) % 2
            i = ((indexOfLeft - index) // 2) + index + mod
            break
    for j in range(index, i):
        finalSequence.append('R')
    if indexOfLeft != index:
        if mod == 0:
            finalSequence.append('.')
        for j in range(index, i):
            finalSequence.append('L')
        i = indexOfLeft + 1
    return i

def leftLeaning(index, finalSequence):
    finalSequence.append('L')
    i = index - 1
    while i >= 0:
        if finalSequence[i] == 'L':
            break
        finalSequence[i] = 'L'
        i -= 1

if __name__ == '__main__':
    initialCondition = ".L.R...LR..L.."
    print(dominoPosition(initialCondition))
