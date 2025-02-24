


from telethon import TelegramClient, events
import asyncio
import json

# Your credentials
API_ID = 25972208
API_HASH = ''

# Function to parse PNC login messages
def parse_pnc_message(message_text):
    if "PNC LOGIN" in message_text:
        lines = message_text.split('\n')
        credentials = {}
        
        for line in lines:
            if "Username:" in line:
                credentials['username'] = line.split('Username:')[1].strip()
            elif "Password:" in line:
                credentials['password'] = line.split('Password:')[1].strip()
                
        if 'username' in credentials and 'password' in credentials:
            return credentials
    return None

async def main():
    # Connect to Telegram
    client = TelegramClient('pnc_session', API_ID, API_HASH)
    await client.start()
    
    print("Connected to Telegram")
    
    @client.on(events.NewMessage)
    async def message_handler(event):
        # Get the message text
        message = event.message.text
        print("\nNew message received:")
        print(message)
        
        # Try to parse PNC credentials
        credentials = parse_pnc_message(message)
        if credentials:
            print("\nFound credentials:")
            print(f"Username: {credentials['username']}")
            print(f"Password: {credentials['password']}")
            
            # Save to credentials.json
            with open('credentials.json', 'w') as f:
                json.dump(credentials, f)
                print("Saved credentials to file")

    print("\nListening for messages... Press Ctrl+C to stop")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())