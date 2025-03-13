def delete_duplicates(head: list[int]) -> list[int]:
    list_of_readed=[]
    for i in range(len(head)):
        if head[i] not in list_of_readed:
            list_of_readed.append(head[i])
    return  list_of_readed

print(delete_duplicates([1,1,2]))
print(delete_duplicates([1,1,2,3,3]))