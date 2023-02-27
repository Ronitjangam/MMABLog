from django.utils.text import slugify

import random,string





 
def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))
    print(res)
    return res

 


def generate_slug(text):
    new_slug=slugify(text)
    from blogapp.models import BlogModel

    print("@@@@@")
    print(new_slug)
    print("@@@@@")
    if BlogModel.objects.filter(slug=new_slug).exists():
        return generate_slug(text+generate_random_string(5))

    return new_slug
    
