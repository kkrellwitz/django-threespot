def unescape(text):
    """
    Convert HTML entities to unicode equivalents.
    By Frederick Lundh: effbot.org/zone/re-sub.html#unescape-html
    """
    import re, html.entities
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character ref
            try:
                if text[:3] == "&#x":
                    return chr(int(text[3:-1],1))
                else:
                    return chr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            #named entity
            try:
                text = chr(html.entities.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text
    return re.sub("&#?\w+;", fixup, text)

def get_readable_file_size(size):
    """
    Returns a human-readable file size given a file size in bytes:

    >>> get_readable_file_size(100)
    '100.0 bytes'
    >>> get_readable_file_size(1024)
    '1.0 KB'
    >>> get_readable_file_size(1024 * 1024 * 3)
    '3.0 MB'
    >>> get_readable_file_size(1024**3)
    '1.0 GB'
    """
    for t in ('bytes', 'KB', 'MB', 'GB', 'TB'):
        if size < 1024.0:
            return "%3.1f %s" % (size, t)
        size /= 1024.0