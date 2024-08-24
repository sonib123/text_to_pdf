# Text to PDF Converter

This script converts all text files in a specified directory to PDF format using the `FPDF` library.

## Getting Started

### Prerequisites

- Python 3.x
- FPDF library

### Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python package:
    ```sh
    pip install fpdf
    ```

3. Ensure you have the text files in the `files` directory.

### Running the Script

1. Run the script:
    ```sh
    python convert_to_pdf.py
    ```

2. The PDFs will be generated in the `PDFs` directory.

## Script Details

### Code Explanation

- **Importing Libraries:**
    ```python
    import glob
    from fpdf import FPDF
    from pathlib import Path
    ```

- **Getting File Paths:**
    ```python
    filepaths = glob.glob("files/*.txt*")
    ```

- **Converting Text Files to PDFs:**
    ```python
    for filepath in filepaths:
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        filename = Path(filepath).stem
        filename = filename.title()
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=filename, ln=1)

        with open(filepath, 'r') as file:
            content = file.read()
            pdf.set_font(family="Times", size=12)
            pdf.multi_cell(w=0, h=8, txt=content)

        pdf.output(f"PDFs/{filename}.pdf")
    ```

### Directory Structure

