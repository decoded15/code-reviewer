import zipfile

import tempfile

import os


def extract_zip_repository(uploaded_zip):

    temp_dir = tempfile.mkdtemp()

    with zipfile.ZipFile(
        uploaded_zip,
        "r"
    ) as zip_ref:

        zip_ref.extractall(temp_dir)

    return temp_dir