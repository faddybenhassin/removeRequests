# Instagram Pending Follow Request Cleaner

A Python automation script to automatically cancel outgoing follow requests (pending requests) using the `instagrapi` library.

## 🚀 Features
* **Automated Unfollowing**: Clears pending requests from a JSON list.
* **Rate Limit Protection**: Includes built-in sleep timers to avoid Instagram account flags.
* **Secure Credentials**: Uses environment variables to manage login sensitive data.
* **Progress Tracking**: Real-time console output of processing status.

## 🛠 Prerequisites
* Python 3.7+
* An Instagram account
* A `pending_follow_requests.json` file (obtained via Instagram "Download Your Information" export)

## 📦 Installation

1. **Clone or save the script** to your local machine.
2. **Install dependencies**:
   ```bash
   pip install instagrapi python-dotenv