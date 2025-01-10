# IAskAI Client

```python
import asyncio
import iask
from iask import buffer

client = iask.Client()

async def main():
    # stream response
    async for chunk in client.ask({
        'mode': 'wiki',
        'q': 'When Symfony 7.2 release?'
    }):
        print(chunk, end='')
    # wait fully response
    response = await buffer(client.ask('Who is Naruto?'))
asyncio.run(main())
```
