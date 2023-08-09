from notes.controller import Controller

def main():
    """
    Main function that runs the note application.
    """
    controller = Controller()

    while True:
        print("\nNote Application Menu:")
        print("1. List Notes")
        print("2. Add Note")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Search Notes")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            controller.list_notes()
        elif choice == '2':
            controller.add_note()
        elif choice == '3':
            note_id = int(input("Enter note ID to edit: "))
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            controller.edit_note(note_id, title, body)
        elif choice == '4':
            note_id = int(input("Enter note ID to delete: "))
            controller.delete_note(note_id)
        elif choice == '5':
            search_char = input("Enter search character: ")
            controller.search_notes(search_char)
        elif choice == '6':
            controller.save_and_exit()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()