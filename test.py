def update_vars(current_position, gem_collection):

    next_position = min(current_position + activeplayermove, len(track) - 1)
    track[current_position] = " "
    current_position += 1
    # print("update_vars(): ", activeplayermove, current_position, next_position)
    while current_position <= next_position:

        gem_collection[playerno].append(track[current_position])

        track[current_position] = " "
        current_position += 1
    track[next_position] = "*"
    # print(gem_collection)

    return " "
