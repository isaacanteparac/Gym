from reactpy import html, hooks, component, event
import aiohttp


@component
def FormBlackList():
    url = "http://127.0.0.1:8000/api/blacklist/create"
    username, setUsername = hooks.use_state(initial_value="")
    codeRegulation, setCodeRegulation = hooks.use_state(initial_value="")
    description, setDescription = hooks.use_state(initial_value="")
    alertShow, setAlertShow = hooks.use_state(initial_value=False)
    alertText, setAlertText = hooks.use_state(initial_value="")

    @event(prevent_default=True)
    async def send(event):
        data = {
            "username": username,
            "codeRegulation": codeRegulation,
            "reason": description,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                setAlertText(response["msg"])
                setAlertShow(True)

    def closeAlert(event):
        setAlertShow(False)
        setAlertText("")

    return html._(
        html.form(
            {"class": "formOp"},
            html.h2("Añadir a lista negra"),
            html.label("username:"),
            html.input(
                {
                    "required": True,
                    "type": "text",
                    "name": "username",
                    "on_change": lambda event: setUsername(event["target"]["value"]),
                }
            ),
            html.label("Codigo de reglamento:"),
            html.input(
                {
                    "required": True,
                    "type": "text",
                    "name": "code",
                    "on_change": lambda event: setCodeRegulation(
                        event["target"]["value"]
                    ),
                }
            ),
            html.label("Rasón de sanción:"),
            html.textarea(
                {
                    "required": True,
                    "name": "reason",
                    "on_change": lambda event: setDescription(event["target"]["value"]),
                }
            ),
            html.button({"type": "button", "on_click": send}, "guardar"),
        ),
        alertShow
        and html.div(
            {"class": "alert"},
            html.label(alertText),
            html.button({"type": "button", "on_click": closeAlert}, "X"),
        )
        or html._(),
    )
