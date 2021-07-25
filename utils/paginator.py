from youtubeSearch.constants import PAGINATOR


class Paginator(object):

    @staticmethod
    def is_valid_page(page, page_size, total_count):
        if not page_size:
            return False, page_size

        if total_count % page_size > 0:
            max_pages = int(total_count / page_size) + 1
        else:
            max_pages = int(total_count / page_size)

        return 0 < page <= max_pages, max_pages

    @staticmethod
    def get_page_info(page, page_size, total_count):
        is_valid, total_pages = Paginator.is_valid_page(page, page_size, total_count)

        page_info = {}

        if not is_valid:
            return page_info
        else:
            page_info['current_page'] = page

        if page < total_pages:
            page_info['next_page'] = page + 1
        else:
            page_info['next_page'] = None

        page_info['total_pages'] = total_pages
        page_info['page_size'] = page_size

        return page_info

    @staticmethod
    def paginate_queryset(queryset, page=PAGINATOR.DEFAULT_PAGE, page_size=PAGINATOR.DEFAULT_PAGE_SIZE):
        start_index = (page - 1) * page_size  # assuming page number starts with 1
        end_index = page * page_size
        return queryset[start_index:end_index]

    @staticmethod
    def get_validated_params(page, page_size):
        try:
            page = int(page)

            if page < PAGINATOR.MIN_PAGE:
                page = PAGINATOR.DEFAULT_PAGE

        except ValueError:
            page = PAGINATOR.DEFAULT_PAGE

        try:
            page_size = int(page_size)

            if page_size < PAGINATOR.MIN_PAGE_SIZE:
                page_size = PAGINATOR.DEFAULT_PAGE_SIZE

            elif page_size > PAGINATOR.MAX_PAGE_SIZE:
                page_size = PAGINATOR.DEFAULT_PAGE_SIZE

        except ValueError:
            page_size = PAGINATOR.DEFAULT_PAGE_SIZE

        idx = (page - 1) * page_size
        if idx > PAGINATOR.MAX_IDX_SIZE:
            page = (PAGINATOR.MAX_IDX_SIZE // page_size) + 1

        return page, page_size
