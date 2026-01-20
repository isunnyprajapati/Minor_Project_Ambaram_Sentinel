@echo off
echo Checking Ambaram...
python --version >nul 2>&1 || echo No Python && exit /b
dir src\scanner.py >nul 2>&1 || echo No src/scanner && exit /b
dir data >nul 2>&1 || echo No data folder && exit /b
pip show h5py >nul 2>&1 || echo No h5py && exit /b
pip show streamlit >nul 2>&1 || echo No streamlit && exit /b
echo Setup OK
pause
