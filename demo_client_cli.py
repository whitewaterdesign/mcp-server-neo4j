import asyncio

from client.agent import get_movie_agent


if __name__ == "__main__":
    asyncio.run(get_movie_agent())