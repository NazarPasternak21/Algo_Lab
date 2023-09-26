def is_subarray(nums1, nums2):
    if not nums1:
        return True

    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            i += 1
        j += 1

    return i == len(nums1)


nums1 = [1, 2, 3, 0]
nums2 = [0, 1, 2, 3, 4, 0]
print(is_subarray(nums1, nums2))

nums1 = [4, 2]
nums2 = [1, 2, 3, 4]
print(is_subarray(nums1, nums2))

nums1 = [1, 3, 5]
nums2 = [1, 2, 3, 4, 5]
print(is_subarray(nums1, nums2))

