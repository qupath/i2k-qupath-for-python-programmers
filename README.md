# QuPath for programmers Python

These are the notebook and qmd files for the QuPath for python programmers.

I will try to make a jupyter notebook slide deck...

## Building

1. Install [quarto](https://quarto.org/)
1. Open QuPath
2. Start a py4j gateway with default params
3. Open this project (coming soon...)
4. Open this image (also coming soon...)
5. Run `quarto render qupath-for-python-programmers.qmd`
6. Run `quarto render clustering-objects.qmd`

## Outline

The content we hope to cover along with tentative presenters and time estimates.

1. Introduction/motivation (5mins)
2. Setup (5mins)
    - Install extension with manager (2mins)
    - Install qubalab (2mins)
3. Basic usage (15mins)
    - Connecting (5mins)  
      Setting up gateway and connecting from qupath
    - Methods returning primitives (5mins)  
      eg, get image name, version...
    - Methods returning java objects (5mins)  
      eg, iterate through cores and count children
      Explain why this is probably not for the best
      (no static methods etc).
4. Advanced usage (20mins)
    - ImageServer (5mins)
    - Objects (5mins)
    - Task --- eg, threshold image (10mins)
5. Conclusion/other possibilities
    - Object clustering
    - Object classifier
    - ...?
