from reactpy import html, hooks, component
from .FormGymBranch import FormGymBranch
from .CardGymBranch import CardGymBranch
import aiohttp



@component
def GymBranch():
    getUrl = "http://127.0.0.1:8000/api/branch/get"
    branchData, setBranchData = hooks.use_state(initial_value="")
    rows, setRows = hooks.use_state(initial_value=[])

    async def getData():
        rows.clear()
        async with aiohttp.ClientSession() as session:
            async with session.get(getUrl) as resp:
                response = await resp.json()
                setBranchData(response)
        renderUsers()

    def renderUsers():
        for branch in branchData:
            rows.append(CardGymBranch(branch))

    # poner el         rows
    
    #hooks.use_effect(getData,[])

    return html.div(
        {"class":"wrapper"},
        FormGymBranch(),
    )
