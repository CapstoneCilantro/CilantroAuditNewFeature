import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from mongoengine import connect
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from cilantro_audit.constants import KIVY_REQUIRED_VERSION, CREATE_COMPLETED_AUDIT_PAGE
from cilantro_audit.constants import PROD_DB
from cilantro_audit.audit_template import AuditTemplate
from cilantro_audit.templates.audit_button import AuditButtonTemplate

# Required Version
kivy.require(KIVY_REQUIRED_VERSION)

Builder.load_file("./widgets/view_audit_templates.kv")



# Handles the retrieval of audit templates for the auditor screens.
class ViewAuditTemplates(Screen):
    # Holds the list of titles retrieved from the database.
    templates_list = ObjectProperty()
    root = ObjectProperty()
    connect(PROD_DB)

    # Constructor utilizes the only method to retrieve audits for use in the associated .kv file.
    def __init__(self, **kw):
        super().__init__(**kw)
        self.titles = []
        self.get_audit_templates()

    # Gets audit template titles for display in the page. Retrieves only title for faster retrieval time.
    def get_audit_templates(self):
        titles = list(map(lambda template: template.title, AuditTemplate.objects().only('title')))
        for title in titles:
            self.templates_list.add_widget(Button(text=title, on_press=self.load_page(title=title)))


    def load_page(self, title):
        self.root.manager.get_screen(CREATE_COMPLETED_AUDIT_PAGE).populate_audit(target=title)

class TestApp(App):
    def build(self):
        return ViewAuditTemplates()


if __name__ == '__main__':
    TestApp().run()
