def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = badge_maker(name)
        badges.append(badge)
    return badges

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names, start=1):
        assignment = "Hello, {}! You'll be assigned to room {}!".format(name, index)
        room_assignments.append(assignment)
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    for assignment in assignments:
        print(assignment)

