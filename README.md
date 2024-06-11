**Comments on the work and a bit of history**

A relatively small but intresting task. One church wanted to use new Bible version but no where on the internet ready to use materials could be found,
they needed it to be in format their software would understand and would be able to use.
Though we found a database file which contained all the verses and Bible books as lists and their numbers,
that was very uncomfortable data structure but I managed to reassembly the whole Bible from it.
Have a look at it.

**Overview**

This script reads Bible verses from a JSON file and structures them into a hierarchical XML format. It ensures that the verses are cleaned of unwanted characters and formatted into chapters and books properly. The output is a beautified XML file that represents the Bible structure.

**Here's main steps:**

1. Imports and Definitions
2. Text Cleaning Function
3. XML Document Initialization
4. Reading JSON Files
5. Initial Setup for Book and Chapter Tracking
6. Processing Verses and Structuring XML
7. Finalizing XML Structure
8. Saving and prettyfing the XML Document

This script effectively reads, processes, and structures biblical text data into a well-formed XML document.
