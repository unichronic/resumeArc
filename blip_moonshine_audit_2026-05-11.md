# Blip AI and Moonshine Audit

Date: 2026-05-11

## Scope

This audit is based on:

- Blip AI public desktop release `v0.5.2` from `abnsl0014/blipai-releases`, extracted from `app.asar`.
- Blip public pages and AppSumo founder answers.
- Moonshine public repository, license, README, and papers.
- Related ASR research around live/on-device dictation.

I did not use private credentials, call Blip production APIs, or inspect any private source repository.

## Executive Verdict

Adapting Moonshine is a credible strategy if the target product is English-first, low-latency, privacy-oriented dictation. For that use case, Moonshine v2 is a better architectural fit than a cloud Whisper pipeline because it is designed around streaming, short utterances, local inference, and low time-to-first-token.

The highest ROI is probably not modifying transformer internals first. The best first move is to adapt the product and inference layer around Moonshine:

- local streaming STT
- endpointing/VAD tuned for dictation
- domain vocabulary and spelling fusion
- confidence scoring and fallback routing
- punctuation/casing/post-processing
- platform-specific quantization and packaging

Only after you have a benchmark harness should you fine-tune or alter the model architecture. Without a strong eval set, model changes will be impossible to judge.

## Blip AI Audit

### Architecture Observed

Blip AI `v0.5.2` is an Electron desktop app. The app captures microphone audio locally, preprocesses it, sends it through Electron IPC, then uses cloud STT and LLM post-processing.

Observed app dependencies include:

- `groq-sdk`
- `microsoft-cognitiveservices-speech-sdk`
- `openai`
- `@azure/identity`
- `@cerebras/cerebras_cloud_sdk`
- `axios`
- `electron-store`
- `wavefile`

The public bundle did not include local model files such as `.onnx`, `.ort`, `.gguf`, `.tflite`, `.mlmodel`, `.pt`, `.pth`, or `.safetensors`.

### STT Path

Blip's default path appears to be Groq-based push-to-talk transcription:

- Audio capture in renderer.
- Resample to 16 kHz mono.
- Convert to 16-bit PCM.
- Local silence trimming/VAD-like preprocessing.
- Encode to WAV.
- Send audio buffer to main process via IPC.
- Transcribe through Groq STT.

The default STT model found in the bundle is:

- `whisper-large-v3`

Credentials are fetched from:

- `https://mantra-backend-app.azurewebsites.net`
- `/api/blipai/stt/credentials`

The public Blip API docs also expose:

- `POST https://mantra-backend-app.azurewebsites.net/api/blipai/stt/transcribe`

### LLM Path

The app then performs correction/formatting using the Groq SDK. The default LLM model found in the bundle is:

- `openai/gpt-oss-20b`

The LLM layer handles:

- style formatting
- command detection
- app-context-specific prompts
- custom dictionary support
- output length guards
- fallback to original text on failures

### Azure Path

An Azure Speech SDK path also exists. It appears to be a real-time or legacy mode:

- 16 kHz PCM push stream
- `speechRecognitionLanguage = "en-US"`
- silence timeout around 800 ms

This path is not the main low-latency/default path in the current UI; the current UI defaults new installs to Groq.

### Language Detection

Blip has two different "auto" ideas:

1. Microphone auto-detect: local device enumeration and selection.
2. Dictation language auto-detect: likely delegated to cloud STT.

I found no bundled local language identification model. When language is set to `auto`, the likely behavior is to let Whisper/Groq infer language. Azure mode is hardcoded around `en-US`, so it is not the multilingual auto-detect path.

### Latency Claim Assessment

I found optimizations, not a hard guarantee:

- local silence trimming
- 16 kHz mono WAV upload
- credential prefetch and 5-minute cache
- backend warmup
- active-app context fetched in parallel with STT
- fast hosted Groq inference

But the bundle's own warning thresholds are much higher than 700 ms:

- STT warning over roughly 3000 ms
- LLM warning over roughly 1500 ms
- total warning over roughly 4000 ms

So a sub-700 ms end-to-end guarantee is not supported by the code I inspected. A best-case short-utterance path might hit that sometimes, but not as a guaranteed full pipeline.

### Blip Differentiation

Blip's differentiation is not model ownership. It is UX and integration:

- system-wide Electron overlay
- global hotkey / push-to-talk workflow
- local audio trimming
- app-aware formatting
- custom dictionary / style layer
- usage/auth/subscription backend
- text injection into active apps

This creates an opening for a true local-first competitor.

## Moonshine Audit

### Model and Runtime Fit

Moonshine is strongly aligned with dictation:

- built for live speech, not batch transcription
- avoids Whisper's fixed 30-second window inefficiency
- supports streaming models
- uses ONNX Runtime in the current repo
- exposes C++, Python, Swift, Android, macOS, Windows, Linux, and Raspberry Pi surfaces
- includes VAD, streaming transcriber APIs, speaker ID, intent recognition, and TTS components in the newer Moonshine Voice stack

The Moonshine v2 paper reports:

- `Moonshine v2 Medium`: 245M parameters, 6.65 percent WER average on Open ASR benchmarks
- `Whisper Large v3`: 1550M parameters, 7.2 percent WER average
- `Moonshine v2 Medium`: about 129.8 ms TTFT at 1 second audio
- `Whisper Large v3`: about 2173 ms TTFT at 1 second audio

That is exactly the kind of advantage that matters for dictation.

### Why Moonshine Is Different From Whisper

Whisper is excellent, but it was not originally shaped around low-latency interactive dictation. Its fixed 30-second input window creates wasted work for short utterances.

Moonshine v1 addressed variable-length speech segments. Moonshine v2 goes further with streaming encoder design using sliding-window attention, which bounds encoder latency while retaining local context.

For live dictation, that is the core architectural advantage.

### License Risk

The current Moonshine repo license says:

- repo code is MIT except `core/third-party`
- English-language models are MIT
- other-language models are under the Moonshine Community License

The non-English model license has commercial registration, attribution, and revenue-threshold conditions. If your product is commercial and multilingual, this needs legal review before shipping.

For English-only dictation, the license posture is much cleaner.

### Technical Risks

Moonshine is not automatically better in every setting:

- English is the strongest case.
- Long-form, multilingual, translation, and noisy real-world audio may still favor Whisper, Parakeet, Canary, or cloud systems.
- A full user-facing pipeline still needs punctuation, casing, app-aware formatting, and custom word handling.
- Streaming ASR quality depends heavily on endpointing and partial/final transcript policy.
- CPU, memory, and battery must be tested per platform.
- Model modifications without a benchmark set are high risk.

## Related Research

### Moonshine: Speech Recognition for Live Transcription and Voice Commands

The original Moonshine paper introduced an encoder-decoder transformer with RoPE and variable-length training without zero-padding. The point was to avoid Whisper-style wasted compute on short live utterances.

Source: https://arxiv.org/abs/2410.15608

### Flavors of Moonshine

This paper supports the idea that small monolingual ASR models can beat much larger multilingual models in targeted language settings. That is strategically important: a dictation product does not always need one huge multilingual model.

Source: https://arxiv.org/abs/2509.02523

### Moonshine v2

Moonshine v2 is the most relevant paper for a Blip-style competitor. It introduces a streaming encoder with sliding-window attention and reports strong WER/latency tradeoffs against Whisper.

Source: https://arxiv.org/abs/2602.12241

### Open ASR Leaderboard

Useful for reproducible benchmarking, but benchmark averages should not be treated as product truth. You still need a dictation-specific benchmark with your target microphones, accents, punctuation expectations, app contexts, and latency targets.

Source: https://arxiv.org/abs/2510.06961

### On-Device Streaming ASR 2026

This paper is relevant because it compares model families and quantization strategies for CPU-only streaming ASR. It highlights Nemotron Speech Streaming and int4 quantization as serious alternatives/benchmarks.

Source: https://arxiv.org/abs/2604.14493

### Edge-ASR Quantization

Relevant for post-training quantization of ASR families including Whisper and Moonshine.

Source: https://arxiv.org/abs/2507.07877

## Adaptation Strategy

### Recommended Approach

Do not start by changing the core architecture. Start with a benchmark harness and a hybrid local-first product path.

Phase 1: Baseline

- Run Moonshine v2 Small and Medium locally.
- Compare against Groq Whisper Large v3, local Whisper/WhisperKit, and at least one Parakeet/Nemotron-style streaming model if feasible.
- Measure WER, CER where relevant, command error rate, punctuation quality, TTFT, final latency, CPU, RAM, and battery.

Phase 2: Product-Layer Adaptation

- Replace Blip-style cloud STT with local Moonshine for English.
- Keep cloud fallback for non-English or low-confidence audio.
- Tune VAD/endpointing for short dictation.
- Add confidence estimation and fallback routing.
- Add app-aware post-processing.
- Add custom vocabulary, contact names, company names, and technical terms.

Phase 3: Light Model/Decoder Adaptation

- Domain word biasing or shallow fusion.
- Spelling/alphanumeric mode.
- Punctuation/casing model or local small LLM postprocessor.
- Quantization for target hardware.
- Export to ONNX Runtime / Core ML / platform-specific backend.

Phase 4: Training-Level Adaptation

Only after the previous phases:

- fine-tune on real dictation data
- add accent/noise augmentation
- train monolingual/domain variants
- distill from stronger cloud models
- experiment with tokenizer or architecture changes

### What To Build Differently From Blip

A serious wedge against Blip would be:

- true local English dictation by default
- no API key or cloud STT requirement for core transcription
- visible privacy mode
- offline mode
- sub-300 ms partial transcript latency target
- cloud fallback as optional enhancement, not dependency
- local domain vocabulary
- app-aware formatting without sending raw audio to the cloud

Blip appears to be cloud-first with local preprocessing. A Moonshine-based product can be local-first with cloud fallback. That is a real positioning difference.

## Open Questions For A Code-Level Audit

To audit your modified Moonshine source properly, I need the local path to the code. The current workspace does not contain it.

Once available, I would inspect:

- training scripts and reproducibility
- model architecture changes
- tokenizer changes
- ONNX export path
- quantization path
- platform bindings
- memory ownership and leaks
- VAD/endpointing behavior
- audio resampling quality
- threading and latency
- benchmark scripts
- license files and third-party dependencies

## Primary Sources

- Blip AI releases: https://github.com/abnsl0014/blipai-releases
- Blip API docs: https://www.blipai.app/api-docs
- Blip privacy page: https://www.blipai.app/privacy
- Blip AppSumo offline answer: https://appsumo.com/products/blip-ai/questions/can-i-use-blip-ai-offline-1495914/
- Blip AppSumo model answer: https://appsumo.com/products/blip-ai/questions/where-is-my-information-going-to-1495797/
- Moonshine repo: https://github.com/moonshine-ai/moonshine
- Moonshine license: https://raw.githubusercontent.com/moonshine-ai/moonshine/main/LICENSE
- Moonshine v1 paper: https://arxiv.org/abs/2410.15608
- Flavors of Moonshine paper: https://arxiv.org/abs/2509.02523
- Moonshine v2 paper: https://arxiv.org/abs/2602.12241
- Open ASR Leaderboard paper: https://arxiv.org/abs/2510.06961
- On-device streaming ASR paper: https://arxiv.org/abs/2604.14493
- Edge-ASR quantization paper: https://arxiv.org/abs/2507.07877
