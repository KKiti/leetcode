# Given a roman numeral, convert it to an int

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_base = {"I":1, "V":5, "X":10, "L":50, "C":100,  "D":500, "M":1000}
        roman_modifiers = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

        sum = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in roman_modifiers:
                sum += roman_modifiers[s[i:i+2]]
                i+=2
            else:
                sum += roman_base[s[i]]
                i+=1
        return sum
