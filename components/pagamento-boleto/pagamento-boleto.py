from django_components import component


@component.register("pagamento-boleto")
class PagamentoBoleto(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "pagamento-boleto/pagamento-boleto.html"

    class Media:
        css = "pagamento-boleto/pagamento-boleto.css"
