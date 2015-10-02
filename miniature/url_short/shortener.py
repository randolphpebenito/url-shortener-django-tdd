import uuid
from .models import Link

def _generate_hashkey():
    hashkey = str(uuid.uuid4())[:7].replace('-', '').lower()
        #ref_id = '9f16a22615'
    try:
        url_exists = Link.objects.get(short_url=hashkey)
        _generate_hashkey()
    except:
        return hashkey

def shorten(link):
    try: 
        s_link  = Link.objects.get(url=link)
    except:
        shortened_url = _generate_hashkey()
        sl = Link.objects.create(url=link,short_url=shortened_url)
        return sl

    return s_link
