#!/usr/bin/python3
""" Prime Game """


def isWinner(
    x, nums
):  # sourcery skip: assign-if-exp, merge-duplicate-blocks, merge-else-if-into-elif, reintroduce-else # noqa
    """Determines the winner of the prime game."""
    if x <= 1 or nums is None or len(nums) == 0:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        if i % 2 == 0:
            if nums[i] % 2 == 0:
                Maria += nums[i]
            else:
                Ben += nums[i]
        else:
            if nums[i] % 2 == 0:
                Ben += nums[i]
            else:
                Maria += nums[i]
    if Maria > Ben:
        return "Maria"
    return "Ben"
