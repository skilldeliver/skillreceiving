def load_input(link, as_string=False):
    import urllib.request

    uf = urllib.request.urlopen(link)
    content = uf.readlines()

    if as_string:
        return content.decode('utf-8').replace('\r\n', '')
    return [line.decode('utf-8').strip('\r\n') for line in content]

