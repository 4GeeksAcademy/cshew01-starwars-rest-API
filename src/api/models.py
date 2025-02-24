from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    favorites = db.relationship('Favorites', backref='user', lazy=True)


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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'), nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)

    def __repr__(self):
        return f"<Favorites: {self.item}>"
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "starships_id": self.starships_id,
            "planets_id": self.planets_id,
            "characters_id": self.characters_id,
        }

class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
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
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "hyperdrive_rating": self.hyperdrive_rating,
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
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
            "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    birth_year = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(30), nullable=False)   

    def __repr__(self):
        return f"<Characters: {self.name}>"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
        }
