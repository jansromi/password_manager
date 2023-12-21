from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Header, Button, Input, Label
from textual.screen import ModalScreen

class LoginScreen(ModalScreen[bool]):
    LOGIN_SCREEN_ID = "login"
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("Username", classes="label"),
            Input(placeholder="Username", id="username_input"),
            Label("Password", classes="label"),
            Input(placeholder="Password", id="password_input", password=True),
            Container(
                Button("Login", id="login_button"),
                Button("Cancel", id="cancel_button")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "login_button":
            self.dismiss(True) 
        if event.button.id == "cancel_button":
            self.dismiss(False)
