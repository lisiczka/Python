# The script iterates over all the PDF files in the folder and looks for the specific text in the document. 
# Later on it's using the found string to use it as a new name for each file.

import fitz
import os
import re

os.system('clear')

for file in os.listdir():
  if file.endswith(".pdf"):
    document = os.path.join(file)
    with fitz.open(document) as doc:
      text = ""
      for page in doc:
        text += page.get_text()
    print(text)

    # Extract the 1st part of the final file name
    name = text.splitlines()[1]
    name = re.sub("/", "", name)

    # Look for the 2nd part of the final file name
    title_search = re.search("...\n:.(\d\d\d)\n", text)
    if title_search:
        fak = title_search.group(1)

    print (name + "-" + fak)
    

    filename = os.path.basename(doc.name)
    print("current filename: ", filename)


    new_filename = (fak + ": " + name)
    print("new filename: ", new_filename)


    os.rename(filename, new_filename + ".pdf")

    print("--")
