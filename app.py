import os
import torch
import shutil
import librosa
import warnings
import numpy as np
import gradio as gr
import librosa.display
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from collections import Counter
from PIL import Image
from tqdm import tqdm
from model import net, _L, MODEL_DIR, TMP_DIR


def most_common_element(input_list):
    counter = Counter(input_list)
    mce, _ = counter.most_common(1)[0]
    return mce


def wav_to_mel(audio_path: str, width=0.18):
    os.makedirs(TMP_DIR, exist_ok=True)
    y, sr = librosa.load(audio_path, sr=48000)
    non_silent = y
    mel_spec = librosa.feature.melspectrogram(y=non_silent, sr=sr)
    log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)
    dur = librosa.get_duration(y=non_silent, sr=sr)
    total_frames = log_mel_spec.shape[1]
    step = int(width * total_frames / dur)
    count = int(total_frames / step)
    begin = int(0.5 * (total_frames - count * step))
    end = begin + step * count
    for i in tqdm(range(begin, end, step), desc="转换 wav 至 jpgs..."):
        librosa.display.specshow(log_mel_spec[:, i : i + step])
        plt.axis("off")
        plt.savefig(
            f"{TMP_DIR}/{os.path.basename(audio_path)[:-4]}_{i}.jpg",
            bbox_inches="tight",
            pad_inches=0.0,
        )
        plt.close()


def embed_img(img_path, input_size=224):
    transform = transforms.Compose(
        [
            transforms.Resize([input_size, input_size]),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )
    img = Image.open(img_path).convert("RGB")
    return transform(img).unsqueeze(0)


def infer(wav_path, folder_path=TMP_DIR):
    status = "Success"
    filename = result = None
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

        if not wav_path:
            raise ValueError("请输入音频!")

        wav_to_mel(wav_path)
        outputs = []
        all_files = os.listdir(folder_path)
        for file_name in all_files:
            if file_name.lower().endswith(".jpg"):
                file_path = os.path.join(folder_path, file_name)
                input = embed_img(file_path)
                output: torch.Tensor = net()(input)
                pred_id = torch.max(output.data, 1)[1]
                outputs.append(pred_id)

        max_count_item = most_common_element(outputs)
        filename = os.path.basename(wav_path)
        result = translate[classes[max_count_item]]

    except Exception as e:
        status = f"{e}"

    return status, filename, result


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    translate = {
        "PearlRiver": _L("珠江"),
        "YoungChang": _L("英昌"),
        "Steinway-T": _L("施坦威剧场"),
        "Hsinghai": _L("星海"),
        "Kawai": _L("卡瓦依"),
        "Steinway": _L("施坦威"),
        "Kawai-G": _L("卡瓦依三角"),
        "Yamaha": _L("雅马哈"),
    }
    classes = list(translate.keys())
    example_wavs = []
    for cls in classes:
        example_wavs.append(f"{MODEL_DIR}/examples/{cls}.wav")

    with gr.Blocks() as demo:
        gr.Interface(
            fn=infer,
            inputs=gr.Audio(type="filepath", label=_L("上传钢琴录音")),
            outputs=[
                gr.Textbox(label=_L("状态栏"), buttons=["copy"]),
                gr.Textbox(label=_L("音频文件名"), buttons=["copy"]),
                gr.Textbox(label=_L("钢琴分类结果"), buttons=["copy"]),
            ],
            examples=example_wavs,
            cache_examples=False,
            flagging_mode="never",
            title=_L("建议录音时长保持在 3s 左右, 过长会影响识别效率"),
        )

        gr.Markdown(
            f"# {_L('引用')}"
            + """
            ```bibtex
            @inproceedings{zhou2023holistic,
                title        = {A Holistic Evaluation of Piano Sound Quality},
                author       = {Monan Zhou and Shangda Wu and Shaohua Ji and Zijin Li and Wei Li},
                booktitle    = {National Conference on Sound and Music Technology},
                pages        = {3--17},
                year         = {2023},
                organization = {Springer}
            }
            ```"""
        )

    demo.launch(css="#gradio-share-link-button-0 { display: none; }")
