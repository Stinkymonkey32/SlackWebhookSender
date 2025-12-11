# SlackbotController

SlackbotController is a lightweight tool that sends messages to a Slack workspace using an **Incoming Webhook**.  
A Windows `.exe` is provided for convenience; macOS and Linux users can run the Python version directly.

> Ideal for automation, alerts, reminders, and harmless trolling (use responsibly).
Also, Please don't bully me if my code isnt very good! I have been learning Python for only a month 😅

---

## Table of Contents

- [Features](#features)  
- [Slack Webhook Setup](#slack-webhook-setup)  
- [Contributing](#contributing)  

---

## Features

- Simple, minimal interface  
- Windows `.exe` provided — no Python required for Windows users  
- Works on macOS / Linux with Python  
- Configuration via a single `webhook.txt` file  
- Lightweight and easy to extend  

---

## Slack Webhook Setup

SlackbotController reads a single Incoming Webhook URL from `webhook.txt`. Follow these steps:

### 1. Open the Slack App Directory
Visit: <https://api.slack.com/messaging/webhooks>  
Click **Create New App → From scratch**.

### 2. Name Your App
Give it a name (e.g., `SlackbotController Bot`) and select the Slack workspace.

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

### 6. Run SlackbotController
**Windows:** run the `.exe`  
**macOS / Linux:** run the Python script:

```bash
python3 SlackbotController.py
```

---

## Contributing

Follow these steps to contribute to **SlackbotController**:

### Fork the Repository
- Fork the repository on GitHub to create your own copy.

### Clone Your Fork
```bash
git clone https://github.com/<your-username>/SlackbotController.git
cd SlackbotController
```

### Create a New Branch
```bash
git checkout -b my-feature
```

### Make Changes and Commit
```bash
git add .
git commit -m "Describe your changes"
```

### Push Your Branch
```bash
git push origin my-feature
```

### Open a Pull Request
- Navigate to your fork on GitHub.  
- Click **Compare & pull request**.  
- Set the base to the original repository and the head to your branch.  
- Submit the pull request.

### Keep Your Fork Updated
```bash
git remote add upstream https://github.com/original-owner/SlackbotController.git
git fetch upstream
git checkout main
git merge upstream/main
```

### Notes
- Use separate branches for each feature or bug fix.  
- Keep pull requests focused and small.  
- Match the project’s code style.  
- Test your changes before submitting a pull request.  
- Merge upstream changes regularly to stay up to date.
- You don't just have to contribute code! I also appreciate any Issue requests or even just a better setup tutorial


