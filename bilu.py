def convert(x):
    if x == "a":
        return 0
    elif x == "b":
        return 1
    elif x == "c":
        return 2
centered = False
print("Welcome to Bilu, an AI especialized in tic-tac-toe, impossible to be beaten > ")
print("Developed by Victor Cortez | 2016 | UFPE")
print("To play, type in the coordinates of your move (example: a2) based in this coordinate system:")
print("- 1 2 3")
print("a x x x")
print("b x x x")
print("c x x x")
print("type exit to exit")
print("Have a nice game!.")
print("----------------------")
saida = False
vitorias = 0
derrotas = 0
empates = 0
while saida is False:
    print("Vitorias: " + str(vitorias))
    print("Derrotas: " + str(derrotas))
    print("Empates: " + str(empates))
    matriz =[
[" "," "," "],
[" "," "," "],
[" "," "," "]
]
    movimentos = []
    while True:
        print("\n".join(
    "|".join(i) for i in matriz
    ))
        movimento = input("Make you move> ")
        while len(movimento) != 2 or movimento[0] not in ["a","b","c"] or movimento[1] not in ["1","2","3"] or matriz[int(movimento[1]) - 1][convert(movimento[0])] != " ":
            movimento = input("Invalid move, try again > ")
            if movimento == "exit":
                break
        if movimento == "exit":
            saida = True
            print ("It was very nice to play with you, till next time!")
            break
        movimentos.append(movimento)
        x = convert(movimento[0])
        y = int(movimento[1]) - 1
        matriz[y][x] = "X"
        finished = False
        winner = ""
        tie = False
        played = False
        if matriz[0].count("X") + matriz[0].count("O") + matriz[1].count("X") + matriz[1].count("O") + matriz[2].count("X") + matriz[2].count("O") == 9:
            finished = True
            tie = True
            played = True
        for i in range(0,3):
            #tryes to win
            if ((matriz[i].count("O") == 2 and matriz[i].count("X") == 0)) and played is False:
                matriz[i] = ["O" if i != "X" else "X" for i in matriz[i]]
                played = True
                print("lol")
                break
            if matriz[0][i] + matriz[1][i] == "OO" and matriz[2][i] == " " and played is False:
                matriz[2][i] = "O"
                played = True
                break
            if matriz[0][i] + matriz[2][i] == "OO" and matriz[1][i] == " " and played is False:
                matriz[1][i] = "O"
                played = True
                break
            if matriz[2][i] + matriz[1][i] == "OO" and matriz[0][i] == " " and played is False:
                matriz[0][i] = "O"
                played = True
                break
        for i in range(0,3):
            #tryes not to lose
            if ((matriz[i].count("X") == 2 and matriz[i].count("O") == 0) or (matriz[i].count("O") == 2 and matriz[i].count("X") == 0)) and played is False:
                matriz[i] = ["O" if i != "X" else "X" for i in matriz[i]]
                played = True
                break
            if matriz[0][i] + matriz[1][i] == "XX" and matriz[2][i] == " " and played is False:
                matriz[2][i] = "O"
                played = True
                break
            if matriz[0][i] + matriz[2][i] == "XX" and matriz[1][i] == " " and played is False:
                matriz[1][i] = "O"
                played = True
                break
            if matriz[2][i] + matriz[1][i] == "XX" and matriz[0][i] == " " and played is False:
                matriz[0][i] = "O"
                played = True
                break
        while played is False:
            #tryes to win
            if matriz[0][0] + matriz[1][1] == "OO" and matriz[2][2] == " ":
                matriz[2][2] = "O"
                played = True
                break
            if matriz[0][0] + matriz[2][2] == "OO" and matriz[1][1] == " ":
                matriz[1][1] = "O"
                played = True
                break
            if matriz[1][1] + matriz[2][2] == "OO"and matriz[0][0] == " ":
                matriz[0][0] = "O"
                played = True
                break
            if matriz[2][0] + matriz[1][1] == "OO" and matriz[0][2] == " ":
                matriz[0][2] = "O"
                played = True
                break
            if matriz[0][2] + matriz[1][1] == "OO" and matriz[2][0] == " ":
                matriz[2][0] = "O"
                played = True
                break
            if matriz[0][2] + matriz[2][0] == "OO" and matriz[1][1] == " ":
                matriz[1][1] = "O"
                played = True
                break
            #tryes not to lose
            if matriz[0][0] + matriz[1][1] == "XX" and matriz[2][2] == " ":
                matriz[2][2] = "O"
                played = True
                break
            if matriz[0][0] + matriz[2][2] == "XX" and matriz[1][1] == " ":
                matriz[1][1] = "O"
                played = True
                break
            if matriz[1][1] + matriz[2][2] == "XX"and matriz[0][0] == " ":
                matriz[0][0] = "O"
                played = True
                break
            if matriz[2][0] + matriz[1][1] == "XX" and matriz[0][2] == " ":
                matriz[0][2] = "O"
                played = True
                break
            if matriz[0][2] + matriz[1][1] == "XX" and matriz[2][0] == " ":
                matriz[2][0] = "O"
                played = True
                break
            if matriz[0][2] + matriz[2][0] == "XX" and matriz[1][1] == " ":
                matriz[1][1] = "O"
                played = True
                break
            if (matriz[0][0] + matriz[0][2] + matriz[2][0] + matriz [2][2]).replace(" ","") == "X" and matriz[0].count("0") + matriz[1].count("O") + matriz[2].count("O") == 0:
                matriz[1][1] = "O"
                played = True
                centered = True
                break
            if centered is True:
                if matriz[2][1] == "X" and matriz[2][2] == " " and played is False:
                    matriz[2][2] = "O"
                    played = True
                if matriz[2][1] == " " and matriz[0][2] != "X" and matriz[0][2] == "X" and played is False:
                    matriz[2][1] = "O"
                    played = True
                if matriz[0][1] == "X" and matriz[0][2] == " " and matriz[2][2] == "X" and played is False:
                    matriz[0][2] = "O"
                    played = True
                if matriz[0][1] == " " and played is False:
                    matriz[0][1] = "O"
                    played = True
                if matriz[1][0] == " " and played is False:
                    matriz[1][0] = "O"
                    played = True
                if matriz[2][1] == " " and played is False:
                    matriz[2][1] = "O"
                    played = True
                played = True
                centered = False
                break
            if (matriz[0].count("X") + matriz[1].count("X") + matriz[2].count("X") == 1) and ((matriz[0][1] + matriz[1][0] + matriz[1][2] + matriz[2][1]).replace(" ","") == "X"):
                matriz[1][1] = "O"
                played = True
                break
            if matriz[0][0] == " ":
                matriz[0][0] = "O"
                played = True
                break
            if matriz[2][2] == " ":
                matriz[2][2] = "O"
                played = True
                break
            if matriz[0][2] == " ":
                matriz[0][2] = "O"
                played = True
                break
            if matriz[2][0] == " ":
                matriz[2][0] = "O"
                played = True
                break
            if matriz[1][2] == " ":
                matriz[1][2] = "O"
                played = True
                break
            elif matriz[0][1] == " ":
                matriz[0][1] = "O"
                played = True
                break
            elif matriz[1][0] == " ":
                matriz[1][0] = "O"
                played = True
                break
            elif matriz[2][1] == " ":
                matriz[2][1] = "O"
                played = True
                break
        for i in range (0,3):
            if matriz [i] == ["X","X","X"]:
                finished = True
                winner = "X"
                break
            if matriz [i] == ["O","O","O"]:
                finished = True
                winner = "O"
                break
            if matriz[0][i] + matriz[1][i] + matriz[2][i] == "XXX":
                finished = True
                winner = "X"
                break
            if matriz[0][i] + matriz[1][i] + matriz[2][i] == "OOO":
                finished = True
                winner = "O"
                break
        if matriz[0][0] + matriz[1][1] + matriz[2][2] == "XXX":
                finished = True
                winner = "X"
        if matriz[0][0] + matriz[1][1] + matriz[2][2] == "OOO":
                finished = True
                winner = "O"
        if matriz[2][0] + matriz[1][1] + matriz[0][2] == "XXX":
                finished = True
                winner = "X"
        if matriz[2][0] + matriz[1][1] + matriz[0][2] == "OOO":
                finished = True
                winner = "O"
        if matriz[0].count("X") + matriz[0].count("O") + matriz[1].count("X") + matriz[1].count("O") + matriz[2].count("X") + matriz[2].count("O") == 9:
            finished = True
            tie = True
        if finished is True:
            print ("Its over!")
            if tie is True:
                print("TIE!")
                empates += 1
            else:
                print("The winner is " + winner)
                if winner == "X":
                    vitorias += 1
                    arquivo = open("victories.txt","a")
                    arquivo.write("|".join(movimentos))
                    arquivo.write("\n")
                    arquivo.close()
                else:
                    derrotas += 1
            print("\n".join(
                "|".join(i) for i in matriz
                ))
            break
arquivo = open("victories.txt","a")
arquivo.write("------------------------")
arquivo.write("\n")
arquivo.close()
