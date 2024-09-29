from django.conf import settings
from django.core.cache import cache

from main.models import Version, Category


def get_caches_versions_for_products(product_pk):
    if settings.CACHE_ENABLED:
        version_list = cache.get(f'version_list_{product_pk}')
        if version_list is None:
            version_list = Version.objects.filter(product_id=product_pk)
            cache.set(f'version_list_{product_pk}', version_list)

    else:
        version_list = Version.objects.filter(product_pk=product_pk)

    return version_list

def get_caches_categorires_for_products():
    if settings.CACHE_ENABLED:
        category_list = cache.get(f'category_list')
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(f'category_list', category_list)

    else:
        category_list = Category.objects.all

    return category_list
