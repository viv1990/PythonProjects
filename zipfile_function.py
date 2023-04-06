import zipfile
import pathlib
def make_zip(filepaths,folder):
    folder=pathlib.Path(folder,"output.zip")
    print(folder)
    with zipfile.ZipFile(folder,'w') as archive:
        for filepath in filepaths:
            filepath=pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)
