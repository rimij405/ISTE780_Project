# clean_features.py
#
# Utility functions for cleaning features.

def rename_columns(df, mapping = {}):
    """Rename columns in a dataframe.
    """
    df_1 = df.rename(mapping, axis=1)
    print("Renamed columns to {}".format(df_1.columns))
    return df_1

def reorganize_columns(df, features):
    """Reorganize features.
    """
    df_1 = df[features]
    print("Reordered columns to {}".format(df_1.columns))
    return df_1