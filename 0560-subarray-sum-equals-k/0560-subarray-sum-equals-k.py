class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            need = prefix_sum - k

            if need in prefix_map:
                count += prefix_map[need]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum,0)+1

        return count