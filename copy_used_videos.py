#!/usr/bin/env python3
"""
Kullanılan videoları yeni bir klasöre kopyalar.
Her dosyanın adına duygu (emotion) ve kafa pozu (head pose) bilgisi eklenir.
"""

import json
import shutil
import re
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "video_pairs_config.json"

# Kaynak klasör: Desktop'taki Data
SOURCE_BASE = Path("/Users/melikekara/Desktop/Research-User-Study/videos/Data")

# Hedef klasör: Yeni oluşturulacak
TARGET_DIR = SCRIPT_DIR / "videos" / "UsedVideos"

# Kafa pozu eşleştirme tablosu
HEAD_POSE_MAP = {
    "041": "left",       # Sola bakış
    "051": "front",      # Önden bakış  
    "080": "right",      # Sağa bakış
}


def detect_emotion(folder_name: str) -> str:
    """Klasör adından duyguyu tespit et."""
    folder_lower = folder_name.lower()
    if "angry" in folder_lower:
        return "angry"
    elif "disgust" in folder_lower:
        return "disgust"
    elif "happy2" in folder_lower:
        return "happy2"
    elif "happy" in folder_lower:
        return "happy"
    elif "sad2" in folder_lower:
        return "sad2"
    elif "sad" in folder_lower:
        return "sad"
    elif "surprise" in folder_lower:
        return "surprise"
    elif "neutral" in folder_lower:
        return "neutral"
    else:
        return "unknown"


def detect_head_pose(file_name: str) -> str:
    """Dosya adından kafa pozunu tespit et.
    
    Dosya adı örneği: 001_01_01_041_17_crop_128--01-01-01-01-01-01-01_with_audio.mp4
    Burada 041, 051, 080 gibi değerler kafa pozunu gösterir.
    """
    # Dosya adındaki _XXX_ pattern'lerini ara (041, 051, 080)
    for code, pose in HEAD_POSE_MAP.items():
        if f"_{code}_" in file_name:
            return pose
    return "unknown"


def main():
    # Config dosyasını oku
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        pairs = json.load(f)

    # Tüm benzersiz video yollarını topla
    video_paths = set()
    for pair in pairs:
        video_paths.add(pair["left"])
        video_paths.add(pair["right"])

    print(f"Toplam benzersiz video sayısı: {len(video_paths)}")

    # Hedef klasörü oluştur
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Hedef klasör: {TARGET_DIR}")

    copied_count = 0
    skipped_count = 0

    for rel_path in sorted(video_paths):
        # rel_path örneği: "videos/Data/out_neutral_001/001_01_01_041_17_crop_128--01-01-01-01-01-01-01_with_audio.mp4"
        # Bunu parçalara ayır
        parts = rel_path.split("/")
        # parts: ['videos', 'Data', 'out_neutral_001', '001_01_01_041_17_crop_128--01-01-01-01-01-01-01_with_audio.mp4']

        if len(parts) < 4:
            print(f"⚠️  Geçersiz yol atlanıyor: {rel_path}")
            skipped_count += 1
            continue

        folder_name = parts[2]  # out_neutral_001, out_angry_001_041, vb.
        file_name = parts[3]    # 001_01_01_041_17_crop_128--01-01-01-01-01-01-01_with_audio.mp4

        # Duyguyu tespit et
        emotion = detect_emotion(folder_name)
        
        # Kafa pozunu tespit et
        head_pose = detect_head_pose(file_name)

        # Kaynak dosya yolu
        source_file = SOURCE_BASE / folder_name / file_name

        # Yeni dosya adı: duygu_kafapozu_originalname.mp4
        # Örnek: neutral_front_001_01_01_041_17_crop_128--01-01-01-01-01-01-01_with_audio.mp4
        new_file_name = f"{emotion}_{head_pose}_{file_name}"
        target_file = TARGET_DIR / new_file_name

        if not source_file.exists():
            print(f"❌ Kaynak bulunamadı: {source_file}")
            skipped_count += 1
            continue

        if target_file.exists():
            print(f"⏭️  Zaten var, atlanıyor: {target_file.name}")
            skipped_count += 1
            continue

        # Kopyala
        shutil.copy2(source_file, target_file)
        print(f"✅ Kopyalandı: {new_file_name}")
        copied_count += 1

    print(f"\n{'='*50}")
    print(f"Kopyalanan: {copied_count}")
    print(f"Atlanan:    {skipped_count}")
    print(f"Hedef:      {TARGET_DIR}")


if __name__ == "__main__":
    main()
