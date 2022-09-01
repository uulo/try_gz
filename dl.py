import os
import contextlib
import sys
import shutil
import zipfile
from pathlib import Path
from urllib.request import urlopen

task_id = 256

config_dir = Path.home() / ".totalsegmentator/nnunet/results/nnUNet/3d_fullres"
config_dir.mkdir(exist_ok=True, parents=True)

old_weights = [
    "Task223_my_test"
]

if task_id == 251:
    weights_path = config_dir / "Task251_TotalSegmentator_part1_organs_1139subj"
    WEIGHTS_URL = "https://zenodo.org/record/6802342/files/Task251_TotalSegmentator_part1_organs_1139subj.zip?download=1"
elif task_id == 252:
    weights_path = config_dir / "Task252_TotalSegmentator_part2_vertebrae_1139subj"
    WEIGHTS_URL = "https://zenodo.org/record/6802358/files/Task252_TotalSegmentator_part2_vertebrae_1139subj.zip?download=1"
elif task_id == 253:
    weights_path = config_dir / "Task253_TotalSegmentator_part3_cardiac_1139subj"
    WEIGHTS_URL = "https://zenodo.org/record/6802360/files/Task253_TotalSegmentator_part3_cardiac_1139subj.zip?download=1"
elif task_id == 254:
    weights_path = config_dir / "Task254_TotalSegmentator_part4_muscles_1139subj"
    WEIGHTS_URL = "https://zenodo.org/record/6802366/files/Task254_TotalSegmentator_part4_muscles_1139subj.zip?download=1"
elif task_id == 255:
    weights_path = config_dir / "Task255_TotalSegmentator_part5_ribs_1139subj"
    WEIGHTS_URL = "https://zenodo.org/record/6802452/files/Task255_TotalSegmentator_part5_ribs_1139subj.zip?download=1"
elif task_id == 256:
    weights_path = config_dir / "Task256_TotalSegmentator_3mm_1139subj"
    WEIGHTS_URL = "https://zenodo.org/record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1"

for old_weight in old_weights:
    if (config_dir / old_weight).exists():
        shutil.rmtree(config_dir / old_weight)

if WEIGHTS_URL is not None and not weights_path.exists():
    print(f"Downloading pretrained weights for Task {task_id} (~230MB) ...")

    data = urlopen(WEIGHTS_URL).read()
    with open(config_dir / "tmp_download_file.zip", "wb") as weight_file:
        weight_file.write(data)

    with zipfile.ZipFile(config_dir / "tmp_download_file.zip", 'r') as zip_f:
        zip_f.extractall(config_dir)
        print(config_dir)

    # delete tmp file
    (config_dir / "tmp_download_file.zip").unlink()