import whisper
import sounddevice as sd
import numpy as np
import webrtcvad
import wave
import time
import os

from ..command import CommandAgent


def write_wave(path, audio_bytes, sample_rate):
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(sample_rate)
        wf.writeframes(audio_bytes)


def transcribe_audio(filename, model):
    result = model.transcribe(filename)
    return result["text"].strip()


def main():
    model = whisper.load_model('tiny')

    sample_rate = 16000
    frame_duration = 30
    frame_size = int(sample_rate * frame_duration / 1000)
    vad = webrtcvad.Vad(3)

    print("음성 인식을 시작합니다. '종료'라고 말하면 종료됩니다.")

    buffer = bytes()
    triggered = False
    num_silence_frames = 0
    silence_threshold = 10  # 연속 무음 프레임 기준

    def audio_callback(indata, frames, time_info, status):
        nonlocal buffer, triggered, num_silence_frames

        int_data = (indata*23767).astype(np.int16)
        audio_bytes = int_data.tobytes()

        for i in range(0, len(audio_bytes), frame_size * 2):
            frame = audio_bytes[i:i + frame_size * 2]
            if len(frame) < frame_size * 2:
                break
            is_speech = vad.is_speech(frame, sample_rate)
            if is_speech:
                if not triggered:
                    triggered = True
                    print('Voice detected')
                buffer += frame
                num_silence_frames = 0
            else:
                if triggered:
                    num_silence_frames += 1
                    if num_silence_frames > silence_threshold:
                        if buffer:
                            temp_filename = "temp_audio.wav"
                            write_wave(temp_filename, buffer, sample_rate)
                            print("processing recorded.")
                            text = transcribe_audio(temp_filename, model)

                            try:
                                result = CommandAgent().process_command(text)
                                print(f"command parsed {result}.")
                            except Exception as e:
                                print(f"Error processing command: {e}")
                                result = "Error processing command"
                                print(result)

                            print(f"Detected : {text}")
                            os.remove(temp_filename)
                        buffer = bytes()
                        triggered = False
                        num_silence_frames = 0
    with sd.InputStream(samplerate=sample_rate, channels=1, dtype='float32',
                        blocksize=frame_size, callback=audio_callback):
        print("Waiting input stream...")
        while True:
            time.sleep(0.1)


if __name__ == '__main__':
    main()
