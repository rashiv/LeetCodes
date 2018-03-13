"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Source: https://leetcode.com/problems/permutations/#/description
"""
#DO NOT CHANGE THIS CLASS
class Solution(object):
	#YOUR CODE GOES HERE
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]] 
        """
        d = []; o = []
        self.permute_helper(nums, d, o)
        return o
        
    def permute_helper(self, src, dst, out):
        if(len(src) == 0):
            out.append(dst)
        for j in range(len(src)):
            tmp_src = src.copy()
            tmp_dst = dst.copy()
            tmp_dst.append(tmp_src.pop(j))
            self.permute_helper(tmp_src, tmp_dst, out)
#test case
def main():
    nums = [1,2,3,4]
    sol = Solution()  
    print ("Input list:", nums)
    out_list = sol.permute(nums)
    print("Output list of permutations:\n", out_list)

    out_list_tuples = [tuple(elem) for elem in out_list]
    # convert 2D list to list of tuples so that it can be converted to a set
    # tuples are fixed length lists
    
    print("If distinct:", len(out_list) == len(set(out_list_tuples)))

if __name__ == "__main__":
    main()
