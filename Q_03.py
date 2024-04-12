
# 20099_Maniruzzaman_Md_lab3
# Week_03/lab_03/Q_03
# Question: program for merges two sorted lists of numbers into a new sorted list ...


def merge_sorted(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append the remaining elements from both lists
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

def main():
    print("=== Merge Sorted Lists Program ===")


    list1 = []
# number of elements as input
    x = int(input("Enter number elements for List-1: "))
# iterating till the range
    for p in range(0, x):
        ele = int(input())
    # adding the element
        list1.append(ele)  
    l1 = list1 
    print("\nInput element of List-1\t\t:", l1)
# sorting list using nested loops
    for p in range(0, len(l1)):
        for q in range(p+1, len(l1)):
            if l1[p] >= l1[q]:
                l1[p], l1[q] = l1[q],l1[p]
# sorted list
    print("Sorted element of List-1\t:", l1)


    list2 = []
# number of elements as input
    n = int(input("\nEnter number elements for list-2: ")) 
# iterating till the range
    for k in range(0, n):
        ele = int(input())
    # adding the element
        list2.append(ele)
    l2 = list2 
    print("Input element of List-2\t\t:", l2) 
# sorting list using nested loops
    for k in range(0, len(l2)):
        for f in range(k+1, len(l2)):
            if l2[k] >= l2[f]:
                l2[k], l2[f] = l2[f],l2[k] 
# sorted list
    print("Sorted element of List-2\t:", l2)


    result = merge_sorted(list1, list2)

    print(f"\nList-1\t: {list1}")
    print(f"List-2\t: {list2}")
    print(f"\nResult\t: {result}")

if __name__ == "__main__":
    main()
