class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nu = len(digits)
        m = ""
        for i in range(0, nu):
            print(i)
            if digits[-1-i] < 9:
                digits[-1-i] = digits[-1-i] + 1
                break
            else:
                digits[-1-i] = 0
                if i == nu-1:
                    digits = [1] + digits
                    break

        return digits