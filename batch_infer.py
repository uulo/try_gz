import os

nii_root = '/data1/yckj4254/seg_data/train_nii'
nii_save_root = '/data1/yckj4254/seg_data/train_nii_vertebrae'    # 先只输出脊骨数据
nii_dir_list = os.listdir(nii_root)
n = 0
for one in nii_dir_list:
    # if n ==0:
    nii_path = os.path.join(nii_root, one, one + '.nii.gz')
    nii_save_path = os.path.join(nii_save_root, one)
    if not os.path.isdir(nii_save_path):os.makedirs(nii_save_path)
    os.system(f'python /data1/yckj4254/seg_data/TotalSegmentator/bin/TotalSegmentator --i {nii_path} --o {nii_save_path} --preview')
    n = n + 1
    print(n)
