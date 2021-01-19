BASE_URL = 'https://tiki.vn/api/v2/'


def remove_skip_values(obj, skip_values=(None, [], {})):
    """Remove None values from the given object."""
    if isinstance(obj, (list, tuple, set)):
        return type(obj)(remove_skip_values(x) for x in obj
                         if x not in skip_values)
    elif isinstance(obj, dict):
        return type(obj)((k, remove_skip_values(v))
                         for k, v in obj.items() if v not in skip_values)
    else:
        return obj


def _build_query_string(**kwargs):
    kwargs = remove_skip_values(kwargs)
    text = []
    for k, v in kwargs.items():
        if isinstance(v, dict):
            v = json.dumps(v)
        text.append(f'{k}={v}')
    return '&'.join(text)


def products_by_cate_url(**kwargs):
    return BASE_URL + 'products?' + _build_query_string(**kwargs)


def reco_by_pid_url(**kwargs):
    return BASE_URL + 'personalization/v2/pdp?' + _build_query_string(**kwargs)


def product_url(id):
    return BASE_URL + 'products/{}?include=breadcrumbs'.format(str(id))
