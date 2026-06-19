"""
Atmosphere Weather App - Single File Python
Uses OpenWeatherMap API (free tier)
Get your API key at: https://openweathermap.org/api
"""

import tkinter as tk
from tkinter import font as tkfont
import threading
import urllib.request
import urllib.parse
import json
import os

# ─── CONFIG ───────────────────────────────────────────────────────────────────
API_KEY = "953fc99364841748413fed72314cd8f8"
# ──────────────────────────────────────────────────────────────────────────────

CONDITION_COLORS = {
    "thunder":    {"bg": "#0d0d1a", "accent": "#7c3aed"},
    "rain":       {"bg": "#1e293b", "accent": "#3b82f6"},
    "snow":       {"bg": "#cbd5e1", "accent": "#94a3b8"},
    "fog":        {"bg": "#475569", "accent": "#94a3b8"},
    "clear":      {"bg": "#1e40af", "accent": "#06b6d4"},
    "clouds":     {"bg": "#334155", "accent": "#64748b"},
    "default":    {"bg": "#0f172a", "accent": "#6366f1"},
}

CONDITION_ICONS = {
    "thunder": "⛈",
    "rain":    "🌧",
    "drizzle": "🌦",
    "snow":    "❄️",
    "fog":     "🌫",
    "clear":   "☀️",
    "clouds":  "☁️",
    "default": "🌡",
}


def get_condition_key(code: int) -> str:
    if 200 <= code < 300: return "thunder"
    if 300 <= code < 400: return "drizzle"
    if 400 <= code < 600: return "rain"
    if 600 <= code < 700: return "snow"
    if 700 <= code < 800: return "fog"
    if code == 800:       return "clear"
    if code > 800:        return "clouds"
    return "default"


def fetch_weather(city: str, api_key: str) -> dict:
    """Fetch weather from OpenWeatherMap. Returns dict or raises Exception."""
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={urllib.parse.quote(city)}&appid={api_key}&units=metric"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "AtmosphereApp/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())

    wi = data["weather"][0]
    return {
        "city":        data["name"],
        "country":     data["sys"]["country"],
        "temp":        data["main"]["temp"],
        "feels_like":  data["main"]["feels_like"],
        "humidity":    data["main"]["humidity"],
        "pressure":    data["main"]["pressure"],
        "wind_speed":  data["wind"]["speed"],
        "description": wi["description"].capitalize(),
        "condition_code": wi["id"],
    }


class AtmosphereApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Atmosphere")
        self.geometry("420x640")
        self.resizable(False, False)
        self.configure(bg="#0f172a")

        # fonts
        self.f_title    = tkfont.Font(family="Segoe UI", size=26, weight="bold")
        self.f_sub      = tkfont.Font(family="Segoe UI", size=11)
        self.f_city     = tkfont.Font(family="Segoe UI", size=20, weight="bold")
        self.f_desc     = tkfont.Font(family="Segoe UI", size=12)
        self.f_icon     = tkfont.Font(family="Segoe UI Emoji", size=52)
        self.f_temp     = tkfont.Font(family="Segoe UI", size=64, weight="normal")
        self.f_feels    = tkfont.Font(family="Segoe UI", size=11)
        self.f_stat_val = tkfont.Font(family="Segoe UI", size=13, weight="bold")
        self.f_stat_lbl = tkfont.Font(family="Segoe UI", size=9)
        self.f_entry    = tkfont.Font(family="Segoe UI", size=13)
        self.f_btn      = tkfont.Font(family="Segoe UI", size=12, weight="bold")

        self._build_ui()
        self._set_theme("default")

    # ── UI BUILD ──────────────────────────────────────────────────────────────

    def _build_ui(self):
        pad = dict(padx=24, pady=0)

        # ── header ──
        tk.Label(self, text="Atmosphere", font=self.f_title,
                 fg="#ffffff", bg="#0f172a").pack(pady=(32, 2))
        tk.Label(self, text="How's the sky today?", font=self.f_sub,
                 fg="#94a3b8", bg="#0f172a").pack(pady=(0, 20))

        # ── search row ──
        search_frame = tk.Frame(self, bg="#1e293b", bd=0,
                                highlightthickness=1,
                                highlightbackground="#334155")
        search_frame.pack(fill="x", padx=24, pady=(0, 24))
        search_frame.pack_propagate(False)
        search_frame.configure(height=48)

        self.entry = tk.Entry(search_frame, font=self.f_entry,
                              fg="#f1f5f9", bg="#1e293b",
                              insertbackground="#f1f5f9",
                              relief="flat", bd=8,
                              highlightthickness=0)
        self.entry.insert(0, "Search for a city…")
        self.entry.config(fg="#64748b")
        self.entry.bind("<FocusIn>",  self._on_entry_focus_in)
        self.entry.bind("<FocusOut>", self._on_entry_focus_out)
        self.entry.bind("<Return>",   lambda e: self._search())
        self.entry.pack(side="left", fill="both", expand=True)

        self.btn = tk.Button(search_frame, text="Go", font=self.f_btn,
                             fg="#ffffff", bg="#6366f1",
                             relief="flat", bd=0, padx=16,
                             cursor="hand2", command=self._search,
                             activebackground="#4f46e5",
                             activeforeground="#ffffff")
        self.btn.pack(side="right", fill="y")

        # ── card ──
        self.card = tk.Frame(self, bg="#1e293b", bd=0,
                             highlightthickness=1,
                             highlightbackground="#334155")
        self.card.pack(fill="both", expand=True, padx=24, pady=(0, 28))

        # placeholder
        self._show_placeholder()

    # ── PLACEHOLDER / LOADING ─────────────────────────────────────────────────

    def _clear_card(self):
        for w in self.card.winfo_children():
            w.destroy()

    def _show_placeholder(self):
        self._clear_card()
        tk.Label(self.card, text="☁️", font=self.f_icon,
                 fg="#334155", bg="#1e293b").pack(expand=True)
        tk.Label(self.card, text="Enter a city to see\ncurrent conditions.",
                 font=self.f_desc, fg="#475569", bg="#1e293b",
                 justify="center").pack(pady=(0, 40))

    def _show_loading(self):
        self._clear_card()
        tk.Label(self.card, text="⏳", font=self.f_icon,
                 fg="#6366f1", bg="#1e293b").pack(expand=True)
        tk.Label(self.card, text="Reading the sky…",
                 font=self.f_desc, fg="#94a3b8", bg="#1e293b").pack(pady=(0, 40))

    def _show_error(self, city: str):
        self._clear_card()
        tk.Label(self.card, text="⚠️", font=self.f_icon,
                 fg="#ef4444", bg="#1e293b").pack(expand=True)
        tk.Label(self.card, text=f'Could not find "{city}".',
                 font=self.f_city, fg="#fca5a5", bg="#1e293b").pack()
        tk.Label(self.card, text="Check spelling and try again.",
                 font=self.f_desc, fg="#94a3b8", bg="#1e293b").pack(pady=(4, 40))

    def _show_no_key(self):
        self._clear_card()
        tk.Label(self.card, text="🔑", font=self.f_icon,
                 fg="#f59e0b", bg="#1e293b").pack(expand=True)
        tk.Label(self.card,
                 text="No API key found.\n\nSet OPENWEATHER_API_KEY\nenvironment variable,\nor paste it into the\nAPI_KEY variable at the\ntop of this script.",
                 font=self.f_desc, fg="#fbbf24", bg="#1e293b",
                 justify="center").pack(pady=(0, 40))

    # ── WEATHER CARD ──────────────────────────────────────────────────────────

    def _show_weather(self, w: dict):
        self._clear_card()
        ckey   = get_condition_key(w["condition_code"])
        colors = CONDITION_COLORS.get(ckey, CONDITION_COLORS["default"])
        icon   = CONDITION_ICONS.get(ckey, CONDITION_ICONS["default"])

        bg = "#1e293b"  # keep card bg consistent, change window bg

        # city / country
        tk.Label(self.card,
                 text=f"{w['city']}, {w['country']}",
                 font=self.f_city, fg="#f1f5f9", bg=bg).pack(pady=(20, 2))
        tk.Label(self.card,
                 text=w["description"],
                 font=self.f_desc, fg="#94a3b8", bg=bg).pack()

        # icon + temp
        tk.Label(self.card, text=icon, font=self.f_icon, bg=bg).pack(pady=(16, 0))
        tk.Label(self.card,
                 text=f"{round(w['temp'])}°C",
                 font=self.f_temp, fg="#ffffff", bg=bg).pack(pady=(0, 0))
        tk.Label(self.card,
                 text=f"Feels like {round(w['feels_like'])}°C",
                 font=self.f_feels, fg="#64748b", bg=bg).pack(pady=(0, 16))

        # divider
        tk.Frame(self.card, height=1, bg="#334155").pack(fill="x", padx=24, pady=(0, 16))

        # stats row
        stats_frame = tk.Frame(self.card, bg=bg)
        stats_frame.pack(fill="x", padx=24, pady=(0, 24))

        stats = [
            ("💨", f"{w['wind_speed']} m/s", "Wind"),
            ("💧", f"{w['humidity']}%",       "Humidity"),
            ("🌡", f"{w['pressure']} hPa",    "Pressure"),
        ]
        for i, (ico, val, lbl) in enumerate(stats):
            col = tk.Frame(stats_frame, bg=bg)
            col.grid(row=0, column=i, expand=True, sticky="nsew")
            stats_frame.columnconfigure(i, weight=1)

            tk.Label(col, text=ico, font=self.f_sub, bg=bg).pack()
            tk.Label(col, text=val, font=self.f_stat_val,
                     fg="#f1f5f9", bg=bg).pack()
            tk.Label(col, text=lbl, font=self.f_stat_lbl,
                     fg="#64748b", bg=bg).pack()

        self._set_theme(ckey)

    # ── THEMING ───────────────────────────────────────────────────────────────

    def _set_theme(self, ckey: str):
        colors = CONDITION_COLORS.get(ckey, CONDITION_COLORS["default"])
        self.configure(bg=colors["bg"])
        self.btn.configure(bg=colors["accent"], activebackground=colors["accent"])
        # update header labels bg
        for w in self.winfo_children():
            if isinstance(w, tk.Label):
                w.configure(bg=colors["bg"])

    # ── SEARCH ────────────────────────────────────────────────────────────────

    def _search(self):
        city = self.entry.get().strip()
        if not city or city == "Search for a city…":
            return
        if not API_KEY:
            self._show_no_key()
            return

        self._show_loading()
        self.update_idletasks()

        threading.Thread(target=self._fetch_thread, args=(city,), daemon=True).start()

    def _fetch_thread(self, city: str):
        try:
            data = fetch_weather(city, API_KEY)
            self.after(0, self._show_weather, data)
        except Exception:
            self.after(0, self._show_error, city)

    # ── ENTRY PLACEHOLDER HELPERS ─────────────────────────────────────────────

    def _on_entry_focus_in(self, _):
        if self.entry.get() == "Search for a city…":
            self.entry.delete(0, "end")
            self.entry.config(fg="#f1f5f9")

    def _on_entry_focus_out(self, _):
        if not self.entry.get().strip():
            self.entry.insert(0, "Search for a city…")
            self.entry.config(fg="#64748b")


if __name__ == "__main__":
    app = AtmosphereApp()
    app.mainloop()