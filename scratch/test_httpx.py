import asyncio
import httpx
from pathlib import Path

async def test_download():
    url = "https://cdn.discordapp.com/attachments/123456789/123456789/test.png"
    # Note: This URL will 404/403 but we want to see if it raises ConnectError or 404
    print(f"Testing connection to {url}...")
    try:
        async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
            response = await client.get(url)
            print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"Caught Exception: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_download())
