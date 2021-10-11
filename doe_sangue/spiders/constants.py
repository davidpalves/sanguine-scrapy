XPATH_ITEMS = {
    "hemato": '//div[contains(@class,"item-estoque")]',
    "hemope": '//ul[contains(@class,"list-estoque")]/li',
}

XPATH_TIPO_SANGUE = {
    "hemato": ".//div[contains(@class, tipo-sangue)][2]/text()",
    "hemope": ".//strong/text()",
}

XPATH_NIVEL_SANGUE = {
    "hemato": './/div[contains(@class, "knob")]/@data-val[1]',
    "hemope": './/div[contains(@class,"bolsa")]/div[2]/@class',
}

XPATH_PAGES = {
    "hemato": './/li[a[@title="Unidades"]]/ul[contains(@class, "dropdown-menu")]/li/a'
}

XPATH_PLACE_NAME = {
    "hemato": '//div[contains(@class, "container-segura")]/section/div/div[1]/p[3]/text()',
    "hemope": "//footer/div[2]//p/img/@alt",
}

XPATH_ADDRESS = {
    "hemato": '//div[contains(@class, "container-segura")]/section/div/div[1]/p[1]/text()',
    "hemope": "//address/text()",
}

XPATH_CITY = {
    "hemato": '//div[contains(@class, "container-segura")]/section/div/div[1]/p[3]/text()'
}

XPATH_CITY_WITHOUT_COMPLEMENT = {
    "hemato": '//div[contains(@class, "container-segura")]/section/div/div[1]/p[2]/text()'
}
