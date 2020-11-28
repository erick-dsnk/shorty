from .extensions import db
from datetime import datetime
import string
from random import choices

class Link(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    original_url = db.Column(
        db.String(512)
    )

    short_url = db.Column(
        db.String(6), unique=True
    )

    visits = db.Column(
        db.Integer,
        default=0
    )

    date_created = db.Column(
        db.DateTime,
        default=datetime.now
    )

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.short_url = self.gen_short_link()
    
    def gen_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=6))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.gen_short_link()
        
        return short_url