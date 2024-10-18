# QuPath for programmers Python

These are the notebooks and associated files for the i2k 2024
**QuPath for python programmers** workshop.

## Running the notebooks

1. Download the [QuPath project](https://github.com/qupath/i2k-qupath-for-python-programmers/releases/download/untagged-caef4b4b6c28c541bcd9/i2k-qupath-python-project.zip)
2. Unzip the project in the i2k-qupath-for-python-programmers directory
3. Create a python virtual environment (bash):
   1. `python -m venv .venv`
   2. `. ./.venv/bin/activate`
   3. `pip install instanseg-torch git+https://github.com/qupath/qubalab.git jupyter ipython leidenalg igraph umap-learn`
4. Open QuPath v0.6.0 rc3
5. Start a py4j gateway with default parameters
6. Open the `i2k-qupath-python-project` in QuPath
7. Open `HE_Hamamatsu.tiff` in QuPath
8. Start a jupyter session using the virtual environment from earlier
9. Run the `qupath-for-python-programmers.ipynb` notebook
10. Open `patient_test_2.ome.tiff` in QuPath and select the annotation
11. Run the `clustering-objects.ipynb` notebook
