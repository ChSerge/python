Week = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 0:'Sunday'}
print(Week)
WeekInv = dict()
for key in Week:
    WeekInv[Week[key]] = key
Week = WeekInv
print(Week)