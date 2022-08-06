from app.models import dashboard
from app.models.storage import schema

def start_db():
    dashboard.start_db()

if __name__ == '__main__':
    schema.create_schema()
    start_db()
