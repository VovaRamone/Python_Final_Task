from datetime import datetime

class Note:
    """
    Represents a note with its properties and methods.
    """
    def __init__(self, note_id, title, body):
        """
        Initialize a new Note object.
        
        :param note_id: Unique identifier for the note.
        :param title: Title of the note.
        :param body: Body content of the note.
        """
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.last_modified = datetime.now()

    def update(self, title, body):
        """
        Update the note's title, body, and last_modified timestamp.
        
        :param title: New title for the note.
        :param body: New body content for the note.
        """
        self.title = title
        self.body = body
        self.last_modified = datetime.now()
