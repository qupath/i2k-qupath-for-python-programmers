for (PathObject po: getDetectionObjects()) {
    po.getMeasurementList().remove("UMAP1")
    po.getMeasurementList().remove("UMAP2")
    po.setPathClass(null)
}
