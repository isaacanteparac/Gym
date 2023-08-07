from reactpy import html, hooks, component
from .FormRegulation import FormRegulation
from .CardRegulation import CardRegulation
import aiohttp



@component
def Regulation():
    getUrl = "http://127.0.0.1:8000/api/regulation/get/all"
    regulationeData, setRegulationeData = hooks.use_state(initial_value="")
    rows, setRows = hooks.use_state(initial_value=[])


    async def getData():
        rows.clear()
        async with aiohttp.ClientSession() as session:
            async with session.get(getUrl) as resp:
                response = await resp.json()
                setRegulationeData(response)
        renderRegulation()

    def renderRegulation():
        for regulation in regulationeData:
            rows.append(CardRegulation(regulation))

    hooks.use_effect(getData)

    return html.div(
        {"class":"wrapper"},
        FormRegulation(),
        rows
    )