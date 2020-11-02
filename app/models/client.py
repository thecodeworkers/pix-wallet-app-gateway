from mongoengine import Document, StringField, BooleanField, DateTimeField
from datetime import datetime

class Client(Document):
    name = StringField(required=True, unique=True)
    app_name = StringField(required=True)
    active = BooleanField(required=True)
    key_expiration = DateTimeField(required=True)
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        return super(Client, self).save(*args, **kwargs)
    
    def update(self, **kwargs):
        kwargs['modified_date'] = datetime.now()
        return super(Client, self).update(**kwargs)
