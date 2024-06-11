import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If the total number of cards is not divisible by groupSize, it's not possible to form the groups
        if len(hand) % groupSize:
            return False

        # Count the frequency of each card in the hand
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # Create a min-heap from the unique card values
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        # Process the cards to form the required groups
        while minHeap:
            # Get the smallest card (the start of a potential group)
            first = minHeap[0]

            # Check if we can form a group starting from 'first' and covering 'groupSize' consecutive cards
            for i in range(first, first + groupSize):
                if i not in count:
                    # If a required card is missing, we cannot form the group
                    return False
                count[i] -= 1  # Use one occurrence of this card
                if count[i] == 0:
                    # If this card is now used up completely, it should be the smallest in the heap
                    if i != minHeap[0]:
                        # If it's not the smallest, something went wrong (heap property violated)
                        return False
                    # Remove the card from the heap
                    heapq.heappop(minHeap)

        # If we successfully formed all groups, return True
        return True


hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
solution_instance = Solution()
print(solution_instance.isNStraightHand(hand, groupSize))
