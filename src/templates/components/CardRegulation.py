from reactpy import html, hooks, component, event
import aiohttp


@component
def CardRegulation(data):
    url = "http://127.0.0.1:8000/api/regulation/put/" + str(data["id"])
    name, setName = hooks.use_state(initial_value=data["name"])
    code, setCode = hooks.use_state(initial_value=data["code"])
    description, setDescription = hooks.use_state(initial_value=data["description"])
    edit, setEdit = hooks.use_state(initial_value=False)

    @event(prevent_default=True)
    async def update(event):
        setEdit(False)
        data = {"name": name, "description": description}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                print(response)

    def cancelEdit(event):
        setEdit(False)
        setName(data["name"])
        setDescription(data["description"])

    return html.div(
        {"class": "cardRegulation"},
        edit
        and html.div(
            html.input(
                {
                    "on_change": lambda event: setName(event["target"]["value"]),
                    "placeholder": "titulo",
                    "value": name,
                }
            ),
            html.label(
                {"placeholder": "Codigo", "value": "codigo" + code, "disabled": True}
            ),
            html.label("descripcion"),
            html.textarea(
                {
                    "on_change": lambda event: setDescription(event["target"]["value"]),
                    "value": description,
                }
            ),
            html.div(
                html.button({"type": "button", "on_click": cancelEdit}, "cancelar"),
                html.button({"type": "button", "on_click": update}, "actualizar"),
            ),
        )
        or html.h3(name),
        html.label(code),
        html.p(description),
        html.button(
            {"type": "button", "on_click": lambda event: setEdit(True)},
            "Editar descripcion",
        ),
    )
