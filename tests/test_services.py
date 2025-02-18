import pytest
import asyncio
from app.services import NtfyService

@pytest.mark.asyncio
async def test_send_message():
    service = NtfyService()
    payload = {"text": "Test Message..."}
    response = await service.send_message(payload)
    
    assert isinstance(response, dict)
    assert "text" in response