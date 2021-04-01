from PIL import Image
import os
from glob import glob
import numpy as np


def data_aug():
    src_root_dir = "/mnt/c/Users/yishi/Desktop/work/input/jscas"
    save_root_dir = "/mnt/c/Users/yishi/Desktop/work/result/Images/jscas"

    src_dirs = glob( os.path.join( src_root_dir, "*") )

    for src_dir in src_dirs:
        labels = glob(
            os.path.join(src_dir, "label/*.png")
        )
        for label_path in labels:
            img_path = label_path.replace("label", "movieframe")
            _augment(label_path, src_root_dir, save_root_dir)
            _augment(img_path, src_root_dir, save_root_dir)


def _augment(img_path, src_root_dir, save_root_dir):
    image = Image.open(img_path)
    image = image.convert("RGB")
    save_path = img_path.replace(src_root_dir, save_root_dir)
    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, angle in enumerate(range(-45,46,45)):
        # 回転
        img_r = image.rotate(angle)
        save_r_path = _change_filename(save_path, f"r{i}")
        img_r.save(save_r_path)

        # 反転
        img_trans = img_r.transpose(Image.FLIP_LEFT_RIGHT)
        save_t_path = _change_filename(save_path, f"t{i}")
        img_trans.save(save_t_path)


def _change_filename(path, addition_txt):
    basename = os.path.basename(path)
    s_basename = basename.split(".")
    new_name = s_basename[0] + addition_txt
    out_path = path.replace(
        s_basename[0],
        new_name
    )
    return out_path

if __name__ == "__main__":
    data_aug()
