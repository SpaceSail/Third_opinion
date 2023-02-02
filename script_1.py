import pydicom as pm
from glob import glob
import os


def anonymize_dicom(in_path, out_path, PatientName='Anonymous'):
    dicom_file = pm.dcmread(in_path)
    dicom_file.PatientName = PatientName
    dicom_file.save_as(out_path)


if __name__ == '__main__':
    path_to_dicoms = '/Volumes/files/Python/Third_opinion/src_1'
    slices = glob(os.path.join(path_to_dicoms, '*'))

    for slice_ in slices:
        anonymize_dicom(slice_, 'test/1.dcm')