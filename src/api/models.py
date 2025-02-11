from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return f"<User: {self.username}>"
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "password": self.password,
            "email": self.email,
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(15), nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(30), nullable=False)
    item_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Favorites: {self.item}>"
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "category": self.category,
            "category_id": self.category_id,
            "item": self.item,
            "item_id": self.item_id,
        }

class Starships(db.Model):
    __tablename__ = 'starships'
    uid = db.Column(db.Integer, db.ForeignKey('favorites.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('favorites.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    starship_class = db.Column(db.String(30), nullable=False)
    cost_in_credits = db.Column(db.String(30), nullable=False)
    crew = db.Column(db.String(30), nullable=False)
    hyperdrive_rating = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"<Starships: {self.name}>"
    
    def serialize(self):
        return {
            "uid": self.uid,
            "category_id": self.category_id,
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "hyperdrive_rating": self.hyperdrive_rating,
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    uid = db.Column(db.Integer, db.ForeignKey('favorites.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('favorites.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    diameter = db.Column(db.String(15), nullable=False)
    rotation_period = db.Column(db.String(15), nullable=False)
    orbital_period = db.Column(db.String(15), nullable=False)
    population = db.Column(db.String(20), nullable=False)
    climate = db.Column(db.String(15), nullable=False)
    terrain = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"<Planets: {self.name}>"
    
    def serialize(self):
        return {
            "uid": self.uid,
            "category_id": self.category_id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    uid = db.Column(db.Integer, db.ForeignKey('favorites.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('favorites.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    birth_year = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.uid'), nullable=False)
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.uid'), nullable=False)    

    def __repr__(self):
        return f"<Characters: {self.name}>"
    
    def serialize(self):
        return {
            "uid": self.uid,
            "category_id": self.category_id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld_id": self.homeworld_id,
            "starships_id": self.starships_id,
        }



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }