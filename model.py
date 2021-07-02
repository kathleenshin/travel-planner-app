"""Models for travel planner app."""

from flask_sqlalchemy import SQLAlchemy # connection to PostgreSql database
# getting this from the Flask-SQLAlchemy helper library

db = SQLAlchemy() # instance of SQLAlchemy


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Wishlist(db.Model):
    """A wishlist."""

    __tablename__ = 'wishlists'

    wishlist_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)   
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.destination_id'))
    note = db.Column(db.String)

    user = db.relationship('User')
    destination = db.relationship('Destination')

    def __repr__(self):
        return f"<Wishlist wishlist_id={self.wishlist_id} note={self.note}>"

class Destination(db.Model):
    """A destination."""

    __tablename__ = 'destinations'

    destination_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    #destination_type_id = db.Column(db.Integer, db.ForeignKey('destination_types.destination_type_id'))
    destination_type = db.Column(db.String)
    average_overall_rating = db.Column(db.Integer)
    name = db.Column(db.String)
    population = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)
    url = db.Column(db.String)
    
    
    #destination_type = db.relationship('Destination_type')

    def __repr__(self):
        return f"<Destination destination_id={self.destination_id} name={self.name} destination_type={self.destination_type}>"

class Destination_type(db.Model):
    """A destination type."""

    __tablename__ = 'destination_types'

    destination_type_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    destination_type = db.Column(db.String) 
    
    def __repr__(self):
        return f"<Destination_type destination_type_id={self.destination_type_id} destination_type={self.destination_type}>"

class Mention(db.Model):
    """A mention."""

    __tablename__ = 'mentions'

    mention_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    title = db.Column(db.String)
    excerpt = db.Column(db.String)
    url = db.Column(db.String)
    source_name = db.Column(db.String) 
    source_domain = db.Column(db.String)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.destination_id'))
    
    destination = db.relationship('Destination')

    def __repr__(self):
        return f"<Mention mention_id={self.mention_id} title={self.title} url={self.url} destination_id={self.destination_id}>"
    
def connect_to_db(flask_app, db_uri='postgresql:///destinations', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)