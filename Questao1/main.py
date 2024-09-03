from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import os


def main() -> None:
    if not os.getenv("LOGIN") or not os.getenv("PASSWORD"):
        raise ValueError("Variáveis de ambiente LOGIN e PASSWORD não definidas")

    settings = get_project_settings()
    configure_logging(settings)
    process = CrawlerProcess(settings)
    process.crawl("compra-agora", login=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))
    process.start()


if __name__ == "__main__":
    main()
