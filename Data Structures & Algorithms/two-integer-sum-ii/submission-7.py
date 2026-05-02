class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1
        val = -9999

        while (index1 < index2):
            val = numbers[index1] + numbers[index2]
            if (val > target):
                index2 -= 1
            elif val < target:
                index1 +=1
            else:
                return [index1+1,index2+1]

        return []


