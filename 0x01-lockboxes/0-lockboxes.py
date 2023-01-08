#!/usr/bin/python3
"""determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    Args::
        boxes(list): list of integer lists
    """
    visited_boxes = set()

    queue = [0]

    while queue:
        box = queue.pop(0)
        if box not in visited_boxes:
            visited_boxes.add(box)
            queue += boxes[box]
    if len(visited_boxes) == len(boxes):
        return True
    else:
        return False
