@echo off
echo ========================================
echo   智能文章生成助手
echo ========================================
echo.

cd /d "%~dp0"

echo 正在检查并安装依赖...
pip install flask requests beautifulsoup4 lxml -i https://pypi.org/simple/

echo.
echo ========================================
echo   启动中...
echo   请在浏览器中打开: http://127.0.0.1:5000
echo ========================================
echo.

python app.py

pause
