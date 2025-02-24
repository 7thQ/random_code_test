import os
import json
import asyncio
from telethon import TelegramClient
import time

# Telegram API credentials
API_ID = 25459752
API_HASH = ''

# File paths
DATA_DIR = os.path.join(os.getcwd(), 'data')
NOT_FINISHED_DIR = os.path.join(DATA_DIR, 'Json')
INPUT_FILE = os.path.join(NOT_FINISHED_DIR, 'readydata.json')

# Target username
TARGET_USERNAME = 'whiteprivilleges'



def format_lead(lead_data):
    """Format a single lead into a message"""
    message = (
        f"================================\n\n"
        f"NAME: {lead_data['NAME']}\n\n"
        f"PHONE: {lead_data['PHONE']}\n\n"
        f"CARD FIRST DIGITS: {lead_data['CARD FIRST DIGITS']}\n\n"
        f"CARD Expiration date: {lead_data['CARD Expiration date']}\n\n"
        f"Address on file: {lead_data['Address on file']}\n\n"
        f"--------------------------------\n\n"
        f"Nothing else is available for security purposes: {lead_data['Nothing else is available for security purposes']}\n\n"
        f"There is limited information and access: {lead_data['there is limited information and access']}\n\n"
        f"================================"
    )
    return message

async def send_leads():
    # Create the client and connect
    client = TelegramClient('lead_sender_session', API_ID, API_HASH)
    await client.start()
    
    print("Loading leads from file...")
    try:
        # Read the JSON file
        with open(INPUT_FILE, 'r') as file:
            leads_data = json.load(file)
        
        # Get the target user entity
        user = await client.get_entity(TARGET_USERNAME)
        
        print(f"Found {len(leads_data)} leads. Starting to send...")
        
        # Send each lead as a separate message
        for lead_num, (lead_key, lead_data) in enumerate(leads_data.items(), 1):
            message = f"Lead #{lead_num}:\n\n{format_lead(lead_data)}"
            
            try:
                await client.send_message(user, message)
                print(f"Sent {lead_key}")
                
                # Wait 2 seconds between messages to avoid flooding
                await asyncio.sleep(2)
                
            except Exception as e:
                print(f"Error sending {lead_key}: {str(e)}")
                continue
        
        print("Finished sending all leads")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    finally:
        await client.disconnect()

if __name__ == "__main__":
    # Create directories if they don't exist
    os.makedirs(NOT_FINISHED_DIR, exist_ok=True)
    
    print("Starting lead sender...")
    asyncio.run(send_leads())