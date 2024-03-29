from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_return_pag_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_paginas=4, current_page=1
        )

        self.assertEqual([1, 2, 3, 4, 5], pagination)

    def test_first_range_is_static_if_current(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_paginas=4, current_page=1
        )

        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_paginas=4, current_page=2
        )

        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_paginas=4, current_page=3
        )

        self.assertEqual([2, 3, 4, 5], pagination)
