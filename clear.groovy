for (PathObject po: getDetectionObjects()) {
    po.getMeasurementList().remove("UMAP1")
    po.getMeasurementList().remove("UMAP2")
    po.setPathClass(null)
}
for (PathObject po: getAnnotationObjects()) {
    po.setName(null)
    po.setPathClass(null)
    if (po.getChildObjects().size() == 0) {
        getCurrentHierarchy().removeObject(po, false)
    }
}
