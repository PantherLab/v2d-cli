def to_unicode(hex):
    return chr(int(hex, 16))


def to_hex(unicode):
    return format(ord(unicode), "05x")
