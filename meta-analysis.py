import numpy as np
from scipy.stats import combine_pvalues

def perform_meta_analysis(data):
    # Initialize the combined p-value
    combined_p_value = None

    # Loop over the data
    for i, d in enumerate(data):
        # If this is the first iteration, simply store the p-value
        if i == 0:
            combined_p_value = d["p_value"]
        else:
            # Otherwise, combine the p-value with the previous combined p-value
            combined_p_value = combine_pvalues(combined_p_value, d["p_value"])

    # Return the combined p-value
    return combined_p_value
