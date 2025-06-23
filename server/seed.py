from server.config import db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User
from server.app import app

with app.app_context():
    print("🌱 Seeding database...")

    # Clear old data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    # Users
    user1 = User(username="admin")
    user1.set_password("admin123")

    # Guests
    guest1 = Guest(name="Robert Downey Jr.", occupation="Actor")
    guest2 = Guest(name="Bill Nye", occupation="Science Guy")
    guest3 = Guest(name="Taylor Swift", occupation="Musician")

    # Episodes
    episode1 = Episode(date="2024-06-01", number=1)
    episode2 = Episode(date="2024-06-02", number=2)

    # Appearances
    a1 = Appearance(rating=5, guest=guest1, episode=episode1)
    a2 = Appearance(rating=4, guest=guest2, episode=episode1)
    a3 = Appearance(rating=5, guest=guest3, episode=episode2)

    # Add and commit
    db.session.add_all([user1, guest1, guest2, guest3, episode1, episode2, a1, a2, a3])
    db.session.commit()

    print("✅ Done seeding!")
