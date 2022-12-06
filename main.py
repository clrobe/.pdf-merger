# Creating a PDF merger for combining notes, documents, or other needs
# Begin by pip installing PyPDF2 in the command line 

from PyPDF2 import PdfMerger

# Put the pdfs you want to merge here, in the particular order you would like

pdfs = ["one.pdf", "two.pdf", "three.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)


# Makes the pdfs combined into "merged.pdf" or whatever name you want 

merger.write("merged.pdf")
merger.close()


