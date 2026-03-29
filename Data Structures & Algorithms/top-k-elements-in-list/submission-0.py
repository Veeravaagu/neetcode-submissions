class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        op = [0]*k
        output = defaultdict(int)
        for i in nums:
            output[i]+=1
    #print(output)
            for j in range (k):
                if (output[i] > output[op[j]]):
                    if i not in op:
               
                #print("the number",output[op[j]],"The Value", output[i])
                            op[j]= i
                #print("The Array",op)
                            break
        return op