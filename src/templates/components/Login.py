from reactpy import component, html, hooks
import aiohttp


@component
def Login():
    url = "http://127.0.0.1:8000/api/user/auth"

    error, set_error = hooks.use_state(initial_value=False)

    textError = "Ingrese correctamente el usuario o contraseña"

    return html.form(
        {"action": url, "method": "POST"},
        html.div(
            {"class": "contentColums spaceBlack register"},
            html.input(
                {
                    "required": True,
                    "placeholder": "username",
                    "class": "input top",
                    "name": "username",
                    "type": "text",
                }
            ),
            html.input(
                {
                    "required": True,
                    "placeholder": "contraseña",
                    "class": "input bottom",
                    "name": "password",
                    "type": "password",
                }
            ),
        ),
        html.button({"class": "btn submit registerBtn", "type": "submit"}, "Log In ➔"),
        error and html.div({"class": "error"}, html.p(textError)),
    )
