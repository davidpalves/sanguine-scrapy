import re

def create_queryset_filters(cidade='', estado='', banco=''):
        filter = {}
        if cidade: filter['cidade'] = re.compile('^' + re.escape(cidade) + '$', re.IGNORECASE)
        if estado: filter['estado'] = re.compile('^' + re.escape(estado) + '$', re.IGNORECASE)
        if banco: filter['banco'] = re.compile('^' + re.escape(banco) + '$', re.IGNORECASE)

        return filter
