import pandas as pd
import numpy as np


def calculate_features(df, feature1, feature2, operation, result_column):
    """
    Perform a specified operation on two features of a DataFrame and store the result.

    Parameters:
    - df: pandas DataFrame containing the features
    - feature1: str, name of the first feature column
    - feature2: str, name of the second feature column
    - operation: str, operation to perform ('sum', 'diff', 'product')
    - result_column: str, name of the column to store the result

    Returns:
    - df: DataFrame with the new column containing the operation result
    """
    if operation == 'sum':
        df[result_column] = df[feature1] + df[feature2]
    elif operation == 'diff':
        df[result_column] = df[feature1] - df[feature2] 
    elif operation == 'product':
        df[result_column] = df[feature1] * df[feature2]
    else:
        raise ValueError("Unsupported operation. Use 'sum', 'diff', or 'product'.")
    return df


def main():
    # Create sample DataFrame
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50]
    })

    print("Initial DataFrame:")
    print(data)

    # Perform operations
    data = calculate_features(data, 'feature1', 'feature2', 'sum', 'sum_result')
    data = calculate_features(data, 'feature1', 'feature2', 'diff', 'diff_result')
    data = calculate_features(data, 'feature1', 'feature2', 'product', 'product_result')

    print("\nFinal DataFrame with calculated features:")
    print(data)


if __name__ == "__main__":
    main()
