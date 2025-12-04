#!/bin/bash
# Script to open the user study in your default browser

echo "Opening Personality Perception User Study..."
echo "============================================="
echo ""
echo "Study Overview:"
echo "- 24 video pairs comparing neutral vs. expressive faces"
echo "- 6 questions per pair (144 total questions)"
echo "- Expressions: Angry, Disgust, Happy, Sad, Surprise"
echo ""
echo "Opening in browser..."

open user_study_prototype.html

echo ""
echo "✓ Study opened in browser"
echo ""
echo "To collect data:"
echo "1. Complete the study"
echo "2. Open browser console (Cmd+Option+I)"
echo "3. Look for '=== STUDY RESPONSES ==='"
echo "4. Copy the JSON data"
