import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from audit_template import AuditTemplate
from create_audit_page import ConfirmationPop
from mongoengine import connect

kivy.require('1.11.1')

connect("toost")

class ViewAuditsPage(Screen, App):

    def build(self):
        # Initialize page information and layout
        self.title = 'CilantroAudit - View Audits Page'
        page_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        # https://kivy.org/doc/stable/api-kivy.uix.scrollview.html?highlight=view#
        page_layout.bind(minimum_height=page_layout.setter('height'))

        # Get a list of strings - the AuditTemplate's titles - from the database
        audits_list = list(map(lambda obj: obj.title, AuditTemplate.objects.only('title')))

        # Add AuditTemplate buttons to the page
        for title in audits_list:
            page_layout.add_widget(Button(text=title,
                                          font_size=30,
                                          size_hint_y=None,
                                          on_press=self.go_to_page))

        # https://kivy.org/doc/stable/api-kivy.uix.scrollview.html?highlight=view#
        root = ScrollView(size_hint=(1,None),
                          size=(Window.width, Window.height),
                          do_scroll_x=False)

        # Add bottom bar to the page
        bottom_layout = GridLayout(cols=2)
        bottom_layout.add_widget(Button(text='Return To Homepage',
                                        font_size=20,
                                        on_press=self.back(root.manager)))
        bottom_layout.add_widget(Button(text='Exit',
                                        font_size=20,
                                        size_hint=(.4, .2),
                                        on_press=self.exit()))
        page_layout.add_widget(bottom_layout)

        root.add_widget(page_layout)
        return root

    def back(self, manager):
        show = ConfirmationPop()
        show.manager = manager
        show.open()

    def exit(self):
        exit(1)

    def go_to_page(self):
        return


if __name__ == '__main__':
    ViewAuditsPage().run()
