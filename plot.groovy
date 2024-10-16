import qupath.lib.gui.charts.Charts

def builder = Charts.scatterChart()
        .viewer(QuPathGUI.getInstance().getViewer())
        .title('UMAP of cell-wise mean channel intensities')
        .measurements(getDetectionObjects(), "UMAP1", "UMAP2")
        .show()
