
import json
import queue
import sys
import time
import re
from pathlib import Path

import pyautogui
import sounddevice as sd
from vosk import Model, KaldiRecognizer


# =========================
# Configuration
# =========================

BASE_DIR = Path(__file__).resolve().parent
SAMPLE_RATE = 16000
BLOCK_SIZE = 4000
MAX_AUDIO_QUEUE = 12

MODELS = {
    "ar": BASE_DIR / "vosk-model-ar-mgb2-0.4",
    "en": BASE_DIR / "vosk-model-small-en-us-0.15",
}

audio_queue = queue.Queue(maxsize=MAX_AUDIO_QUEUE)
pyautogui.PAUSE = 0.05


# =========================
# Voice commands
# =========================

AR_NEXT = {
    "التالي",
    "التالية",
    "اللي بعده",
    "اللي بعد كده",
    "اللي بعد كدا",
    "اللي بعد",
    "بعده",
    "بعد كده",
    "بعد كدا",
    "روح للي بعده",
    "روح بعده",
    "الصفحة التالية",
    "الشريحة التالية",
    "الشريحة اللي بعدها",
    "السلايد اللي بعده",
    "السلايد اللي بعدها",
    "السلايد التالي",
    "كمل",
    "قدم",
    "قدام",
}

AR_PREVIOUS = {
    "السابق",
    "السابقة",
    "اللي قبله",
    "اللي قبلها",
    "اللي قبل كده",
    "اللي قبل كدا",
    "اللي قبل ككدا",
    "اللي قبل",
    "قبل كده",
    "قبل كدا",
    "ارجع",
    "رجع",
    "ارجع للي قبله",
    "روح للي قبله",
    "الشريحة السابقة",
    "الشريحة اللي قبلها",
    "السلايد السابق",
    "السلايد اللي قبله",
    "السلايد اللي قبلها",
    "ورا",
    "للوراء",
}

EN_NEXT = {
    "next",
    "next slide",
    "go next",
    "go to next slide",
    "forward",
    "move forward",
}

EN_PREVIOUS = {
    "previous",
    "previous slide",
    "go back",
    "go to previous slide",
    "back",
    "go previous",
    "go to previous",
}


def normalize_text(text):
    """Normalize common Arabic spelling variations and punctuation."""
    text = text.strip().lower()
    text = re.sub(r"[ًٌٍَُِّْـ]", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    # Common speech recognition spelling variations
    text = text.replace("ككدا", "كدا")
    text = text.replace("كده", "كدا")
    text = text.replace("اللى", "اللي")
    text = text.replace("إرجع", "ارجع")

    return text


def audio_callback(indata, frames, time_info, status):
    if status:
        print(f"\nAudio warning: {status}", file=sys.stderr)

    data = bytes(indata)

    # Drop oldest blocks if recognition falls behind.
    if audio_queue.full():
        try:
            audio_queue.get_nowait()
        except queue.Empty:
            pass

    try:
        audio_queue.put_nowait(data)
    except queue.Full:
        pass


def find_command(text, language):
    """Return 'next', 'previous', or None."""
    text = normalize_text(text)

    if language == "ar":
        next_commands = AR_NEXT
        previous_commands = AR_PREVIOUS
    else:
        next_commands = EN_NEXT
        previous_commands = EN_PREVIOUS

    # Exact matches first, then phrases found within a longer sentence.
    if text in next_commands:
        return "next"

    if text in previous_commands:
        return "previous"

    # Prefer the longer phrase to avoid matching a short command
    # inside a longer command.
    for command in sorted(next_commands, key=len, reverse=True):
        if command in text:
            return "next"

    for command in sorted(previous_commands, key=len, reverse=True):
        if command in text:
            return "previous"

    return None


def main():
    print("Choose recognition language:")
    print("  ar = Arabic")
    print("  en = English")

    language = input("Language [ar/en]: ").strip().lower()

    if language not in MODELS:
        print("Invalid choice. Enter ar or en.")
        return

    model_path = MODELS[language]

    if not model_path.is_dir():
        print(f"Model folder not found:\n{model_path}")
        return

    print("\nLoading speech model...")
    model = Model(str(model_path))
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    # Clear any stale audio before starting.
    while not audio_queue.empty():
        try:
            audio_queue.get_nowait()
        except queue.Empty:
            break

    print("\nVoice control is ready.")
    print("Arabic commands: اللي بعده / اللي قبله / التالي / السابق")
    print("English commands: Next / Previous")
    print("Open PowerPoint Slide Show before giving commands.")
    print("Press Ctrl+C to stop.\n")

    last_command = None
    last_command_time = 0.0

    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        dtype="int16",
        channels=1,
        callback=audio_callback,
    ):
        while True:
            data = audio_queue.get()

            if not recognizer.AcceptWaveform(data):
                partial_result = json.loads(recognizer.PartialResult())
                partial_text = partial_result.get("partial", "").strip()

                if partial_text:
                    print(f"\rHearing: {partial_text}          ", end="", flush=True)

                continue

            result = json.loads(recognizer.Result())
            recognized_text = result.get("text", "").strip()

            if not recognized_text:
                continue

            print(f"\nHeard: {recognized_text}")

            command = find_command(recognized_text, language)

            if command is None:
                print("No slide command detected.")
                continue

            now = time.monotonic()

            # Prevent accidental repeated actions within 0.8 seconds.
            if command == last_command and now - last_command_time < 0.8:
                print("Duplicate command ignored.")
                continue

            if command == "next":
                pyautogui.press("right")
                print("-> Next slide")

            elif command == "previous":
                pyautogui.press("left")
                print("-> Previous slide")

            last_command = command
            last_command_time = now


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nVoice control stopped.")
    except Exception as exc:
        print(f"\nError: {exc}")
        input("Press Enter to exit...")
