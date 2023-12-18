import os
import csv
from typing import List


def create_csv(type_name: str, csv_name: str, dir_name: str) -> None:
    """
    The function creates a csv file and writes information from the dataset into it
    """
    abs_path = os.path.abspath(dir_name)
    rel_path = os.path.relpath(dir_name)
    img_f = os.listdir(os.path.join(abs_path, type_name))
    with open(csv_name, 'a') as f_csv:
        writer = csv.writer(f_csv, delimiter=',', lineterminator='\r')
        writer.writerow(["Absolute path", "Relative path", "Class name"])
        for img in img_f:
            writer.writerow([os.path.join(abs_path, type_name, img),
                             os.path.join(rel_path, type_name, img), type_name])


def main() -> None:

    create_csv('polar_bear', 'annotation.csv', 'dataset')
    create_csv('brown_bear', 'annotation.csv', 'dataset')


if __name__ == "__main__":
    main()