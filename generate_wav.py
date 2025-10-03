import numpy as np
import wave

# Параметры звука
sample_rate = 44100  # Частота дискретизации (Гц)
duration = 5.0       # Длительность звука (секунды)
frequency = 10000     # Частота звука "тика" (Гц)
tick_duration = 0.1  # Длительность одного "тика" (секунды)
tick_interval = 0.5  # Интервал между "тиками" (секунды)

# Генерация звука
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio = np.zeros_like(t)

for i in range(int(duration / tick_interval)):
    start = int(i * tick_interval * sample_rate)
    end = int(start + tick_duration * sample_rate)
    audio[start:end] = 0.5 * np.sin(2 * np.pi * frequency * t[start:end])

# Нормализация аудио
audio = np.int16(audio / np.max(np.abs(audio)) * 32767)

# Сохранение в WAV-файл
with wave.open('turn_signal.wav', 'w') as wav_file:
    wav_file.setnchannels(1)  # Моно
    wav_file.setsampwidth(2)  # 16 бит
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio.tobytes())

print("WAV-файл со звуком поворотника создан: turn_signal.wav")