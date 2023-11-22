def f(dice):
    previous = dice[0]
    current_streak = 1
    max_streak = 1
    leader = previous
    for i in range(1, len(dice)):
        if dice[i] == previous:
            current_streak += 1
            if current_streak >= max_streak:
                max_streak = current_streak
                leader = dice[i]
        else:
            current_streak = 1

        previous = dice[i]
    return leader


print(f("2133"))
