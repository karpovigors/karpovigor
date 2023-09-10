import aiohttp
import asyncio
import requests
import os
import time
import sys
from multiprocessing import Pool, cpu_count
from threading import Thread


async def download_file_async(url, session):
    start_time = time.time()
    filename = url.split("/")[-1]

    async with session.get(url, ssl=False) as response:
        with open(filename, "wb") as f:
            f.write(await response.read())

    end_time = time.time() - start_time
    print(f"Скачано {filename} за {end_time:.2f} секунд.")


async def main_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_file_async(url, session) for url in urls]
        await asyncio.gather(*tasks)


def download_file_thread(url):
    start_time = time.time()
    filename = url.split("/")[-1]
    response = requests.get(url)

    with open(filename, "wb") as f:
        f.write(response.content)

    end_time = time.time() - start_time
    print(f"Скачано {filename} за {end_time:.2f} секунд.")


def main_thread(urls):
    threads = [Thread(target=download_file_thread, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def download_file_process(url):
    start_time = time.time()
    filename = url.split("/")[-1]
    response = requests.get(url)

    with open(filename, "wb") as f:
        f.write(response.content)

    end_time = time.time() - start_time
    print(f"Скачано {filename} за {end_time:.2f} секунд.")


def main_process(urls):
    with Pool(cpu_count()) as pool:
        pool.map(download_file_process, urls)


if __name__ == "__main__":
    urls = sys.argv[1:]

    start_time = time.time()

    print("\nАсинхронный подход:")
    asyncio.run(main_async(urls))

    print("\nМногопоточный подход:")
    main_thread(urls)

    print("\nМногопроцессорный подход:")
    main_process(urls)

    end_time = time.time() - start_time
    print(f"\nОбщее время выполнения программы: {end_time:.2f} секунд.")
