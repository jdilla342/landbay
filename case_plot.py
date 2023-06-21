import argparse
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.ParserError:
        raise ValueError(f"Error parsing CSV file: {file_path}")

def filter_by_month(df, month):
    df['APPLICATION_SUBMITTED_DATE'] = pd.to_datetime(df['APPLICATION_SUBMITTED_DATE'])
    return df[df['APPLICATION_SUBMITTED_DATE'].dt.strftime('%Y-%m') == month]

def filter_by_category(df, category):
    if category is not None:
        return df[df['PROPERTY_CATEGORY'] == category]
    return df

def calculate_completion_time(df):
    df = df.copy()
    df['COMPLETED_DATE'] = pd.to_datetime(df['COMPLETED_DATE'])
    df['COMPLETION_TIME'] = (df['COMPLETED_DATE'] - df['APPLICATION_SUBMITTED_DATE']).dt.days / 30
    return df

def group_and_count(df):
    grouped = df.groupby('COMPLETION_TIME').size()
    return grouped

def generate_plot(grouped, month, category):
    plt.bar(grouped.index, grouped.values)
    plt.xlabel('Completion Time (Months)')
    plt.ylabel('Number of Cases')
    plt.title(f'Cases submitted in {month} ({category if category else "All Categories"})')
    plt.show()

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Generate a plot of completed cases.')
    parser.add_argument('month', type=str, help='Month in the format "YYYY-MM"')
    parser.add_argument('--category', type=str, help='Optional property category')
    args = parser.parse_args()

    try:
        # Load the data
        data = load_data('data_task_part_1.csv')

        # Perform data transformations
        filtered_data = filter_by_month(data, args.month)
        filtered_data = filter_by_category(filtered_data, args.category)
        transformed_data = calculate_completion_time(filtered_data)
        grouped_data = group_and_count(transformed_data)

        # Check if any data is available for the given month and category
        if grouped_data.empty:
            if args.category:
                raise ValueError(f"No data available for the month {args.month} and category '{args.category}'.")
            else:
                raise ValueError(f"No data available for the month {args.month}.")

        # Generate the plot
        generate_plot(grouped_data, args.month, args.category)

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
