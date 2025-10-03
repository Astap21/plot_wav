import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def FltNew():
    # Преобразование Фурье
    fft_result = np.fft.fft(signal)
    fft_freq = np.fft.fftfreq(len(t), 1 / sampling_rate)
    # Амплитуды (по модулю) и частоты
    amplitudes = np.abs(fft_result)
    # Положительные частоты и амплитуды
    positive_freqs = fft_freq[:len(fft_freq)//2]
    positive_amplitudes = amplitudes[:len(amplitudes)//2]

# Параметры сигнала
sampling_rate = 1000  # Частота дискретизации, Гц
T = 1.0  # Продолжительность сигнала, секунда
t = np.linspace(0.0, T, int(sampling_rate * T), endpoint=False)

# Сигнал состоит из низкой и высокой частоты
low_freq_signal = np.sin(2 * np.pi * 5 * t)  # Низкая частота 5 Гц
high_freq_signal = np.sin(2 * np.pi * 50 * t)  # Высокая частота 50 Гц
signal = low_freq_signal + high_freq_signal
# Преобразование Фурье
fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(t), 1 / sampling_rate)
# Амплитуды (по модулю) и частоты
amplitudes = np.abs(fft_result)
# Положительные частоты и амплитуды
positive_freqs = fft_freq[:len(fft_freq)//2]
positive_amplitudes = amplitudes[:len(amplitudes)//2]

# Параметры фильтра
cutoff_frequency = 10  # Частота среза, Гц
filter_order = 4  # Порядок фильтра
# Получаем коэффициенты фильтра
b, a = butter(filter_order, cutoff_frequency, btype='low', fs=sampling_rate)
# Применяем фильтр к сигналу
filtered_signal = filtfilt(b, a, signal)

# Построение графиков
plt.figure(figsize=(12, 6))

# Исходный сигнал
plt.subplot(2, 1, 1)
plt.plot(positive_freqs, positive_amplitudes, label='Исходный сигнал')
plt.title('Исходный сигнал')
plt.xlabel('Время [с]')
plt.ylabel('Амплитуда')
plt.grid(True)

# Преобразование Фурье
fft_result = np.fft.fft(filtered_signal)
fft_freq = np.fft.fftfreq(len(t), 1 / sampling_rate)
# Амплитуды (по модулю) и частоты
amplitudes = np.abs(fft_result)
# Положительные частоты и амплитуды
positive_freqs = fft_freq[:len(fft_freq)//2]
positive_amplitudes = amplitudes[:len(amplitudes)//2]

# Отфильтрованный сигнал
plt.subplot(2, 1, 2)
plt.plot(positive_freqs, positive_amplitudes, label='Отфильтрованный сигнал (НЧ фильтр)', color='orange')
plt.title('Отфильтрованный сигнал (Низкочастотный фильтр)')
plt.xlabel('Время [с]')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.tight_layout()
plt.show()