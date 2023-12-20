from components.sidebar import Sidebar
from components.main_screen import Searchbar
from core.password_manager_app import PasswordManagerApp

async def test_launch():
    app = PasswordManagerApp()
    async with app.run_test() as pilot:
        # in login screen, skip it for now
        await pilot.press("tab")
        await pilot.press("tab")
        await pilot.press("enter")

        # press a key
        await pilot.press("a")
        # value of the searchbar should be "a"
        assert app.query_one(Searchbar).value == "a"
        
        await pilot.press("ctrl+t")
        # sidebar should be open, ie. has class "-active"
        sidebar = app.query_one(Sidebar)
        assert sidebar.has_class("-active")

        menulist = sidebar.query_one("#sidebar_listview")
        # menulist should be focused
        assert menulist.has_focus

