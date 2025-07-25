# plugin_registry/registry.py

def load_all_plugins():
    from plugins.preprocessors.DataCleanerPlugin import DataCleanerPlugin
    from plugins.predictive.TrafficPredictorRF import TrafficPredictorRF
    from plugins.coverage.KrigingCoveragePlugin import KrigingCoveragePlugin
    from plugins.geometry.SiteGeometryLoaderPlugin import SiteGeometryLoaderPlugin

    plugin_registry = {
        "Preprocessor": {
            "DataCleanerPlugin": DataCleanerPlugin
        },
        "Predictive": {
            "TrafficPredictorRF": TrafficPredictorRF
        },
        "Coverage": {
            "KrigingCoveragePlugin": KrigingCoveragePlugin
        },
        "Geometry": {
            "SiteGeometryLoaderPlugin": SiteGeometryLoaderPlugin
        }
    }

    return plugin_registry