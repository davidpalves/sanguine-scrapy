import re

def create_queryset_filters(cidade='', estado='', banco=''):
        filter = {}
        if cidade: filter['cidade'] = re.compile('^' + re.escape(cidade) + '$', re.IGNORECASE)
        if estado: filter['estado'] = re.compile('^' + re.escape(estado) + '$', re.IGNORECASE)
        if banco: filter['banco'] = re.compile('^' + re.escape(banco) + '$', re.IGNORECASE)

        return filter

def build_email_body(recipient_name):
        EMAIL_BODY = (
                f"Olá, {recipient_name}, " +
                "notamos que há bancos " +
                "de sangue na sua região " +
                "com os estoques de sangue " +
                "em estado de alerta ou crítico. \n" +
                "pelos nossos cálculos, você já está uma pessoa apta para doar, "
                "então que tal tirar um tempinho para salvar vidas?"
        )

        return EMAIL_BODY