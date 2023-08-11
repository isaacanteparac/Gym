from reactpy import html, hooks, component
import aiohttp
from .UserAssistence import UserAssistence


@component
def Assitence():
    getUrl = "http://127.0.0.1:8000/api/assitance/get"
    urlBranch = "http://127.0.0.1:8000/api/branch/get"
    userAsistenceData, set_userAsistence = hooks.use_state(initial_value="")
    branchData, setBranchData = hooks.use_state(initial_value=[])
    rows, setRows = hooks.use_state(initial_value=[])


    async def getData():
        rows.clear()
        branchData.clear()
        async with aiohttp.ClientSession() as session:
            async with session.get(getUrl) as resp:
                user_response = await resp.json()
            async with session.get(urlBranch) as respBranch:
                branch_response = await respBranch.json()
            set_userAsistence(user_response)
            branchData.extend(branch_response)

    def renderUsers():
        for user in userAsistenceData:
            user['branch'] = branchData
            rows.append(UserAssistence(user))
        return rows
    
    async def listUpdate(event):
        await getData()

    hooks.use_effect(getData,[])

    return html.div(
        html.button({"on_click":listUpdate, "type":"button", "class":"btn_update"},"🔄️ Actualizar"),
        html.table(
            {"class": "tableAssistence"},
            html.tr({"class":"titleTable"},
                html.th("username"),
                html.th("nombre"),
                html.th("apellido"),
                html.th("fecha"),
                html.th("hora"),
                html.th("sucursal"),
                html.th("asistencia"),
            ),
            renderUsers(),
        ),
    )
