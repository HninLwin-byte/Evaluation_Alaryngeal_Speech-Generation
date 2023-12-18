import os

# Specify the path to the folder containing audio files
folder_path = '/Users/krislwin/Documents/Speech_Website/assets'

# List all files in the folder
audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav', '.ogg', '.flac', '.aac'))]

# Rename the audio files
for i, old_name in enumerate(audio_files, start=1):
    # Specify the new name format, for example, "new_name_1.wav", "new_name_2.wav", etc.
    new_name = f"female_converted_{i}.wav"
    
    # Create the full paths for old and new names
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)

print("Audio files have been successfully renamed.")
