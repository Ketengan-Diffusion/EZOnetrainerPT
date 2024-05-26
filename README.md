# EZOnetrainerPT
An Easy tool for adding additional embedding in Onetrainer diffusion trainer just point it into OT's .json preset and txt file with your concept keyword

This script is to mass adding additional embedding at once with concept.txt (or any name.txt) without hassle. We strive to make the OT's additional embedding feature easy to use

## Features
- Automaticly count the CLIP token, thanks to instant_clip_tokenizer module
- Load the onetrainer preset to adding additional embedding concepts into preset

## How to use
1. Clone this repository `https://github.com/Ketengan-Diffusion/EZOnetrainerPT.git`
2. Navigate to cloned directory `cd EZOnetrainerPT`
3. Install the required module by using `pip install -r requirements.txt`
4. Run the script `python Pivotal-Embedding`

## Usage example
Assuming we want use example.txt (You can see the example content in this repository) as the embedding concepts, so the usage will be
`python "H:\Pivotal-Embedding.py" -s "H:\EZOnetrainerPT\example.txt" -lp "J:\OneTrainer\training_presets\#sdxl 1.0.json" -d FormattedEmbedding.json` (*This command launched on windows)

The output should be on root folder of the script with name `FormattedEmbedding.json`

Next you can copy the `FormattedEmbedding.json` into Onetrainer's training_presets folder and load that preset. The loaded preset should be loaded with additional embedding configuration
