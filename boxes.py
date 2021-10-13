import chess

boxes = [
    [chess.A1, chess.A2, chess.A3, chess.A4, chess.A5, chess.A6, chess.A7, chess.A8],
    [chess.B1, chess.B2, chess.B3, chess.B4, chess.B5, chess.B6, chess.B7, chess.B8],
    [chess.C1, chess.C2, chess.C3, chess.C4, chess.C5, chess.C6, chess.C7, chess.C8],
    [chess.D1, chess.D2, chess.D3, chess.D4, chess.D5, chess.D6, chess.D7, chess.D8],
    [chess.E1, chess.E2, chess.E3, chess.E4, chess.E5, chess.E6, chess.E7, chess.E8],
    [chess.F1, chess.F2, chess.F3, chess.F4, chess.F5, chess.F6, chess.F7, chess.F8],
    [chess.G1, chess.G2, chess.G3, chess.G4, chess.G5, chess.G6, chess.G7, chess.G8],
    [chess.H1, chess.H2, chess.H3, chess.H4, chess.H5, chess.H6, chess.H7, chess.H8],
]


def get_box(s: str):
    lt = s[0]
    col = int(s[1]) - 1
    row = ord("a") - ord(lt.lower())
    return boxes[row][col]
