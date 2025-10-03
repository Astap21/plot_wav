import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

# путь к загруженному файлу
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

duration = n_frames / sample_rate

# спектр
fft_spectrum = np.fft.rfft(samples)
freqs = np.fft.rfftfreq(len(samples), 1/sample_rate)
magnitude = np.abs(fft_spectrum)

# графики
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(np.linspace(0, duration, len(samples)), samples)
plt.title("Временная форма сигнала")
plt.xlabel("Время, с")
plt.ylabel("Амплитуда")

plt.subplot(1,2,2)
plt.semilogy(freqs, magnitude)
plt.title("Спектр сигнала")
plt.xlabel("Частота, Гц")
plt.ylabel("Амплитуда (лог)")
plt.tight_layout()
plt.show()