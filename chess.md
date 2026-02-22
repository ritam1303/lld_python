# ♟️ Simple Chess Pawn Engine (Python OOP)

This project is a minimal **object-oriented chess simulation** focused on pawn movement, board state management, and turn-based gameplay.

It demonstrates:

* Object-Oriented Design
* Encapsulation of movement logic
* Turn validation
* Capture mechanics
* Clean separation of game, board, and piece logic

---

# 🧠 Class Design (UML)

```
+----------------------+
|        Game          |
+----------------------+
| - board: ChessBoard  |
| - players: dict      |
| - turn: str          |
+----------------------+
| + move(row, col)     |
| + print_board()      |
+----------+-----------+
           |
           | uses
           v
+----------------------+
|     ChessBoard       |
+----------------------+
| - board: list[list]  |
| - pawn: Pawn         |
+----------------------+
| + move_pawn(r,c)     |
| + print_board()      |
+----------+-----------+
           |
           | delegates movement logic
           v
+----------------------+
|        Pawn          |
+----------------------+
|                      |
+----------------------+
| + move_pawn(board,r,c)|
+----------------------+


+----------------------+
|        Player        |
+----------------------+
| - name: str          |
| - color: str         |
+----------------------+
```

---

# 📂 Implementation Code

```python
class Pawn:
    
    def move_pawn(self, board, row: int, col: int):

        piece = board[row][col]
        if piece is None:
            return

        # ---------- BLACK PAWN ----------
        if piece == "Black-Pawn":

            if row+1 < 8 and col+1 < 8 and board[row+1][col+1] == "White-Pawn":
                board[row+1][col+1] = piece
                board[row][col] = None
                print("Black captured at", row+1, col+1)
                return

            if row+1 < 8 and col-1 >= 0 and board[row+1][col-1] == "White-Pawn":
                board[row+1][col-1] = piece
                board[row][col] = None
                print("Black captured at", row+1, col-1)
                return

            if row+1 < 8 and board[row+1][col] is None:
                board[row+1][col] = piece
                board[row][col] = None
                print("Black moved to", row+1, col)
                return

        # ---------- WHITE PAWN ----------
        if piece == "White-Pawn":

            if row-1 >= 0 and col+1 < 8 and board[row-1][col+1] == "Black-Pawn":
                board[row-1][col+1] = piece
                board[row][col] = None
                print("White captured at", row-1, col+1)
                return

            if row-1 >= 0 and col-1 >= 0 and board[row-1][col-1] == "Black-Pawn":
                board[row-1][col-1] = piece
                board[row][col] = None
                print("White captured at", row-1, col-1)
                return

            if row-1 >= 0 and board[row-1][col] is None:
                board[row-1][col] = piece
                board[row][col] = None
                print("White moved to", row-1, col)
                return


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.pawn = Pawn()

        for col in range(8):
            self.board[1][col] = "Black-Pawn"
            self.board[6][col] = "White-Pawn"

    def print_board(self):
        for row in self.board:
            print(row)
        print()

    def move_pawn(self, row: int, col: int):
        self.pawn.move_pawn(self.board, row, col)


class Player:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.players = {
            "White": Player("Alice", "White"),
            "Black": Player("Bob", "Black")
        }
        self.turn = "White"

    def print_board(self):
        self.board.print_board()

    def move(self, row, col):
        piece = self.board.board[row][col]

        if piece is None:
            print("No piece at this square")
            return

        if not piece.startswith(self.turn):
            print(f"{self.turn}'s turn. You cannot move {piece}")
            return

        self.board.move_pawn(row, col)
        self.turn = "Black" if self.turn == "White" else "White"
        print("Next turn:", self.turn)


# ---- RUN ----
game = Game()
game.print_board()

game.move(6,6)
game.print_board()

game.move(1,5)
game.print_board()
```

---

# ▶️ How to Run

```bash
python chess.py
```

---

# 🚀 Future Improvements

* Add first-move double pawn step
* Add en-passant
* Add pawn promotion
* Convert pieces into real classes instead of strings
* Introduce base `Piece` class with polymorphism
* Implement full chess move validation engine

---

# 📌 Why This Project Is Valuable

This project showcases:

* Clean OOP modeling
* Turn-based game design
* Separation of concerns
* Extensible architecture

These skills are directly useful in:

* Backend engineering interviews
* Machine coding rounds
* Low Level Design interviews
* Game simulation systems

---
