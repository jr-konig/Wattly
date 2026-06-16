import time
from datetime import datetime

from storage import add_session, load_data
from energy import calc_kwh, calc_cost, DEFAULT_WATTS

session = None

def start():
    global session
    if session:
        print("Session already running")
        return

    session = {
        "start": time.time(),
        "watts": DEFAULT_WATTS
    }

    print("⚡ Wattly session started")

def stop():
    global session
    if not session:
        print("No active session")
        return

    end = time.time()
    hours = (end - session["start"]) / 3600

    kwh = calc_kwh(session["watts"], hours)
    cost = calc_cost(kwh)

    result = {
        "start": datetime.fromtimestamp(session["start"]).isoformat(),
        "end": datetime.fromtimestamp(end).isoformat(),
        "hours": hours,
        "watts": session["watts"],
        "kwh": kwh,
        "cost_dkk": cost
    }

    add_session(result)
    session = None

    print("\n--- Wattly Session ---")
    print(f"Hours: {hours:.2f}")
    print(f"kWh: {kwh:.3f}")
    print(f"Cost: {cost:.2f} DKK")

def summary():
    data = load_data()
    sessions = data["sessions"]

    total_cost = sum(s["cost_dkk"] for s in sessions)
    total_kwh = sum(s["kwh"] for s in sessions)

    print("\n--- Wattly Summary ---")
    print(f"Sessions: {len(sessions)}")
    print(f"Total kWh: {total_kwh:.3f}")
    print(f"Total cost: {total_cost:.2f} DKK")

def menu():
    while True:
        print("\n⚡ Wattly")
        print("1. Start session")
        print("2. Stop session")
        print("3. Summary")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            start()
        elif choice == "2":
            stop()
        elif choice == "3":
            summary()
        elif choice == "4":
            break

if __name__ == "__main__":
    menu()