import pydicom
import os
b = []


def abs_adress(directory):
    for root, dirs, files in os.walk(os.path.abspath(directory)):
        for file in files:
            a = (os.path.join(root, file))
            b.append(a)
        return(b)

def make_dirs(first_level, second_level, name):
    if not os.path.isdir(f'{first_level}/{second_level}'):
        os.makedirs(f'{first_level}/{second_level}')


    ds.save_as(f'{name}.dcm')

'''def get_adress(file):
    adress = str(os.path.abspath(file))
    new_adress = str(os.path.abspath(f"{first_level}/{second_level}/{name}.dcm"))
    return (adress, new_adress)'''

def write_adress(adress, new_adress):
    with open('adress.txt', 'a') as f:
        f.write(adress + ':' + new_adress+ '\n')
files = b

abs_adress('src')
for file in files:
    ds = pydicom.dcmread(file)
    ds.PatientName = 'Anonymous'
    make_dirs(ds.StudyInstanceUID, ds.SeriesInstanceUID, ds.SOPInstanceUID )


