### --------------------------------------------------------------------
### 1.0 Verify the terminal is at repo root

In the VS Code Terminal, run:

```powershell
Get-Location
```

Expected:
- the terminal path ends in: ...\LightUpTailgate

The virtual environment path is relative to the current working directory.

### --------------------------------------------------------------------
### 1.1 Create the Virtual Environment: LightUpTailgate

In the VS Code terminal, from the repo root, run:

```powershell
python -m venv LightUpTailgate
```

(if applicable) Click **Yes** when asked, "We noticed a new environment has been created.  Do you want to select if for the workspace folder?".  

Verify that the environment folder exists:

```powershell
Test-Path LightUpTailgate
```

Expected:
- True

### --------------------------------------------------------------------
### 1.2 Activate the Virtual Environment

In the VS Code Terminal, run:

```powershell
LightUpTailgate\Scripts\Activate
```

If PowerShell blocks activation with an execution-policy error, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
LightUpTailgate\Scripts\Activate
```

Expected:
- the terminal prompt begins with (LightUpTailgate)

Example:

```plain text
(LightUpTailgate) PS C:\Users\<your-user>\Documents\LightUpTailgate>
```

### --------------------------------------------------------------------
# 1.3 Confirm the interpreter is the repo-local Virtual Envoronment

Run:

```powershell
where.exe python
python -c "import sys; print(sys.executable)"
```

Expected:
- both point to: ...\LightUpTailgate\LightUpTailgate\Scripts\python.exe

If not, stop and fix the interpreter before continuing.

### --------------------------------------------------------------------
### 1.4 Install Python dependencies

From the active LightUpTailgate Virtual Environment, run:

```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify basic imports:

```powershell
python -c "import manim; print('Manim OK')"
```

Expected:
```plain text
Manim OK
```

### 1.5 Select the correct Python interpreter in VS Code

In VS Code:
1. Press Ctrl+Shift+P
2. Search:
   >Python: Select Interpreter
3. Press **ENTER**
4. Select interpreter:
   Python 3.11.9 (LightUpTailgate) .\LightUpTailgate\Scripts\python.exe

If the desired interpreter path stated in step 4 doesn't appear, follow steps 1 though 4 again.
This must point to the repo-local .venv, not a global Python installation.

Verify interpreter is selected:
1. Press Ctrl+Shift+P
2. Search: 
   >Python: Select Interpreter
3. Press **ENTER**

Expected:
In the dropdown, you should see:
Selected Interpreter: .\LightUpTailgate\Scripts\python.exe