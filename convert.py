from pydub import AudioSegment
import os

def convert_m4a_to_wav(input_file, output_file):
    try:
        # Load the M4A file
        audio = AudioSegment.from_file(input_file, format="m4a")
        
        # Export as WAV
        audio.export(output_file, format="wav")
        print(f"Conversion successful! WAV file saved at: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input and output file paths
    input_path = "./notion.m4a"
    output_path = "./isdone.wav"

    if not os.path.exists(input_path):
        print("Error: The specified M4A file does not exist.")
    else:
        convert_m4a_to_wav(input_path, output_path)
