import pdb

from src.crawling.session import TikiSession
from src.crawling.static.endpoints import (product_url, products_by_cate_url,
                                           reco_by_pid_url)


class TikiCrawlingApi:

    def __init__(self):
        self.new_session()

    def new_session(self):
        self._sess = TikiSession()

    def get_products_by_cate(self, category=None, limit=300):
        current_page = 1
        last_page = current_page + 1
        while current_page <= last_page:
            try:
                r = self._sess.get(
                    products_by_cate_url(
                        limit=limit, aggregations=1,
                        category=category, page=current_page)).json()
                current_page += 1
                last_page = r['paging']['last_page']
                yield r['data']
            except:
                pass

    def get_subcate_by_category(self, category, id_only=False):
        r = self._sess.get(products_by_cate_url(
            limit=1, aggregations=1,
            category=category, page=1)).json()
        filters = r['filters']
        category = [f for f in filters if f['query_name'] == 'category']
        if len(category):
            category = category[0]['values']
        if id_only:
            category = [i['query_value'] for i in category]
        return category

    def get_product_info(self, id):
        data = dict()
        r = self._sess.get(product_url(id)).json()
        data['id'] = id
        data['category'] = [i for i in r['breadcrumbs'] if i.get('category_id')]
        return data

    def get_product_reco(self, mpid=None):
        r = self._sess.get(reco_by_pid_url(mpid=mpid))
        similar_products = r['widgets']['0']['items']
        maybe_you_like = r['widgets']['1']['items']
        return (similar_products, maybe_you_like)
