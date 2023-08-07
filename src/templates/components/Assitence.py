from reactpy import html, hooks, component
import aiohttp
from .UserAssistence import UserAssistence


@component
def Assitence():
    getUrl = "http://127.0.0.1:8000/api/assitance/get"
    userAsistenceData, set_userAsistence = hooks.use_state(initial_value="")
    rows, setRows = hooks.use_state(initial_value=[])


    async def getData():
        rows.clear()
        async with aiohttp.ClientSession() as session:
            async with session.get(getUrl) as resp:
                response = await resp.json()
                set_userAsistence(response)
        renderUsers()

    def renderUsers():
        for user in userAsistenceData:
            rows.append(UserAssistence(user))

    hooks.use_effect(getData)

    return html.div(
        html.table(
            {"class": "tableAssistence"},
            html.tr({"class":"titleTable"},
                html.th("username"),
                html.th("nombre"),
                html.th("apellido"),
                html.th("fecha"),
                html.th("hora"),
                html.th("asistencia"),
            ),
            rows,
        ),
    )
