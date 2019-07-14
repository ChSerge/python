List = [1, 10, 9, 8, 7, 5, 10, 35, 32, 9]
List.sort()
CurElement = None
NewList = []
for i in range(len(List)):
    if List[i] != CurElement:
        NewList.append(List[i])
    CurElement = List[i]