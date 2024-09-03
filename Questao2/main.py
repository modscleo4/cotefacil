from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import argparse
import os


def main() -> None:
    if not os.getenv("LOGIN") or not os.getenv("PASSWORD"):
        raise ValueError("Variáveis de ambiente LOGIN e PASSWORD não definidas")

    parser = argparse.ArgumentParser(description="Script para obter o retorno de faturamento do pedido na Servimed")
    parser.add_argument("pedido", type=int, help="Número do pedido")
    args = parser.parse_args()

    pedido = args.pedido

    settings = get_project_settings()
    configure_logging(settings)
    process = CrawlerProcess(settings)
    process.crawl("servimed", login=os.getenv("LOGIN"), password=os.getenv("PASSWORD"), pedido=pedido)
    process.start()


if __name__ == "__main__":
    main()
