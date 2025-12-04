# Personality Perception User Study

## Overview
This is a psychology user study investigating how facial expressions and head positions influence personality perception during conversation.

## File Structure
```
Research-User-Study/
├── user_study_prototype.html    # Main study interface
├── videos/
│   └── Data/
│       ├── out_neutral_001/
│       ├── out_angry/
│       ├── out_happy/
│       ├── out_sad/
│       ├── out_disgust/
│       ├── out_surprise/
│       └── ... (29 folders total)
├── analyze_videos.py            # Script to analyze video structure
└── video_pairs_config.json      # Generated video pairs configuration
```

## Video Pairs Summary
- **Total Pairs**: 24 video pairs (removed examples.mp4 pair)
- **Expressions**: Angry (4), Disgust (3), Happy (7), Sad (7), Surprise (3)
- **Format**: Each pair compares a neutral expression video (left) with an expressive video (right)

## How to Use

### 1. Open the Study
Simply double-click `user_study_prototype.html` to open it in your default browser.
Or right-click → "Open With" → Choose your preferred browser (Chrome, Safari, Firefox).

### 2. Study Flow
1. **Consent Screen** - Read and agree to participate
2. **Demographics** - Optional age, gender, country (can skip)
3. **Instructions** - Task explanation
4. **Main Task** - View 24 video pairs and answer 6 questions each
5. **Debrief** - Thank you message

### 3. Collect Data
When a participant completes the study:
- Open browser console (F12 or Cmd+Option+I on Mac)
- Look for "=== STUDY RESPONSES ===" in the console
- Copy the JSON data
- Data is also saved to browser's localStorage

### Example Response Data Structure
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
    // ... 23 more pairs
  ]
}
```

## Questions Asked
For each video pair, participants answer:
1. Which video looks more **extraverted, expressive, and energetic**?
2. Which video looks more **friendly, warm, and cooperative**?
3. Which video looks more **organized, controlled, and deliberate**?
4. Which video looks **calmer, more emotionally steady, and less tense**?
5. Which video looks more **open-minded, curious, and thoughtful**?
6. Which video appears more **natural and human-like**?

Response options: **Left** | **Equal** | **Right**

## For Ethics Application
To take screenshots:
1. Open `user_study_prototype.html` in your browser
2. Navigate through each screen
3. Take screenshots of:
   - Consent screen
   - Demographics form
   - Instructions
   - Main task screen (with video pairs and questions)
   - Debrief/Thank you screen

## Customization

### Modify Video Pairs
Edit the `videoPairs` array in `user_study_prototype.html` (around line 421):
```javascript
const videoPairs = [
    {
        id: "pair1_angry_1",
        left: "videos/Data/out_neutral_001/final_with_audio.mp4",
        right: "videos/Data/out_angry/final_with_audio.mp4"
    },
    // Add or remove pairs here
];
```

### Modify Questions
Edit the `questions` array in `user_study_prototype.html` (around line 553):
```javascript
const questions = [
    {
        id: "extraversion",
        text: "Which video looks more extraverted, expressive, and energetic?"
    },
    // Add or modify questions here
];
```

## Technical Details
- **No Backend Required**: Everything runs in the browser
- **Browser Compatibility**: Works on Chrome, Firefox, Safari, Edge
- **Data Storage**: Responses stored in memory and localStorage
- **Video Format**: MP4 with audio, autoplay and loop enabled
- **Responsive Design**: Works on different screen sizes

## Troubleshooting

### Videos Not Playing
- Check if video files exist in `videos/Data/` folders
- Try a different browser (Chrome recommended)
- Check browser console for errors (F12)

### Videos Playing Without Sound
- Click on the video to unmute
- The videos are muted by default for autoplay compatibility
- Participants can enable sound using video controls

### Data Not Saving
- Check browser console (F12) for JavaScript errors
- Data is logged to console when study completes
- Also check localStorage: `localStorage.getItem('studyResponses')`

## Contact
For questions about this study, contact: [Your contact information]

## Generated Files
- `analyze_videos.py` - Python script to analyze video folder structure
- `video_pairs_config.json` - Complete video pairs configuration in JSON format
