class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Had no idea how to solve so saw neetcode and wrote code myself had errors so used GPT
        if len(nums1) > len(nums2):
            A, B = nums2, nums1
        else:
            A, B = nums1, nums2
        left, right = 0, len(A)
        half = (len(A) + len(B) + 1) // 2
        while left <= right:
            px = (left + right) // 2
            py = half - px
            Lx = A[px - 1] if px > 0 else float('-inf')
            Rx = A[px]     if px < len(A) else float('inf')
            Ly = B[py - 1] if py > 0 else float('-inf')
            Ry = B[py]     if py < len(B) else float('inf')
            if Lx <= Ry and Ly <= Rx:
                if (len(A) + len(B)) % 2:
                    return max(Lx, Ly)
                else:
                    return (max(Lx, Ly) + min(Rx, Ry)) / 2
            elif Lx > Ry:
                right = px - 1
            else:
                left = px + 1





        