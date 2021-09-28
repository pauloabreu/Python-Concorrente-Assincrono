import asyncio
from os import link
import typing
import aiofiles
import aiohttp
import bs4

async def pegar_links():
    links = []
    async with aiofiles.open('links.txt') as arquivo:
        async for link in arquivo:
            links.append(link.strip())
    return links


async def pegar_html(link):
    print(f'Pegando HTMl da página: {link}')

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            resp.raise_for_status()

            return await resp.text()


def pegar_titulo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    title = soup.select_one('title').text

    return title


async def imprimir_titulos():
    links = await pegar_links()
    
    tarefas = []
    for link in links:
        tarefas.append(asyncio.create_task(pegar_html(link)))

    for tarefa in tarefas:
        html = await tarefa

        title = pegar_titulo(html)
        print(f'Página: {title}')


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(imprimir_titulos())
    el.close()


if __name__ == "__main__":
    main()