import requests

# Reads webhook.txt for Slack webhook URL
try:
    with open("webhook.txt") as webhook_temp:
        webhook = webhook_temp.read().strip()
except FileNotFoundError:
    print("Sorry! webhook.txt was not found.")
    input("Press Enter to exit...")
    exit("Exiting program...")

# Provides user instructions
print("\nWelcome to Slack Webhook Sender! Enter 'exit' to quit. ")

# Loop for sending multiple messages
while True:

# Prompts user for message to send
    message = input("\nPlease enter a message to send to Slack: ")

# Checks if user wants to exit
    if message.lower() == "exit":
        input("\nPlease press Enter to exit...")
        break

# Defines payload for Slack API
    payload = {"text": message}

    response = requests.post(webhook, json=payload)

# Checks response status
    if response.status_code == 200:
        print("\nMessage sent to Slack!")
    else:
        print(f"\nMessage failed to send with status code: {response.status_code}")

# Wow, You actually read the source code!, Good for you 😁
