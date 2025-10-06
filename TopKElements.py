from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach : Use a dictionary to find the frequency of the elements. 
        # And reverse sort this by values. 
        # then pick the k-elements from first.
        di = Counter(nums)
        pairs = [(value,key) for key,value in di.items()]

        #Keep the -x inside a tuple.
        pairs.sort(key = lambda x : (-x[0],-x[1]))

        res = []
        for i in range(k):
            res.append(pairs[i][1])
        return res
