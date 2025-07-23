# 🕵️‍♂️ Domain Checker Bot

Check if a domain is real, recently registered, or flagged as malicious — directly from Telegram.

🔗 **Try it here:** [@realweborfake_bot](https://t.me/realweborfake_bot)

---

## 💡 Features

- ✅ Validates domain format
- 🗓️ Retrieves WHOIS info: creation date, registrar, domain age
- 🧪 Checks domain on [VirusTotal](https://www.virustotal.com/)
- ⚠️ Warns about suspicious or new domains
- 🤖 Fast response via Telegram Bot

---

## 📦 Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

---

## 🔐 How to Get Your API Keys

### 1. Telegram Bot Token from @BotFather

1. Open [@BotFather](https://t.me/BotFather) in Telegram
2. Send `/start` and then `/newbot`
3. Choose a name and username (e.g., `realweborfake_bot`)
4. BotFather will give you a token like:123456789:ABCDefGhIJKlmNoPQRstuVWXyz123456789

   
Copy and save this — it goes into your `.env`.

---

### 2. VirusTotal API Key

1. Go to [https://www.virustotal.com/gui/join-us](https://www.virustotal.com/gui/join-us) and sign up
2. After logging in, visit [https://www.virustotal.com/gui/user/YOUR_USERNAME/apikey](https://www.virustotal.com/gui/user/YOUR_USERNAME/apikey)
3. Copy your API key — it goes in your `.env`

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/tanish19078/domain_checker_bot.git
cd domain_checker_bot
```

### 2. Create a .env file in the root folder (⚠️ Do not share publicly):

```bash
BOT_TOKEN=your-telegram-bot-token-here
VT_API_KEY=your-virustotal-api-key-here
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Run the bot

```bash
python domain_checker_bot.py
```

