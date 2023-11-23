li=[[1],[2],[3],[4],[5],[1],[2],[3]]
new_list=[]
for i in li:
    if i not in new_list:
        new_list.append(i)
print(new_list)