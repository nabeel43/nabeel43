import librosa
import os
import numpy as np


def load_audio_files(directory, num_files=100, sample_rate=44100):
    """
    Loads a given number of audio files from a directory into a list of numpy arrays.

    Args:
        directory (str): Path to the directory containing the audio files.
        num_files (int): Number of audio files to load (default is 100).
        sample_rate (int): Sample rate to load the audio files (default is 44.1kHz).

    Returns:
        audio_files (list): A list of numpy arrays containing audio data.
    """
    # List to store audio data
    audio_files = []

    # Get all files with .wav extension in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.wav')]

    # Limit the number of files to the desired amount (num_files)
    files = files[:num_files]

    for file in files:
        # Get the full file path
        file_path = os.path.join(directory, file)

        # Load the audio file (returns a numpy array)
        audio, sr = librosa.load(file_path, sr=sample_rate, mono=True)

        # Append to the list
        audio_files.append(audio)

    return audio_files


# Example Usage
directory_path = './audio_files/'  # Path to your folder of audio files
audio_data = load_audio_files(directory_path, num_files=100)

# Check the loaded data
print(f"Loaded {len(audio_data)} audio files.")
print(f"Shape of the first audio file: {audio_data[0].shape}")
