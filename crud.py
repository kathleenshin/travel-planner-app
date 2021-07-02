
"""CRUD operations."""

from model import User, Wishlist, Destination, Destination_type, Mention, connect_to_db, db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


def get_destinations():
    """Returns all destinations."""

    return Destination.query.all()


def create_user(email, password, first_name, last_name):
    """Create and return a new user."""

    user = User(email=email, password=password, first_name=first_name, last_name=last_name)

    db.session.add(user)
    db.session.commit()

    return user

def create_destination(destination_type, average_overall_rating, name, population, latitude, longitude, url):
    """Create a destination."""

    destination = Destination(destination_type=destination_type, average_overall_rating=average_overall_rating, name=name, population=population, latitude=latitude, longitude=longitude, url=url)
    
    db.session.add(destination)
    db.session.commit()
    
    return destination

def get_destination_by_id(destination_id):
    """Return destination with the destination's ID"""

    destination_id_q = Destination.query.get(destination_id)

    return destination_id_q

def get_destination_by_name(name):
    """Return search result for destination's name."""

    destination_name_q = Destination.query.filter(Destination.name == name).all()

    return destination_name_q

def get_user_by_id(user_id):
    """Return user profile"""

    #.filter() or .filter_by
    #REMEMBER it must end with .one(), .first() or .all()
    user_id_q = User.query.filter(User.user_id == user_id).first()

    return user_id_q

def get_user_by_email(email):
    """Return user if email exists; otherwise None"""

    return User.query.filter(User.email == email).first()