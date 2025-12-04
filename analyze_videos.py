#!/usr/bin/env python3
"""
Analyze video files and generate videoPairs configuration for the user study
"""

import os
import json
from pathlib import Path

# Base directory
base_dir = Path("videos/Data")

# Find all folders
folders = sorted([f for f in os.listdir(base_dir) if f.startswith("out_") and os.path.isdir(base_dir / f)])

print(f"Found {len(folders)} video folders:\n")

# Group by expression
expressions = {}
for folder in folders:
    # Parse expression name (e.g., "out_angry_001_041" -> "angry")
    parts = folder.replace("out_", "").split("_")
    
    # Get expression name (first part)
    expression = parts[0]
    if expression.endswith("2"):
        expression = expression[:-1]  # Remove the "2" suffix
    
    if expression not in expressions:
        expressions[expression] = []
    
    # Find the video file matching pattern: *_crop_*_with_audio.mp4
    # Exclude files with "concat" or "final" in the name
    folder_path = base_dir / folder
    video_files = []
    if folder_path.is_dir():
        for file in folder_path.iterdir():
            if (file.suffix == '.mp4' and 
                '_with_audio.mp4' in file.name and
                'concat' not in file.name and
                'final' not in file.name and
                'crop' in file.name):
                video_files.append(file)
    
    # Use the first matching video file
    if video_files:
        expressions[expression].append({
            "folder": folder,
            "path": str(video_files[0])
        })

# Print summary
print("=" * 60)
print("VIDEO SUMMARY BY EXPRESSION")
print("=" * 60)
for expression, videos in sorted(expressions.items()):
    print(f"\n{expression.upper()}: {len(videos)} videos")
    for v in videos:
        print(f"  - {v['folder']}")

print("\n" + "=" * 60)
print("GENERATING VIDEO PAIRS")
print("=" * 60)

# Generate video pairs (comparing neutral with each expression)
video_pairs = []
pair_id = 1

# Get neutral videos as baseline
neutral_videos = expressions.get("neutral", [])

if neutral_videos:
    print(f"\nUsing {len(neutral_videos)} neutral videos as baseline")
    
    for expression, exp_videos in sorted(expressions.items()):
        if expression == "neutral":
            continue
            
        print(f"\n{expression.upper()} pairs:")
        for i, exp_video in enumerate(exp_videos):
            # Use corresponding neutral video (or first one if not enough)
            neutral_video = neutral_videos[min(i, len(neutral_videos) - 1)]
            
            pair = {
                "id": f"pair{pair_id}_{expression}_{i+1}",
                "left": neutral_video["path"],
                "right": exp_video["path"],
                "description": f"Neutral vs {expression.capitalize()}"
            }
            video_pairs.append(pair)
            print(f"  Pair {pair_id}: {neutral_video['folder']} vs {exp_video['folder']}")
            pair_id += 1

# Save to JSON file
output_file = "video_pairs_config.json"
with open(output_file, "w") as f:
    json.dump(video_pairs, f, indent=2)

print(f"\n{'-' * 60}")
print(f"Generated {len(video_pairs)} video pairs")
print(f"Configuration saved to: {output_file}")
print(f"{'-' * 60}")

# Generate JavaScript code for HTML
print("\n" + "=" * 60)
print("JAVASCRIPT CODE FOR HTML")
print("=" * 60)
print("\nconst videoPairs = [")
for pair in video_pairs[:10]:  # Show first 10 as example
    print(f'  {{')
    print(f'    id: "{pair["id"]}",')
    print(f'    left: "{pair["left"]}",')
    print(f'    right: "{pair["right"]}"')
    print(f'  }},')
if len(video_pairs) > 10:
    print(f'  // ... {len(video_pairs) - 10} more pairs')
print('];')
