import asyncio
import os

async def run_main():
    for i in range(1, 10):
        os.system('python main.py')

async def main():
    tasks = [run_main() for _ in range(10)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
