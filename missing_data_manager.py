import pandas
import numpy

from sklearn.impute import SimpleImputer

print("Missing Data Manager - By Aaditya Awati\n")

dataset_path = input("Please Enter Dataset(.csv) Path -> ")
dataset = pandas.read_csv(dataset_path).to_dict()

dataset_name = dataset_path.split("/")[-1] if "/" in dataset_path else dataset_path

print("\nProcessing ...\n")

missing_values = []
unnamed_columns = [column_name for column_name in dataset if "Unnamed" in column_name]

dataset_keys = list(dataset.keys())

print("Missing Values :-\n")

for column in dataset:
    if "Unnamed" in column:
        missing_values.append((f"Column Name - No.", dataset_keys.index(unnamed_columns[0])))
        dataset_keys.pop(0)

        print(missing_values[-1][0], missing_values[-1][1])

    for key in dataset[column]:
        if not isinstance(dataset[column][key], (str, int, bool)) and numpy.isnan(dataset[column][key]):
             missing_values.append((f"Column: {column} | Row: {key} -", dataset[column][key], column, key))
             print(missing_values[-1][0], missing_values[-1][1])
        else:
            continue

if not missing_values:
    print("No Missing Values Have Been Found.\n")
else:
    dataset_keys = list(dataset.keys())

    fill_missing_values = input("\nWould you like to fill the numerical missing values? (Y/n) -> ").lower()

    if fill_missing_values == "y":
        strategy = input("Please Enter Strategy to be used for filling out Missing Values (mean/median/constant/most_frequent) -> ")

        if strategy in ("mean", "median", "constant", "most_frequent"):

            if strategy == "constant":
                constant = input("Please Enter the Constant -> ")

                print("\nProcessing ...\n")

                for missing_value in missing_values:
                    if len(missing_value) == 4:
                        column = missing_value[2]
                        row = missing_value[3]

                        if type(dataset[column][0]) == int or type(dataset[column][0]) == float:
                            dataset[column][row] = constant
                        else:
                            continue
                    else:
                        continue

                dataset = pandas.DataFrame(dataset)
                dataset.to_csv(f"Filled Datasets/{dataset_name}", index=False)

                print(f"All Numerical Values have been replaced with the constant - {constant}")
                print(dataset)
                print(f"Dataset '{dataset_name}' saved to Filled Datasets/{dataset_name}")

            elif strategy in ("mean", "median", "most_frequent"):
                print("\nProcessing ...\n")

                imputer = SimpleImputer(missing_values=numpy.nan, strategy=strategy)

                missing_value_columns = [missing_data[2] for missing_data in missing_values if len(missing_data) == 4]
                missing_value_columns = [missing_value for missing_value in missing_value_columns
                                         if type(dataset[missing_value][0]) == int or type(dataset[missing_value][0]) == float]

                dataset = pandas.DataFrame(dataset)
                dataset[missing_value_columns] = imputer.fit_transform(dataset[missing_value_columns])

                dataset.to_csv(f"Filled Datasets/{dataset_name}", index=False)

                print(f"All Numerical Values have been replaced with their column's {strategy} value(s).")
                print(dataset)
                print(f"Dataset '{dataset_name}' saved to Filled Datasets/{dataset_name}")
