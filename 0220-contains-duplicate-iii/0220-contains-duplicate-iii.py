class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        window = [] #sorted, indexDiff wide

        for idx, val in enumerate(nums):
            # hypothetical value pos in window
            position = bisect.bisect_left(window, val)
            # checks right neighbor
            if position < len(window) and abs(window[position] - val) <= valueDiff:
                return True
            # checks left neighbor
            if position > 0 and abs(val - window[position - 1]) <= valueDiff:
                return True
            # adds val to the window, sorts
            bisect.insort(window, val)
            # evicts old element to maintain indexDiff size
            if idx >= indexDiff:
                oldVal = nums[idx-indexDiff]
                remove = bisect.bisect_left(window, oldVal)
                if remove < len(window) and window[remove] == oldVal:
                    window.pop(remove)
            
        return False