import os

def display_menu():
    print("\n=== Simple Note App ===")
    print("1. Xem ghi chú")
    print("2. Thêm ghi chú")
    print("3. Xóa ghi chú")
    print("4. Thoát")

def view_notes():
    if not os.path.exists("notes.txt"):
        print("\nChưa có ghi chú nào!")
        return
    with open("notes.txt", "r", encoding="utf-8") as file:
        notes = file.readlines()
    if notes:
        print("\n=== Danh sách ghi chú ===")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note.strip()}")
    else:
        print("\nChưa có ghi chú nào!")

def add_note():
    note = input("\nNhập nội dung ghi chú: ")
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")
    print("Ghi chú đã được thêm!")

def delete_notes():
    if os.path.exists("notes.txt"):
        os.remove("notes.txt")
        print("Tất cả ghi chú đã bị xóa!")
    else:
        print("Không có ghi chú nào để xóa!")

def main():
    while True:
        display_menu()
        choice = input("\nChọn một tùy chọn (1-4): ")
        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()