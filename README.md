# Personality Perception on Neural Rendered Videos

## Overview
This repository contains the dataset and stimuli for investigating how facial expressions and head orientation influence personality perception in neural-rendered talking head videos. The work is based on our research paper: **"The Impact of Facial Expression and Head Orientation on Personality Perception"** published in *Computers & Graphics* (2025).

This dataset was created to study how nonverbal visual cues—specifically facial expressions and head poses—shape first impressions and personality attribution in synthetic faces, with implications for designing more relatable digital humans and virtual assistants.

## Stimulus Generation Method

To implement a controlled approach for studying personality perception, we utilize high-quality driving signals from the speech subset of the [RAVDESS](https://doi.org/10.1371/journal.pone.0196391) (Ryerson Audio-Visual Database of Emotional Speech and Song) corpus, which provides professionally acted emotional expressions under consistent recording conditions. All auditory and linguistic channels were removed to isolate the impact of nonverbal facial motion and head dynamics on personality perception, preventing cross-modal dominance effects.

Using left and front images of a neutral base identity from the [Multi-PIE dataset](https://www.kaggle.com/datasets/aliates/multi-pie) and the [LivePortrait](https://arxiv.org/abs/2407.03168) neural reenactment model, we generated controlled stimuli featuring:

- **Base Identity**: Single neutral identity from Multi-PIE dataset providing consistent facial structure across all conditions
- **Emotional Expressions**: Four universal emotions (angry, happy, sad, surprise) from RAVDESS driving videos
- **Head Orientations**: Two viewing angles (frontal and left-facing) to examine head pose effects
- **Controlled Duration**: 3-4 second clips with comparable temporal duration and expressive salience

LivePortrait's neural reenactment pipeline disentangles identity-specific appearance features from motion representations through dense motion fields and keypoint-based correspondence, enabling controlled manipulation of expression and head orientation while preserving identity-specific shape. This methodology ensures high fidelity and controlled variation across experimental conditions while maintaining ecological validity through naturalistic expressions.

## Dataset Structure
```
videos/
├── StudyStimuli/                 # Final stimuli used in the user study (as described in paper)
│                                  # Contains 24 video pairs for personality perception experiments
└── GeneratedVideos/              # All generated videos from neural rendering pipeline
    ├── out_neutral_001/          # Neutral expression baseline
    ├── out_angry/                # Angry expression videos
    ├── out_angry_001_041/
    ├── out_angry_001_051/
    ├── out_angry_001_080/
    ├── out_disgust_001_01_01_041_17_crop_128/
    ├── out_disgust_001_01_01_051_04_crop_128/
    ├── out_disgust_001_01_01_080_08_crop_128/
    ├── out_happy/
    ├── out_happy_001_041/
    ├── out_happy_001_051/
    ├── out_happy_001_080/
    ├── out_happy2_001_01_01_041_17_crop_128/
    ├── out_happy2_001_01_01_051_04_crop_128/
    ├── out_happy2_001_01_01_080_08_crop_128/
    ├── out_sad/
    ├── out_sad_001_041/
    ├── out_sad_001_051/
    ├── out_sad_001_080/
    ├── out_sad2_001_01_01_041_17_crop_128/
    ├── out_sad2_001_01_01_051_04_crop_128/
    ├── out_sad2_001_01_01_080_08_crop_128/
    ├── out_surprise_001_041/
    ├── out_surprise_001_051/
    └── out_surprise_001_080/
```

**Note**: The `StudyStimuli/` folder contains the curated video pairs used in the user study described in our paper. The `GeneratedVideos/` folder contains all videos generated during the neural rendering process, including various quality levels and experimental variations.

## Video Specifications
- **Format**: MP4 with audio (muted during experiments)
- **Expressions**: Four basic emotions (Angry, Happy, Sad, Surprise)
- **Head Orientations**: Frontal view and left-facing view
- **Base Identity**: Single neutral identity from Multi-PIE dataset
- **Total Conditions**: 8 video clips (4 expressions × 2 head poses)
- **Comparison Pairs**: 10 pairs for controlled pairwise comparison
- **Duration**: 3-4 seconds per clip (looped during presentation)

## User Study Design

The dataset supports personality perception studies using a forced-choice pairwise comparison paradigm. We generated **8 video clips** (4 expressions × 2 head poses) and constructed **10 comparison pairs** to isolate the effects of facial expression and head orientation on perceived personality traits.

### Experimental Design

From the 8 base video conditions, we systematically constructed two types of comparison pairs:

**Type 1: Same Expression, Different Head Orientation (4 pairs)**
- Isolates the effect of head orientation by comparing frontal and left-facing views under the same emotional expression
- Examples: Happy-Front vs. Happy-Left, Angry-Front vs. Angry-Left

**Type 2: Different Expression, Same Head Orientation (6 pairs)**
- Isolates the effect of facial expression by comparing different emotions under a fixed frontal pose
- Examples: Angry-Front vs. Happy-Front, Happy-Front vs. Sad-Front

### Questions Asked

For each video pair, participants answer six questions based on the Big Five personality traits plus perceived naturalness:

1. **Extraversion**: Which video looks more *extraverted, expressive, and energetic*?
2. **Agreeableness**: Which video looks more *friendly, warm, and cooperative*?
3. **Conscientiousness**: Which video looks more *organized, controlled, and deliberate*?
4. **Emotional Stability**: Which video looks *calmer, more emotionally steady, and less tense*?
5. **Openness**: Which video looks more *open-minded, curious, and thoughtful*?
6. **Naturalness**: Which video appears more *natural and human-like*?

**Response Options**: Left | Equal | Right

**Note**: Naturalness is included as a control dimension to ensure that observed personality differences are driven by intended visual cues rather than technical rendering artifacts or motion instability.

### Study Configuration

- **Participants**: N = 80 (recruited via Prolific, UK/US, English-fluent, desktop/laptop required)
- **Total Pairs**: 10 comparison pairs
- **Expressions**: Angry, Happy, Sad, Surprise (4 emotions)
- **Head Poses**: Frontal view, Left-facing view (2 orientations)
- **Format**: Side-by-side video comparison with forced-choice responses
- **Randomization**: Pair order and left-right video placement randomized per participant
- **Data Collection**: Responses encoded as -1 (left stronger), 0 (equal), +1 (right stronger)

## Dataset Usage

This dataset is designed for research on:
- **Personality perception** in synthetic/neural-rendered faces
- **Effects of emotional expressions** on first impressions and social judgments
- **Head pose influence** on personality attribution in talking heads
- **Avatar realism** and uncanny valley effects in neural-rendered videos
- **Facial expression synthesis** quality assessment
- **Human-computer interaction** and virtual agent design
- **Design guidelines** for socially expressive digital humans

### Key Findings

Our user study (N=80) revealed:
- **Happy expressions** dominate positive social traits (extraversion, agreeableness, emotional stability, openness)
- **Head orientation effects are context-dependent**: frontal view is perceived as more extraverted, but left-facing view projects greater emotional stability when expressing sadness or surprise
- **Design implications**: Virtual agents can be programmed to automatically adjust head orientation based on emotional context (e.g., turning to the side when expressing sadness to appear more emotionally stable)

## Video Configuration

The `video_pairs_config.json` file contains metadata about the 10 comparison pairs used in the user study, including:
- Pair IDs and types (same-expression or different-expression comparisons)
- Video file paths for each condition
- Expression labels and head orientation information
- Experimental configurations for replication

## Utility Scripts

- `analyze_videos.py` - Analyze video folder structure and extract metadata
- `copy_used_videos.py` - Organize and copy videos for experiments
- `create_selected_grid.py` - Generate video grid visualizations
- `create_stimuli_grid.py` - Create stimulus presentation grids for figures
- `extract_happy_left_last_frames.py` - Extract specific frames from video sequences
- `extract_middle_frames.py` - Extract middle frames for static analysis

## Stimuli Figures

The `stimuli_figures/frames_for_selection/` directory contains extracted frames used for stimulus selection, visualization, and figure generation in the paper.

## References

This dataset builds upon the following resources:

- **LivePortrait**: Guo, J., Zhang, D., Liu, X., et al. (2025). [LivePortrait: Efficient portrait animation with stitching and retargeting control](https://arxiv.org/abs/2407.03168). arXiv:2407.03168.

- **RAVDESS**: Livingstone, S.R., Russo, F.A. (2018). [The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS)](https://doi.org/10.1371/journal.pone.0196391). PLOS One, 13(5):e0196391.

- **Multi-PIE**: Gross, R., Matthews, I., Cohn, J., Kanade, T., Baker, S. (2010). [Multi-PIE](https://doi.org/10.1016/j.imavis.2009.08.002). Image and Vision Computing, 28(5):807-813.


## Contact

For questions about this dataset, please open an issue on this repository.
