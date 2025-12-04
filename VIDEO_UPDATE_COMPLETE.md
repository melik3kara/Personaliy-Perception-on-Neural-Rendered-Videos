# ✅ Video Paths Updated Successfully!

## Changes Made

### Updated Video File Selection
- **OLD**: Used `final_with_audio.mp4` files (concatenated versions)
- **NEW**: Using original `*_crop_*_with_audio.mp4` files
- **Excluded**: Files with "concat" or "final" in the name

### Video Pairs Summary
- **Total Pairs**: 21 (reduced from 24)
- **Removed**: 
  - `out_angry` folder (no crop file)
  - `out_happy` folder (no crop file)  
  - `out_sad` folder (no crop file)
  - `out_examples.mp4` folder (not a proper video folder)

### Current Video Distribution
- **Angry**: 3 pairs
- **Disgust**: 3 pairs
- **Happy**: 6 pairs
- **Sad**: 6 pairs
- **Surprise**: 3 pairs
- **Total**: 21 pairs × 6 questions = **126 total responses**

## File Naming Pattern

All videos now follow this pattern:
```
001_01_01_[ID]_crop_128--01-01-[EXPRESSION]-[PARAMS]_with_audio.mp4
```

### Expression Codes in Filenames
- `01-01-01-...` = Neutral
- `01-01-03-...` = Happy
- `01-01-04-...` = Sad
- `01-01-05-...` = Angry
- `01-01-07-...` = Disgust
- `01-01-08-...` = Surprise

### Example Video Pair

**Pair 1 - Neutral vs Angry:**
- **Left** (Neutral): `out_neutral_001/001_01_01_041_17_crop_128--01-01-01-01-01-01-01_with_audio.mp4`
- **Right** (Angry): `out_angry_001_041/001_01_01_041_17_crop_128--01-01-05-01-01-01-01_with_audio.mp4`

## Verified File Paths

✅ All 21 video pairs have been verified to exist in:
```
/Users/melikekara/Desktop/Research-User-Study/videos/Data/
```

## Files Updated

1. ✅ **analyze_videos.py** - Updated to select correct video files
2. ✅ **video_pairs_config.json** - Regenerated with 21 pairs
3. ✅ **user_study_prototype.html** - Updated with correct video paths

## Ready to Test!

Open the HTML file now:
```bash
open user_study_prototype.html
```

Or use the quick launcher:
```bash
./open_study.sh
```

## What to Expect

When you open the study:
1. **Consent Screen** ✅
2. **Demographics** (optional) ✅
3. **Instructions** ✅
4. **21 Video Pairs** - Each with:
   - Left video (Neutral expression)
   - Right video (Expressive: angry, happy, sad, disgust, or surprise)
   - 6 personality questions
   - Left/Equal/Right buttons
5. **Thank You Screen** ✅

## Video Details

Each video is:
- **Format**: MP4 with audio
- **Size**: ~50-60 KB each
- **Duration**: Short clips (few seconds)
- **Features**: Looping, controls enabled, autoplay (muted by default)

## Data Collection

After completing the study, data will be available in:
1. **Browser Console** - Look for `=== STUDY RESPONSES ===`
2. **LocalStorage** - Key: `studyResponses`

### Expected Data Format
```json
{
  "demographics": {
    "age": "25",
    "gender": "female",
    "country": "Turkey"
  },
  "trials": [
    {
      "pairId": "pair1_angry_1",
      "answers": {
        "extraversion": "right",
        "agreeableness": "left",
        "conscientiousness": "equal",
        "emotionalStability": "left",
        "openness": "equal",
        "naturalness": "left"
      }
    }
    // ... 20 more pairs
  ]
}
```

## Troubleshooting

### If Videos Don't Play
1. Check browser console (Cmd+Option+I) for errors
2. Verify video files exist in `videos/Data/` folders
3. Try a different browser (Chrome recommended)
4. Check if file paths match exactly

### If You Need to Regenerate Config
```bash
python3 analyze_videos.py
```

This will scan your videos folder and regenerate `video_pairs_config.json` with the correct file paths.

## Study Statistics

- **Questions per pair**: 6
- **Total pairs**: 21
- **Total questions**: 126
- **Response options**: 3 (Left/Equal/Right)
- **Estimated completion time**: 10-12 minutes

## All Set! 🎉

Your study is now configured with the correct video files. The videos use the original `*_crop_*_with_audio.mp4` format without concatenation or final processing.

---
*Updated: November 25, 2025*
*Video count: 21 pairs (42 unique videos)*
