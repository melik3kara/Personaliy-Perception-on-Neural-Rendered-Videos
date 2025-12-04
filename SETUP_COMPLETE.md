# Study Setup Complete! ✅

## What I Did

### 1. **Analyzed Your Videos** 📹
- Found 29 video folders in `/Users/melikekara/Downloads/Data/`
- Organized by expressions: Angry, Disgust, Happy, Sad, Surprise, Neutral
- Each folder contains `final_with_audio.mp4`

### 2. **Copied Videos to Project** 📁
- Copied all videos from Downloads to `Research-User-Study/videos/Data/`
- Total size: ~29 folders with multiple videos each

### 3. **Generated Video Pairs** 🎬
- Created 24 video pairs (removed the "examples.mp4" pair)
- Each pair compares **Neutral (left)** vs. **Expression (right)**
- Breakdown:
  - Angry: 4 pairs
  - Disgust: 3 pairs  
  - Happy: 7 pairs
  - Sad: 7 pairs
  - Surprise: 3 pairs

### 4. **Updated HTML File** 💻
- Replaced placeholder Google Drive URLs with local video paths
- All 24 pairs are now configured and ready to use
- Videos will play directly from your project folder

## Files Created

1. **user_study_prototype.html** - Main study interface (UPDATED ✨)
2. **analyze_videos.py** - Script to analyze video structure
3. **video_pairs_config.json** - Complete video configuration
4. **README.md** - Full documentation
5. **open_study.sh** - Quick launcher script

## How to Test Your Study

### Option 1: Double-Click
Simply double-click `user_study_prototype.html` in Finder

### Option 2: Use the Script
```bash
cd /Users/melikekara/Desktop/Research-User-Study
./open_study.sh
```

### Option 3: Terminal Command
```bash
open /Users/melikekara/Desktop/Research-User-Study/user_study_prototype.html
```

## Study Flow
1. **Consent Screen** ✅
2. **Demographics** (optional) ✅
3. **Instructions** ✅
4. **24 Video Pairs** × 6 Questions = 144 responses ✅
5. **Thank You Screen** ✅

## Data Collection

When someone completes the study:

1. **Open Browser Console**
   - Mac: `Cmd + Option + I`
   - Windows: `F12`

2. **Find the Data**
   - Look for `=== STUDY RESPONSES ===`
   - Copy the JSON data below it

3. **Alternative: LocalStorage**
   ```javascript
   localStorage.getItem('studyResponses')
   ```

## Video Pairs Structure

Each pair follows this pattern:
```javascript
{
    id: "pair1_angry_1",
    left: "videos/Data/out_neutral_001/final_with_audio.mp4",  // Neutral face
    right: "videos/Data/out_angry/final_with_audio.mp4"        // Expressive face
}
```

## Screenshots for Ethics Application

Navigate through the study and capture:
1. ✅ Consent screen
2. ✅ Demographics form  
3. ✅ Instructions page
4. ✅ Task screen with videos and questions
5. ✅ Completion/debrief screen

## Questions Participants Answer

For EACH of the 24 video pairs:

1. Which video looks more **extraverted, expressive, and energetic**?
2. Which video looks more **friendly, warm, and cooperative**?
3. Which video looks more **organized, controlled, and deliberate**?
4. Which video looks **calmer, more emotionally steady, and less tense**?
5. Which video looks more **open-minded, curious, and thoughtful**?
6. Which video appears more **natural and human-like**?

**Response options**: Left | Equal | Right

## Tips

### ✅ Everything Works Offline
- No internet connection needed
- All videos are local
- No backend server required

### ✅ Browser Compatibility
- Chrome ⭐ (recommended)
- Safari ✓
- Firefox ✓
- Edge ✓

### ✅ Data Privacy
- All data stays in browser
- Nothing sent to any server
- Completely anonymous

## Need to Modify?

### Change Number of Pairs
Edit `videoPairs` array in HTML (line ~421)

### Change Questions
Edit `questions` array in HTML (line ~553)

### Regenerate Video Pairs
```bash
python3 analyze_videos.py
```

## Quick Stats

- **Total Pairs**: 24
- **Questions per Pair**: 6
- **Total Responses**: 144
- **Estimated Time**: 10-15 minutes
- **Video Format**: MP4 with audio
- **File Size**: ~26KB HTML + videos

## All Set! 🎉

Your study is ready to go. Just open the HTML file and test it out!

For questions or issues, check the README.md file for troubleshooting tips.

---
*Generated on: November 25, 2025*
