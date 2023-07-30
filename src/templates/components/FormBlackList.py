from reactpy import html, hooks, component, event
import aiohttp


@component
def FormBlackList():
    url = "http://127.0.0.1:8000/api/blacklist/create"
    username, setUsername = hooks.use_state(initial_value="")
    codeRegulation, setCodeRegulation = hooks.use_state(initial_value="")
    description, setDescription = hooks.use_state(initial_value="")

    @event(prevent_default=True)
    async def send(event):
        data = {"username": username, "codeRegulation": codeRegulation, "reason": description}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                print(response)

    return html.form(
        {"class": "form"},
        html.input(
            {
                "required": True,
                "type": "text",
                "placeholder": "Username",
                "name": "username",
                "on_change": lambda event: setUsername(event["target"]["value"]),
            }
        ),
        html.input(
            {
                "required": True,
                "type": "text",
                "placeholder": "Codigo de reglamento",
                "name": "code",
                "on_change": lambda event: setCodeRegulation(event["target"]["value"]),
            }
        ),
        html.textarea(
            {
                "required": True,
                "name": "reason",
                "on_change": lambda event: setDescription(event["target"]["value"]),
            }
        ),
        html.button({"type": "button", "on_click": send}, "enviar"),
    )