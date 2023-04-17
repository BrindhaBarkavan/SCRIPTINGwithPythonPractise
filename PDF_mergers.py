import PyPDF2
import sys

# this input will get all the needed pdf files to merge
input = sys.argv[1:]
print(input)


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(input)
