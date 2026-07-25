# AWS Machine Learning Services

> **Exam note:** ML isn't a tested domain on SOA-C03 — this note is here for general AWS literacy (and because a couple of these, like DevOps Guru, actually do brush up against CloudOps monitoring work). Don't sink exam-prep time into memorizing all of these.

## Amazon SageMaker
The central platform for building, training, and deploying ML models, with managed infrastructure and tools to simplify the whole ML workflow. If one service on this list is worth actually remembering, it's this one — it's the "core" AWS ML product everything else sits around.

## Core Pre-Built AI Services
The ones from the original notes — a small model wrapped in an API call, no ML expertise required:
- **Amazon Rekognition** — image and video analysis (object/face detection, content moderation)
- **Amazon Textract** — extracts text and data from scanned documents/forms (goes further than plain OCR — understands tables and form fields)
- **Amazon Comprehend** — natural language processing (sentiment analysis, entity/key phrase extraction)
- **Amazon Lex** — the tech behind chatbot deployment (same tech that powers Alexa)

## Additional Pre-Built AI Services
- **Amazon Polly** — text-to-speech
- **Amazon Transcribe** — speech-to-text (transcribes audio)
- **Amazon Translate** — real-time language translation
- **Amazon Forecast** — time-series forecasting (demand, inventory, financial planning) using ML instead of manual spreadsheet models
- **Amazon Personalize** — builds real-time product/content recommendation systems, the same tech used behind Amazon.com's "recommended for you"
- **Amazon Kendra** — enterprise search powered by natural language, so employees can search internal docs conversationally instead of with keyword matching
- **Amazon Fraud Detector** — detects potentially fraudulent online activity (fake accounts, payment fraud)
- **Amazon Comprehend Medical** — like Comprehend, but tuned to extract info from unstructured medical text (clinical notes, prescriptions)

## Developer & Ops-Focused ML
Worth knowing even outside of pure ML study, since these overlap with day-to-day CloudOps work:
- **Amazon CodeGuru** — automated code reviews and application performance profiling
- **Amazon DevOps Guru** — uses ML to automatically detect operational anomalies (unusual latency spikes, error rate increases) across your AWS resources and suggests remediation — directly relevant to [monitoring-services.md](monitoring-services.md) even though it's filed as an "ML" service

## Generative AI
- **Amazon Bedrock** — access foundation models (Claude, Titan, and others) via API to build generative AI apps, without managing the underlying infrastructure
- **Amazon Q** — AWS's generative AI assistant, available in different flavors (Q Developer for coding help, Q Business for internal company knowledge)

## Niche / Specialized
- **AWS Panorama** — brings computer vision to on-prem cameras/edge devices
- **AWS DeepRacer** — a physical/virtual autonomous race car used to learn reinforcement learning in a hands-on way (more of an education tool than a production service)

## Related Notes
- [monitoring-services.md](monitoring-services.md) — DevOps Guru's anomaly detection complements CloudWatch's metric/alarm monitoring
- Peripheral to [cloudops-progress.md](cloudops-progress.md) — not a tested domain, kept for general AWS service literacy
