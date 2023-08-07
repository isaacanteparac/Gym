from reactpy import html, hooks, component
from .FormBlackList import FormBlackList
from .CardBlackList import CardBlackList
import aiohttp



@component
def BlackList():
    getUrl = "http://127.0.0.1:8000/api/blacklist/get/all"
    regulationeData, setRegulationeData = hooks.use_state(initial_value="")
    rows, setRows = hooks.use_state(initial_value=[])


    async def getData():
        rows.clear()
        async with aiohttp.ClientSession() as session:
            async with session.get(getUrl) as resp:
                response = await resp.json()
                setRegulationeData(response)
        renderBlackList()

    def renderBlackList():
        for regulation in regulationeData:
            rows.append(CardBlackList(regulation))

    hooks.use_effect(getData)

    return html.div(
        {"class":"wrapper"},
        FormBlackList(),
        rows
    )