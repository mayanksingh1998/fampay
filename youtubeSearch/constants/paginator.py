class Paginator(object):
    PAGE_INFO = 'page_info'

    PAGE = 'page'
    DEFAULT_PAGE = 1

    PAGE_SIZE = 'page_size'
    DEFAULT_PAGE_SIZE = 10

    CONTENT_DEFAULT_PAGE_SIZE = 20

    MIN_PAGE_SIZE = 0
    MAX_PAGE_SIZE = 50

    MIN_PAGE = 1
    MAX_IDX_SIZE = 9223372036854775807  # BigInt

    PAGINATE = 'paginate'
    DEFAULT_PAGINATE = True


PAGINATOR = Paginator()
