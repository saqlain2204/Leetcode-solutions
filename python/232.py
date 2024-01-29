'''
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
'''
class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop(0)

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(9)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
    
'''
Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Test Cases:
["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]
["MyQueue","push","push","pop","peek","empty"]
[[],[1],[2],[],[],[]]
["MyQueue","push","push","push","pop","pop","pop","empty"]
[[],[1],[2],[3],[],[],[],[]]

'''