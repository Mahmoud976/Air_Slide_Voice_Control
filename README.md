# Air Slide Voice Control

Control PowerPoint slide navigation using offline Arabic or English voice commands.

## Features

- Offline speech recognition with [Vosk](https://alphacephei.com/vosk/)
- Arabic and English language-model options
- Navigate to the next or previous PowerPoint slide using voice
- Microphone input through `sounddevice`
- Keyboard automation through `pyautogui`

## Requirements

- Windows
- Python 3.10 or a compatible Python version supported by the installed dependencies
- A working microphone
- Microsoft PowerPoint open in slide-show mode
- The Arabic and/or English Vosk model downloaded separately

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Mahmoud976/Air_Slide_Voice_Control.git
   cd Air_Slide_Voice_Control
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```
   On Windows PowerShell, activate it with:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the Vosk language models you need and extract them into the project folder. The application has been tested with:
   - `vosk-model-ar-mgb2-0.4`
   - `vosk-model-small-en-us-0.15`

   Model downloads are available from the [Vosk models page](https://alphacephei.com/vosk/models). Model folders are intentionally excluded from Git because they are large.

## Run

Start PowerPoint and enter Slide Show mode, then run:

```bash
python voice_control.py
```

Choose the language when prompted and speak the supported slide-navigation commands. Recognition accuracy depends on microphone quality, background noise, pronunciation, and the selected model.

## Notes

- Keep the Vosk model folders at the paths expected by `voice_control.py`.
- Check the command names in `voice_control.py` if you want to customize the phrases.
- This project performs local/offline speech recognition; it does not require a cloud speech API.

## License

No license has been specified yet. Add a license file if you intend to permit reuse or redistribution.
