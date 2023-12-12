#!/usr/bin/env python
# encoding: utf-8

import npyscreen
import components.main_form as MainForm
import components.settings_form as SettingsForm

class PasswordManagerApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm.MainForm(cycle_widgets=True))
        self.registerForm("SETTINGS", SettingsForm.SettingsForm(cycle_widgets=True))

def main():
    PMA = PasswordManagerApp()
    PMA.run()

if __name__ == '__main__':
    main()