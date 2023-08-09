import json
import os
import logging
from datetime import datetime
from notes.note import Note

class NotesManager:
    """
    Manages the collection of notes and their interactions with a file.
    """
    def __init__(self, filename):
        """
        Initialize a new NotesManager object.
        
        :param filename: The name of the file to store notes.
        """
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        """
        Load notes from the file and populate the notes list.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                note_list = json.load(f)
                for note_data in note_list:
                    note = Note(note_data['note_id'], note_data['title'], note_data['body'])
                    note.created_at = datetime.strptime(note_data['created_at'], '%Y-%m-%d %H:%M:%S')
                    note.last_modified = datetime.strptime(note_data['last_modified'], '%Y-%m-%d %H:%M:%S')
                    self.notes.append(note)

    def save_notes(self):
        """
        Save notes to the file.
        """
        with open(self.filename, 'w') as f:
            note_list = [{'note_id': note.note_id, 'title': note.title, 'body': note.body,
                          'created_at': note.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                          'last_modified': note.last_modified.strftime('%Y-%m-%d %H:%M:%S')} for note in self.notes]
            json.dump(note_list, f, indent=4)

            logging.info("Notes saved successfully.")
