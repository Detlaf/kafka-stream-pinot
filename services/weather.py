from typing import List

import httpx


async def get_weather_singapore(api_url: str) -> List[dict]:
    async with httpx.AsyncClient() as client:
        res = await client.get(api_url)
    if res.status_code == 200:
        return res.json()["items"][0]["readings"]
    else:
        raise Exception(f"Request error {res.status_code} {res.text}")
