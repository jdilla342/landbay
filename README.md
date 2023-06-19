# landbay Case Plot

## Private landbay technical test repo

This script generates a plot of completed cases based on a provided month and an optional property category. It loads data from a CSV file, filters it based on the given month and category, calculates the completion time, and generates a bar plot.

### Prerequisites
* Python 3.8 or later
* pandas
* matplotlib

### Dataset
The dataset should be in the same directory as the script and named **'data_task_part_1.csv'**. Please ensure that the dataset is in the correct format with the required columns: **'APPLICATION_SUBMITTED_DATE'**, **'COMPLETED_DATE'**, and **'PROPERTY_CATEGORY'**.

### Usage
1. Clone the repository or download the script file case_plot.py.

2. Ensure that Python 3.8 or later is installed on your system.

3. Install the required dependencies by running the following command:

```
pip install pandas matplotlib
```
4. Place the dataset file (data_task_part_1.csv) in the same directory as the script.

5. Open a command-line or terminal window.

6. Navigate to the directory containing the script and dataset.

7. Run the script using the following command:

```
python case_plot.py <month> --category <category>
```
Replace <month> with the desired month in the format YYYY-MM, and <category> with an optional property category.

Example usage:

```
python case_plot.py 2023-06 --category Commercial
```
The script will generate a bar plot of completed cases based on the provided month and category given the data exists.

