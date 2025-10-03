import wave
import numpy as np

# путь к эталонному сигналу
input_file = "warningSound.wav"

# читаем wav
with wave.open(input_file, "rb") as f:
    n_channels = f.getnchannels()
    sample_rate = f.getframerate()
    n_frames = f.getnframes()
    sampwidth = f.getsampwidth()
    audio_data = f.readframes(n_frames)

# преобразуем в numpy
dtype = np.int16 if sampwidth == 2 else np.uint8
samples = np.frombuffer(audio_data, dtype=dtype)

# если стерео — берём один канал
if n_channels > 1:
    samples = samples[::n_channels]

# нормализуем в float32
samples = samples.astype(np.float32) / np.iinfo(dtype).max

# целевая длительность одного сигнала = 0.5 с
n_beep = int(sample_rate * 0.2)
n_pause = int(sample_rate * 0.2)

# если эталон длиннее — обрежем до 0.5 с, если короче — дополним нулями
if len(samples) > n_beep:
    beep = samples[:n_beep]
else:
    beep = np.zeros(n_beep, dtype=np.float32)
    beep[:len(samples)] = samples

# итоговый сигнал: beep + pause + beep
# final = np.zeros(n_beep + n_pause + n_beep, dtype=np.float32)
# print(len(final))
# final[:n_beep] = beep
# final[n_beep + n_pause: n_beep + n_pause + n_beep] = beep
final = np.zeros(n_beep + n_pause + n_beep + n_pause + n_beep, dtype=np.float32)
final[0:n_beep] = beep
final[n_beep + n_pause : n_beep + n_pause + n_beep] = beep
final[2*(n_beep + n_pause) : 2*(n_beep + n_pause) + n_beep] = beep

# конвертация обратно в int16
final_int16 = np.int16(final * 32767)

# запись WAV
output_file_beep_pause_beep = "warningSound3.wav"
with wave.open(output_file_beep_pause_beep, "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    f.writeframes(final_int16.tobytes())