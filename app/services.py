import aiohttp

class NtfyService:
    def __init__(self):
        self.base_url = "https://ntfy.sh/"
        self.headers={
            "Authorization": "Bearer YOUR_TOKEN"
        }
        
    async def send_message(self, payload):
        topic = 'response'  
        url = f'{self.base_url}{topic}'
        
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload ,headers=self.headers) as response:
                return await response.json()
            
            
            
    async def send_message_to_reddit(self,payload):
        topic = payload['topic_name']
        url = f'{self.base_url}{topic}'
        
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url,
                                    json=payload,
                                    headers=self.headers
                                    ) as response:
                return await response.json()
        