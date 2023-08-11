from reactpy import html, hooks, component, event
import aiohttp


@component
def UserAssistence(data):
    assitenceState, setAssitenceState = hooks.use_state(eval(str(data["state"])))
    color, setColor = hooks.use_state({"background-color": "#f0f0f0"})
    url = "http://127.0.0.1:8000/api/assitance/put/" + str(data["id"])
    idBranch, setIdBranch = hooks.use_state(initial_value=0)

    @event(prevent_default=True)
    async def send(event):
        color_()
        data = {"state": assitenceState, "idBranch": idBranch}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                setIdBranch(0)
                print(response)

    def createOnClickHandler(id):
        setIdBranch(id)

    def renderBranch():
        row = []
        for branchOne in data['branch']:
            row.append(html.option({"value": branchOne["id"], "on_click":createOnClickHandler(branchOne["id"])}, branchOne["name"]))
        return row

    def toggle(event):
        toggle_state = not assitenceState
        setAssitenceState(toggle_state)
    

    def color_():
        if assitenceState:
            setColor({"background-color": "#0076ff", "color": "white"})
        else:
            setColor({"background-color": "#f0f0f0", "color": "black"})

    hooks.use_effect(color_, [])

    return html.tr(
        {"id": data["id"], "class": "contentTable"},
        html.td(data["username"]),
        html.td(data["first_name"]),
        html.td(
            data["last_name"],
        ),
        html.td(
            data["date"],
        ),
        html.td(
            data["hour"],
        ),
        html.td(
            html.select(
                {
                    "name": "idBranch"
                },
                renderBranch(),
            )
        ),
        html.td(
            html.input(
                {"type": "checkbox", "on_click": toggle, "checked": assitenceState}
            )
        ),
        html.td(
            html.button({"class": "save", "on_click": send, "style": color}, "Guardar"),
        ),
    )
