from setuptools import setup


setup(name="folder_sorting_biletska",
      version="0.0.1",
      description="This script will sort your files in the folder",
      url="https://github.com/IrynaBiletskaa/Homework_6",
      author="IrynaBiletskaa",
      author_email="irinacat3211@gmail.com",
      license="MIT",
    #   data_files=["clean_folder"],
      entry_points={"console_scripts": [
          "sortfolder = clean_folder.clean:main"]}
      )
