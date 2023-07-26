import os 
from pdf2image import convert_from_path

# download from https://github.com/oschwartz10612/poppler-windows/releases/, unzip, and copy this bin path from ur own machine
poppler_path = r"..\Release-23.07.0-0\poppler-23.07.0\Library\bin"

# set yourself
working_path = r"<>"

#place filename here
filename = r"<>"
filepath = os.path.join(working_path, filename)
filename_extensionless = os.path.splitext(str(filename))[0]

pages = convert_from_path(pdf_path=filepath, poppler_path=poppler_path)

i = 1
for page in pages:
    image_page = f"page-{i}.jpeg"
    new_filename = filename_extensionless + "_" + image_page
    page.save(os.path.join(working_path, new_filename), 'JPEG')
    i += 1

