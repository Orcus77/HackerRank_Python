if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = list(set(arr))
    arr2.sort()
    print(arr2[-2])
"""
set(arr): This converts the list arr into a set, which is an unordered collection of unique elements. 
By doing this, any duplicate elements in arr are automatically removed since sets only allow unique values.

list(set(arr)): The set obtained in the previous step is then converted back into a list. 
This operation effectively removes duplicates from the original list. 
Since sets do not preserve the original order of elements, converting it back to a list ensures that the order is maintained.
"""
