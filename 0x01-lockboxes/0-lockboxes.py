#!/usr/bin/python3
'''A module for working with lockboxes.
'''
from collections import deque


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    seen_boxes = [False]*n
    seen_boxes[0] = True
    queue = deque(boxes[0])
    
    while queue:
        boxIdx = queue.popleft()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if not seen_boxes[boxIdx]:
            queue.extend(boxes[boxIdx])
            seen_boxes[boxIdx] = True
            
    return all(seen_boxes)

