from typing import Iterable
import json
import scrapy
from scrapy.http import Response, HtmlResponse, Request
from ..items import CompraAgoraProdutoItem


class CompraAgoraSpider(scrapy.Spider):
    name = "compra-agora"
    url = "https://www.compra-agora.com"


    def __init__(self, login: str, password: str, **kw) -> None:
        super(CompraAgoraSpider, self).__init__(**kw)
        self.login = login
        self.password = password


    def start_requests(self) -> Iterable[Request]:
        self.logger.info("Buscando itens por categoria")
        yield scrapy.Request(
            url=self.url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"
            },
            callback=self.parse_categories
        )


    def parse_categories(self, response: HtmlResponse) -> Iterable[Request]:
        for category in response.css("li.lista-menu-itens a"):
            name = str(category.xpath('./text()[2]').get()).strip()
            if name == "Novidades":
                yield scrapy.Request(
                    url=str(category.css("::attr(href)").get()),
                    callback=self.parse_html
                )

            self.logger.info(f"Capturando produtos da categoria: {name}...")
            api_url = str(category.css("::attr(href)").get()).replace('/loja/', '/api/catalogproducts/')

            yield scrapy.Request(
                url=api_url,
                callback=self.parse
            )


    def parse(self, response: Response) -> Iterable[CompraAgoraProdutoItem]:
        json_response = json.loads(response.body)
        for product in json_response["produtos"]:
            yield CompraAgoraProdutoItem(
                name=product["Nome"],
                manufacter=product["Marca"],
                barcode=product["Codigo"],
                image_url='https://images-unilever.ifcshop.com.br/200x200/produto/' + product["Foto"]
            )


    def parse_html(self, response: HtmlResponse) -> Iterable[CompraAgoraProdutoItem]:
        for product in response.css("div#divProdutos ul li"):
            yield CompraAgoraProdutoItem(
                name=str(product.css("div.produto-nome::text").get()).strip(),
                manufacter=str(product.css("div.produto-marca::text").get()).strip(),
                barcode=str(product.css("div.produto-ean p").xpath('./text()[2]').get()).strip()[2:],
                image_url=str(product.css("img.img-fluid::attr(src)").get()).strip()
            )
