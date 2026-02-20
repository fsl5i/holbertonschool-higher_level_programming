#!/usr/bin/env python3
"""List all State objects and their City objects from the database."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State
from relationship_city import City


def list_states_cities(engine):
    """Print all states and their cities ordered by state.id and city.id."""
    Session = sessionmaker(bind=engine)
    session = Session()

    # Load all states with their cities in one query
    states = session.query(State).options(joinedload(State.cities)).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        # Cities sorted by id
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <username> <password> <database>")
        exit(1)

    user, password, db = argv[1], argv[2], argv[3]
    # Connect to MySQL
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}")
    list_states_cities(engine)
