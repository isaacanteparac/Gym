from reactpy import component, html, hooks


@component
def Signup():
    url = "http://127.0.0.1:8000/api/user/create"
    error, set_error = hooks.use_state(initial_value=False)
    textError = "El email o username ya existen"

    return html.form(
        {"action": url, "method": "POST"},
        html.div(
            {"class": "contentColums spaceBlack register"},
            html.input(
                {
                    "required":True,
                    "placeholder": "Nombre",
                    "class": "input top",
                    "name": "first_name",
                    "type": "text",
                }
            ),
            html.input(
                {
                    "placeholder": "Apellido",
                    "class": "input",
                    "name": "last_name",
                    "type": "text",
                    "required":True
                }
            ),
            html.input(
                {
                    "placeholder": "Email",
                    "class": "input",
                    "name": "email",
                    "type": "email",
                    "required":True
                }
            ),
            html.input(
                {
                    "placeholder": "Username",
                    "class": "input",
                    "name": "username",
                    "type": "text",
                    "required":True
                }
            ),
            html.input(
                {
                    "placeholder": "Contraseña",
                    "class": "input",
                    "name": "password",
                    "type": "password",
                    "required":True
                }
            ),
            html.input(
                {
                    "placeholder": "Repetir Contraseña",
                    "class": "input bottom",
                    "name": "passwordRepeat",
                    "type": "password",
                    "required":True
                }
            ),
        ),
        html.button({"class": "btn submit registerBtn", "type": "submit"}, "Log In ➔"),
        error and html.div({"class": "error"}, html.p(textError)),
    )
