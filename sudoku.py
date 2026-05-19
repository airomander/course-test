import tkinter as tk
from tkinter import font as tkfont
import json
import os
import time

# ── 10 fixed puzzles ──

PUZZLES = [
    {
        "name": "Карта 1",
        "difficulty": "Легкий",
        "puzzle": [[4,0,8,0,1,9,0,6,0],[0,0,3,7,6,4,0,0,0],[6,1,2,0,0,8,7,0,0],[2,0,6,0,0,0,9,7,5],[9,0,0,6,4,0,8,2,1],[1,8,0,9,0,0,0,0,4],[8,2,0,0,0,0,0,0,0],[7,0,0,5,3,0,0,0,0],[0,0,9,8,0,0,0,1,6]],
        "solution": [[4,7,8,2,1,9,5,6,3],[5,9,3,7,6,4,1,8,2],[6,1,2,3,5,8,7,4,9],[2,4,6,1,8,3,9,7,5],[9,3,7,6,4,5,8,2,1],[1,8,5,9,7,2,6,3,4],[8,2,1,4,9,6,3,5,7],[7,6,4,5,3,1,2,9,8],[3,5,9,8,2,7,4,1,6]],
    },
    {
        "name": "Карта 2",
        "difficulty": "Легкий",
        "puzzle": [[1,4,0,0,0,0,7,0,0],[5,9,0,7,0,8,0,0,0],[0,8,7,0,6,9,0,0,0],[0,0,0,0,0,1,6,4,0],[0,7,9,0,3,0,0,2,0],[0,0,0,6,0,0,0,0,3],[0,2,0,0,9,5,0,7,6],[0,3,1,8,4,6,0,5,0],[9,6,5,0,2,7,0,0,0]],
        "solution": [[1,4,6,2,5,3,7,8,9],[5,9,3,7,1,8,2,6,4],[2,8,7,4,6,9,1,3,5],[3,5,2,9,8,1,6,4,7],[6,7,9,5,3,4,8,2,1],[4,1,8,6,7,2,5,9,3],[8,2,4,1,9,5,3,7,6],[7,3,1,8,4,6,9,5,2],[9,6,5,3,2,7,4,1,8]],
    },
    {
        "name": "Карта 3",
        "difficulty": "Легкий",
        "puzzle": [[9,0,0,1,2,4,6,7,0],[0,7,0,3,9,0,1,0,5],[0,0,0,0,0,7,2,0,9],[0,5,7,4,8,0,0,6,2],[0,0,0,0,0,1,0,8,0],[4,0,0,0,0,0,9,5,0],[7,8,0,6,0,3,5,0,0],[0,4,3,0,0,2,8,1,0],[6,0,0,8,4,0,7,0,3]],
        "solution": [[9,3,5,1,2,4,6,7,8],[2,7,6,3,9,8,1,4,5],[8,1,4,5,6,7,2,3,9],[1,5,7,4,8,9,3,6,2],[3,6,9,2,5,1,4,8,7],[4,2,8,7,3,6,9,5,1],[7,8,2,6,1,3,5,9,4],[5,4,3,9,7,2,8,1,6],[6,9,1,8,4,5,7,2,3]],
    },
    {
        "name": "Карта 4",
        "difficulty": "Средний",
        "puzzle": [[0,9,0,0,0,0,4,8,5],[8,0,0,0,3,0,0,7,9],[1,0,4,8,0,0,0,0,0],[4,0,0,0,2,0,3,0,7],[5,0,8,0,4,0,0,1,6],[2,0,7,0,0,0,0,9,0],[0,0,1,0,0,0,0,0,2],[3,4,2,0,8,7,0,0,1],[0,0,0,2,0,3,0,4,8]],
        "solution": [[6,9,3,1,7,2,4,8,5],[8,2,5,4,3,6,1,7,9],[1,7,4,8,9,5,6,2,3],[4,1,9,6,2,8,3,5,7],[5,3,8,7,4,9,2,1,6],[2,6,7,3,5,1,8,9,4],[7,8,1,5,6,4,9,3,2],[3,4,2,9,8,7,5,6,1],[9,5,6,2,1,3,7,4,8]],
    },
    {
        "name": "Карта 5",
        "difficulty": "Средний",
        "puzzle": [[0,0,0,1,3,0,7,4,9],[0,0,0,0,0,4,0,0,0],[0,0,4,0,9,0,1,0,0],[3,0,0,0,0,9,6,0,5],[0,0,9,0,0,0,4,0,7],[0,4,0,0,0,7,9,0,0],[0,0,0,0,0,0,2,6,0],[0,0,6,2,0,3,0,0,0],[4,0,0,0,6,8,5,7,3]],
        "solution": [[8,6,5,1,3,2,7,4,9],[1,9,2,6,7,4,3,5,8],[7,3,4,8,9,5,1,2,6],[3,1,7,4,2,9,6,8,5],[2,5,9,3,8,6,4,1,7],[6,4,8,5,1,7,9,3,2],[9,8,3,7,5,1,2,6,4],[5,7,6,2,4,3,8,9,1],[4,2,1,9,6,8,5,7,3]],
    },
    {
        "name": "Карта 6",
        "difficulty": "Сложный",
        "puzzle": [[9,0,0,0,0,0,5,0,0],[0,0,0,0,5,0,4,0,9],[8,0,0,0,7,0,0,0,0],[6,3,0,0,1,5,0,0,0],[0,0,0,9,6,0,0,0,0],[0,9,0,8,0,0,6,5,1],[7,0,0,6,8,3,2,0,0],[4,0,0,5,0,0,0,6,0],[0,6,0,0,0,0,9,0,0]],
        "solution": [[9,4,1,3,2,6,5,8,7],[3,7,6,1,5,8,4,2,9],[8,5,2,4,7,9,1,3,6],[6,3,7,2,1,5,8,9,4],[1,8,5,9,6,4,3,7,2],[2,9,4,8,3,7,6,5,1],[7,1,9,6,8,3,2,4,5],[4,2,3,5,9,1,7,6,8],[5,6,8,7,4,2,9,1,3]],
    },
    {
        "name": "Карта 7",
        "difficulty": "Средний",
        "puzzle": [[0,7,2,1,0,4,6,9,8],[1,6,0,2,5,0,7,0,0],[0,0,0,0,0,0,0,0,0],[2,1,0,4,0,6,0,0,3],[6,0,0,5,0,1,9,4,2],[0,0,0,8,0,0,0,0,6],[0,0,0,0,8,0,1,6,0],[0,0,6,0,0,0,0,2,0],[0,5,0,0,0,0,0,0,9]],
        "solution": [[5,7,2,1,3,4,6,9,8],[1,6,9,2,5,8,7,3,4],[3,4,8,7,6,9,2,5,1],[2,1,5,4,9,6,8,7,3],[6,8,3,5,7,1,9,4,2],[4,9,7,8,2,3,5,1,6],[9,2,4,3,8,5,1,6,7],[8,3,6,9,1,7,4,2,5],[7,5,1,6,4,2,3,8,9]],
    },
    {
        "name": "Карта 8",
        "difficulty": "Сложный",
        "puzzle": [[0,3,0,0,0,5,0,0,0],[0,4,0,0,0,8,5,0,0],[8,0,0,0,0,0,1,6,0],[0,0,0,4,0,0,8,0,1],[0,0,0,0,0,0,0,4,7],[5,0,0,0,0,7,0,3,0],[0,0,0,3,0,0,2,0,6],[0,0,0,7,8,0,3,0,5],[0,6,0,0,5,2,0,0,0]],
        "solution": [[1,3,2,6,4,5,7,8,9],[6,4,7,1,9,8,5,2,3],[8,5,9,2,7,3,1,6,4],[2,7,6,4,3,9,8,5,1],[3,9,8,5,2,1,6,4,7],[5,1,4,8,6,7,9,3,2],[9,8,5,3,1,4,2,7,6],[4,2,1,7,8,6,3,9,5],[7,6,3,9,5,2,4,1,8]],
    },
    {
        "name": "Карта 9",
        "difficulty": "Легкий",
        "puzzle": [[7,0,5,0,1,0,0,9,0],[0,2,0,4,0,8,0,7,0],[4,0,8,0,6,0,0,0,2],[2,1,6,9,0,0,7,0,4],[0,8,9,2,7,0,0,3,1],[3,0,0,1,0,6,9,0,5],[6,0,7,8,0,0,0,4,0],[0,3,0,7,0,0,2,6,0],[9,0,0,6,3,1,0,0,7]],
        "solution": [[7,6,5,3,1,2,4,9,8],[1,2,3,4,9,8,5,7,6],[4,9,8,5,6,7,3,1,2],[2,1,6,9,5,3,7,8,4],[5,8,9,2,7,4,6,3,1],[3,7,4,1,8,6,9,2,5],[6,5,7,8,2,9,1,4,3],[8,3,1,7,4,5,2,6,9],[9,4,2,6,3,1,8,5,7]],
    },
    {
        "name": "Карта 10",
        "difficulty": "Средний",
        "puzzle": [[6,2,0,1,3,0,4,7,8],[0,0,5,0,9,4,0,0,6],[4,0,0,0,0,0,2,0,0],[0,8,0,0,6,1,0,0,5],[0,0,7,0,4,9,0,0,3],[0,9,0,8,0,0,6,1,0],[0,0,0,0,5,2,0,6,4],[9,0,6,0,0,0,3,8,0],[0,0,0,0,8,0,0,0,0]],
        "solution": [[6,2,9,1,3,5,4,7,8],[8,7,5,2,9,4,1,3,6],[4,3,1,6,7,8,2,5,9],[2,8,3,7,6,1,9,4,5],[1,6,7,5,4,9,8,2,3],[5,9,4,8,2,3,6,1,7],[3,1,8,9,5,2,7,6,4],[9,5,6,4,1,7,3,8,2],[7,4,2,3,8,6,5,9,1]],
    },
]

STATS_FILE = "sudoku_stats.json"

CELL = 54
GRID = 9 * CELL
OFF = CELL // 6

DIFF_COLORS = {
    "Легкий": "#2e7d32",
    "Средний": "#e65100",
    "Сложный": "#c62828",
}

DIFF_BG = {
    "Легкий": "#e8f5e9",
    "Средний": "#fff3e0",
    "Сложный": "#ffebee",
}

ERROR_LIMITS = {"Легкий": 6, "Средний": 4, "Сложный": 2}

# ── theme colours ──
BG_GIVEN = "#f0f0f0"
BG_EMPTY = "#ffffff"
BG_SELECTED = "#e3f2fd"
BG_WRONG = "#ffebee"
BG_COMPLETE = "#e8f5e9"
BG_WIN = "#e8f5e9"

FG_GIVEN = "#424242"
FG_CORRECT = "#1b5e20"
FG_WRONG = "#c62828"
FG_PENCIL = "#9e9e9e"

GRID_THIN = "#c0c0c0"
GRID_THICK = "#424242"
GRID_BG = "#fafafa"

# ── panel colors ──
PANEL_SET_BG = "#ffffff"
PANEL_SET_FG = "#1565c0"
PANEL_SET_HOVER = "#e3f2fd"
PANEL_SET_ACTIVE = "#bbdefb"
PANEL_SET_BORDER = "#90caf9"

PANEL_MARK_BG = "#f5f5f5"
PANEL_MARK_FG = "#616161"
PANEL_MARK_HOVER = "#eeeeee"
PANEL_MARK_ACTIVE = "#e0e0e0"
PANEL_MARK_BORDER = "#bdbdbd"

DISABLED_FG = "#e0e0e0"
BG_DISABLED = "#fafafa"


def _fmt_time(seconds):
    if seconds is None:
        return "\u2014"
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"


class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Судоку")
        self.root.resizable(False, False)
        self.root.configure(bg=GRID_BG)

        self.stats = self._load_stats()
        self.puzzle_idx = None
        self.puzzle_data = None

        self.board = None
        self.solved = None
        self.original = None
        self.pencil = None
        self.completed = None
        self.completed_numbers = None
        self.undo_st = None
        self.redo_st = None
        self.selected = None
        self.panel = None
        self.mode = "set"
        self.errors_made = 0
        self.error_limit = 6
        self.game_over = False

        self.cv = None
        self.timer_label = None
        self.error_label = None
        self.start_time = None
        self.elapsed = 0
        self.timer_running = False
        self.won = False

        self._panel_gen = 0
        self._panel_pixel = tk.PhotoImage(width=1, height=1)
        self._btn_frm = None
        self._game_over_frm = None
        self._remaining_frm = None
        self._remaining_labels = []
        self._bind_hotkeys()
        self.root.bind("<Button-1>", self._on_any_click, add="+")
        self.show_menu()

    # ── stats ──

    def _load_stats(self):
        if os.path.exists(STATS_FILE):
            try:
                with open(STATS_FILE, encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {str(i + 1): {"best_time": None, "best_errors": None} for i in range(10)}

    def _save_stats(self):
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.stats, f, ensure_ascii=False, indent=2)

    # ── styled button helper ──

    @staticmethod
    def _make_btn(parent, text, command, **kw):
        opts = dict(
            text=text, command=command,
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, bd=0,
            cursor="hand2",
            padx=14, pady=6,
        )
        opts.update(kw)
        btn = tk.Button(parent, **opts)
        return btn

    # ── menu ──

    def show_menu(self):
        self._stop_timer()
        for w in self.root.winfo_children():
            w.destroy()
        self.cv = None
        self.panel = None

        self.root.geometry("")
        self.root.minsize(440, 100)
        self.root.configure(bg=GRID_BG)

        header_bg = "#1565c0"
        title_frame = tk.Frame(self.root, bg=header_bg, height=72)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)

        tk.Label(
            title_frame, text="Судоку",
            font=("Segoe UI", 22, "bold"), bg=header_bg, fg="white"
        ).pack(expand=True)

        tk.Label(
            self.root, text="Выберите уровень:",
            font=("Segoe UI", 11), bg=GRID_BG, fg="#555"
        ).pack(pady=(14, 2))

        sep = tk.Frame(self.root, height=1, bg="#e0e0e0")
        sep.pack(fill=tk.X, padx=24)

        head_font = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        header_row = tk.Frame(self.root, bg=GRID_BG)
        header_row.pack(fill=tk.X, padx=28, pady=(8, 0))
        for txt, w in [("Название", 10), ("Сложность", 11), ("Лучшее", 10), ("Ошибки", 8)]:
            tk.Label(
                header_row, text=txt, font=head_font,
                width=w, anchor=tk.W, bg=GRID_BG, fg="#777"
            ).pack(side=tk.LEFT)

        container = tk.Frame(self.root, bg=GRID_BG)
        container.pack(padx=24, pady=(4, 18), fill=tk.X)

        for i, p in enumerate(PUZZLES):
            idx = str(i + 1)
            best = self.stats[idx]["best_time"]
            diff = p["difficulty"]
            dc = DIFF_COLORS[diff]
            dbg = DIFF_BG[diff]

            row = tk.Frame(container, cursor="hand2", pady=5, padx=8, bg="white", highlightthickness=1, highlightcolor="#e0e0e0", highlightbackground="#e0e0e0")
            row.pack(fill=tk.X, pady=2)

            name_lbl = tk.Label(row, text=p["name"], font=("Segoe UI", 10, "bold"), width=10, anchor=tk.W, bg="white", fg="#333")
            name_lbl.pack(side=tk.LEFT, padx=(4, 0))

            diff_lbl = tk.Label(row, text=diff, font=("Segoe UI", 9, "bold"), width=11, anchor=tk.CENTER, bg=dbg, fg=dc)
            diff_lbl.pack(side=tk.LEFT, padx=4)

            time_lbl = tk.Label(row, text=_fmt_time(best), font=("Segoe UI", 10), width=10, anchor=tk.W, bg="white", fg="#888")
            time_lbl.pack(side=tk.LEFT)

            best_err = self.stats[idx].get("best_errors")
            err_text = f"{best_err}/{ERROR_LIMITS[diff]}" if best_err is not None else "\u2014"
            err_lbl = tk.Label(row, text=err_text, font=("Segoe UI", 10), width=8, anchor=tk.W, bg="white", fg="#888")
            err_lbl.pack(side=tk.LEFT)

            def on_enter(e, r=row, n=name_lbl, t=time_lbl, e_lbl=err_lbl):
                c = "#f5f5f5"
                r.configure(bg=c); n.configure(bg=c); t.configure(bg=c); e_lbl.configure(bg=c)
            def on_leave(e, r=row, n=name_lbl, t=time_lbl, e_lbl=err_lbl):
                c = "white"
                r.configure(bg=c); n.configure(bg=c); t.configure(bg=c); e_lbl.configure(bg=c)

            for widget in (row, name_lbl, diff_lbl, time_lbl, err_lbl):
                widget.bind("<Button-1>", lambda e, idx=i: self.start_game(idx))
                widget.bind("<Enter>", on_enter)
                widget.bind("<Leave>", on_leave)

    # ── game ──

    def start_game(self, idx):
        self.puzzle_idx = idx
        self.puzzle_data = PUZZLES[idx]
        self.won = False
        self.game_over = False

        for w in self.root.winfo_children():
            w.destroy()
        self.panel = None
        self.root.configure(bg=GRID_BG)

        p = self.puzzle_data
        self.solved = [row[:] for row in p["solution"]]
        self.original = [row[:] for row in p["puzzle"]]
        self.board = [row[:] for row in p["puzzle"]]
        self.pencil = set()
        self.completed = set()
        self.completed_numbers = set()
        self.undo_st = []
        self.redo_st = []
        self.selected = None
        self.mode = "set"
        self.errors_made = 0

        diff = p["difficulty"]
        dc = DIFF_COLORS[diff]
        if diff == "Легкий":
            self.error_limit = 6
        elif diff == "Средний":
            self.error_limit = 4
        else:
            self.error_limit = 2

        self.root.title(f"Судоку — {p['name']}")

        game_frame = tk.Frame(self.root, bg=GRID_BG)
        game_frame.pack(padx=14, pady=(10, 12), fill=tk.BOTH)

        self.cv = tk.Canvas(game_frame, width=GRID + 2, height=GRID + 2, bg=BG_EMPTY, highlightthickness=0)
        self.cv.pack(side=tk.LEFT)

        self.cv.bind("<Button-1>", self._on_left)
        self.cv.bind("<Button-3>", self._on_right)
        self.cv.bind("<Motion>", self._on_hover)

        info_frm = tk.Frame(game_frame, bg=GRID_BG, padx=20)
        info_frm.pack(side=tk.LEFT, fill=tk.Y, padx=(14, 0))
        self._info_frm = info_frm

        tk.Label(info_frm, text=p["name"], font=("Segoe UI", 16, "bold"),
                 bg=GRID_BG, fg="#333").pack(anchor=tk.W)

        diff_badge = tk.Frame(info_frm, bg=dc, padx=10, pady=2)
        diff_badge.pack(anchor=tk.W, pady=(4, 0))
        tk.Label(diff_badge, text=diff, font=("Segoe UI", 9, "bold"),
                 bg=dc, fg="white").pack()

        tk.Frame(info_frm, height=1, bg="#e0e0e0").pack(fill=tk.X, pady=(10, 6))

        timer_frm = tk.Frame(info_frm, bg=GRID_BG)
        timer_frm.pack(anchor=tk.W)
        tk.Label(timer_frm, text="\u23f1", font=("Segoe UI", 13),
                 bg=GRID_BG, fg="#aaa").pack(side=tk.LEFT)
        self.timer_label = tk.Label(timer_frm, text="00:00",
                                    font=("Segoe UI", 13, "bold"),
                                    bg=GRID_BG, fg="#555")
        self.timer_label.pack(side=tk.LEFT, padx=(4, 0))

        self.error_label = tk.Label(info_frm, font=("Segoe UI", 11, "bold"), bg=GRID_BG)
        self.error_label.pack(anchor=tk.W, pady=(6, 0))

        tk.Frame(info_frm, height=1, bg="#e0e0e0").pack(fill=tk.X, pady=(10, 6))

        tk.Label(info_frm, text="Осталось:", font=("Segoe UI", 9),
                 bg=GRID_BG, fg="#999").pack(anchor=tk.W)
        grid_frm = tk.Frame(info_frm, bg=GRID_BG)
        grid_frm.pack(pady=(4, 0))
        self._remaining_labels = []
        for i in range(3):
            for j in range(3):
                n = i * 3 + j + 1
                lbl = tk.Label(grid_frm, text=str(n),
                               font=("Segoe UI", 11, "bold"),
                               width=2, relief=tk.FLAT,
                               bg=GRID_BG, fg="#555")
                lbl.grid(row=i, column=j, padx=3, pady=2)
                self._remaining_labels.append(lbl)

        tk.Frame(info_frm, height=1, bg="#e0e0e0").pack(fill=tk.X, pady=(10, 6))

        self._btn_frm = tk.Frame(info_frm, bg=GRID_BG)
        self._btn_frm.pack(anchor=tk.W)
        self._make_btn(self._btn_frm, "\u25c0 Отменить", self._undo,
                       bg="#e0e0e0", fg="#333",
                       activebackground="#bdbdbd",
                       activeforeground="#333").pack(fill=tk.X, pady=2)
        self._make_btn(self._btn_frm, "\u25b6 Повторить", self._redo,
                       bg="#e0e0e0", fg="#333",
                       activebackground="#bdbdbd",
                       activeforeground="#333").pack(fill=tk.X, pady=2)
        self._make_btn(self._btn_frm, "\u21e6 К выбору уровней", self.show_menu,
                       bg="#1565c0", fg="white",
                       activebackground="#0d47a1",
                       activeforeground="white").pack(fill=tk.X, pady=2)

        self._hover_cell = None

        if self._game_over_frm:
            self._game_over_frm.destroy()
            self._game_over_frm = None

        self._update_error_display()
        self._draw()
        self._start_timer()

    # ── timer ──

    def _start_timer(self):
        self.start_time = time.time()
        self.elapsed = 0
        self.timer_running = True
        self._update_timer()

    def _stop_timer(self):
        self.timer_running = False

    def _update_timer(self):
        if not self.timer_running:
            return
        self.elapsed = time.time() - self.start_time
        self.timer_label.config(text=_fmt_time(self.elapsed))
        self.root.after(1000, self._update_timer)

    # ── hotkeys ──

    def _bind_hotkeys(self):
        self.root.bind_all("<Control-z>", self._undo)
        self.root.bind_all("<Control-y>", self._redo)
        self.root.bind_all("<Control-Z>", self._undo)
        self.root.bind_all("<Control-Y>", self._redo)
        self.root.bind("<Escape>", lambda e: self._hide_panel())

    # ── panel ──

    def _show_panel(self, event, mode):
        if self.won or self.game_over:
            return
        self.mode = mode
        self._hide_panel()

        is_mark = mode == "mark"

        if is_mark:
            bg_color = PANEL_MARK_BG
            fg_color = PANEL_MARK_FG
            hover_bg = PANEL_MARK_HOVER
            active_bg = PANEL_MARK_ACTIVE
            border_color = PANEL_MARK_BORDER
        else:
            bg_color = PANEL_SET_BG
            fg_color = PANEL_SET_FG
            hover_bg = PANEL_SET_HOVER
            active_bg = PANEL_SET_ACTIVE
            border_color = PANEL_SET_BORDER

        p = tk.Toplevel(self.root)
        p.overrideredirect(True)
        p.attributes("-topmost", True)
        x, y = event.x_root, event.y_root - 160
        if y < 0:
            y = event.y_root + 20
        p.geometry(f"+{x}+{y}")

        f = tk.Frame(p, bg=border_color, relief=tk.SOLID, bd=0, highlightthickness=2, highlightbackground=border_color)
        f.pack()

        for i in range(3):
            for j in range(3):
                n = i * 3 + j + 1
                is_blocked = not is_mark and n in self.completed_numbers
                btn_fg = DISABLED_FG if is_blocked else fg_color
                btn_state = tk.DISABLED if is_blocked else tk.NORMAL

                btn = tk.Button(
                    f, text=str(n), image=self._panel_pixel, compound=tk.CENTER,
                    width=44, height=44,
                    font=("Segoe UI", 15, "bold"),
                    relief=tk.FLAT, bd=0,
                    bg=bg_color, fg=btn_fg,
                    activebackground=active_bg, activeforeground=fg_color,
                    cursor="hand2" if not is_blocked else "arrow",
                    state=btn_state,
                    command=lambda v=n: self._pick(v),
                )
                btn.grid(row=i, column=j, padx=1, pady=1)

                if not is_blocked:
                    btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=hover_bg))
                    btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=bg_color))
                    btn.bind("<ButtonPress-1>", lambda e, b=btn, cb=active_bg: b.configure(bg=cb))
                    btn.bind("<ButtonRelease-1>", lambda e, b=btn, cb=bg_color: b.configure(bg=cb))

        if not is_mark:
            sep_line = tk.Frame(f, height=1, bg="#e0e0e0")
            sep_line.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(4, 2))
            clear_btn = tk.Button(
                f, text="\u2715", image=self._panel_pixel, compound=tk.CENTER,
                width=44, height=32,
                font=("Segoe UI", 11, "bold"),
                relief=tk.FLAT, bd=0,
                bg="#fff", fg="#c62828",
                activebackground="#ffebee", activeforeground="#b71c1c",
                cursor="hand2",
                command=lambda: self._clear_cell(),
            )
            clear_btn.grid(row=4, column=0, columnspan=3, pady=(0, 1))

        self._panel_gen += 1
        gen = self._panel_gen
        p.bind("<FocusOut>", lambda e: self._on_panel_focus_out(gen))
        p.bind("<Escape>", lambda e: self._maybe_close_panel(gen))
        p.focus_force()
        self.panel = p

    def _on_panel_focus_out(self, gen):
        self.root.after_idle(lambda g=gen: self._maybe_close_panel(g))

    def _maybe_close_panel(self, gen):
        if gen != self._panel_gen or not self.panel:
            return
        self.selected = None
        self._hide_panel()
        self._draw()

    def _hide_panel(self):
        if self.panel:
            self.panel.destroy()
            self.panel = None

    # ── actions ──

    def _pick(self, num):
        if self.selected is None or self.won or self.game_over:
            self._hide_panel()
            return
        r, c = self.selected
        if self.original[r][c] != 0:
            self._hide_panel()
            return

        if self.mode == "set":
            old = self.board[r][c]
            if old == num:
                num = 0
            if old != num:
                old_was_wrong = old != 0 and old != self.solved[r][c]
                new_is_wrong = num != 0 and num != self.solved[r][c]
                caused_error = new_is_wrong and not old_was_wrong
                if caused_error:
                    self.errors_made += 1
                self._push_undo(("set", r, c, old, num, caused_error))
                self.board[r][c] = num
                self._clear_pencil_cell(r, c)
        else:
            pm = (r, c, num)
            if pm in self.pencil:
                self.pencil.discard(pm)
                self._push_undo(("unmark", r, c, num))
            else:
                self.pencil.add(pm)
                self._push_undo(("mark", r, c, num))

        self._hide_panel()
        self._sync()

    def _clear_cell(self):
        if self.selected is None or self.won or self.game_over:
            self._hide_panel()
            return
        r, c = self.selected
        if self.original[r][c] != 0:
            self._hide_panel()
            return
        old = self.board[r][c]
        if old != 0:
            self._push_undo(("set", r, c, old, 0, False))
            self.board[r][c] = 0
            self._clear_pencil_cell(r, c)
        self._hide_panel()
        self._sync()

    def _push_undo(self, action):
        self.undo_st.append(action)
        if len(self.undo_st) > 3:
            self.undo_st.pop(0)
        self.redo_st.clear()

    def _clear_pencil_cell(self, r, c):
        to_rm = [p for p in self.pencil if p[0] == r and p[1] == c]
        for p in to_rm:
            self.pencil.discard(p)

    # ── undo / redo ──

    def _undo(self, event=None):
        if self.cv is None or self.won or self.game_over or not self.undo_st:
            return
        self._hide_panel()
        a = self.undo_st.pop()
        self.redo_st.append(a)
        t = a[0]
        if t == "set":
            _, r, c, old, _, caused_error = a
            self.board[r][c] = old
            if caused_error:
                self.errors_made = max(0, self.errors_made - 1)
        elif t == "mark":
            _, r, c, n = a
            self.pencil.discard((r, c, n))
        elif t == "unmark":
            _, r, c, n = a
            self.pencil.add((r, c, n))
        self._sync()

    def _redo(self, event=None):
        if self.cv is None or self.won or self.game_over or not self.redo_st:
            return
        self._hide_panel()
        a = self.redo_st.pop()
        self.undo_st.append(a)
        t = a[0]
        if t == "set":
            _, r, c, _, new, caused_error = a
            self.board[r][c] = new
            if caused_error:
                self.errors_made += 1
        elif t == "mark":
            _, r, c, n = a
            self.pencil.add((r, c, n))
        elif t == "unmark":
            _, r, c, n = a
            self.pencil.discard((r, c, n))
        self._sync()

    # ── highlighting logic ──

    def _check_regions(self):
        self.completed.clear()
        for r in range(9):
            if all(self.board[r][c] != 0 for c in range(9)):
                if sorted(self.board[r]) == list(range(1, 10)):
                    self.completed.add(("r", r))
        for c in range(9):
            col = [self.board[r][c] for r in range(9)]
            if all(v != 0 for v in col):
                if sorted(col) == list(range(1, 10)):
                    self.completed.add(("c", c))
        for br in range(3):
            for bc in range(3):
                vals = []
                for i in range(3):
                    for j in range(3):
                        vals.append(self.board[br * 3 + i][bc * 3 + j])
                if all(v != 0 for v in vals):
                    if sorted(vals) == list(range(1, 10)):
                        self.completed.add(("b", br * 3 + bc))

    def _cell_in_completed(self, r, c):
        if ("r", r) in self.completed:
            return True
        if ("c", c) in self.completed:
            return True
        if ("b", 3 * (r // 3) + c // 3) in self.completed:
            return True
        return False

    # ── completed numbers, errors ──

    def _check_completed_numbers(self):
        counts = {i: 0 for i in range(1, 10)}
        for r in range(9):
            for c in range(9):
                v = self.board[r][c]
                if v != 0 and v == self.solved[r][c]:
                    counts[v] += 1
        self.completed_numbers = {n for n, cnt in counts.items() if cnt == 9}

    def _update_error_display(self):
        if not self.error_label or self.cv is None:
            return
        remaining = self.error_limit - self.errors_made
        if remaining <= 0:
            color = "#c62828"
        elif remaining <= 2:
            color = "#e65100"
        else:
            color = "#2e7d32"
        self.error_label.config(
            text=f"Ошибки: {self.errors_made}/{self.error_limit}",
            fg=color,
        )

    def _update_remaining_display(self):
        if not self._remaining_labels:
            return
        for n in range(1, 10):
            done = n in self.completed_numbers
            self._remaining_labels[n - 1].config(
                fg=BG_COMPLETE if done else "#555",
                text=f"{n}" if not done else f"{n}\u2713",
            )

    def _check_game_over(self):
        if self.game_over:
            return
        if self.errors_made >= self.error_limit:
            self.game_over = True
            self.won = True
            self._stop_timer()
            self._draw_game_over()
            self._show_game_over_buttons()

    def _round_rect(self, x1, y1, x2, y2, r=20, **kwargs):
        points = [
            x1 + r, y1,  x2 - r, y1,
            x2, y1,  x2, y1 + r,
            x2, y2 - r,  x2, y2,  x2 - r, y2,
            x1 + r, y2,  x1, y2,  x1, y2 - r,
            x1, y1 + r,  x1, y1,  x1 + r, y1,
        ]
        return self.cv.create_polygon(points, smooth=True, **kwargs)

    def _draw_game_over(self):
        cw = GRID + 2
        cx = cw // 2
        self.cv.create_rectangle(0, 0, cw, cw, fill="#ffebee", stipple="gray25", outline="")
        self._round_rect(cx - 210, cx - 70, cx + 210, cx + 70, r=22,
                         fill="#000", stipple="gray50", width=0)
        self._round_rect(cx - 210, cx - 70, cx + 210, cx + 70, r=22,
                         fill="#c62828", outline="#ef5350", width=2)
        self.cv.create_line(cx - 130, cx + 5, cx + 130, cx + 5,
                            fill="white", width=1)
        self.cv.create_text(
            cx, cx - 30,
            text="\u2718 \u0418\u0413\u0420\u0410 \u041e\u041a\u041e\u041d\u0427\u0415\u041d\u0410",
            font=("Segoe UI", 28, "bold"), fill="white",
        )
        self.cv.create_text(
            cx, cx + 35,
            text=f"\u041e\u0448\u0438\u0431\u043a\u0438: {self.errors_made}/{self.error_limit} \u2022 "
                 f"\u0412\u0440\u0435\u043c\u044f: {_fmt_time(self.elapsed)}",
            font=("Segoe UI", 15), fill="white",
        )

    def _show_game_over_buttons(self):
        if self._btn_frm:
            self._btn_frm.pack_forget()
        if self._game_over_frm:
            self._game_over_frm.destroy()

        frm = tk.Frame(self._info_frm, bg=GRID_BG)
        frm.pack(anchor=tk.W)
        self._game_over_frm = frm

        self._make_btn(frm, "\u21bb \u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c \u0443\u0440\u043e\u0432\u0435\u043d\u044c",
                       lambda: self.start_game(self.puzzle_idx),
                       bg="#e65100", fg="white",
                       activebackground="#bf360c", activeforeground="white").pack(side=tk.LEFT, padx=3)
        self._make_btn(frm, "\u2630 \u0412 \u043c\u0435\u043d\u044e \u0443\u0440\u043e\u0432\u043d\u0435\u0439",
                       self.show_menu,
                       bg="#1565c0", fg="white",
                       activebackground="#0d47a1", activeforeground="white").pack(side=tk.LEFT, padx=3)

    # ── draw ──

    def _sync(self):
        self._check_regions()
        self._check_completed_numbers()
        self._update_error_display()
        self._update_remaining_display()
        self._draw()
        if not self.game_over:
            self._check_win()
        self._check_game_over()

    def _draw(self):
        self.cv.delete("all")
        self.cv.configure(bg=BG_EMPTY)

        for r in range(9):
            for c in range(9):
                x1, y1 = c * CELL, r * CELL
                x2, y2 = x1 + CELL, y1 + CELL

                val = self.board[r][c]
                is_given = self.original[r][c] != 0
                is_wrong = not is_given and val != 0 and val != self.solved[r][c]
                is_correct = val != 0 and val == self.solved[r][c]
                is_selected = self.selected == (r, c)
                in_completed = self._cell_in_completed(r, c)
                num_completed = val != 0 and val in self.completed_numbers and is_correct

                if is_selected:
                    bg = BG_SELECTED
                elif num_completed or (in_completed and is_correct):
                    bg = BG_COMPLETE
                elif is_wrong:
                    bg = BG_WRONG
                elif is_given:
                    bg = BG_GIVEN
                else:
                    bg = BG_EMPTY

                self.cv.create_rectangle(x1, y1, x2, y2, fill=bg, outline="", width=0)

                if val != 0:
                    if is_given:
                        fc = FG_GIVEN
                        fw = "bold"
                    elif val == self.solved[r][c]:
                        fc = FG_CORRECT
                        fw = "bold"
                    else:
                        fc = FG_WRONG
                        fw = "bold"
                    self.cv.create_text(
                        x1 + CELL // 2, y1 + CELL // 2,
                        text=str(val), font=("Segoe UI", 17, fw), fill=fc,
                    )
                else:
                    marks = sorted(n for (rr, cc, n) in self.pencil if rr == r and cc == c)
                    if marks:
                        pos = {
                            1: (1, 1), 2: (3, 1), 3: (5, 1),
                            4: (1, 3), 5: (3, 3), 6: (5, 3),
                            7: (1, 5), 8: (3, 5), 9: (5, 5),
                        }
                        for m in marks:
                            px, py = pos[m]
                            self.cv.create_text(
                                x1 + OFF * px, y1 + OFF * py,
                                text=str(m), font=("Segoe UI", 8), fill=FG_PENCIL,
                            )

        for i in range(10):
            w = 2 if i % 3 == 0 else 1
            c = GRID_THICK if i % 3 == 0 else GRID_THIN
            offset = 0.5
            end = GRID + 0.5 if i in (0, 9) else GRID
            self.cv.create_line(
                offset + i * CELL, 0, offset + i * CELL, end,
                width=w, fill=c,
            )
            self.cv.create_line(
                0, offset + i * CELL, end, offset + i * CELL,
                width=w, fill=c,
            )

    def _is_correct_number(self, r, c):
        return self.board[r][c] != 0 and self.board[r][c] == self.solved[r][c]

    def _is_wrong_number(self, r, c):
        return self.board[r][c] != 0 and self.board[r][c] != self.solved[r][c]

    def _check_win(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != self.solved[r][c]:
                    return
        if self.won:
            return
        self.won = True
        self._stop_timer()

        idx = str(self.puzzle_idx + 1)
        best = self.stats[idx]["best_time"]
        best_err = self.stats[idx].get("best_errors")
        time_improved = best is None or self.elapsed < best
        errors_improved = best_err is None or self.errors_made < best_err
        if time_improved or errors_improved:
            if time_improved:
                self.stats[idx]["best_time"] = self.elapsed
            if errors_improved:
                self.stats[idx]["best_errors"] = self.errors_made
            self._save_stats()

        cw = GRID + 2
        cx = cw // 2
        if time_improved or errors_improved:
            card_h = 160
            rec_y = cx + 65
        else:
            card_h = 125
            rec_y = None
        self.cv.create_rectangle(0, 0, cw, cw, fill="#e8f5e9", stipple="gray25", outline="")
        self._round_rect(cx - 200, cx - card_h // 2, cx + 200, cx + card_h // 2, r=22,
                         fill="#000", stipple="gray50", width=0)
        self._round_rect(cx - 200, cx - card_h // 2, cx + 200, cx + card_h // 2, r=22,
                         fill="#2e7d32", outline="#66bb6a", width=2)
        self.cv.create_line(cx - 115, cx + 5, cx + 115, cx + 5,
                            fill="white", width=1)
        self.cv.create_text(
            cx, cx - 25,
            text="\u2714 \u041f\u041e\u0411\u0415\u0414\u0410!",
            font=("Segoe UI", 34, "bold"), fill="white",
        )
        self.cv.create_text(
            cx, cx + 35,
            text=f"\u0412\u0440\u0435\u043c\u044f: {_fmt_time(self.elapsed)}",
            font=("Segoe UI", 15), fill="white",
        )
        if rec_y is not None:
            self.cv.create_text(
                cx, rec_y,
                text="\u2605 \u041d\u043e\u0432\u044b\u0439 \u0440\u0435\u043a\u043e\u0440\u0434! \u2605",
                font=("Segoe UI", 15, "bold"), fill="white",
            )

    # ── events ──

    def _on_hover(self, event):
        r, c = event.y // CELL, event.x // CELL
        if 0 <= r < 9 and 0 <= c < 9:
            self._hover_cell = (r, c)
        else:
            self._hover_cell = None

    def _on_any_click(self, event):
        if not self.panel:
            return
        if event.widget == self.cv:
            return
        w = event.widget
        while w:
            if w is self.panel:
                return
            try:
                w = w.master
            except:
                break
        self.selected = None
        self._hide_panel()
        self._draw()

    def _on_left(self, event):
        r, c = event.y // CELL, event.x // CELL
        if not (0 <= r < 9 and 0 <= c < 9) or self.won or self.game_over:
            return

        is_empty = self.board[r][c] == 0
        is_wrong = not is_empty and self.board[r][c] != self.solved[r][c]
        can_open = is_empty or is_wrong

        if self.selected == (r, c):
            self.selected = None
            self._hide_panel()
            self._draw()
            return

        if self.selected is not None:
            self.selected = None
            self._hide_panel()
            self._draw()

        if not can_open:
            return

        self.selected = (r, c)
        self._show_panel(event, "set")

    def _on_right(self, event):
        r, c = event.y // CELL, event.x // CELL
        if not (0 <= r < 9 and 0 <= c < 9) or self.won or self.game_over:
            return "break"

        is_empty = self.board[r][c] == 0
        is_wrong = not is_empty and self.board[r][c] != self.solved[r][c]
        can_open = is_empty or is_wrong

        if not can_open:
            return "break"

        if self.selected == (r, c) and self.panel and self.mode == "mark":
            self.selected = None
            self._hide_panel()
            self._draw()
            return "break"

        self.selected = (r, c)
        self._hide_panel()
        self._show_panel(event, "mark")
        return "break"


def main():
    root = tk.Tk()
    SudokuApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
