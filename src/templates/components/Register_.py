from reactpy import html, hooks, component
from .Login import Login
from .Signup import Signup


@component
def Register():
    showForms, setForms = hooks.use_state(initial_value=True)
    return html._(
        html.nav(
            {"class": "navRegister"},
            html.ul(
                {"class": "navRegister_ul"},
                html.li(
                    {"class": "navRegister_li"},
                    html.a({"on_click": lambda event: setForms(True)}, "Log in"),
                ),
                html.li(
                    {"class": "navRegister_li"},
                    html.a({"on_click": lambda event: setForms(False)}, "Sign up"),
                ),
            ),
        ),
        showForms and Login() or Signup(),
    )
