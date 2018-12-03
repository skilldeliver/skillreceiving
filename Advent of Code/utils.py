def load_input(link):
    import urllib.request

    uf = urllib.request.urlopen(link)
    content = uf.readlines()
    return [line.decode('utf-8').strip('\r\n') for line in content]
