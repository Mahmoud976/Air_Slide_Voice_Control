# AirSlide Voice Control 🎙️

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=230&color=0:111827,45:164E63,100:06B6D4&text=AirSlide&fontColor=FFFFFF&fontSize=76&fontAlignY=38&desc=Offline%20Voice-Powered%20Presentation%20Control&descAlignY=60&descSize=18&animation=scaleIn" width="100%" alt="AirSlide Voice Control banner" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=22D3EE&center=true&vCenter=true&width=900&lines=Your+voice.+Your+slides.+Your+flow.;Arabic+%2B+English+%7C+Offline+speech+recognition;Built+with+Python%2C+Vosk%2C+and+PyAutoGUI" alt="Your voice. Your slides. Your flow." />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/Speech-Vosk-0F766E?style=for-the-badge" alt="Vosk offline speech recognition" />
  <img src="https://img.shields.io/badge/Languages-Arabic%20%7C%20English-0891B2?style=for-the-badge" alt="Arabic and English" />
  <img src="https://img.shields.io/badge/Mode-Offline-16A34A?style=for-the-badge&logo=shield&logoColor=white" alt="Offline" />
  <img src="https://img.shields.io/badge/Platform-Windows-2563EB?style=for-the-badge&logo=windows&logoColor=white" alt="Windows" />
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-7C3AED?style=for-the-badge" alt="MIT License" /></a>
</p>

<p align="center">
  <a href="#-overview">Overview</a> · <a href="#-features">Features</a> · <a href="#-supported-commands">Commands</a> · <a href="#-quick-start">Quick Start</a> · <a href="#-windows-executable">Windows EXE</a> · <a href="#-how-it-works">How It Works</a>
</p>

---

## ✨ Overview

**AirSlide Voice Control** lets you navigate a PowerPoint slideshow using spoken commands in **Arabic or English**. It uses Vosk for local speech recognition and PyAutoGUI to send the keyboard input for the next or previous slide.

No cloud speech API is needed: audio recognition runs locally on your computer after the language model has been downloaded.

> **Current scope:** AirSlide Voice Control supports next/previous slide navigation by keyboard input. It does not control PowerPoint through its internal API, so keep the slide show focused while speaking commands.

## 🚀 Features

- **Arabic and English modes** — choose your preferred recognition language at startup.
- **Offline speech recognition** — powered by Vosk and a locally stored model.
- **PowerPoint navigation** — voice commands send Right Arrow or Left Arrow.
- **Arabic phrase normalization** — handles common spelling and pronunciation variations.
- **Low-latency audio queue** — keeps recent microphone audio when recognition falls behind.
- **Duplicate-command guard** — reduces accidental repeated actions within a short interval.
- **Windows-friendly setup** — run from Python or package the script into an executable.
- **Privacy-minded by design** — no cloud speech service is called by the app.

## 🎤 Supported commands

### Arabic

| Action | Examples |
|---|---|
| Next slide | `التالي` · `التالية` · `اللي بعده` · `اللي بعدها` · `بعده` · `كمل` |
| Previous slide | `السابق` · `السابقة` · `اللي قبله` · `اللي قبل كده` · `ارجع` · `ورا` |

### English

| Action | Examples |
|---|---|
| Next slide | `Next` · `Next slide` · `Go next` · `Forward` |
| Previous slide | `Previous` · `Previous slide` · `Go back` · `Back` |

Commands are matched against recognized speech, so accuracy depends on the model, microphone, background noise, and pronunciation. You can customize the phrases in `voice_control.py`.

## 🧠 How it works

1. **Capture audio** — `sounddevice` streams microphone audio at 16 kHz.
2. **Recognize speech** — Vosk converts audio into text using the selected local model.
3. **Normalize and match** — the app cleans the recognized phrase and checks it against supported commands.
4. **Prevent rapid repeats** — a short duplicate-command guard filters accidental repeated actions.
5. **Navigate** — PyAutoGUI presses the Right Arrow or Left Arrow key.

## 🧰 Tech stack

| Technology | Role |
|---|---|
| [Python](https://www.python.org/) | Application logic |
| [Vosk](https://alphacephei.com/vosk/) | Offline speech recognition |
| [sounddevice](https://python-sounddevice.readthedocs.io/) | Microphone audio capture |
| [PyAutoGUI](https://pyautogui.readthedocs.io/) | Sends slide-navigation key presses |
| [NumPy](https://numpy.org/) | Dependency used by the Python audio stack |

## ⚡ Quick start

### Requirements

- Windows 10/11
- Python 3.10+ (64-bit recommended)
- A working microphone
- Microsoft PowerPoint or another presentation app that supports arrow-key navigation
- The Vosk model for the language you want to use

### 1. Clone the project

```cmd
git clone https://github.com/Mahmoud976/Air_Slide_Voice_Control.git
cd Air_Slide_Voice_Control
```

### 2. Create a virtual environment

Run these commands in **Windows Command Prompt**:

```cmd
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Download a speech model

Download the model you need from the official [Vosk Models page](https://alphacephei.com/vosk/models), extract it, then place the model folder directly inside the project directory using one of these exact folder names:

| Language | Expected folder |
|---|---|
| Arabic | `vosk-model-ar-mgb2-0.4` |
| English | `vosk-model-small-en-us-0.15` |

The model folders are intentionally excluded from Git because they are large. The program checks the expected folder name at startup.

### 4. Start presenting

Open PowerPoint, start **Slide Show**, then run:

```cmd
python voice_control.py
```

Choose `ar` for Arabic or `en` for English, then speak one of the supported commands. Press **Ctrl+C** in the terminal to stop.

## 📦 Download and run on Windows (no Python required)

**Want to use AirSlide instead of developing it? Download the ready-to-run EXE from the latest release.** You do not need to install Python or clone the repository.

### 1. Download the app

1. Open the [Latest Release](https://github.com/Mahmoud976/Air_Slide_Voice_Control/releases/latest).
2. Under **Assets**, download `AirSlideVoiceControl.exe`.
3. Create a folder such as `AirSlide` and move the EXE into it.

### 2. Download the language model(s)

The EXE does **not** include the large Vosk language models. Download only the language(s) you want to use from the official [Vosk Models page](https://alphacephei.com/vosk/models), then extract each ZIP file. Put the extracted model folder(s) in the **same folder as the EXE**. Keep the folder names exactly as shown:

| Language | Model folder name |
|---|---|
| Arabic | `vosk-model-ar-mgb2-0.4` |
| English | `vosk-model-small-en-us-0.15` |

Your folder should look like this (include only the model(s) you downloaded):

```text
AirSlide/
├── AirSlideVoiceControl.exe
├── vosk-model-ar-mgb2-0.4/
│   ├── am/
│   ├── conf/
│   └── ...
└── vosk-model-small-en-us-0.15/
    ├── am/
    ├── conf/
    └── ...
```

**Important:** Extract the ZIP first. Do not leave the model inside the ZIP or accidentally create an extra nested folder. The model folder itself should contain folders/files such as `am` and `conf`.

### 3. Start using AirSlide

1. Connect your microphone and allow microphone access in Windows if prompted.
2. Open PowerPoint and start **Slide Show**.
3. Double-click `AirSlideVoiceControl.exe`.
4. Choose Arabic (`ar`) or English (`en`) when prompted, then speak a supported command.
5. Keep the PowerPoint slide show as the active window so the arrow-key command goes to your presentation.

Say a next-slide phrase such as **“اللي بعدها”** or **“Next slide”**, or a previous-slide phrase such as **“اللي قبل كده”** or **“Previous slide”**. See [Supported commands](#-supported-commands) for more examples.

To stop the program, use **Ctrl+C** if a console window is shown; otherwise close the app window or end `AirSlideVoiceControl.exe` from Task Manager.

### Troubleshooting the downloaded EXE

- **Model not found:** check that the extracted model folder is beside the EXE and its name matches the table exactly.
- **Windows blocks the EXE:** Windows may show a SmartScreen warning for an unsigned app. Only continue if you trust this project and downloaded it from the official release page.
- **No voice detected:** check Windows **Settings → System → Sound → Input** and microphone permissions.
- **Slides do not move:** make sure PowerPoint is in Slide Show mode and is the active window.

## 🧑‍💻 Run from source or build the EXE

This section is for developers. If you only want to use AirSlide, follow the download steps above instead.

### Run from source

1. Install Python 3.10+ (64-bit recommended) and clone the repository.
2. Open Command Prompt in the project folder and run:

```cmd
py -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
python voice_control.py
```

3. Download the required Vosk model(s) from the [official model page](https://alphacephei.com/vosk/models) and place them in the project folder using the exact names in the table above.

### Build locally

1. Open Command Prompt in the project folder.
2. Run `build_exe.bat`.
3. Find the executable at `dist\\AirSlideVoiceControl.exe`.
4. Copy the Vosk model folder(s) you want to use into the same `dist` folder as the EXE.

GitHub Actions also builds the EXE. You can inspect the [Build Windows EXE workflow](https://github.com/Mahmoud976/Air_Slide_Voice_Control/actions/workflows/build-windows-exe.yml); the latest downloadable release is linked above.

## 🛠️ Troubleshooting

- **Model folder not found:** confirm the model is extracted and its folder name matches the table above exactly.
- **No microphone audio / PortAudio error:** check Windows microphone permissions and select a working default input device.
- **Commands are not recognized:** reduce background noise, speak clearly, check the selected language, and try the example phrases above.
- **Slides do not move:** start Slide Show and make sure PowerPoint is the active/focused window.
- **Python cannot find a package:** activate `.venv` and run `python -m pip install -r requirements.txt` from the repository directory.

## 🔐 Privacy and safety

- Speech recognition is performed locally using the downloaded Vosk model.
- The app sends keyboard presses to the active window; focus the presentation before using it.
- Test commands on a sample deck before a live presentation.
- Stop the app with **Ctrl+C** if it behaves unexpectedly.

## 🗺️ Roadmap

- [x] Offline Arabic and English recognition
- [x] Voice-controlled next/previous slide navigation
- [x] Duplicate-command guard
- [x] Windows executable build workflow
- [ ] Add a short demo video/GIF
- [ ] Add configurable microphone selection and sensitivity options
- [ ] Expand supported presentation commands

## 🤝 Contributing

Ideas, bug reports, and pull requests are welcome. For useful bug reports, include your Windows version, Python version, selected model, microphone setup, and the exact command you spoke.

## 👨‍💻 Author

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=150&color=0:111827,45:164E63,100:06B6D4&text=BUILT%20BY&fontColor=FFFFFF&fontSize=38&fontAlignY=42&animation=fadeIn" width="100%" alt="Built by banner" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=22D3EE&center=true&vCenter=true&width=850&lines=Mahmoud+Mohammed+El+Sayed+Saleh" alt="Mahmoud Mohammed El Sayed Saleh" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/mahmoud-m-saleh/"><img src="https://img.shields.io/badge/LinkedIn-Connect%20with%20Mahmoud-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/Mahmoud976"><img src="https://img.shields.io/badge/GitHub-Mahmoud976-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub profile" /></a>
</p>

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:111827,45:164E63,100:06B6D4&section=footer&animation=twinkling&reversal=true" width="100%" alt="AirSlide footer" />
</p>
