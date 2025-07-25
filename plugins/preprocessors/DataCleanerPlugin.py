# plugins/preprocessors/DataCleanerPlugin.py

class DataCleanerPlugin:
    metadata = {
        "plugin_name": "DataCleanerPlugin",
        "category": "Preprocessor",
        "description": "Cleans KPI data by handling nulls and normalizing features"
    }

    def __init__(self):
        pass

    def process(self, df):
        df_clean = df.copy()
        df_clean.fillna(0, inplace=True)  # Simple null handling
        # You could add normalization or feature mapping here
        return df_clean