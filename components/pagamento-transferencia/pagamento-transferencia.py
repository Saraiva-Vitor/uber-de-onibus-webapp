from django_components import component


@component.register("pagamento-transferencia")
class PagamentoTranferencia(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "pagamento-transferencia/pagamento-transferencia.html"

    class Media:
        css = "pagamento-transferencia/pagamento-transferencia.css"
