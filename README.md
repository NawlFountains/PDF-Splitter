# PDF Splitter
## Setup
1. python -m venv venv
2. Activate: "venv\Scripts\activate" (Windows) or "source venv/bin/activate" (Linux)
3. pip install -r requirements.txt

## Usage
After setup you can use the script as follows (If in doubt add -h flag for usage help): 

```python pdf\_splitter.py <source_pdf> <start_page> <end_page>```

with source_pdf being the path of the PDF document to split,
start_page the number of the initial page to take into account for the range to split and
end_page the end of said range.
