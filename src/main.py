#!/usr/bin/env python
# encoding: utf-8

from textual.app import App, ComposeResult
from textual.binding import Binding

import components.main_screen as MainScreen
import components.settings_screen as SettingsScreen
import core.password_manager as pwm

class PasswordManager(App):
    PWM = pwm.PasswordManager()
    CSS_PATH = "style.tcss"
    MENU_ACTIVATED = False
    BINDINGS = [
        Binding(key="ctrl+t", action="show_menu", description="Menu"),
        Binding(key="ctrl+q", action="debug", description="Debug")
    ]

    MODES = {
        "main": MainScreen.MainScreen,
        "settings" : SettingsScreen.SettingsScreen
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
    app = PasswordManager()
    app.run()