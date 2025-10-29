@echo off
REM ARQV30 Enhanced v3.0 - Launcher Desktop
REM Executa aplicação desktop

echo ========================================
echo ARQV30 Enhanced v3.0 - Desktop Mode
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo Por favor, instale Python 3.11+ primeiro.
    pause
    exit /b 1
)

REM Verifica se arquivo principal existe
if not exist "arqv30_desktop.py" (
    echo [ERRO] Arquivo arqv30_desktop.py nao encontrado!
    echo Certifique-se de estar na pasta correta.
    pause
    exit /b 1
)

REM Verifica se .env existe
if not exist ".env" (
    echo [AVISO] Arquivo .env nao encontrado!
    echo Por favor, configure suas chaves de API no arquivo .env
    echo.
    pause
)

echo [INFO] Iniciando ARQV30 Enhanced v3.0...
echo.
echo DICA: Para fechar, clique no X da janela ou use Ctrl+C aqui.
echo.

REM Executa aplicação desktop
python arqv30_desktop.py

echo.
echo Aplicacao encerrada.
pause
