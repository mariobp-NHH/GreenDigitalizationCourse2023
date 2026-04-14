from capp.models import Transport
from capp import db
from datetime import timedelta, datetime

""" Step 1. Query to the database. Raw data """
def get_emissions_by_transport(user, days=5):
    return (
        db.session.query(
            db.func.sum(Transport.total),
            Transport.transport
        )
        .filter(Transport.date > (datetime.now() - timedelta(days=days)))
        .filter_by(author=user)
        .group_by(Transport.transport)
        .order_by(Transport.transport.asc())
        .all()
    )

""" Step 2. Transform the SQLAlchemy object from the first step 
in a dictionary. Formatted data """

def format_emissions_for_chart(raw_data):
    # Fixed order (important for Chart.js)
    labels = ['Bicycle', 'Bus', 'Car', 'Ferry', 'Motorbike', 'Plane', 'Scooter', 'Walk']

    # Initialize dictionary with zeros
    emissions_dict = {label: 0 for label in labels}

    # Fill with real data
    for total, transport in raw_data:
        if transport in emissions_dict:
            emissions_dict[transport] = float(total)

    # Convert to list (ordered)
    data = [emissions_dict[label] for label in labels]

    return labels, data

""" Step 3. Debug function """
def debug_chart_data(raw, labels, data):
    print("\n--- CHART DEBUG START ---")

    print("RAW TYPE:", type(raw))
    print("RAW CONTENT:", raw)

    if raw:
        print("FIRST ROW TYPE:", type(raw[0]))
        print("FIRST ROW:", raw[0])

    print("\nLABELS:", labels)
    print("DATA:", data)

    if data:
        print("FIRST VALUE TYPE:", type(data[0]))

    print("--- CHART DEBUG END ---\n")

