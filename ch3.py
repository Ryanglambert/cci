class Stack(object):
    "3.2 Make a stack that has O(1) lookup time for the minimum"
    def __init__(self):
        self._stack = []

    def _update_min(self):
        self.minimum_val = min(self._stack)

    def push(self, item):
        self._stack.append(item)
        self._update_min()

    def pop(self):
        return self._stack.pop()

    def min(self):
        return self.minimum_val


class StackSet(object):
    "3.3 make a StackSet class that maintains a series of stacks"
    def __init__(self, size_limit=3):
        self.size_limit = size_limit
        self._stacks = [[]]

    def __repr__(self):
        return str(self._stacks)

    def push(self, item):
        self._ensure_stack_limit()
        self._stacks[-1].append(item)

    def pop(self):
        value = self._stacks[-1].pop()
        self._ensure_last_stack_not_empty()
        return value

    def _ensure_stack_limit(self):
        if len(self._stacks[-1]) >= self.size_limit:
            self._stacks.append([])

    def _ensure_last_stack_not_empty(self):
        if len(self._stacks) > 1:
            for i, stack in enumerate(self._stacks):
                if len(stack) == 0:
                    self._stacks.pop(i)


