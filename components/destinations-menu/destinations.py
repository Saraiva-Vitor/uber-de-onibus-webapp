from django_components import component


@component.register("destinations-menu")
class Destinations(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "destinations-menu/destinations.html"

    class Media:
        css = "destinations-menu/destinations.css"
