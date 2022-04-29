###########################################################################
# TextIndexNG V 3
# The next generation TextIndex for Zope
#
# This software is governed by a license. See
# LICENSE.txt for the terms of this license.
###########################################################################

from zope.interface import Interface

class ILexicon(Interface):
    """ Interface for Lexicon objects. A TextIndexNG3 lexicon act as a storage
        for multilingual content. Words are stored per-language. 
    """

    def getLanguages():
        """ return a list of languages handled by the lexicon """

    def addLanguage(self):
        """ prepare lexicon to store words in a new language """

    def hasLanguage(self):
        """ check if the lexicon is configured for a language """

    def insertWords(self, language):
        """ Insert a sequence of words for a given language.  Return a sequence of wordids. """

    def insertWord(self, language):
        """ Insert a word for a given language. Return a wordid. """

    def getWord(self):
        """ return the word for the given wordid """

    def getWordId(self, language='xx'):
        """ return the word id for a given word """

    def getWordIds(self, language='xx'):
        """ return a list of wordid for a list for words """

    def getWordsForLanguage(self):
        """ return all words for a given language """

    def getWordAndLanguage(self):
        """ return the (word, language) tuple  for the given wordid """

    def getWordsForRightTruncation(self, language='en'):
        """ return a sequence of words with a given prefix """

    def getWordsForLeftTruncation(self, language='en'):
        """ return a sequence of words with a given suffix"""

    def getWordsForPattern(self, language='en'):
        """ return a sequence of words that match 'pattern'.  'pattern' is a
            sequence of characters including the wildcards '?' and '*'.
        """         

    def getWordsInRange(self, w2, language='en'):
        """ return a sorted list of words where w1 <= w(x) <= w2  """

    def getSimiliarWords(self, threshold, language='en'):
        """ return a list of that are similar based on a similarity measure"""

    def getWordsForSubstring(self, language='en'):
        """ return all words that match the given substring """

