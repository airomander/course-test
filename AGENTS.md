# AGENTS.md

Single-file Python Sudoku game with tkinter GUI, 10 fixed puzzles,
Russian UI.

```
python sudoku.py
```

## Architecture

- **Board**: `list[list[int]]` 9×9, `0` = empty
- **10 hand-written puzzles** in `PUZZLES` list (not generated) —
  each has `puzzle` (givens) + `solution` (full grid)
- **Original cells** (`original[r][c] != 0`) are immutable givens
- **Win**: all cells match `solution`
- **Error limits** per difficulty: Легкий = 6, Средний = 4, Сложный = 2
- **Undo / Redo**: max 3 steps, Ctrl+Z / Ctrl+Y or bottom buttons;
  redo stack clears on new action
- **sudoku_stats.json**: auto-created, stores `best_time` and `best_errors`
  per puzzle (keys `"1"`..`"10"`)
- **`.gitignore`** ignores `__pycache__/`, `*.pyc`, `*.pyo`, `*.pyd`

## GUI layout

Game window: canvas (left) + info panel (right). Info panel shows:
card name + difficulty badge, timer, errors, remaining numbers as 3×3
grid, and action buttons (undo / redo / back) stacked vertically.

## GUI quirks

- Left-click empty/wrong cell → popup number panel near cursor
- Right-click → same panel but toggles pencil marks (grey corner digits)
- Wrong numbers highlighted in red (`#ffebee`), completed rows/columns/
  3×3 boxes glow green (`#e8f5e9`)
- Popup (`overrideredirect`) auto-closes on focus loss or Escape

## Verification

No tests, linter, or typechecker. Run manually only.
