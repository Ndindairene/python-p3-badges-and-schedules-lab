def badge_maker(name = 'irene'):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    return [f'Hello, my name is {name}.' for name in names]

speakers = ["Arel", "Carol"]
badge_messages = batch_badge_creator(speakers)
print(badge_messages)


def assign_rooms(names):
    return([f'Hello, {name}! You\'ll be assigned to room {i + 1}!' for i, name in enumerate(names)])

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)


