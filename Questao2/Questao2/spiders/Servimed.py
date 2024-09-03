import base64
import json
import scrapy
from typing import Iterable
from scrapy.http import Response, Request
from scrapy.http.cookies import CookieJar
from ..items import ServimedPedidoItem


class ServimedSpider(scrapy.Spider):
    name      = "servimed"
    url       = "https://pedidoeletronico.servimed.com.br"
    api_url   = "https://peapi.servimed.com.br"


    def __init__(self, login: str, password: str, pedido: int, **kw) -> None:
        super(ServimedSpider, self).__init__(**kw)
        self.login = login
        self.password = password
        self.pedido = pedido


    def get_access_token(self, response: Response) -> str:
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        return cookie_jar._cookies['.servimed.com.br']["/"]["accesstoken"].value


    def get_access_token_id(self, token: str) -> str:
        header, jwt, signature = token.split(".")
        decoded = base64.urlsafe_b64decode(jwt + '=' * (4 - len(jwt) % 4))
        json_data = json.loads(decoded)
        return json_data["token"]


    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request(
            url=f"{self.api_url}/api/usuario/login",
            method="POST",
            headers={"Content-Type": "application/json"},
            body=json.dumps({"usuario": self.login, "senha": self.password}),
            callback=self.after_login
        )


    def after_login(self, response: Response) -> Iterable[Request]:
        if response.status != 200:
            self.logger.error("Falha no login")
            return

        self.logger.info("Login efetuado com sucesso")

        access_token = self.get_access_token(response)
        json_response = json.loads(response.body)
        codigo_externo = json_response["usuario"]["codigoExterno"]
        codigo_usuario = json_response["usuario"]["codigoUsuario"]
        users = json_response["usuario"]["users"]

        self.logger.info(f"Buscando pedido {self.pedido}")

        yield scrapy.Request(
            url=f"{self.api_url}/api/Pedido",
            method="POST",
            headers={
                "Content-Type": "application/json",
                "contentType": "application/json",
                "accesstoken": self.get_access_token_id(access_token),
                "loggedUser": codigo_usuario
            },
            body=json.dumps({
                "dataInicio": "",
                "dataFim": "",
                "filtro": str(self.pedido),
                "pagina": 1,
                "registrosPorPagina": 10,
                "codigoExterno": codigo_externo,
                "codigoUsuario": codigo_usuario,
                "kindSeller": 0,
                "users": users
            }),
            callback=self.parse
        )


    def parse(self, response: Response) -> Iterable[ServimedPedidoItem]:
        if response.status != 200:
            self.logger.error(f"Falha ao buscar pedido {self.pedido}")
            return

        json_response = json.loads(response.body)
        total_registros = json_response["totalRegistros"]
        lista = json_response["lista"]
        if total_registros == 0:
            self.logger.error(f"Pedido {self.pedido} não encontrado")
            return

        pedido = lista[0]
        self.logger.info(f"Pedido {self.pedido} encontrado")
        self.logger.info(f"Situação: {pedido['situacao']}")

        yield ServimedPedidoItem(
            id=pedido["id"],
            dataCadastro=pedido["dataCadastro"],
            situacao=pedido["situacao"],
            cliente=pedido["cliente"],
            pedidoStatusId=pedido["pedidoStatusId"],
            pedidoStatusDescricao=pedido["pedidoStatusDescricao"],
            categoriaCodigoExterno=pedido["categoriaCodigoExterno"],
            codigoExterno=pedido["codigoExterno"],
            cpnj=pedido["cpnj"],
            valorLiquido=pedido["valorLiquido"],
            valorLiquidoFaturado=pedido["valorLiquidoFaturado"]
        )
