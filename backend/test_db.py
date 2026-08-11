from app.database import SessionLocal
from app.models import User

db = SessionLocal()

new_user = User(email="test@example.com", hashed_password="placeholder")
db.add(new_user)
db.commit()
db.refresh(new_user)
print("Inserted:", new_user.id, new_user.email, new_user.created_at)

fetched = db.query(User).filter(User.email == "test@example.com").first()
print("Fetched:", fetched.id, fetched.email)

db.close()