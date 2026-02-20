#!/usr/bin/env python3
"""List all states and their cities from the database."""

from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Example function to list states and cities
def list_states_cities(engine):
    """Print each state followed by its cities."""
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.name}:")
        for city in state.cities:
            print(f"  {city.name}")

    session.close()


# Example usage (replace credentials as needed)
if __name__ == "__main__":
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <user> <password> <database>")
        exit(1)

    user, password, db = argv[1], argv[2], argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{db}")
    list_states_cities(engine)
