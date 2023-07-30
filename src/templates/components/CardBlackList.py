from reactpy import html, hooks, component, event
import aiohttp


@component
def CardBlackList(data):
    url = "http://127.0.0.1:8000/api/blacklist/delete/" + str(data["id"])
    fullnane = f"{data['first_name']} {data['last_name']} ({data['username']})"
    code = f"Codigo: {data['codeRegulation']}"
    codeName = f"Nombre del codigo: {data['titleRegulation']}"
    @event(prevent_default=True)
    async def delete(event):
        async with aiohttp.ClientSession() as session:
            async with session.delete(url) as resp:
                response = await resp.json()
                print(response)

    return html.div(
        {"class": "cardRegulation"},
        html.h3(fullnane),
        html.label(code),
        html.label(codeName),
        html.p(data["reason"]),
        html.button(
            {"type": "button", "on_click": delete},
            "Eliminar",
        ),
    )
