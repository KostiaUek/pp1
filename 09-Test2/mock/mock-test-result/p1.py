values = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def f(player1, player2):
    player_1_list = list(player1)
    i = 0
    while i in range(len(player_1_list)):
        if player_1_list[i] in values.keys():
            player_1_list[i] = values[player_1_list[i]]

        if type(player_1_list[i]) != int:
            player_1_list[i] = int(player_1_list[i])

        i += 1

    player_2_list = list(player2)
    i = 0
    while i in range(len(player_2_list)):
        if player_2_list[i] in values.keys():
            player_2_list[i] = values[player_2_list[i]]

        if type(player_2_list[i]) != int:
            player_2_list[i] = int(player_2_list[i])

        i += 1

    score_1 = sum(player_1_list)
    score_2 = sum(player_2_list)
    return score_1 >= score_2


if __name__ == "__main__":
    print(f("AJ972", "AQT72"))
    print(f("9532", "K8"))
