"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        for char in s:
            s_chars[char] = 1 + s_chars.get(char, 0)
        
        for char in t:
            if char not in s_chars:
                return False
            else:
                s_chars[char] -= 1
        
        return min(s_chars.values())==max(s_chars.values())==0