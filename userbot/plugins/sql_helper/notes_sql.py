from sqlalchemy import Column, UnicodeText, LargeBinary, Numeric
from userbot.plugins.sql_helper import SESSION, BASE


class notes(BASE):
    __tablename__ = "notes"
    note = Column(UnicodeText, primary_key=True)
    reply = Column(UnicodeText)
    note_type = Column(Numeric)
    media_id = Column(UnicodeText)
    media_access_hash = Column(UnicodeText)
    media_file_reference = Column(LargeBinary)

    def __init__(
        self,
        note, reply, note_type,
        media_id=None, media_access_hash=None, media_file_reference=None
    ):
        self.note = note
        self.reply = reply
        self.note_type = note_type
        self.media_id = media_id
        self.media_access_hash = media_access_hash
        self.media_file_reference = media_file_reference


notes.__table__.create(checkfirst=True)


def get_notes(keyword):
    try:
        return SESSION.query(notes).get(keyword)
    except:
        return None
    finally:
        SESSION.close()


def get_all_notes():
    try:
        return SESSION.query(notes).all()
    except:
        return None
    finally:
        SESSION.close()


def add_note(keyword, reply, note_type, media_id, media_access_hash, media_file_reference):
    adder = SESSION.query(notes).get(keyword)
    if adder:
        adder.reply = reply
        adder.note_type = note_type
        adder.media_id = media_id
        adder.media_access_hash = media_access_hash
        adder.media_file_reference = media_file_reference
    else:
        adder = notes(keyword, reply, note_type, media_id,
                      media_access_hash, media_file_reference)
    SESSION.add(adder)
    SESSION.commit()


def remove_note(keyword):
    note = SESSION.query(notes).filter(notes.note == keyword)
    if note:
        note.delete()
        SESSION.commit()
