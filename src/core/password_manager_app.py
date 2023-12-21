from textual.app import App, ComposeResult
from textual.binding import Binding

from src.components.login_screen import LoginScreen
from src.components.main_screen import MainScreen
from src.components.settings_screen import SettingsScreen
from src.core.password_manager import PasswordManager as pwm

class PasswordManagerApp(App):
    """
    Class for launching the password manager text-based interface

    On startup, launches the login screen.
    On successful login, it initializes PWM-core class and launches the main screen.

    @attr PWM: PasswordManager instance for actual logic
    @attr CSS_PATH: Path to the CSS file
    @attr BINDINGS: Keybindings for quick actions
    """
    PWM = None
    CSS_PATH = "../components/style.tcss"
    BINDINGS = [
        Binding(key="ctrl+t", action="show_menu", description="Menu"),
        Binding(key="ctrl+q", action="debug", description="Debug")
    ]

    def on_mount(self) -> None:
        self.action_request_login()

    def startup(self) -> None:
        """
        Add the pwm-instance, screens and switch to the main screen
        """
        self.PWM = pwm()
        self.add_mode("main", MainScreen)
        self.add_mode("settings", SettingsScreen)
        self.switch_mode("main")

    def action_show_menu(self) -> None:
        """
        Launches the sidebar menu
        """
        if self.current_mode == "main":
            self.MODES["main"].action_show_menu(self)
            return
        if self.current_mode == "settings":
            self.MODES["settings"].action_show_menu(self)
            return
        
    def action_request_login(self) -> None:
        """
        Executes the login for the user.

        If login is successful, it will switch to the main mode.
        If login is not successful, it will notify the user and stay in the login mode.
        """
        def check_login(login: bool) -> None:
            if login:
                self.startup()
                self.app.notify(message="Login successful", title="Login")
            if not login:
                self.app.notify(message="Login failed", title="Login", severity="error")
                self.action_request_login()

        self.push_screen(LoginScreen(id="login_screen"), check_login)

        
if __name__ == "__main__":
    app = PasswordManagerApp()
    app.run()