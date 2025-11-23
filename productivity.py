import json
import sys
from datetime import date
from pathlib import Path

FILE = Path("history.json")

def load_data():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return {}

def save_data(data):
    FILE.write_text(json.dumps(data, indent=2))

def add_score(score):
    score = int(score)
    if not (1 <= score <= 10):
        print("Score must be between 1 and 10.")
        return

    data = load_data()
    today = str(date.today())
    data[today] = score
    save_data(data)
    print(f"Added: {score}")

def show_history():
    data = load_data()
    if not data:
        print("No history yet.")
        return
    for day, score in data.items():
        print(f"{day}: {score}")

def show_avg():
    data = load_data()
    if not data:
        print("No data to calculate average.")
        return
    avg = sum(data.values()) / len(data)
    print(f"Average productivity: {avg:.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python productivity.py [add/history/avg]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "add" and len(sys.argv) == 3:
        add_score(sys.argv[2])
    elif cmd == "history":
        show_history()
    elif cmd == "avg":
        show_avg()
    else:
        print("Unknown or invalid command.")
