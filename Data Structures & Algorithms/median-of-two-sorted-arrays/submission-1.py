class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute Force :
        # 1. Use Two pointers or loops for nums1 and nums2 Iterate and form and m+n array.
        # 2. Then Find the median in the sorted array.
        #Optimal:
        # 1. since time is O(log(m+n)) i can't iterate throughout the array, I need to use bi nary search simultaneously on both arrays to find the median.
        # 2 Since ascending order I need to find the range. so compare nums1[0] and nums2[0] as well as nums1[-1] and nums2[-1] to find the range.
        # 3. Then maybe compare the mids of the both the arrays?
        # 4. Since we want median we find the element which forms the median so, in an array of length 3 it is index-1 and for 4 it is index 1 and 2.
        # 5. Like that we can compare the mids and see which 
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity") 
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1  
        
        