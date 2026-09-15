---
source: user-provided-learning-resources
ingested: 2026-09-15
---

# Multimodal Tokenization Image

This manifest records the diagram used for the 2026-09-15 `multimodal-tokenization` concept synthesis. The image remains in the user's private Hermes image cache and is represented by its filename and content hash rather than copied into the repository.

- File: `img_21dc73931019.png` (Hermes image cache)
- Hash (sha256): `f8797f61a5b36d542409423a112cfe63a62f9f3c4d1c5096712a9455e389393f`

## Content transcription

"How Different Modalities Become Tokens" — how text, images, audio, video, 3D point clouds, and robotic/embodied inputs are converted into tokens a Transformer can process:

- **Text**: tokenization then embedding (e.g. 768-dimensional vectors).
- **Images**: split into 16×16 patches.
- **Audio**: spectrogram features extracted from a 16 kHz waveform.
- **Video**: sampled frames and tubelets.
- **3D data**: organized as points, voxels, or patches.
- **Robotics/embodied**: visual, state, tactile, and action streams are preprocessed.

Each modality passes through a dedicated encoder that emits a `[N × D]` vector sequence. These sequences are then fed into a Transformer, or fused into a unified token sequence for a cross-modal model.