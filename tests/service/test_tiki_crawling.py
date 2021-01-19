from src.service.tiki_crawling import TikiCrawlingService

service = TikiCrawlingService()


def test_get_all_subcate():
    result = service.get_all_subcate('1818')
    print(result)
