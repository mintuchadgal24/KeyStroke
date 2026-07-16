from datetime import datetime

LOG_FILE = "input_log.txt"

print("Input Logger (consent-based)")
print("Type 'exit' to quit.\n")

with open(LOG_FILE, "a", encoding="utf-8") as file:
    while True:
        text = input("Enter text: ")

        if text.lower() == "exit":
            break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {text}\n")

print(f"\nInputs saved to {LOG_FILE}")
