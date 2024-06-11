import json
import xml.dom.minidom
import string
import re

def clean_text(text):
    pattern1 = re.compile('[^а-яА-ЯіІєЄїЇґҐ,.\s—!\-\[\]:…’\?]|(?<!\w)-(?!\w)|  ')
    pattern2 = re.compile(r'\[\s*\]')
    
    # Use the pattern to substitute all characters except those specified
    cleaned_text = re.sub(pattern1, '', text)
    cleaned_text = re.sub(pattern2, '', cleaned_text)
    
    return cleaned_text

xmldoc = xml.dom.minidom.parse("cuv23.xml")
bible = xmldoc.getElementsByTagNameNS('*', 'XMLBIBLE')[0]

with open('verses.json', mode='r', encoding='utf8') as verses_file:
    verses = json.load(verses_file)

with open('books.json', mode='r', encoding='utf8') as books_file:
    books = json.load(books_file)

# for control and comparison in cycle
verse_chapter = 1
verse_book = 1

# first chapter
chapter = xmldoc.createElement("CHAPTER")
chapter.setAttribute("cnumber", str(verse_chapter))

# first book
biblebook = xmldoc.createElement("BIBLEBOOK")
biblebook.setAttribute("bnumber", str(verse_book))
biblebook.setAttribute("bname", "БУТТЯ")
biblebook.appendChild(chapter)

bible.appendChild(biblebook)

book_counter = 2

for verse in verses:
    # taking out data
    verse_book_number = int(int(verse["book_number"])/10)
    verse_chapter_number = int(verse["chapter"])
    verse_text = clean_text(str(verse["text"]))
    verse_number = int(verse["verse"])

    # making xml verse
    vers = xmldoc.createElement("VERS")
    vers.setAttribute("vnumber", str(verse_number))
    vers.appendChild(xmldoc.createTextNode(verse_text))

    if (verse_chapter_number == verse_chapter and verse_book_number == verse_book): # if still same chapter and same book
        chapter.appendChild(vers) # adding to existing chapter

    # logic for new chapters and books

    elif (verse_chapter_number != verse_chapter and verse_book_number == verse_book): # new chapter but same book
        biblebook.appendChild(chapter)
        chapter = xmldoc.createElement("CHAPTER")
        chapter.setAttribute("cnumber", str(verse_chapter_number))
        chapter.appendChild(vers) # adding verse to new chapter
        # updating counters for further comparison
        verse_chapter = verse_chapter_number 
        verse_book = verse_book_number

    elif (verse_book_number != verse_book): #new book
        biblebook.appendChild(chapter) # adding last chapter
        bible.appendChild(biblebook) # adding prevoius book before creating new one
        biblebook = xmldoc.createElement("BIBLEBOOK")
        biblebook.setAttribute("bnumber", str(book_counter))
        for counter in range(len(books)):
            if int(int(books[counter]["book_number"])/10) == verse_book_number:
                biblebook.setAttribute("bname", str(books[counter]["long_name"]))
                break
        # making new chapter 
        chapter = xmldoc.createElement("CHAPTER")
        chapter.setAttribute("cnumber", str(verse_chapter_number))
        # adding verse to the new chapter of the new book
        chapter.appendChild(vers)
        verse_chapter = verse_chapter_number 
        verse_book = verse_book_number
        book_counter+=1

    else:
        print("ERROR " * 10)

# adding last chapter
biblebook.appendChild(chapter) # adding last chapter
# adding last book to the bible
biblebook.setAttribute("bname", "ОБ’ЯВЛЕННЯ")
biblebook.setAttribute("bnumber", "66")
bible.appendChild(biblebook) # adding prevoius book before creating new one

# pasting all to xml file
xmldoc.writexml(open('xmldoc', 'w', encoding="utf8"))

# Beautify the XML structure
xml_str = xmldoc.toprettyxml(indent="  ")

# Save the modified XML
with open('cuv23.xml', 'w', encoding="utf8") as xml_file:
    xml_file.write(xml_str)

# cuv23
# structure of xml file for generation:

# <?xml version="1.0" ?>
# <XMLBIBLE xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" biblename="CUV">
# </XMLBIBLE>