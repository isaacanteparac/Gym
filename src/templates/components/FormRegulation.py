from reactpy import html, hooks, component, event
import aiohttp


@component
def FormRegulation():
    url = "http://127.0.0.1:8000/api/regulation/create"
    name, setName = hooks.use_state(initial_value="")
    code, setCode = hooks.use_state(initial_value="")
    description, setDescription = hooks.use_state(initial_value="")
    alertShow, setAlertShow = hooks.use_state(initial_value=False)
    alertText, setAlertText = hooks.use_state(initial_value="")

    @event(prevent_default=True)
    async def send(event):
        data = {"name": name, "code": code, "description": description}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                setAlertText(response["msg"])
                setAlertShow(True)
        setName("")
        setCode("")
        setDescription("")

    def closeAlert(event):
        setAlertShow(False)
        setAlertText("")

    return html._(
        html.form(
            {"class": "formOp"},
            html.h2("crear reglamentos"),
            html.label("nombre"),
            html.input(
                {
                    "type": "text",
                    "required": True,
                    "name": "name",
                    "value": name,
                    "on_change": lambda event: setName(event["target"]["value"]),
                }
            ),
            html.label("Codigo"),
            html.input(
                {
                    "required": True,
                    "type": "text",
                    "name": "code",
                    "value": code,
                    "on_change": lambda event: setCode(event["target"]["value"]),
                }
            ),
            html.label("descripcion"),
            html.textarea(
                {
                    "required": True,
                    "name": "description",
                    "value": description,
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
