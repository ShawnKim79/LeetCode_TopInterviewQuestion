class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman_split = s

        if "CM" in s :
            temp_split = roman_split.split("CM")
            total += self.addRoman(temp_split[0])
            total += 900
            roman_split = temp_split[1]

        if "CD" in roman_split :
            temp_split = roman_split.split("CD")
            total += self.addRoman(temp_split[0])
            total += 400
            roman_split = temp_split[1]
        
        if "XC" in roman_split :
            temp_split = roman_split.split("XC")
            total += self.addRoman(temp_split[0])
            total += 90
            roman_split = temp_split[1]
        
        if "XL" in roman_split :
            temp_split = roman_split.split("XL")
            total += self.addRoman(temp_split[0])
            total += 40
            roman_split = temp_split[1]

        if "IX" in roman_split :
            temp_split = roman_split.split("IX")
            total += self.addRoman(temp_split[0])
            total += 9
            roman_split = temp_split[1]
        
        if "IV" in roman_split :
            temp_split = roman_split.split("IV")
            total += self.addRoman(temp_split[0])
            total += 4
            roman_split = temp_split[1]
        
        total += self.addRoman(roman_split)

        return total
            
    
    def addRoman(self, tokens:str) -> int:
        roman = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000,     
        }
        token_sum = 0

        for token in tokens:
            token_sum += roman[token]
        return token_sum
        



def main():
    objSolution = Solution()

    print(objSolution.romanToInt("MCMXCIV"))


if __name__  == "__main__":
    main()