class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_counts={}
        for num in nums:
            if num not in num_counts:
                num_counts[num]=0
            num_counts[num]+=1
        for num in num_counts:
            if num_counts[num]==1:
                single_num=num
                break
        return single_num
