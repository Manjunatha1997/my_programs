# ===================== IMPORTS =====================
import os
import cv2
import torch
import numpy as np
import xml.etree.ElementTree as ET
from pascal_voc_writer import Writer
import kornia.augmentation as K
from tqdm import tqdm  # <-- progress bar

# ===================== CONFIG =====================
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
IMAGE_DIR = r"D:\test_aug"
OUTPUT_DIR = IMAGE_DIR + "_aug"
TARGET_SIZE = (800, 800)

GPU_AUGS = {
    "brightness": K.ColorJitter(brightness=0.5, contrast=0.0, saturation=0.0, hue=0.0, p=1.0),
    "contrast": K.ColorJitter(brightness=0.0, contrast=1.5, saturation=0.0, hue=0.0, p=1.0),
    "horizontal_flip": K.RandomHorizontalFlip(p=1.0),
    "rotate": None  # handled separately
}

# ===================== HELPER FUNCTIONS =====================
def create_dir(path):
    os.makedirs(path, exist_ok=True)

def read_voc_annotation(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    boxes, labels = [], []
    for obj in root.findall("object"):
        label = obj.find("name").text
        bnd = obj.find("bndbox")
        xmin = int(bnd.find("xmin").text)
        ymin = int(bnd.find("ymin").text)
        xmax = int(bnd.find("xmax").text)
        ymax = int(bnd.find("ymax").text)
        boxes.append([float(xmin), float(ymin), float(xmax), float(ymax)])
        labels.append(label)
    return boxes, labels

def rotate_fit(image, boxes, angle, target_size=None):
    """Rotate image and bounding boxes without cropping corners."""
    h, w = image.shape[:2]
    rad = np.deg2rad(angle)
    cos_a, sin_a = np.cos(rad), np.sin(rad)
    new_w = int(abs(h*sin_a) + abs(w*cos_a))
    new_h = int(abs(h*cos_a) + abs(w*sin_a))

    if target_size:
        scale = min(target_size[0]/new_w, target_size[1]/new_h)
        new_w = int(new_w*scale)
        new_h = int(new_h*scale)
        image = cv2.resize(image, (int(w*scale), int(h*scale)))
        boxes = [[x*scale, y*scale, x2*scale, y2*scale] for x,y,x2,y2 in boxes]
        h, w = image.shape[:2]

    cx, cy = w/2, h/2
    M = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)
    M[0,2] += (new_w - w)/2
    M[1,2] += (new_h - h)/2

    rotated_img = cv2.warpAffine(image, M, (new_w, new_h), borderValue=(0,0,0))
    rotated_boxes = []
    for box in boxes:
        x1, y1, x2, y2 = box
        pts = np.array([[x1, y1],[x2, y1],[x2, y2],[x1, y2]])
        pts_h = np.hstack([pts, np.ones((4,1))])
        rot_pts = (M @ pts_h.T).T
        x_min, y_min = rot_pts[:,0].min(), rot_pts[:,1].min()
        x_max, y_max = rot_pts[:,0].max(), rot_pts[:,1].max()
        rotated_boxes.append([x_min, y_min, x_max, y_max])
    return rotated_img, rotated_boxes

def augment_and_save(image_path, output_dir, device, target_size=None):
    base_name = os.path.basename(image_path)
    name_only, ext = os.path.splitext(base_name)

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    xml_path = os.path.splitext(image_path)[0] + ".xml"
    boxes, labels = read_voc_annotation(xml_path)
    h, w, c = image.shape

    img_tensor = torch.from_numpy(image).permute(2,0,1).unsqueeze(0).float()/255.0
    img_tensor = img_tensor.to(device)

    for aug_name, aug_module in GPU_AUGS.items():
        if aug_name == "rotate":
            angle = np.random.uniform(-30, 30)
            aug_img, aug_boxes = rotate_fit(image, boxes, angle, target_size=target_size)
            aug_h, aug_w = aug_img.shape[:2]
        else:
            aug_img_tensor = aug_module(img_tensor)
            aug_img = (aug_img_tensor[0].permute(1,2,0).cpu().numpy()*255).astype(np.uint8)
            if aug_name == "horizontal_flip":
                aug_boxes = [[w - x2, y1, w - x1, y2] for x1,y1,x2,y2 in boxes]
            else:
                aug_boxes = boxes.copy()
            aug_h, aug_w = h, w

        save_img_path = os.path.join(output_dir, f"{name_only}_{aug_name}{ext}")
        cv2.imwrite(save_img_path, cv2.cvtColor(aug_img, cv2.COLOR_RGB2BGR))

        writer = Writer(save_img_path, aug_w, aug_h)
        for box, label in zip(aug_boxes, labels):
            writer.addObject(label, int(box[0]), int(box[1]), int(box[2]), int(box[3]))
        writer.save(save_img_path.replace(ext, ".xml"))

# ===================== MAIN =====================
if __name__ == "__main__":
    create_dir(OUTPUT_DIR)
    print(f"Using device: {DEVICE}")

    image_files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith((".jpg",".png",".jpeg"))]

    # Use tqdm for progress bar
    for img_file in tqdm(image_files, desc="Augmenting images", unit="image"):
        augment_and_save(os.path.join(IMAGE_DIR, img_file), OUTPUT_DIR, DEVICE, target_size=TARGET_SIZE)

    print("All images and XMLs saved in:", OUTPUT_DIR)
