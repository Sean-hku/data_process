import os
import shutil
from tqdm import tqdm

def split_file(in_pth, out_pth):
    files = os.listdir(in_pth)
    for file in tqdm(files):
        if file.endswith('.txt'):
            shutil.move(os.path.join(in_pth, file), os.path.join(out_pth, file))

if __name__ == "__main__":
    in_pth = './0607_new'
    out_pth = "./0607_labels"
    os.makedirs(out_pth, exist_ok=True)
    split_file(in_pth, out_pth)
