import uuid
import re
import json
import argparse
from instant_clip_tokenizer import Tokenizer

def clean_text(text):
    # Remove specified symbols except parentheses / Menghapus simbol tertentu kecuali tanda kurung
    return re.sub(r'[",.;*]', '', text)

def process_text(input_file_path):
    tokenizer = Tokenizer()
    entries = []

    # Reading the input file / Membaca file input
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        name = clean_text(line.strip())
        if not name:
            continue

        tokens = tokenizer.encode(name)
        token_count = len(tokens)
        first_word = clean_text(name.split()[0])
        unique_id = uuid.uuid4()

        entry = {
            "__version": 0,
            "uuid": str(unique_id),
            "model_name": "",
            "placeholder": name,
            "train": True,
            "stop_training_after": None,
            "stop_training_after_unit": "NEVER",
            "token_count": token_count,
            "initial_embedding_text": first_word
        }
        entries.append(entry)

    return entries

def main():
    parser = argparse.ArgumentParser(description='Process text from an input file and generate a formatted output.')
    parser.add_argument('-s', '--source', required=True, help='Input .txt file with names')
    parser.add_argument('-d', '--destination', required=True, help='Output .json file to write formatted content')
    parser.add_argument('-lp', '--loadpreset', required=False, help='Input .json preset file to load')

    args = parser.parse_args()

    # Process the text from input file / Memproses teks dari file input
    additional_embeddings = process_text(args.source)

    if args.loadpreset:
        # Load the JSON preset file / Memuat file preset JSON
        with open(args.loadpreset, 'r') as preset_file:
            preset_data = json.load(preset_file)

        # Replace "additional_embeddings": [] line from preset / Merubah baris "additional_embeddings": [] dari preset
        preset_data["additional_embeddings"] = additional_embeddings

        # Write the updated JSON content to the destination file / Menulis konten JSON yang telah diperbarui ke file tujuan
        with open(args.destination, 'w') as output_file:
            json.dump(preset_data, output_file, indent=4)

        print(f"The formatted output has been written to '{args.destination}' using preset '{args.loadpreset}'")

    else:
        # Create a new JSON structure if no preset is provided / Membuat struktur JSON baru jika preset tidak disediakan
        output_data = {
            "additional_embeddings": additional_embeddings
        }

        # Write the new JSON content to the destination file / Menulis konten JSON baru ke file tujuan
        with open(args.destination, 'w') as output_file:
            json.dump(output_data, output_file, indent=4)

        print(f"The formatted output has been written to '{args.destination}'")

if __name__ == "__main__":
    main()