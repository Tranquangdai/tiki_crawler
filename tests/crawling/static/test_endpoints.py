from src.crawling.static.endpoints import (product_url, products_by_cate_url,
                                           reco_by_pid_url)


def test_build_endpoints():
    url = products_by_cate_url(limit=48, aggregations=1,
                               category=1801, page=1)
    assert url == 'https://tiki.vn/api/v2/products?limit=48&aggregations=1&category=1801&page=1'

    url = reco_by_pid_url(mpid='70842987')
    assert url == 'https://tiki.vn/api/v2/personalization/v2/pdp?mpid=70842987'

    url = product_url('32923633')
    assert url == 'https://tiki.vn/api/v2/products/32923633?include=breadcrumbs'
