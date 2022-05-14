import os
import shutil
import argparse
from DL.models.utils.image_crop import image_crop


class Preprocess:
    def __init__(self, src_dir, dst_dir):
        self.src_dir = src_dir
        self.dst_dir = dst_dir
        self.split_dir = os.listdir(src_dir)
        self.waste_class = []

    def create_folder(self):
        """최상위 쓰레기 분류군 이름의 폴더 생성"""
        if not os.path.isdir(self.dst_dir):
            os.mkdir(self.dst_dir)

        for folder in self.split_dir:
            if not os.path.isdir(self.dst_dir + '/' + folder):
                os.mkdir(self.dst_dir + '/' + folder)

            for dir_ in os.listdir(self.src_dir + '/Training'):
                wc = dir_.split('_')[0].split(']')[1]
                self.waste_class.append(wc)
                wc_dir = os.path.join(self.dst_dir, folder, wc)
                if not os.path.isdir(wc_dir):
                    os.makedirs(wc_dir)

        print("Waste class directories were successfully created")

    def move_files(self):
        """분류군 폴더에 맞게 쓰레기 이미지와 주석 파일 이동"""
        try:
            cur_wc = ''
            paste_path = ''

            for (root, dirs, files) in os.walk(self.src_dir):
                for f in files:
                    cur_path = os.path.join(root, f)
                    for wc in self.waste_class:
                        if wc in cur_path:
                            cur_wc = wc

                    for folder in self.split_dir:
                        if folder in cur_path:
                            paste_path = os.path.join(self.dst_dir, folder, cur_wc, f)

                    if not os.path.exists(paste_path):
                        shutil.copy(cur_path, paste_path)

            print("Waste images and annotations were successfully copied")

        except Exception as e:
            print(e)

    def do_image_crop(self):
        """쓰레기가 찍힌 범위로 이미지 자르기"""
        try:
            cur_wc = ''
            jpath = ''

            for (root, dirs, files) in os.walk(self.dst_dir):
                if '_라벨링데이터' in root:
                    continue

                for f in files:
                    cur_path = os.path.join(root, f)
                    for wc in self.waste_class:
                        if wc in cur_path:
                            cur_wc = wc

                    ipath = os.path.join(root, f)
                    jf = os.path.join(f).replace('.jpg', '.Json')

                    for folder in self.split_dir:
                        if folder in ipath:
                            jpath = os.path.join(self.dst_dir, folder + '_라벨링데이터', cur_wc, jf)

                    image_crop(ipath, jpath)

            print("Images were successfully cropped")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="preprocess")
    parser.add_argument('--src_dir', required=True, help='source path')
    parser.add_argument('--dst_dir', required=True, help='destination path')
    args = parser.parse_args()

    p = Preprocess(args.src_dir, args.dst_dir)
    p.create_folder()
    p.move_files()
    p.do_image_crop()
