import iask
import pytest
from iask import buffer


@pytest.mark.asyncio
async def test_client():
    client = iask.Client()
    assert isinstance(await buffer(client.ask("Who is Yugi?")), str)
