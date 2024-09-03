# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ServimedPedidoItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    dataCadastro = scrapy.Field()
    situacao = scrapy.Field()
    cliente = scrapy.Field()
    pedidoStatusId = scrapy.Field()
    pedidoStatusDescricao = scrapy.Field()
    categoriaCodigoExterno = scrapy.Field()
    codigoExterno = scrapy.Field()
    cpnj = scrapy.Field()
    valorLiquido = scrapy.Field()
    valorLiquidoFaturado = scrapy.Field()
