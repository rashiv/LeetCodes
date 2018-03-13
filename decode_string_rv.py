""": 
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Source: https://leetcode.com/problems/decode-string/#/description
"""


#DO NOT CHANGE THIS CLASS
class Solution(object):
	#YOUR CODE GOES HERE
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
	return self.decodeString_helper(s)
    
    def is_num(self, string):
        for i in range(1,10):
            if(str(i) in string):
                return True
        return False
        
    def decodeString_helper(self, src):
        j = 0
        while(self.is_num(src)):
            if(self.is_num(src[j])):
                dst = src[0:j]
                n = int(src[j])
                repeat = ''
                while(src[j] != ']'):
                    repeat += src[j+1]
                    j += 1
                dst += n*repeat + src[j+1:]
                src = dst
                j = 0
            j += 1
                   
        dst = src.replace("[", "")
        src = dst.replace("]", "")
        return src

#test case
def main():
    s = "3[a2[c]]" #"3[a]2[bc]" #"2[abc]3[cd]ef"
    sol = Solution()  
    print ("Encoded string:", s)
    out_string = sol.decodeString(s)
    print("Decoded string:", out_string)

if __name__ == "__main__":
    main()
