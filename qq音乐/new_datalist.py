from torch.utils.data import Dataset
from PIL import Image


class ImageListDataset(Dataset):
    def __init__(self, txt_path, transform=None, target_transform=None):
        fh = open(txt_path, 'r')  # 只读
        imgs = []
        for line in fh:
            line = line.rstrip()  # rstrip删除空格
            words = line.split()
            imgs.append((words[0], int(words[1])))  # 添加数据和标签
        # imgs.append((words[1], int(words[2])))

        self.imgs = imgs  # 最主要就是要生成这个list， 然后DataLoader中给index，通过getitem读取图片数据
        self.transform = transform
        self.target_transform = target_transform

    def __getitem__(self, index):
        # 获取图像和标签
        fn, label = self.imgs[index]
        img = Image.open(fn).convert('RGB')  # 像素值 0~255，在transfrom.totensor会除以255，使像素值变成 0~1
        if self.transform is not None:
            img = self.transform(img)  # 在这里做transform，转为tensor等
        # img = torchvision.transforms.functional.to_tensor(img)
        return img, label

    def __len__(self):
        return len(self.imgs)

