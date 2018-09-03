def domain_name(url):
    import re
    return re.findall(r"(//)?(www.)?(\w+)\.", url)[0][2]