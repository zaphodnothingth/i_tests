class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        outs = []
        if len(nums) > 0:
            star = nums[0]
            curr = star
            leng = 1
            for i, num in enumerate(nums):
                if i == 0:
                    continue
                if num - 1 == curr:
                    leng += 1
                else:
                    if leng == 1:
                        outs.append(str(star))
                    else:
                        outs.append('{}->{}'.format(star,nums[i-1]))
                    star = num
                    leng = 1
                curr = num

            if leng == 1:
                outs.append(str(num))
            else:
                outs.append('{}->{}'.format(star,nums[-1]))
        return outs
        