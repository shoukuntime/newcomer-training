def delete_duplicates(head: list[int]) -> list[int]:
    result = [head[i] for i in range(len(head)) if head[0:i].count(head[i]) == 0]
    return  result

print(delete_duplicates([1,1,2]))
print(delete_duplicates([1,1,2,3,3]))