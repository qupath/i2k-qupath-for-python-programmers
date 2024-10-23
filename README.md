# QuPath for programmers Python

These are the notebooks and associated files for the i2k 2024
**QuPath for python programmers** workshop.

## Running the notebooks

1. Download the latest QuPath v0.6.0 release candidate from the [github releases page](https://github.com/qupath/qupath/releases).
2. Download the [QuPath project](https://github.com/qupath/i2k-qupath-for-python-programmers/releases/download/untagged-0dd17955cb74744f7ce5/i2k-qupath-python-project.zip)
   for this workshop.
3. Unzip the project in the i2k-qupath-for-python-programmers directory
4. Create a python virtual environment (bash):
   1. `python -m venv .venv`
   2. `. ./.venv/bin/activate`
   3. `pip install instanseg-torch git+https://github.com/qupath/qubalab.git jupyter ipython leidenalg igraph umap-learn`
5. Open QuPath v0.6.0
6. Start a py4j gateway with default parameters
7. Open the `i2k-qupath-python-project` in QuPath
8. Open `HE_Hamamatsu.tiff` in QuPath
9. Start a jupyter session using the virtual environment from earlier
10. Run the `qupath-for-python-programmers.ipynb` notebook
11. Open `patient_test_2.ome.tiff` in QuPath and select the annotation
12. Run the `clustering-objects.ipynb` notebook
