# DataFrame Feature Calculator 🚀

## Overview 📊
This Python script processes a pandas DataFrame by performing arithmetic operations (sum, difference, or product) on two specified features. The results are stored in new columns, and the script includes a main function to demonstrate usage with sample data. 📊✨

## Requirements 🛠
- Python 3.8+
- Libraries:
  - pandas 2.0+: For DataFrame operations 🗃
  - numpy 1.24+: For numerical operations 🔢

### Install dependencies using pip:
```bash
pip install pandas numpy
```

## Usage ▶️
Ensure all required libraries are installed. ✅
Run the script:
```bash
python process_features.py
```

## Code Explanation 💡
### process_features.py
**Function: `calculate_features(df, feature1, feature2, operation, result_column)`**

The function takes the following parameters:
- `df`: pandas DataFrame containing the features
- `feature1`: str, name of the first feature column
- `feature2`: str, name of the second feature column
- `operation`: str, operation to perform ('sum', 'diff', 'product')
- `result_column`: str, name of the column to store the result

The function performs the specified operation on the two features and stores the result in a new column. It supports three operations: addition (`sum`), subtraction (`diff`), and multiplication (`product`). Check the code for detailed comments and example usage in the `main()` function.

**Function: `main()`**

The main function creates a sample DataFrame, calls `calculate_features` for each operation, and prints the initial and final DataFrames.

## Limitations 🚧
- The script assumes the input features exist in the DataFrame and are numeric. 🧮
- No error handling for cases like non-numeric columns or missing columns. ❌
- Only supports 'sum', 'diff', and 'product' operations; additional operations would require code modification. ⚙️

## Example Output 🌟
Console output example:
```
Initial DataFrame:
   feature1  feature2
0        1       10
1        2       20
2        3       30
3        4       40
4        5       50

Final DataFrame with calculated features:
   feature1  feature2  sum_result  diff_result  product_result
0        1       10         11           9            10
1        2       20         22          18            40
2        3       30         33          27            90
3        4       40         44          36           160
4        5       50         55          45           250
```

## License 📜
This project is unlicensed and provided as-is for educational purposes. 🎓
