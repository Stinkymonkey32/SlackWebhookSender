# Slack Webhook Sender

Slack Webhook Sender is a lightweight tool that sends messages to a Slack workspace using an **Incoming Webhook**.  
A Windows `.exe` is provided for convenience; macOS and Linux users can run the Python version directly.

> Ideal for automation, alerts, reminders, and harmless trolling (use responsibly).
Also, Please don't bully me if my code isnt very good! I have been learning Python for only a month 😅

---

## Table of Contents

- [Features](#features)  
- [Slack Webhook Setup](#slack-webhook-setup)  

---

## Features

- Simple, minimal interface  
- Windows `.exe` provided — no Python required for Windows users  
- Works on macOS / Linux with Python  
- Configuration via a single `webhook.txt` file  
- Lightweight and easy to extend  

---

## Slack Webhook Setup

Slack Webhook Sender reads a single Incoming Webhook URL from `webhook.txt`. Follow these steps:

### 1. Open the Slack App Directory
Visit: <https://api.slack.com/messaging/webhooks>  
Click **Create New App → From scratch**.
(You will need a Slack workplace, If you don't know how to do this go here: https://slack.com/help/articles/206845317-Create-a-Slack-workspace)

### 2. Name Your App
Give it a name (e.g., `'My Bot'`) and select the Slack workspace.

### 3. Enable Incoming Webhooks
In the app settings sidebar go to **Incoming Webhooks** and toggle **Activate Incoming Webhooks**.  
Click **Add New Webhook to Workspace**.

### 4. Choose a Channel
Select the channel where messages will be sent. Slack generates a webhook URL:

```
https://hooks.slack.com/services/XXXX/YYYY/ZZZZ
```

### 5. Save Your Webhook URL
Open the file named `webhook.txt` in the same directory as the `.exe` or `.py` file.  
Paste only the webhook URL (no quotes, spaces, or blank lines):

```
https://hooks.slack.com/services/XXXX/YYYY/ZZZZ
```

### 6. Run Slack Webhook Sender
**Windows:** run the `.exe`  
**macOS / Linux:** run the Python script:

```bash
python3 slackwebhooksender.py
```

---



