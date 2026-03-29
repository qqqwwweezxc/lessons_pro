class StringProcessor:
    """Class with methods for working with strings"""

    @staticmethod
    def reverse_string(s: str) -> str:
        """Return the reversed string"""
        return s[::-1]
    
    @staticmethod
    def capitalize_string(s: str) -> str:
        """Capitalize the first letter of the string"""
        if not s:
            return s
        return s[0].upper() + s[1:]

    @staticmethod
    def count_vowels(s: str) -> int:
        """Count the number of vowels in the string"""
        vowels = "aeiouAEIOU" + "аеёиоуыэюяАЕЁИОУЫЭЮЯ" + "аеєиіїоуюяАЕЄИІЇОУЮЯ"
        return sum(1 for char in s if char in vowels)
    
