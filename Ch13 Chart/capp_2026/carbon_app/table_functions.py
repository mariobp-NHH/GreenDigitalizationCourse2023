from capp.models import Transport
from capp import db
from datetime import timedelta, datetime

""" Step 1. Query to the database. Raw data """
def get_entries(user, days=5):
    return (
        Transport.query
        .filter_by(author=user)
        .filter(Transport.date > (datetime.now() - timedelta(days=days)))
        .order_by(Transport.date.desc(), Transport.transport.asc())
        .all()
    )

""" Step 2. Transform the SQLAlchemy object from the first step 
in a dictionary. Formatted data """
def format_entries_for_table(entries):
    formatted = []

    for entry in entries:
        formatted.append({
            "username": entry.author.username,
            "date": entry.date.strftime("%m-%d-%Y"),
            "kms": entry.kms,
            "transport": entry.transport,
            "fuel": entry.fuel,
            "co2": entry.co2,
            "ch4": entry.ch4,
            "total": entry.total,
            "id": entry.id
        })
    
    """ Step 3.a. Debug the backend data """
    print(f"\n--- BACKEND DEBUG START ---")
    for entry in entries:
        print("ENTRY TYPE:", type(entry))
        print("DATE TYPE:", type(entry.date))
        print("KMS TYPE:", type(entry.kms))
        break
    print(f"--- BACKEND DEBUG END ---")
    
    """ Step 3.b. Debug the frontend data """
    print(f"\n--- FRONTEND DEBUG START ---")
    for format in formatted:
        print("FORMATED TYPE:", type(formatted))
        for key, value in formatted[0].items():
            print(f"{key}: {value} | TYPE: {type(value)}")
        print("DATE TYPE:", type(formatted[0]))
        break
    print(f"--- FRONTEND DEBUG END ---")

    return formatted

""" Step 3.c Debug the backend data in the browser """
def debug_raw_entries(entries):
    debug_list = []

    for entry in entries:
        debug_list.append({
            "username": entry.author.username,
            "date": str(entry.date),  # convert safely
            "kms": entry.kms
        })

    return debug_list

""" Improved debug function that includes backend and fronted debug """
def debug_entries(entries, label="DATA"):
    print(f"\n--- {label} DEBUG START ---")

    print("CONTAINER TYPE:", type(entries))

    if not entries:
        print("No data")
        return

    first = entries[0]

    print("FIRST ELEMENT TYPE:", type(first))

    # If it's a SQLAlchemy object
    if hasattr(first, "__table__"):
        print("→ Detected SQLAlchemy model")

        print("date:", first.date, "| TYPE:", type(first.date))
        print("kms:", first.kms, "| TYPE:", type(first.kms))
        print("transport:", first.transport, "| TYPE:", type(first.transport))

    # If it's a dictionary (formatted data)
    elif isinstance(first, dict):
        print("→ Detected dictionary (formatted data)")

        for key, value in first.items():
            print(f"{key}: {value} | TYPE: {type(value)}")

    else:
        print("→ Unknown type")

    print(f"--- {label} DEBUG END ---\n")