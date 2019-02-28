import sys
import re

def cleanText(theText):
    return ''.join(c for c in theText if c not in '\r\t\n').strip()

def getEnglishSentenseOnly(theText):
    return re.sub("[^A-Za-z\S+]", "", theText.strip())
# def add(value1, value2):
#     return value1 + value2

# result = add(3, 5)
# print(result)

