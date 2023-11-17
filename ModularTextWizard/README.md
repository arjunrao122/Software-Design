# ModularTextWizard

This Text Processing System is a modular Python application designed for performing various text transformations. It includes a range of functions like character blocking, case conversion, character multiplication, and a flexible block processing mechanism that applies a series of transformations to the input text.

## Features

- Character Blockers: Remove specific characters ('k', 'z', 'Z') from text.
- Case Converters: Convert text to either lowercase or uppercase.
- Multiplier: Duplicate each character in the text.
- Block Processor: Apply a series of transformation blocks to text in sequence.
- Dynamic Module Loading: Automatically load transformation functions from a specified directory.

## Blocks

The toolkit comes with the following blocks:

- `lower_case_converter`: Converts all characters in the text to lower case.
- `upper_case_converter`: Converts all characters in the text to upper case.
- `multiplier`: Duplicates each character in the text.
- `k_blocker`: Blocks all 'k' characters from the text.
- `z_blocker`: Blocks all 'z' characters from the text.
- `z_caps_blocker`: Blocks all 'Z' characters from the text.

## Installation

Clone this repository to your local machine using:

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/arjunrao122/Software-Design.git
    cd Software-Design/ModularTextWizard
    ```
2. Run the `text_processor.py` script.

## Usage

To use the text processing toolkit, follow these steps:

1. The script will display the available blocks.
3. Specify the blocks by number, in the order they should be applied.
4. Enter the text you wish to process.
5. The script will output the processed text.

## Contributing

Contributions to the HealthKitHeartRateStream SwiftUI project are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Arjun Rao - rao.arjun122@gmail.com
Project Link: [https://github.com/arjunrao122/Software-Design]
