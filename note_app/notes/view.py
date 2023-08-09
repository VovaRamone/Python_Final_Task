class View:
    """
    Displays notes and messages to the user.
    """
    @staticmethod
    def display_notes(notes):
        """
        Display a list of notes to the user.
        
        :param notes: List of Note objects to display.
        """
        for note in notes:
            print(f"ID: {note.note_id}, Title: {note.title}, Body: {note.body}, Created: {note.created_at}, Last Modified: {note.last_modified}")
