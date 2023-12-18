#!/usr/bin/env python
# encoding: utf-8

from textual.app import App, ComposeResult
from textual.binding import Binding

from src.components.main_screen import MainScreen
from src.components.settings_screen import SettingsScreen
from src.core.password_manager import PasswordManager as pwm

class PasswordManagerApp(App):
    PWM = pwm()
    CSS_PATH = "style.tcss"
    MENU_ACTIVATED = False
    BINDINGS = [
        Binding(key="ctrl+t", action="show_menu", description="Menu"),
        Binding(key="ctrl+q", action="debug", description="Debug")
    ]

    MODES = {
        "main": MainScreen,
        "settings" : SettingsScreen
    }

    def on_mount(self) -> None:
        self.switch_mode("main")

    def action_show_menu(self) -> None:
        if self.current_mode == "main":
            self.MODES["main"].action_show_menu(self)
            return
        if self.current_mode == "settings":
            self.MODES["settings"].action_show_menu(self)
            return
        
if __name__ == "__main__":
    app = PasswordManagerApp()
    app.run()