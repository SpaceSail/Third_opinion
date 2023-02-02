import pydicom
import os
b = []



for root, dirs, files in os.walk(os.path.abspath("src")):
    for file in files:
        a = (os.path.join(root, file))
        b.append(a)
    print(b)
files = b
print(files)

for file in files:
    filename = file
    ds = pydicom.dcmread(file)
    first_level = ds.StudyInstanceUID
    second_level = ds.SeriesInstanceUID
    name = ds.SOPInstanceUID
    ds.PatientName = 'Anonymous'
    if not os.path.isdir(f'{first_level}/{second_level}'):
        os.makedirs(f'{first_level}/{second_level}')
    os.chdir(f'{first_level}/{second_level}')
    ds.save_as(f'{name}.dcm')
    adress = str(os.path.abspath(filename))
    new_adress = str(os.path.abspath(f"{first_level}/{second_level}/{name}.dcm"))

    os.chdir('/Volumes/files/Python/Third_opinion/')
    with open('adress.txt', 'a') as f:
        f.write(adress + ':' + new_adress+ '\n')
