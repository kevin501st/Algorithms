class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__stacks = []
        self.__capacity = capacity
        self.__left_most = 0
        self.__pop_index = len(self.__stacks) - 1

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.__left_most > (len(self.__stacks) - 1):
            self.__stacks.append([val])
            self.__left_most = len(self.__stacks) - 1
            self.__pop_index += 1
        else:
            while len(self.__stacks[self.__left_most]) >= self.__capacity:
                self.__left_most += 1
                if self.__left_most == len(self.__stacks):
                    self.__stacks.append([])
                self.__pop_index += 1
            self.__stacks[self.__left_most].append(val)

    def pop(self):
        """
        :rtype: int
        """
        if not self.__stacks:
            return -1
        while 0 < self.__pop_index < len(self.__stacks) and not self.__stacks[self.__pop_index]:
            self.__pop_index -= 1
        if not self.__stacks[self.__pop_index]:
            return -1
        if not 0 <= self.__pop_index < len(self.__stacks):
            while not 0 <= self.__pop_index < len(self.__stacks):
                self.__pop_index -= 1

            if self.__pop_index == 0 and not self.__stacks[self.__pop_index]:
                return -1
        item = self.__stacks[self.__pop_index].pop()
        if not self.__stacks[self.__pop_index] and self.__pop_index > 0:
            self.__pop_index -= 1
        if self.__left_most > self.__pop_index:
            self.__left_most = self.__pop_index
        return item

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if not 0 <= index < len(self.__stacks):
            return -1
        if not self.__stacks[index]:
            return -1
        stack = self.__stacks[index].pop()
        # if not self.__stacks[index]:
        #     self.__stacks.pop(index)
        if self.__left_most >= index:
            self.__left_most = index
        # if self.__pop_index >= index:
        #     self.__pop_index -= 1
        #
        return stack


# Your DinnerPlates object will be instantiated and called as such:
obj = DinnerPlates(1)
obj.push(1)
obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.push(5)
obj.popAtStack(1)
# obj.push(20)
# obj.push(21)
# obj.popAtStack(1)
# obj.popAtStack(2)
print(obj.pop())
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# obj.push(3)
# obj.popAtStack(0)
