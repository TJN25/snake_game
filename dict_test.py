



wRook = 1
height = [665, 575, 484, 401, 318, 235, 145, 55]
width = [55, 145, 235, 318, 401, 484, 575, 665]

def wRook_draw(values):
    x = v[0]
    y = v[1]

    print("X: "+str(height[x]))
    print("Y: "+str(width[y]))

d = {"wr1" : [0, 0, "wRook"],
"wk1" : [0, 1, "wKnight"],
"wb1" : [0, 2, "wBishop"],
"wQ" : [0, 3, "wQueen"],
"wK" : [0, 4, "wKing"],
"wb2" : [0, 5, "wBishop"],
"wk2" : [0, 6, "wKnight"],
"wr2" : [0, 7, "wRook"],
"wp1" : [0, 0, "wPawn"],
"wp2" : [1, 1, "wPawn"],
"wp3" : [1, 2, "wPawn"],
"wp4" : [1, 3, "wPawn"],
"wp5" : [1, 4, "wPawn"],
"wp6" : [1, 5, "wPawn"],
"wp7" : [1, 6, "wPawn"],
"wp8" : [1, 7, "wPawn"]}


for k,v in d.items():
    if v[2] == "wRook":
        wRook_draw(v)
