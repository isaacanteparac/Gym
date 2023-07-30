from reactpy import html, hooks, component, event
import aiohttp

@component
def UserAssistence(data):
    assitenceState, setAssitenceState = hooks.use_state(eval(str(data["state"])))
    color, setColor = hooks.use_state({"background-color":"#f0f0f0"})
    url = "http://127.0.0.1:8000/api/assitance/put/" + str(data["id"])

    @event(prevent_default=True)
    async def send(event):
        color_()
        data = {"state": assitenceState}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                response = await resp.json()
                print(response)

    def toggle(event):
        toggle_state = not assitenceState
        setAssitenceState(toggle_state)

    def color_():
        if assitenceState:
            setColor({"background-color":"#0076ff", "color":"white"})
        else:
            setColor({"background-color":"#f0f0f0", "color":"black"})
    
    hooks.use_effect(color_, [])

    return html.tr(
        {"id": data["id"],"class":"contentTable"},
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
            html.input(
                {"type":"checkbox","on_click": toggle, "checked":assitenceState}
            )
        ),
        html.td(
            html.button({"class":"save","on_click": send, "style":color}, "Guardar"),
        ),
    )
