# AGENTS.md

## Project structure

Single-file Python Sudoku game with GUI. Only stdlib dependency is `tkinter`.

- `sudoku.py` — run via `python sudoku.py`
- UI language is Russian

## Architecture

- **Board**: `list[list[int]]` 9×9, `0` = empty
- **Generation**: `generate_solved()` — fills 3 diagonal boxes with shuffled 1–9, then backtracking-solves; `create_puzzle(solved, clues=30)` removes `81 - clues` random cells
- **Original cells** (`original[r][c] != 0`) are immutable givens
- **Win**: all cells match `solved`

## GUI (tkinter)

- **Left-click** empty cell → number panel appears near cursor → click digit to set it (click same digit again to clear)
- **Right-click** → same panel but toggles pencil marks (small grey numbers in cell corners)
- **Instant validation**: wrong numbers turn the cell red (`#f5c5c5`)
- **Completed regions**: any correctly filled row / column / 3×3 box glows green (`#b8f0b5`); multiple regions can be lit simultaneously
- **Undo / Redo**: buttons at bottom, max 3 steps, redo clears on new action
- **Panel**: `overrideredirect(True)` popup positioned above cursor, auto-closes on focus loss or pick

## Verification

No tests, linter, or typechecker. Run manually:

```bash
python sudoku.py
```
