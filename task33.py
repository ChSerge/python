List = [1, 10, 9, 8, 7, 5, 10, 35, "22", 32, 9]
CurElement = None
NewList = []
for i in range(len(List)):
    if List[i] not in NewList:
        NewList.append(List[i])
    #CurElement = List[i]