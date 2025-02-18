class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code, title, text, importance, creation_date):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: str = creation_date
        self.tags: list[str] = []

    def add_tag(self):
        pass

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str, importance: str):
        code = len(self.notes) + 1
        new_note = Note(code, title, text, importance)
        self.notes.append(new_note)
        return code
    def delete_note(self, code: int):
      self.notes = [note for note in self.notes if note.code != code]

    def importance_note(self):
     return [note for note in self.notes if note.importance in [Note.HIGH, Note.MEDIUM]]

    def notes_by_tag(self, tag: str):
     return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self):
      tag_counts = {}
      for note in self.notes:
        for tag in note.tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
      if tag_counts:
        max_tag = min(tag_counts, key=lambda k: (-tag_counts[k], k))
        return max_tag
      return ""