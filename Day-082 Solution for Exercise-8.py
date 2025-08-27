from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
folder = "clutteredFolder"

files = sorted([file for file in os.listdir(folder) if file.endswith(".pdf")])

for pdf in files:
    full_path = os.path.join(folder,pdf) #full path for each input pdf
    merger.append(full_path)

# save merged files inside the same folder
output_path = os.path.join(folder, "merged_pdf.pdf")

with open(output_path, "wb") as f:
    merger.write(f)

# open(..., "wb") → opens the file in write-binary mode.
# "w" = write (create new or overwrite if exists)
# "b" = binary (important for non-text files like PDFs)
# as f: → assigns that opened file object to variable f.
# merger.write(f) → tells PdfWriter to write all merged pages into that file.

# with ... as f: → ensures the file closes automatically after writing (even if errors happen).
# That’s why we don’t need f.close() here.

merger.close()