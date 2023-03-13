# -*- coding: utf-8 -*-

"""
Add directory bookmarks to the pdf file.

Public:

- function: add_bookmark(path, index_dict)

"""

from .pikepdf import Pdf


def add_bookmark(path, index_dict):
    """
    Add directory bookmarks to the pdf file.
    :param path: pdf file path.
    :param index_dict: bookmarks dict, like {0:{'title':'A', 'pagenum':1}, 1:{'title':'B', pagenum:2, parent: 0} ......}
    """
    pdf = Pdf(path)
    pdf.add_bookmarks(index_dict)
    return pdf.save_pdf()

