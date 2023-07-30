from reactpy import html, hooks, component, event
import aiohttp


@component
def FormRegulation():
    url = "http://127.0.0.1:8000/api/regulation/create"
    name, setName = hooks.use_state(initial_value="")
    code, setCode = hooks.use_state(initial_value="")
    description, setDescription = hooks.use_state(initial_value="")

    @event(prevent_default=True)
    async def send(event):
        data = {"name": name, "code": code, "description": description}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                print(response)

    return html.form(
        {"class": "form"},
        html.input(
            {
                "type": "text",
                "required": True,
                "placeholder": "Titulo",
                "name": "name",
                "on_change": lambda event: setName(event["target"]["value"]),
            }
        ),
        html.input(
            {
                "required": True,
                "type": "text",
                "placeholder": "Codigo",
                "name": "code",
                "on_change": lambda event: setCode(event["target"]["value"]),
            }
        ),
        html.textarea(
            {
                "required": True,
                "name": "description",
                "on_change": lambda event: setDescription(event["target"]["value"]),
            }
        ),
        html.button({"type": "button", "on_click": send}, "enviar"),
    )
