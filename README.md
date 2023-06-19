# landbay Case Plot

## Private landbay technical test repo

This script generates a plot of completed cases based on a provided month and an optional property category. It loads data from a CSV file, filters it based on the given month and category, calculates the completion time, and generates a bar plot.

### Prerequisites
* Python 3.x
* pandas
* matplotlib

### Dataset
The dataset should be in the same directory as the script and named **data_task_part_1.csv**. Please ensure that the dataset is in the correct format with the required columns: **APPLICATION_SUBMITTED_DATE**, **COMPLETED_DATE**, and **PROPERTY_CATEGORY**.

### Usage
Clone the repository or download the script file case_plot.py.

Ensure that Python 3.x is installed on your system.

Install the required dependencies by running the following command:

Copy code
```
pip install pandas matplotlib
```
Place the dataset file (data_task_part_1.csv) in the same directory as the script.

Open a command-line or terminal window.

Navigate to the directory containing the script and dataset.

Run the script using the following command:

Copy code
```
python case_plot.py <month> --category <category>
```
Replace <month> with the desired month in the format YYYY-MM, and <category> with an optional property category.

Example usage:

Copy code
```
python case_plot.py 2023-06 --category Commercial
```
The script will generate a bar plot of completed cases based on the provided month and category.

