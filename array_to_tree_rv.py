"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#DO NOT CHANGE THIS CLASS
class Solution(object):
    def sortedArrayToBST(self, nums):
    	#YOUR CODE GOES HERE
    	##
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
	if(len(nums) == 0): # check if empty array
            return None
        if(len(nums) == 1):
            return TreeNode(nums[0])
        centre = len(nums)//2
        root = TreeNode(nums[centre]) # // returns floor of integer division
        
        print(nums[centre]) # printing out where splits happen and remaining array as a sanity check
        print(nums)
        
        root.left = self.sortedArrayToBST(nums[:centre])
        root.right = self.sortedArrayToBST(nums[centre+1:])
        return root
