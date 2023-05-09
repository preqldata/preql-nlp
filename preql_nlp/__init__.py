from .monkeypatch import patch_promptimize

patch_promptimize()

from .main import build_query  # noqa: E402
from .client import NlpPreqlModelClient


__version__ = "0.0.5"

__all__ = ["build_query", "NlpPreqlModelClient"]
