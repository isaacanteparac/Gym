from reactpy import html, hooks, component, event
import aiohttp


@component
def FormGymBranch():
    url = "http://127.0.0.1:8000/api/branch/create"
    name, setName = hooks.use_state(initial_value="")
    phone, setPhone = hooks.use_state(initial_value="")
    location, setLocation = hooks.use_state(initial_value="")
    open_, setOpen = hooks.use_state(initial_value=False)
    alertShow, setAlertShow = hooks.use_state(initial_value=False)
    alertText, setAlertText = hooks.use_state(initial_value="")

    @event(prevent_default=True)
    async def send(event):
        setOpen(bool(open_))
        data = {"name": name, "phone": phone, "location": location, "open": open_}
        print(data)
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                setAlertText(response["msg"])
                setAlertShow(True)
        setName("")
        setPhone("")
        setLocation("")
        setOpen(False)

    def toggle(event):
        toggle_state = not open_
        setOpen(toggle_state)

    def closeAlert(event):
        setAlertShow(False)
        setAlertText("")


    return html._(
        html.form(
            {"class": "formOp"},
            html.h2("crear sucursal"),
            html.label("nombre:"),
            html.input(
                {
                    "type": "text",
                    "required": True,
                    "name": "name",
                    "value": name,
                    "on_change": lambda event: setName(event["target"]["value"]),
                }
            ),
            html.label("ubicacion:"),
            html.input(
                {
                    "required": True,
                    "type": "text",
                    "name": "location",
                    "value": location,
                    "on_change": lambda event: setLocation(event["target"]["value"]),
                }
            ),
            html.label("telefono:"),
            html.input(
                {
                    "required": True,
                    "name": "phone",
                    "value": phone,
                    "on_change": lambda event: setPhone(event["target"]["value"]),
                }
            ),
            html.label("Abierto:"),
            html.input({"type": "checkbox", "on_click": toggle, "checked": open_}),
            html.button({"type": "button", "on_click": send}, "enviar"),
        ),
        alertShow
        and html.div(
            {"class": "alert"},
            html.label(alertText),
            html.button({"type": "button", "on_click": closeAlert}, "X"),
        )
        or html._(),
    )
