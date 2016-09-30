###########################################################################
# TextIndexNG V 3
# The next generation TextIndex for Zope
#
# This software is governed by a license. See
# LICENSE.txt for the terms of this license.
###########################################################################

"""
Stopwords

$Id: stopwords.py 2080 2009-03-14 11:23:05Z ajung $
"""

import os
import re

from zopyx.txng3.core.interfaces import IStopwords
from zopyx.txng3.ext.support import stopwordfilter
from zope.interface import implementer

sw_dir = os.path.join(os.path.dirname(__file__), 'data', 'stopwords')


@implementer(IStopwords)
class Stopwords:
    """  class for handling stopwords """


    def __init__(self):
        self._cache = {}

    def stopwordsForLanguage(self, language):
        if language not in self._cache:
            self._cache[language] = readStopwords(language)
        return list(self._cache[language].keys())

    def process(self, words, language):
        cache = self._cache
        if language not in cache:
            cache[language] = readStopwords(language)
        return stopwordfilter(words, cache[language])

    def availableLanguages(self):
        files = [f for f in os.listdir(sw_dir) if f.endswith('.txt')]
        return [os.path.splitext(f)[0] for f in files]

    def __repr__(self):
        return self.__class__.__name__


enc_reg = re.compile('#\s*encoding\s*=\s*([\w\-]+)')


def readStopwords(language):
    """ read a stopword file from the filesystem """

    words = {}    # words -> None
    encoding = None

    fname = os.path.join(sw_dir, '%s.txt' % language)
    if not os.path.exists(fname):
        return {}

    for l in open(fname, encoding='iso-8859-15'):
        if not l.strip():
            continue

        mo = enc_reg.match(l)
        if mo:
            encoding = mo.group(1)
            continue

        if l.startswith('#'):
            continue

        word = l.lower()
        words[word] = None

    return words

StopwordUtility = Stopwords()
