import asyncio

from aiohttp import ClientSession
import pandas as pd
import os

async def fetch(jenis_bencana: int, tahun: int) -> dict:
    BASE_URL = "https://siandalan.sulselprov.go.id/data"

    params = params = {
        "data": 1, # Show only data
        "jenis": jenis_bencana,
        "tahun": tahun,
        "bulan": "",
        "kab": "",
        "kec": "",
        "status": "",
    }
    try:
        async with ClientSession() as session:
            async with session.get(BASE_URL, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error: {response.status}")
                    return {}
    except Exception as e:
        print(f"Exception occurred: {e}")
        return {}


def add_to_csv(data: dict, filename: str) -> None:
    num_of_data = data.get("recordsTotal", 0)
    if num_of_data > 0:
        df = pd.DataFrame(data["data"])
        is_first = not os.path.exists(filename)
        df.to_csv(filename, mode="a", header=is_first, index=False)
    else:
        print("No data to write to CSV.")


async def main():
    jenis_bencana = 101  # Flood
    list_tahun = range(2010, 2026) 
    filename = "south_sulawesi_flood_data.csv"
 
    for index, tahun in enumerate(list_tahun):
        data = await fetch(jenis_bencana, tahun)
        num_data = data.get("recordsTotal", 0)
        print(f"Year: {tahun}, Number of records: {num_data}")
        if num_data > 0 and data:
            
            add_to_csv(data, filename)
        else:
            print(f"No data found for year {tahun}.")


if __name__ == "__main__":
    asyncio.run(main())
