"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Users, Favorites, Planets, Characters, Starships
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


# User Endpoints 
@api.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    return jsonify([user.serialize() for user in users])

@api.route('/users/favorites', methods=['GET'])
def get_favorites():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    favorites = Favorites.query.filter_by(user_id=user_id).all()
    return jsonify([favorite.serialize() for favorite in favorites])


# Starships Endpoints
@api.route('/starships', methods=['GET'])
def get_starships():
    starships = Starships.query.all()
    return jsonify([starship.serialize() for starship in starships])

@api.route('/starships/<int:starships_id>', methods=['GET'])
def get_starship(starships_id):
    starship = Starships.query.get(starships_id)
    if starship is None:
        return jsonify({"error": "Starship not found"}), 404
    return jsonify(starship.serialize())


# Planet Endpoints
@api.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    return jsonify([planet.serialize() for planet in planets])

@api.route('/planets/<int:planets_id>', methods=['GET'])
def get_planet(planets_id):
    planet = Planets.query.get(planets_id)
    if planet is None:
        return jsonify({"error": "Character not found"}), 404
    return jsonify(planet.serialize())


# Character Endpoints
@api.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    return jsonify([character.serialize() for character in characters])

@api.route('/characters/<int:characters_id>', methods=['GET'])
def get_character(characters_id):
    character = Characters.query.get(characters_id)
    if character is None:
        return jsonify({"error": "Character not found"}), 404
    return jsonify(character.serialize())


# Favorites Endpoints
# favorite starship Post and Delete endpoints
@api.route('/favorite/starships/<int:starships_id>', methods=['POST'])
def add_favorite_starships(starships_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    existing_favorite = Favorites.query.filter_by(user_id=user_id, starships_id=starships_id).first()
    if existing_favorite:
        return jsonify({"error": "Favorite starship already exists"}), 400

    try:
        favorite = Favorites(user_id=user_id, starships_id=starships_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

@api.route('/favorite/starships/<int:starships_id>', methods=['DELETE'])
def delete_favorite_starships(starships_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    favorite = Favorites.query.filter_by(user_id=user_id, starships_id=starships_id).first()
    if not favorite:
        return jsonify({"error": "Favorite not found"}), 404

    try:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite starship deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

# favorite planet Post and Delete endpoints    
@api.route('/favorite/planets/<int:planets_id>', methods=['POST'])
def add_favorite_planets(planets_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    existing_favorite = Favorites.query.filter_by(user_id=user_id, planets_id=planets_id).first()
    if existing_favorite:
        return jsonify({"error": "Favorite planet already exists"}), 400

    try:
        favorite = Favorites(user_id=user_id, planets_id=planets_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

@api.route('/favorite/planets/<int:planets_id>', methods=['DELETE'])
def delete_favorite_planets(planets_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    favorite = Favorites.query.filter_by(user_id=user_id, planets_id=planets_id).first()
    if not favorite:
        return jsonify({"error": "Favorite not found"}), 404

    try:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite planet deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# favorite character Post and Delete endpoints
@api.route('/favorite/characters/<int:characters_id>', methods=['POST'])
def add_favorite_characters(characters_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    existing_favorite = Favorites.query.filter_by(user_id=user_id, characters_id=characters_id).first()
    if existing_favorite:
        return jsonify({"error": "Favorite character already exists"}), 400

    try:
        favorite = Favorites(user_id=user_id, characters_id=characters_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

@api.route('/favorite/characters/<int:characters_id>', methods=['DELETE'])
def delete_favorite_characters(characters_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    favorite = Favorites.query.filter_by(user_id=user_id, characters_id=characters_id).first()
    if not favorite:
        return jsonify({"error": "Favorite not found"}), 404

    try:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite character deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500