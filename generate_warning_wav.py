import numpy as np
import wave

# параметры
sample_rate = 44100  # Гц
duration_beep = 0.5  # сек
duration_total = 1.0 # сек
frequency = 1000     # Гц (частота сигнала)

# количество сэмплов
n_beep = int(sample_rate * duration_beep)
n_total = int(sample_rate * duration_total)

# генерируем сигнал (синус)
t = np.linspace(0, duration_beep, n_beep, False)
signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# дополняем тишиной
samples = np.zeros(n_total, dtype=np.float32)
samples[:n_beep] = signal

# конвертация в int16
samples_int16 = np.int16(samples * 32767)

# запись в WAV
with wave.open("warning.wav", "w") as f:
    f.setnchannels(1)          # моно
    f.setsampwidth(2)          # 16 бит
    f.setframerate(sample_rate)
    f.writeframes(samples_int16.tobytes())

print("WAV-файл со звуком поворотника создан: warning1.wav")
# параметры
# sample_rate = 44100
# duration_beep = 0.5
# duration_total = 1.0
# frequency = 3000   # пик обычно выше, чем 1 кГц

# # количество сэмплов
# n_beep = int(sample_rate * duration_beep)
# n_total = int(sample_rate * duration_total)

# # время
# t = np.linspace(0, duration_beep, n_beep, False)

# # сигнал (синус)
# signal = np.sin(2 * np.pi * frequency * t)

# # огибающая: экспоненциальное затухание (короткий "пик")
# envelope = np.exp(-5 * t)  
# signal = signal * envelope

# # нормализация
# signal = 0.5 * signal

# # массив с тишиной в конце
# samples = np.zeros(n_total, dtype=np.float32)
# samples[:n_beep] = signal

# # конвертация в int16
# samples_int16 = np.int16(samples * 32767)

# # запись WAV
# with wave.open("beep.wav", "w") as f:
#     f.setnchannels(1)          # моно
#     f.setsampwidth(2)          # 16 бит
#     f.setframerate(sample_rate)
#     f.writeframes(samples_int16.tobytes())

# print("Файл beep.wav создан")