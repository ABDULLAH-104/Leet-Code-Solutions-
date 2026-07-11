class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # size of the combined left half
        
        lo, hi = 0, m
        
        while lo <= hi:
            cut1 = (lo + hi) // 2       # how many elements of nums1 go to the left half
            cut2 = total_left - cut1    # how many elements of nums2 go to the left half
            
            # Values just around the cut points
            left1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            right1 = nums1[cut1] if cut1 < m else float('inf')
            left2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            right2 = nums2[cut2] if cut2 < n else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                # Correct partition found
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return float(max(left1, left2))
            elif left1 > right2:
                # nums1's left part too big, move cut1 left
                hi = cut1 - 1
            else:
                # nums1's left part too small, move cut1 right
                lo = cut1 + 1
        
        return 0.0  # unreachable if input is valid