import os
from app import add_note, delete_notes

def test_add_note():
    note_content = "Ghi chú kiểm thử"
    if os.path.exists("notes.txt"):
        os.remove("notes.txt")
    add_note(note_content)
    with open("notes.txt", "r", encoding="utf-8") as file:
        notes = file.readlines()
    assert len(notes) == 1
    assert notes[0].strip() == note_content

def test_delete_notes():
    with open("notes.txt", "w", encoding="utf-8") as file:
        file.write("Test ghi chú\n")
    delete_notes()
    assert not os.path.exists("notes.txt")
from app import add_note, delete_notes
from unittest.mock import patch

def test_add_note():
    note_content = "Ghi chú kiểm thử"
    if os.path.exists("notes.txt"):
        os.remove("notes.txt")
    
    with patch("builtins.input", return_value=note_content):
        add_note()  # Gọi hàm không có tham số

    with open("notes.txt", "r", encoding="utf-8") as file:
        notes = file.readlines()
    assert len(notes) == 1
    assert notes[0].strip() == note_content
