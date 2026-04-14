from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from components.navigation.sidebar_item_list_component import SidebarItemListComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item =SidebarItemListComponent(page, identifier='logout')
        self.courses_list_item = SidebarItemListComponent(page, identifier='courses')
        self.dashboard_list_item = SidebarItemListComponent(page, identifier='dashboard')

    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')
