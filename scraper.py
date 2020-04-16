#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
from urllib.request import urlopen
import string


def searcher(year='', month='', day=''):
    if year == '' or month == '' or day == '':
        raise SyntaxError('You must have search terms to search a directory')
    else:
        search_string = 'https://magic.wizards.com/en/articles/archive/mtgo-standings/legacy-challenge-' + year + '-' + month + '-' +day

    url = urlopen(search_string)
    html = url.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def cardCounter(soup, searchTerm = ''):
    counts = []
    names = []
    cards = []
    cardCounts = {}
    for entry in soup.body.find_all(class_='card-count'):
        counts.append(entry.get_text())
    for entry in soup.body.find_all(class_='card-name'):
        names.append(entry.get_text())

    for index in range(0, len(counts)):
        countName = names[index].replace(' ', '')
        for punct in string.punctuation:
            countName = countName.replace(punct, '')
        countName = countName.lower()

        if countName in cardCounts:
            cardCounts[countName] += int(counts[index])
        else:
            cardCounts[countName] = int(counts[index])
        cards.append(counts[index] + ' ' + names[index])
    if searchTerm == '':
        return cardCounts
    else:
        searchTerm = searchTerm.replace(' ', '')
        for punct in string.punctuation:
            searchTerm = searchTerm.replace(punct, '')
        searchTerm = searchTerm.lower()
        return cardCounts[searchTerm]


def mainCounter(soup, searchTerm = ''):
    counts = []
    names = []
    lists = []
    cards = []
    cardCounts = {}
    for deck in soup.body.find_all(class_='sorted-by-overview-container sortedContainer'):
        lists.append(deck)
    for deck in range(0, len(lists)):
        for entry in lists[deck].find_all(class_='card-count'):
            counts.append(entry.get_text())
        for entry in lists[deck].find_all(class_='card-name'):
            names.append(entry.get_text())

    for index in range(0, len(counts)):
        countName = names[index].replace(' ', '')
        for punct in string.punctuation:
            countName = countName.replace(punct, '')
        countName = countName.lower()
        if countName in cardCounts:
            cardCounts[countName] += int(counts[index])
        else:
            cardCounts[countName] = int(counts[index])
        cards.append(counts[index] + ' ' + names[index])
    if searchTerm == '':
        return cardCounts
    else:
        searchTerm = searchTerm.replace(' ', '')
        for punct in string.punctuation:
            searchTerm = searchTerm.replace(punct, '')
        searchTerm = searchTerm.lower()
        return cardCounts[searchTerm]


def sideCounter(soup, searchTerm = ''):
    counts = []
    names = []
    lists = []
    cards = []
    cardCounts = {}
    for deck in soup.body.find_all(class_='sorted-by-sideboard-container clearfix element'):
        lists.append(deck)
    for deck in range(0, len(lists)):
        for entry in lists[deck].find_all(class_='card-count'):
            counts.append(entry.get_text())
        for entry in lists[deck].find_all(class_='card-name'):
            names.append(entry.get_text())

    for index in range(0, len(counts)):
        countName = names[index].replace(' ', '')
        for punct in string.punctuation:
            countName = countName.replace(punct, '')
        countName = countName.lower()
        if countName in cardCounts:
            cardCounts[countName] += int(counts[index])
        else:
            cardCounts[countName] = int(counts[index])
        cards.append(counts[index] + ' ' + names[index])
    if searchTerm =='':
        return cardCounts
    else:
        searchTerm = searchTerm.replace(' ', '')
        for punct in string.punctuation:
            searchTerm = searchTerm.replace(punct, '')
        searchTerm = searchTerm.lower()
        return cardCounts[searchTerm]

def search(year, month, day, deck='', card=''):
    soup = searcher(year, month, day)
    if deck == 'main':
        return mainCounter(soup, card)
    elif deck == 'side':
        return sideCounter(soup, card)
    else:
        return cardCounter(soup, card)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        print(search(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        raise SyntaxError('You must have search terms to search a directory')
