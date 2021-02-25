class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        i = 0

        while True:
            gas_amt = gas[i]
            s = i
            while gas_amt >= cost[s]:
                gas_amt = gas_amt - cost[s]
                s = (s + 1) % len(cost)
                # if gas_amt <= 0:
                #     break
                gas_amt += gas[s]

                if s == i:
                    return i
                # i = (i + 1) % len(cost)
                # if i == 0:
                #     return -1
            i = (i + 1) % len(cost)
            if i == 0:
                return -1

a = Solution()
print(a.canCompleteCircuit([3,3,4],[3,4,4]))
