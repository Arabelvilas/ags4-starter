# ags4-starter

Minimal reproducible AGS4 data validation and exploration toolkit for geotechnical engineers.

This repository demonstrates how to read, validate, convert and export AGS4 files using Python and the `python-ags4` library.  
It replaces manual spreadsheet workflows with transparent, reproducible scripts.

---

## Why This Exists

AGS4 is the industry-standard data exchange format for geotechnical investigations in the UK and internationally.

In practice, AGS files are often:
- Manually converted to Excel
- Copied between spreadsheets
- Modified without traceability
- Poorly validated before analysis

This toolkit demonstrates a structured Python workflow to:

- Load AGS groups as pandas DataFrames  
- Convert string fields to numeric types  
- Validate AGS structure  
- Export clean outputs to Excel or back to AGS  
- Form the basis for reproducible geotechnical data analysis  

This is the foundation layer for automated geotechnical workflows.

Use this only for reference

Check more about AGS4 in my blog: https://www.geotechpython.com/?p=197

---

## Dependencies

Install required packages:

    pip install python-AGS4 pandas openpyxl matplotlib pathlib

Import in Python:

```python
from python_ags4 import AGS4
from pathlib import Path
import pandas as pd
