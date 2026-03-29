class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        array = []
        array = list(hashmap.items())
        array.sort()
        res = []
        for i in range(k):
            num = array.pop()
            res.append(num[0])
        return res
