import os
import gdown
import zipfile

# Download the zipped dataset

url = 'https://drive.google.com/file/d/1a5WaYMRVjo0sjOrmPj9rhH1k_q7wLxG0/view?usp=sharing'
zip_name = "archive.zip"
gdown.download(url=url,output=zip_name,quiet=False,fuzzy=True)



# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()

os.remove(zip_name)
print('\nAll files are being extracted.')
