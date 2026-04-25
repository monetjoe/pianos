import os
import torch
import torch.nn as nn
from torchvision.models import squeezenet1_1

TMP_DIR = "./__pycache__/tmp"
EN_US = os.getenv("LANG") != "zh_CN.UTF-8"

ZH2EN = {
    "上传钢琴录音": "Upload a piano recording",
    "状态栏": "Status",
    "音频文件名": "Audio filename",
    "钢琴分类结果": "Piano classification result",
    "建议录音时长保持在 3s 左右, 过长会影响识别效率": "It is recommended to keep the duration of recording around 3s, too long will affect the recognition efficiency.",
    "引用": "Cite",
    "珠江": "Pearl River",
    "英昌": "YOUNG CHANG",
    "施坦威剧场": "STEINWAY Theater",
    "星海": "HSINGHAI",
    "卡瓦依": "KAWAI",
    "施坦威": "STEINWAY",
    "卡瓦依三角": "KAWAI Grand",
    "雅马哈": "YAMAHA",
}

if EN_US:
    import huggingface_hub

    MODEL_DIR = huggingface_hub.snapshot_download(
        "ccmusic-database/pianos",
        cache_dir="./__pycache__",
    )

else:
    import modelscope

    MODEL_DIR = modelscope.snapshot_download(
        "ccmusic-database/pianos",
        cache_dir="./__pycache__",
    )


def _L(zh_txt: str):
    return ZH2EN[zh_txt] if EN_US else zh_txt


def Classifier(cls_num=8, output_size=512, linear_output=False):
    q = (1.0 * output_size / cls_num) ** 0.25
    l1 = int(q * cls_num)
    l2 = int(q * l1)
    l3 = int(q * l2)
    if linear_output:
        return torch.nn.Sequential(
            nn.Dropout(),
            nn.Linear(output_size, l3),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(l3, l2),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(l2, l1),
            nn.ReLU(inplace=True),
            nn.Linear(l1, cls_num),
        )

    else:
        return torch.nn.Sequential(
            nn.Dropout(),
            nn.Conv2d(output_size, l3, kernel_size=(1, 1), stride=(1, 1)),
            nn.ReLU(inplace=True),
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(l3, l2),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(l2, l1),
            nn.ReLU(inplace=True),
            nn.Linear(l1, cls_num),
        )


def net(weights=MODEL_DIR + "/save.pt"):
    model = squeezenet1_1(pretrained=False)
    model.classifier = Classifier()
    model.load_state_dict(
        torch.load(
            weights,
            map_location=torch.device("cuda:0") if torch.cuda.is_available() else "cpu",
        )
    )
    model.eval()
    return model
