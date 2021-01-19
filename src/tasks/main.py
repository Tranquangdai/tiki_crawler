import json
import pdb
from os.path import join

import pandas as pd
from src import APP_DIR
from src.crawling.static.category import CATEGORY_ID
from src.service.tiki_crawling import TikiCrawlingService
from src.utils.logger import get_logger
from tqdm import tqdm

logger = get_logger(__name__)
service = TikiCrawlingService()


def save_all_tiki_product():
    for cate_name, cate_id in CATEGORY_ID.items():
        logger.info(f'Crawl product for cate {cate_name}')
        result = service.crawl_products_by_cate(cate_id)
        result = pd.DataFrame(result)
        result['cate_id'] = cate_id
        result.to_csv(join(APP_DIR, '_data', f'{cate_name}.csv'), index=False)


def get_all_tiki_cate():
    data = []
    for name, c0 in CATEGORY_ID.items():
        logger.info(f'Crawl subcate for {name}')
        sub = service.get_all_subcate(c0)
        data.append({c0: sub})

    path = join(APP_DIR, '_data/cate.json')
    with open(path, 'w') as f:
        json.dump(data, f)


def get_product_by_cate():
    path = join(APP_DIR, '_data/cate.json')
    with open(path) as f:
        content = json.load(f)

    result = []
    for item in content:
        for _, v in item.items():
            result.extend(v)
    data = []
    for i in tqdm(result):
        tmp = service.crawl_products_by_cate(i)
        data.extend(tmp)
    data = pd.DataFrame(data)
    data.to_csv(join(APP_DIR, '_data/products.csv'), index=False)


def get_product_with_cate():
    df = pd.read_csv(join(APP_DIR, '_data/products.csv'))
    pids = df['id'].values.tolist()
    data = []
    for pid in tqdm(pids):
        data.extend(service.api.get_product_info(pid))
    data = pd.DataFrame(data)
    data.to_csv(join(APP_DIR, '_data/products_with_cate.csv'), index=False)


if __name__ == '__main__':
    get_product_with_cate()
