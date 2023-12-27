from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Header, Button, Input, Label, Footer
from textual.screen import ModalScreen

class LoginScreen(ModalScreen[bool]):
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("Username", classes="label"),
            Input(placeholder="Username", id="username_input"),
            Label("Password", classes="label"),
            Input(placeholder="Password", classes="password_input", password=True),
            Container(
                Button("Login", id="login_button"),
                Button("Register", id="register_button")
            )    
        )

    def action_register(self) -> None:
        info = None
        def get_user_info(user_info: dict) -> None:
            info = user_info

        self.app.push_screen(RegisterForm(), variable = get_user_info)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "login_button":
            self.dismiss(True) 
        if event.button.id == "register_button":
            user_info = self.action_register()
            print(user_info) 

class RegisterForm(ModalScreen[dict]):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("Username", classes="label"),
            Input(placeholder="Username", id="username_register"),
            Label("Master password", classes="label"),
            Input(placeholder="Master password", classes="password_input", id="password_register", password=True),
            Label("Retype master password", classes="label"),
            Input(placeholder="Retype", classes="password_input", password=True)
        )
        yield Container(
            Button("Register", id="register_confirm_button"),
            Button("Cancel", id="cancel_button")
            )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "register_confirm_button":
            userinfo = {
                "username": self.query_one("#username_register").value,
                "password": self.query_one("#password_register").value
            }
            self.dismiss(userinfo)
        if event.button.id == "cancel_button":
            self.dismiss(None)