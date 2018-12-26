XPATH_ITEMS = {
    'hemato': '//div[contains(@class,"item-estoque")]',
    'hemope': '//ul[contains(@class,"list-estoque")]/li'
}

XPATH_TIPO_SANGUE = {
    'hemato': './/div[contains(@class, tipo-sangue)][2]/text()',
    'hemope': './/strong/text()'
}

XPATH_NIVEL_SANGUE = {
    'hemato': './/div[contains(@class, "knob")]/@data-val[1]',
    'hemope': './/div[contains(@class,"bolsa")]/div[2]/@class'
}
