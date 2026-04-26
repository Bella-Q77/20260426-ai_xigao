@echo off
chcp 65001 >nul
cls
echo ========================================
echo   Zhi Neng Wen Zhang Sheng Cheng Zhu Shou
echo   (Smart Article Generator)
echo ========================================
echo.

cd /d "%~dp0"

echo Checking and installing dependencies...
pip install flask requests beautifulsoup4 lxml -i https://pypi.org/simple/

echo.
echo ========================================
echo   Starting...
echo   Please open in browser: http://127.0.0.1:5000
echo ========================================
echo.

python app.py

pause
