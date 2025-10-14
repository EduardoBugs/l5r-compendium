"""
Enhanced CLI logger with colors, emojis, and visual stage grouping.
"""

import sys
from datetime import datetime
from typing import Optional


class Log:
    COLORS = {
        "reset": "\033[0m",
        "gray": "\033[90m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "bold": "\033[1m",
    }

    def _timestamp(self) -> str:
        """Return a formatted timestamp for each log entry."""
        return datetime.now().strftime("%H:%M:%S")

    def _print(self, icon: str, color: str, label: str, message: str, *, stream=sys.stdout) -> None:
        """Generic print formatter with timestamp and color."""
        c = self.COLORS
        formatted = f"{c['gray']}[{self._timestamp()}]{c['reset']} {color}{icon} [{label}] {c['reset']}{message}"
        print(formatted, file=stream)

    # --- Stage grouping ---

    def stage(self, message: str, icon: Optional[str] = "🧩") -> None:
        """Print a visual group header (no timestamp)."""
        c = self.COLORS
        print(f"{c['blue']}── {icon} {message}{c['reset']}")

    def stage_end(self) -> None:
        """Print a separator line to visually close a stage."""
        c = self.COLORS
        print(f"{c['gray']}────────────────────────────────────────────{c['reset']}")

    # --- Standard log levels ---

    def info(self, message: str) -> None:
        self._print("ℹ️", self.COLORS["cyan"], "INFO", message)

    def success(self, message: str) -> None:
        self._print("✅", self.COLORS["green"], "OK", message)

    def warning(self, message: str) -> None:
        self._print("⚠️", self.COLORS["yellow"], "WARN", message)

    def error(self, message: str) -> None:
        self._print("❌", self.COLORS["red"], "ERROR", message, stream=sys.stderr)

    def debug(self, message: str) -> None:
        self._print("🐛", self.COLORS["magenta"], "DEBUG", message)


# Global instance
log = Log()
