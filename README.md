# Slack Webhook Sender

A simple Python script that sends messages to a Slack channel using an incoming webhook.

## Features

* Send messages directly from the terminal
* Supports sending multiple messages in one session
* Reads the webhook URL from a local file
* Simple and lightweight

## Requirements

* Python 3.x
* `requests`

Install dependencies:

```bash
pip install requests
```

## Setup

1. Create a Slack Incoming Webhook for your workspace.
2. Create a file named `webhook.txt` in the same folder as the script.
3. Paste your webhook URL into `webhook.txt`.

Example:

```txt
https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXX
```

## Usage

Run the script:

```bash
python main.py
```

Enter a message when prompted and it will be sent to Slack.

To exit the program, type:

```txt
exit
```

## Example

```txt
Welcome to Slack Webhook Sender! Enter 'exit' to quit.

Please enter a message to send to Slack: Hello Slack!

Message sent to Slack!
```

## Troubleshooting

### webhook.txt not found

Make sure `webhook.txt` exists in the same directory as the script.

### Message failed to send

Verify that:

* Your webhook URL is correct
* The webhook has not been deleted or disabled
* Your internet connection is working

## License

Feel free to use, modify, and distribute this project.

---
