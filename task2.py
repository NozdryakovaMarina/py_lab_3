import os
import csv
import shutil
from typing import List


def create_dir(dir_name: str) -> None:
    """
    The fanction create a new directory
    """
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def  change(old: str, new: str, type: List[str]) -> None:
    """
    The function copies images from the old directory to the new one,
    changing the name 
    """
    create_dir(new)
    abs_path = os.path.abspath(new)
    rel_path = os.path.relpath(new)
    for name in type:
        path = os.path.join(os.path.abspath(old), name)
        list_img = os.listdir(path)
        for img in list_img:
            shutil.copy(os.path.join(path, img), os.path.join(new, F'{name}_{img}'))
                

def create_csv2(dir_name: str, csv_name: str) -> None:
    """
    The function create CSV file  and writes information about the images to a CSV file
    """
    abs_path = os.path.abspath(dir_name)
    rel_path = os.path.relpath(dir_name)
    img_f = os.listdir(dir_name)
    with open('annotation2.csv', 'a') as f_csv:
        writer = csv.writer(f_csv, delimiter=',', lineterminator='\r')
        for img in img_f:
            writer.writerow([os.path.join(abs_path, img),
                             os.path.join(rel_path, img), img.split('_')[0]])
            

def main() -> None:
    types = ['polarbear', 'brownbear']

    old_d = 'dataset'
    new_d = 'dataset2'

    change(old_d, new_d, types)
    create_csv2(new_d, 'annotation2.csv')


if __name__ == "__main__":
    main()