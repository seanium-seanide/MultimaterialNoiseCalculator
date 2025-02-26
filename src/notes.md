---
notes:
---

# Compiling Qt Resource Files (.qrc) and Qt UI Files (.ui)

## Required packages

```python
import subprocess
import sys
import shutil
import pathlib
import os
```

## UI Files

### Compile Function

```python
def compileUI(inFileName: str, outFileName: str) -> None:
    """
    Description: Compile a Qt UI file into a Python file
    
    Inputs
    ------

    inFileName: Name of input .ui file
    outFileName: Name of output .py file

    Outputs
    -------

    None
    """

    # Check whether pyside-uic is installed
    if not shutil.which("pyside6-uic"):
        print("Error: pyside6-uic not found!")
        sys.exit(1)

    # Check whether input file exists
    if not os.path.exists(inFileName):
        print("Error: Could not find input UI file!")
        sys.exit(1)
      
    # Run pyside6-uic
    try:
        subprocess.run(["pyside6-uic", inFileName, "-o", outFileName], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to compile UI file {inFileName}. ")
        sys.exit(1)
```

### GLOB compile

```python
uiFiles = list(pathlib.Path(".").glob("*.ui"))

if len(uiFiles) == 0:
    print("No UI files found!")
    sys.exit(1)

for uiFile in uiFiles:
    inFileName = str(uiFile)
    outFileName = str(uiFile.with_suffix(".py"))
    compileUI(inFileName, outFileName)
```

## Resource Files

### Compile Function

```python
def compileQRC(inFileName: str, outFileName: str) -> None:
    """
    Description: Compile a Qt UI file into a Python file
    
    Inputs
    ------

    inFileName: Name of input .ui file
    outFileName: Name of output .py file

    Outputs
    -------

    None
    """

    # Check whether pyside-qrc is installed
    if not shutil.which("pyside6-qrc"):
        print("Error: pyside6-rcc not found!")
        sys.exit(1)

    # Check whether input file exists
    if not os.path.exists(inFileName):
        print("Error: Could not find input QRC file!")
        sys.exit(1)
      
    # Run pyside6-uic
    try:
        subprocess.run(["pyside6-rcc", inFileName, "-o", outFileName], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to compile QRC file {inFileName}.")
        sys.exit(1)
```
    
## Finding all

```python
def 
```
