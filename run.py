import asyncio
from app.services import NtfyService

if __name__ == "__main__":
        app = NtfyService()
        data = {
                'text':'New messages on Reddit',
                'Click': 'https://www.reddit.com/message/messages',
                'topic_name':'jhon doe'
        }
        
        result = asyncio.run(app.send_message_to_reddit(data))
        print(result)
