import numpy as np
import wave
import struct

# Параметры звука
sample_rate = 44100  # Частота дискретизации (Гц)
duration_click = 0.02  # Длительность щелчка (20 мс)
duration_silence = 0.48  # Пауза между щелчками (480 мс)
frequency = 3000  # Уменьшенная частота для более глухого звука (Гц)
num_repeats = 10  # Количество повторов (примерно 5 секунд звука)

def generate_click():
    num_samples = int(sample_rate * duration_click)
    samples = np.zeros(num_samples)
    for i in range(num_samples):
        samples[i] = np.exp(-i / (sample_rate * 0.005)) * np.sin(2 * np.pi * frequency * i / sample_rate)
    
    # Применяем сглаживающий фильтр (усреднение)
    kernel_size = 10  # Размер окна сглаживания
    samples = np.convolve(samples, np.ones(kernel_size)/kernel_size, mode='same')
    
    return samples

def generate_turn_signal():
    click = generate_click()
    silence = np.zeros(int(sample_rate * duration_silence))
    signal = np.concatenate([(np.concatenate([click, silence])) for _ in range(num_repeats)])
    return signal

def save_wave(filename, samples, sample_rate):
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)  # Моно
        wf.setsampwidth(2)  # 16 бит
        wf.setframerate(sample_rate)
        samples = (samples * 32767).astype(np.int16)
        wf.writeframes(samples.tobytes())

# Генерация и сохранение
samples = generate_turn_signal()
save_wave('turn_signal.wav', samples, sample_rate)

print("Файл turn_signal.wav создан.")

