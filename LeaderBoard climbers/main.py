def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, delta = change.split()
        idx = leaderboard.index(name)
        leaderboard.insert(idx - int(delta), leaderboard.pop(idx))
    print(leaderboard)
    return leaderboard

leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1'])# , ['Fred', 'John', 'Dave', 'Brian', 'Jim']
# leaderboard_sort(['Bob', 'Larry', 'Kevin', 'Jack', 'Max'], ['Max +3', 'Kevin -1', 'Kevin +3']), ['Bob', 'Kevin', 'Max', 'Larry', 'Jack']