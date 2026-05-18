"""
Email Categorizer & Summarizer - Powered by Claude AI

A simple tool that takes email content and:
1. Categorizes it (Work, Personal, Marketing, Support, etc.)
2. Summarizes the key points
3. Suggests urgency level

Usage:
    Set environment variable: export ANTHROPIC_API_KEY="your-key-here"
    Run: python email_processor.py
    Or with Docker: docker run -e ANTHROPIC_API_KEY="your-key" email-organizer
"""

import anthropic
import os
import json

# Initialize Anthropic client
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable not set!")

client = anthropic.Anthropic(api_key=api_key)

def process_email(subject: str, body: str) -> dict:
    """
    Process an email: categorize, summarize, and assess urgency.
    
    Args:
        subject: Email subject line
        body: Email body content
        
    Returns:
        Dictionary with category, summary, and urgency
    """
    
    # Create prompt for Claude
    prompt = f"""Analyze this email and provide:
1. CATEGORY: Classify it as one of: Work, Personal, Marketing, Support, Other
2. SUMMARY: 2-3 sentences summarizing the key point
3. URGENCY: Rate as Low, Medium, or High
4. ACTION_ITEMS: List any action items mentioned (if any)

Email Subject: {subject}
Email Body: {body}

Respond in JSON format:
{{
    "category": "...",
    "summary": "...",
    "urgency": "...",
    "action_items": ["...", "..."]
}}
"""

    try:
        # Call Claude API
        response = client.messages.create(
            model="claude-opus-4-1-20250805",
            max_tokens=500,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        # Extract response text
        response_text = response.content[0].text
        
        # Parse JSON response
        # Try to extract JSON from response (Claude might wrap it with markdown)
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0]
        elif "```" in response_text:
            json_str = response_text.split("```")[1].split("```")[0]
        else:
            json_str = response_text
            
        result = json.loads(json_str.strip())
        return result
        
    except json.JSONDecodeError:
        return {
            "category": "Error",
            "summary": "Could not parse response",
            "urgency": "Unknown",
            "action_items": []
        }
    except anthropic.APIError as e:
        return {
            "category": "Error",
            "summary": f"API Error: {str(e)}",
            "urgency": "Unknown",
            "action_items": []
        }

def format_output(email_data: dict, result: dict) -> str:
    """Format the email processing result for display"""
    return f"""
{'='*60}
📧 EMAIL ANALYSIS
{'='*60}
Subject: {email_data['subject']}
---
Category:     {result.get('category', 'Unknown')}
Urgency:      {result.get('urgency', 'Unknown')}
Summary:      {result.get('summary', 'No summary')}
Action Items: {', '.join(result.get('action_items', ['None'])) if result.get('action_items') else 'None'}
{'='*60}
"""

def interactive_mode():
    """Run the tool in interactive mode"""
    print("\n🤖 Email Categorizer & Summarizer")
    print("Powered by Claude AI\n")
    
    while True:
        print("\nOptions:")
        print("1. Process an email")
        print("2. Exit")
        
        choice = input("\nChoose option (1 or 2): ").strip()
        
        if choice == "2":
            print("\nGoodbye!")
            break
        elif choice == "1":
            subject = input("\nEmail Subject: ").strip()
            if not subject:
                print("❌ Subject cannot be empty!")
                continue
                
            print("Email Body (paste content, press Enter twice when done):")
            lines = []
            while True:
                line = input()
                if line == "":
                    if lines and lines[-1] == "":
                        break
                    lines.append(line)
                else:
                    lines.append(line)
            
            body = "\n".join(lines[:-1]).strip()
            if not body:
                print("❌ Body cannot be empty!")
                continue
            
            print("\n⏳ Processing email...")
            result = process_email(subject, body)
            print(format_output({"subject": subject}, result))
        else:
            print("❌ Invalid choice!")

def demo_mode():
    """Run with sample emails for demonstration"""
    print("\n🤖 Email Categorizer & Summarizer - DEMO MODE")
    print("Processing sample emails...\n")
    
    sample_emails = [
        {
            "subject": "Q4 Sales Report - Action Required",
            "body": "Hi team, please find the Q4 sales report attached. We need your feedback by EOD Friday. The numbers show a 15% increase from Q3. Please review and let me know if you have any questions."
        },
        {
            "subject": "Special offer just for you! 50% off today",
            "body": "Hey valued customer! We're running a flash sale today only. Get 50% off everything with code SPECIAL50. This offer expires at midnight. Shop now!"
        },
        {
            "subject": "Birthday Lunch Next Friday?",
            "body": "Hey! A group of us are planning to go out for lunch next Friday to celebrate Sarah's birthday. Want to join? We're thinking of that Italian place downtown. Let me know!"
        }
    ]
    
    for email in sample_emails:
        print(f"Processing: {email['subject']}")
        result = process_email(email['subject'], email['body'])
        print(format_output(email, result))

if __name__ == "__main__":
    import sys
    
    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_mode()
    else:
        interactive_mode()
