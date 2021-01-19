from src.crawling.apis.web import TikiCrawlingApi

api = TikiCrawlingApi()


def test_get_products_by_cate():
    gen = api.get_products_by_cate(category='1801')
    result = next(gen)
    assert len(result) == 300


def test_get_product_info():
    result = api.get_product_info(32923633)
    print(result)
