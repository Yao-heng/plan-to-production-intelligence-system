"""Unit tests for the file_loader service.

PROJECT_ROOT is monkeypatched to a tmp directory so the tests exercise
the real read/write helpers without touching the repository tree.
"""

from pathlib import Path

import pytest

from app.services import file_loader


@pytest.fixture
def project_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(file_loader, "PROJECT_ROOT", tmp_path)
    return tmp_path


def test_write_text_creates_parent_dirs_and_roundtrips(project_root: Path) -> None:
    path = file_loader.write_text("inputs/nested/note.md", "hello")

    assert path == project_root / "inputs" / "nested" / "note.md"
    assert path.read_text(encoding="utf-8") == "hello"
    assert file_loader.read_text("inputs/nested/note.md") == "hello"


def test_write_json_roundtrips_structured_data(project_root: Path) -> None:
    payload = {"requirements": [{"id": "BIOS-REQ-1", "teams": ["BIOS", "BMC"]}], "count": 1}

    path = file_loader.write_json("outputs/data.json", payload)

    assert file_loader.read_json("outputs/data.json") == payload
    # Written as pretty-printed JSON (indent=2), not a single line.
    assert "\n  " in path.read_text(encoding="utf-8")


def test_read_text_missing_file_raises(project_root: Path) -> None:
    with pytest.raises(FileNotFoundError):
        file_loader.read_text("inputs/does-not-exist.md")
