from src.crawling.apis.web import TikiCrawlingApi
from src.utils.parser import parse_product_info


class TikiCrawlingService:

    def __init__(self):
        self.api = TikiCrawlingApi()

    def crawl_products_by_cate(self, cid=None, limit=300):
        # if category in list(CATEGORY_ID.values()):
        if not isinstance(cid, str):
            cid = str(cid)
        result = []
        gen = self.api.get_products_by_cate(cid, limit)
        for batch in gen:
            if not len(batch):
                continue
            tmp = [parse_product_info(item) for item in batch]
            result.extend(tmp)
        return result

    def get_all_subcate(self, c0):
        result = []
        c1 = self.api.get_subcate_by_category(c0, id_only=True)
        for _ in c1:
            c2 = self.api.get_subcate_by_category(_, id_only=True)
            if len(c2):
                for _ in c2:
                    c3 = self.api.get_subcate_by_category(_, id_only=True)
                    if len(c3):
                        result.extend(c3)
                    else:
                        result.extend(c2)
            else:
                result.extend(c1)
        return list(set(result))
