import wave
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    #fileName = "errorSound.wav"
    fileName = "turnSignalSound.wav"
    
    wav_file = wave.open(fileName)
    print ("framerate:", wav_file.getframerate())
    print ("nsamples:", wav_file.getnframes())
    print ("sample size:", wav_file.getsampwidth())
    print ("channels:", wav_file.getnchannels())
    data = wav_file.readframes(wav_file.getnframes())
    #data = wav_file.readframes(1024)
    print ("number of samples read:", len(data) / (wav_file.getsampwidth() * wav_file.getnchannels()))
    
    

    signal = np.frombuffer(data , dtype=np.int16)
    signal_32 = signal.astype(np.int32)
    signal_32 = signal_32 - signal_32.min()
    devider = signal_32.max() / 250
    signal_32 = signal_32 / devider
    print("Devider = ", devider)
    # Вычисляем преобразование Фурье
    fft_result = np.fft.fft(signal)
    # Вычисляем частоты, соответствующие бинам преобразования Фурье
    frequencies = np.fft.fftfreq(len(fft_result), 1 / wav_file.getframerate())
    # Находим индекс максимального значения амплитуды
    max_index = np.argmax(np.abs(fft_result))
    # Получаем частоту синусоиды
    detected_frequency = frequencies[max_index]

    print("Sin frequency:", detected_frequency, "Hz")

    plt.plot(np.round(signal_32))
    #plt.plot(signal)
    plt.title(fileName)
    plt.show()