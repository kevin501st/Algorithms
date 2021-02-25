def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    #         l, r = 0

    #         longer = nums1
    #         shorter = nums2
    #         if len(nums1) < len(nums2):
    #             longer = nums2
    #             shorter = nums1

    #         while l < len(longer) and r < len(shorter):
    #             while longer[l] < shorter[r]:
    #                 l += 1
    #             longer.insert(l, shorter[r])
    #             l += 1
    #             r += 1

    #         if r == len(shorter):
    #             return

    if not len(nums1) % 2:
        med1 = (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
    else:
        med1 = nums1[len(nums1) // 2]

    if not len(nums2) % 2:
        med2 = (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
    else:
        med2 = nums2[len(nums2) // 2]

    print(med1, med2)
    return (med1 + med2) / 2

print( findMedianSortedArrays([1,2], [3,4]))