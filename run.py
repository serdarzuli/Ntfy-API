from App import ntfy
import asyncio

app = ntfy()
data = {'text':'New messages on Reddit',
        'Click': 'https://www.reddit.com/message/messages',
        'topic_name':'zuli_s'}

result = asyncio.run(app.send_message_to_reddit(data))
print(result)



payload = {'topic_name' : 'test',
           'data': 'imperum test'}

result = asyncio.run(app.send_message(data))
print(result)