def parse_product_info(item):
    result = {}
    for key in ['id', 'name', 'brand_name', 'price', 'thumbnail_url',
                'productset_group_name']:
        result[key] = item.get(key, '')
    return result
