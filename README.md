# 📧 Email Categorizer & Summarizer

A Python tool that uses Claude AI to intelligently analyze and organize emails. Categorizes emails, generates summaries, assesses urgency, and identifies action items.

## Features

- 🏷️ **Smart Categorization** - Automatically sorts emails into Work, Personal, Marketing, Support, etc.
- 📝 **Auto-Summarization** - Generates concise 2-3 sentence summaries
- ⚠️ **Urgency Assessment** - Rates emails as Low, Medium, or High priority
- ✅ **Action Item Extraction** - Identifies tasks that need to be done
- 🎯 **Claude AI Powered** - Uses Anthropic's advanced language model
- 🐳 **Docker Ready** - Containerized for easy deployment
- 💻 **Interactive & Demo Modes** - Test with sample emails or your own

## Prerequisites

- Python 3.11+ (or Docker)
- Claude API key from https://console.anthropic.com

## Setup & Installation

### Option 1: Local Python Setup

1. **Clone or download this project**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API key**:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-your-actual-key-here"
   ```
   On Windows (PowerShell):
   ```powershell
   $env:ANTHROPIC_API_KEY="sk-ant-your-actual-key-here"
   ```

5. **Run the tool**:
   ```bash
   # Demo mode with sample emails
   python email_processor.py --demo
   
   # Interactive mode to process your emails
   python email_processor.py
   ```

### Option 2: Docker Setup

1. **Set your API key**:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-your-actual-key-here"
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t email-organizer .
   ```

3. **Run demo mode**:
   ```bash
   docker run -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" email-organizer
   ```

4. **Run interactive mode**:
   ```bash
   docker run -it -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
     email-organizer python email_processor.py
   ```

### Option 3: Docker Compose (Easiest)

1. **Set your API key**:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-your-actual-key-here"
   ```

2. **Run with Docker Compose**:
   ```bash
   docker-compose up
   ```

## Usage

### Demo Mode (Fastest Way to See It Work)

```bash
python email_processor.py --demo
```

This processes 3 sample emails (Work, Marketing, Personal) to show you how the tool works.

### Interactive Mode

```bash
python email_processor.py
```

Then:
1. Choose option "1. Process an email"
2. Enter the email subject
3. Paste the email body (press Enter twice when done)
4. See the analysis!

### Example Output

```
============================================================
📧 EMAIL ANALYSIS
============================================================
Subject: Q4 Sales Report - Action Required
---
Category:     Work
Urgency:      High
Summary:      The Q4 sales report shows a 15% increase from Q3. 
              Team feedback is needed by end of Friday.
Action Items: Review Q4 report, Provide feedback by EOD Friday
============================================================
```

## Project Structure

```
project2-email-organizer/
├── email_processor.py     # Main application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
└── README.md            # This file
```

## How It Works

1. **User provides** email subject and body
2. **Claude AI analyzes** the email content
3. **AI categorizes** the email (Work, Personal, etc.)
4. **AI generates** a concise summary
5. **AI rates** the urgency level
6. **AI extracts** any action items
7. **Results displayed** in formatted output

## Environment Variables

- `ANTHROPIC_API_KEY` - Your Claude API key (required)

## Key Functions

### `process_email(subject: str, body: str) -> dict`
Analyzes an email and returns categorization, summary, and urgency assessment.

### `interactive_mode()`
Prompts user to input email details and processes them.

### `demo_mode()`
Processes sample emails to demonstrate the tool's capabilities.

## Sample Emails Included

The demo mode includes 3 sample emails:
1. **Work Email** - Q4 Sales Report with action items
2. **Marketing Email** - Flash sale promotion
3. **Personal Email** - Birthday lunch invitation

## For Dynaforge Interview

This project demonstrates:
- ✅ Python scripting skills
- ✅ Claude AI API integration
- ✅ NLP/Email processing understanding
- ✅ Clean, readable code
- ✅ Docker containerization
- ✅ Real-world application (email organization for small businesses)

## Use Cases for Small Businesses

- 📥 Automatically sort incoming emails
- ⏰ Prioritize urgent messages
- 📋 Extract to-do items from email threads
- 🗂️ Organize inbox by category
- 🤖 Build automated email workflows

## Future Enhancements

- [ ] Integration with Gmail API
- [ ] Batch processing (multiple emails)
- [ ] Persistent storage (save categorized emails)
- [ ] Web interface (Streamlit or FastAPI)
- [ ] Automatic folder/label assignment
- [ ] Custom category definitions
- [ ] Sentiment analysis
- [ ] Spam/phishing detection

## Limitations

- Currently processes one email at a time in interactive mode
- Uses Claude API (costs money after free credits)
- Demo mode is limited to 3 sample emails

## Troubleshooting

**Error: "ANTHROPIC_API_KEY environment variable not set!"**
- Make sure you've set the environment variable before running the script
- Check with `echo $ANTHROPIC_API_KEY` (or `echo $env:ANTHROPIC_API_KEY` on Windows)

**Error: "Could not parse response"**
- This can happen if Claude's response format changes
- Try again - it's usually a one-off issue

## License

MIT License - Feel free to use and modify!

## Questions?

Check the inline comments in `email_processor.py` for detailed explanations.
