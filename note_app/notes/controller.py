from notes.note import Note
from notes.view import View
from notes.notes_manager import NotesManager

class Controller:
    """
    Controls the interaction between the user, notes, and the data manager.
    """
    def __init__(self):
        """
        Initialize a new Controller object.
        """
        self.notes_manager = NotesManager('notes.json')

    def list_notes(self):
        """
        Display a sorted list of notes to the user.
        """
        sort_choice = input("Sort by (1) Creation Date or (2) Last Modified Date? ")
        if sort_choice == '1':
            notes = sorted(self.notes_manager.notes, key=lambda note: note.created_at)
        elif sort_choice == '2':
            notes = sorted(self.notes_manager.notes, key=lambda note: note.last_modified)
        else:
            print("Invalid sort choice. Please choose 1 or 2.")
            return
        View.display_notes(notes)
    
    def add_note(self):
        """
        Add a new note to the collection.
        """
        title = input("Enter title: ")
        body = input("Enter body: ")
        new_note = Note(len(self.notes_manager.notes) + 1, title, body)
        self.notes_manager.notes.append(new_note)
        print("Note added successfully.")

    def edit_note(self, note_id, title, body):
        """
        Edit an existing note by updating its title and body.
        
        :param note_id: ID of the note to be edited.
        :param title: New title for the note.
        :param body: New body content for the note.
        """
        for note in self.notes_manager.notes:
            if note.note_id == note_id:
                note.update(title, body)
                print("Note edited successfully.")
                break
        else:
            print("Note not found.")

    def delete_note(self, note_id):
        """
        Delete a note from the collection by its ID.
        
        :param note_id: ID of the note to be deleted.
        """
        for note in self.notes_manager.notes:
            if note.note_id == note_id:
                self.notes_manager.notes.remove(note)
                print("Note deleted successfully.")
                break
        else:
            print("Note not found.")

    def search_notes(self, search_char):
        """
        Search and display notes containing the search character in title or body.
        
        :param search_char: Character to search for in notes.
        """
        matching_notes = []
        for note in self.notes_manager.notes:
            if search_char in note.title or search_char in note.body:
                matching_notes.append(note)

        if matching_notes:
            View.display_notes(matching_notes)
        else:
            print("No matching notes found.")

    def save_and_exit(self):
        """
        Save notes and exit the application.
        """
        self.notes_manager.save_notes()