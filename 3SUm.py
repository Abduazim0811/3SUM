class Solution(object):
    def threeSum(self, nums):
        lst=[]; nums.sort()
        print(nums)
        for i,v in enumerate(nums):
            if i and v==nums[i-1]:
                continue
            left=i+1; 
            right=len(nums)-1
            print(left)
            while left<right:
                son=v+nums[left]+nums[right]
                if son<0:
                    left+=1
                elif son>0:
                    right-=1
                else:
                    lst.append([v, nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return lst
print(Solution().threeSum(nums=[1,-1,-1,0]))