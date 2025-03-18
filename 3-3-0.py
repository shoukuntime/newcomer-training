def delete_duplicates(head: list[int]) -> list[int]:
    def f(head: list[int], list_of_readed=None) -> list[int]:
        if list_of_readed is None:
            list_of_readed = []
        if not head:
            return list_of_readed
        if head[0] not in list_of_readed:
            list_of_readed.append(head[0])
        return f(head[1:], list_of_readed)
    return f(head)

print(delete_duplicates([1,1,2]))
print(delete_duplicates([1,1,2,3,3]))