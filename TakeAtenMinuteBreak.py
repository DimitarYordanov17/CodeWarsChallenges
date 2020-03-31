def is_valid_walk(walk):
    west = walk.count("w")
    east = walk.count("e")
    north = walk.count("n")
    south = walk.count("s")
    if not len(walk) == 10 or (west != east or north != south):
        return False
    else:
        return True


print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
