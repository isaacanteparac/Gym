from reactpy import html, hooks, component, event
import aiohttp


@component
def CardGymBranch(data):
    url = "http://127.0.0.1:8000/api/branch/put/" + str(data["id"])
    urlDelete = "http://127.0.0.1:8000/api/branch/delete/" + str(data["id"])
    name, setName = hooks.use_state(initial_value=data["name"])
    phone, setPhone = hooks.use_state(initial_value=data["phone"])
    location, setLocation = hooks.use_state(initial_value=data["location"])
    open_, setOpen = hooks.use_state(initial_value=bool(data["open"]))
    text_, setText = hooks.use_state("")

    edit, setEdit = hooks.use_state(initial_value=False)

    @event(prevent_default=True)
    async def update(event):
        setEdit(False)
        setOpen(bool(open_))
        data = {"name": name, "phone": phone, "location": location, "open": open_}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                print(response)

    @event(prevent_default=True)
    async def delete(event):
        setEdit(False)
        async with aiohttp.ClientSession() as session:
            async with session.delete(urlDelete) as resp:
                response = await resp.json()
                print(response)

    def cancelEdit(event):
        setEdit(False)
        setName(data["name"])
        setPhone(data["phone"])
        setLocation(data["location"])
        setOpen(data["open"])

    def openState():
        if open_:
            setText("Abierto")
            return text_
        else:
            setText("Cerrado")
            return text_

    def toggle(event):
        toggle_state = not open_
        setOpen(toggle_state)


    return html.div(
        {"class": "card"},
        edit
        and html.div(
            {"class": "editForm"},
            html.label("nombre:"),
            html.input(
                {
                    "required": True,
                    "on_change": lambda event: setName(event["target"]["value"]),
                    "value": name,
                }
            ),
            html.label("Ubicacion:"),
            html.input(
                {
                    "required": True,
                    "on_change": lambda event: setLocation(event["target"]["value"]),
                    "value": location,
                }
            ),
            html.label("Telefono:"),
            html.input(
                {
                    "required": True,
                    "on_change": lambda event: setPhone(event["target"]["value"]),
                    "value": phone,
                }
            ),
            html.label("Abierto:"),
            html.input({"type": "checkbox", "on_click": toggle, "checked": open_}),
            html.div(
                html.div(
                    {"class": "twoButton"},
                    html.button({"type": "button", "on_click": update}, "actualizar"),
                    html.button({"type": "button", "on_click": delete}, "Eliminar"),
                ),
                html.button({"type": "button", "on_click": cancelEdit}, "cancelar"),
            ),
        )
        or html._(
            html.label({"class":"subTitle"},"nombre de sucursal:"),
            html.label(name),
            html.label({"class":"subTitle"},"ubicacion:"),
            html.label(location),
            html.label({"class":"subTitle"},"Telefono o celular:"),
            html.label(phone),
            html.label({"class":"subTitle"},"Abierto:"),
            html.label(openState()),
            html.button(
                {"type": "button", "on_click": lambda event: setEdit(True)},
                "opciones",
            ),
        ),
    )
