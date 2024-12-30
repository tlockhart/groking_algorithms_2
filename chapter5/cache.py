cache = {}
def get_page(url):
    
    if url in cache:
        # if the url is in the cache then return it
        return cache[url]
    else:
        # if the url isn't in the cache populate a new url
        data = get_data_from_server(url)
        cache[url] = data
    return data