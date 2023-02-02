import pydicom
import os

filename = ('/Volumes/files/Python/Third_opinion/src/0a67f9edb4915467ac16a565955898d3.dcm')
dataset = pydicom.dcmread(filename)

first_level = dataset.StudyInstanceUID
second_level = dataset.SeriesInstanceUID
name = dataset.SOPInstanceUID
dataset.PatientName = 'Anonymous'

def anonim(in_path, out_path, PatientName = 'Anonymous'):
    filename = pydicom.dcmread(in_path)
    filename.PatientName = PatientName
    file_save = structure()


def structure():
    os.makedirs(f'{first_level}/{second_level}')
    os.chdir(f"{first_level}/{second_level}")
    dataset.save_as(f"{name}.dcm")

def adresses():
    adress = str(os.path.abspath(filename))
    new_adress = str(os.path.abspath(f"{first_level}/{second_level}/{name}.dcm"))
    open('adress.txt', 'w').write(adress + ':' + new_adress)


structure()
adresses()
#dataset.save_as('test.dcm')
#print(dataset.PatientName)





