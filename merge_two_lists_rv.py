"""
Merge two sorted lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
Source: https://leetcode.com/problems/merge-two-sorted-lists/#/description
"""


def merge_two_list_helper(list1, list2):
    #NOTE: YOU CAN NOT USE ANY SORTING LIBRARIES
    #YOUR CODE GOES HERE

    l1 = 0; l2 = 0; total = len(list1) + len(list2)
    while(l1 + l2 < total):
        if(list2[l2] < list1[l1]):
            list1.insert(l1, list2[l2])
            l1 += 1; l2 += 1
        else:
            l1 += 1
    list1.extend(list2[l2:len(list2)])
    return list1


#DO NOT CHANGE THIS FUNCTION
def merge_two_list(list1,list2):
	return merge_two_list_helper(list1, list2)


#test cases
def main():
    list1 = [1,3,5]
    list2 = [2,4,6]
    print ("merging [1,3,5] and [2,4,6]......")
    print ("expected result is [1,2,3,4,5,6]")
    print ("your output is {}".format(merge_two_list(list1, list2)))

if __name__ == "__main__":
    main()
