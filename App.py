import requests

import aiohttp
import asyncio
class ntfy:
    base_url = "https://ntfy.sh/"
    headers={
            "Authorization": "Bearer "
        }
    async def send_message(self,payload):
        topic = 'response'  
        data=payload  
        url = f'{self.base_url}{topic}'
        async with aiohttp.ClientSession() as session:
            async with session.post(url,data=data,headers=self.headers) as response:
                return await response.json()
            
            
            
    async def send_message_to_reddit(self,payload):
        topic = payload['topic_name']
        url = f'{self.base_url}{topic}'
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url,
                                    headers=self.headers,
                                    data=payload,
                                    ) as response:
                return await response.json()
        
    
# for run        
app = ntfy()

data1={'text':"New messages on Reddit",
        "Click": "https://www.reddit.com/message/messages",
        'topic_name' : 'Luffy'}
result = asyncio.run(app.send_message(data1))
print(result)

data = {'text':"New messages on Reddit",
        "Click": "https://www.reddit.com/message/messages",
        'topic_name' : 'Luffy'}

result = asyncio.run(app.send_message_to_reddit(data))
print(result)
