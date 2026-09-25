class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = 0
        b = 0
        final = []

        while a < m and b < n:
            if nums1[a] <= nums2[b]:
                final.append(nums1[a])
                a += 1
            else:
                final.append(nums2[b])
                b += 1

        while a < m:
            final.append(nums1[a])
            a += 1

        while b < n:
            final.append(nums2[b])
            b += 1

        nums1[:] = final