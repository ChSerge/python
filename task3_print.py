List = [1, 10, 9, 8, 7, 5, 10, 35, 32, 9]
print(List)
List.sort()
print(List)
CurElement = None
NewList = []
print(NewList)
for i in range(len(List)):
    if List[i] != CurElement:
        NewList.append(List[i])
    CurElement = List[i]
print(NewList)