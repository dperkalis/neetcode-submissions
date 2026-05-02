class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1
        val = -9999

        while (val != target):
            val = numbers[index1] + numbers[index2]
            print(index1,index2,val)
            if (val > target):
                index2 -= 1
            elif val < target:
                index1 +=1

        return [index1+1,index2+1]


