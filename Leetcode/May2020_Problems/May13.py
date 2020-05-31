""" Remove K Digits """
from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return None

        if len(num) == k:
            return '0'


        stack = []

        for i in num:

            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1

            stack.append(i)


        while k > 0:
            stack.pop()
            k -= 1

        out = int(''.join(stack))
        return ''.join(stack).lstrip('0') if out else '0'

