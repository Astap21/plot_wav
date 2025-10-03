import numpy as np
import wave

# параметры из анализа
sample_rate = 22050
duration_beep = 0.5
duration_pause = 0.5
frequency = 2000  # примерно основной тон из анализа

# количество сэмплов
n_beep = int(sample_rate * duration_beep)
n_pause = int(sample_rate * duration_pause)
n_total = n_beep + n_pause + n_beep

# сигнал (прямоугольная волна)
t = np.linspace(0, duration_beep, n_beep, False)
signal = np.sign(np.sin(2 * np.pi * frequency * t))

# уменьшаем громкость до 0.5, чтобы не клиппировало
signal = 0.2 * signal

# итоговый массив: пик + пауза + пик
samples = np.zeros(n_total, dtype=np.float32)
samples[:n_beep] = signal
samples[n_beep + n_pause: n_beep + n_pause + n_beep] = signal

# конвертация в int16
samples_int16 = np.int16(samples * 32767)

# запись WAV
output_file_match = "double_beep_match.wav"
with wave.open(output_file_match, "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    f.writeframes(samples_int16.tobytes())

# output_file_match
# Результат
# '/mnt/data/double_beep_match.wav'