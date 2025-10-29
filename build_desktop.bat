@echo off
REM ARQV30 Enhanced v3.0 - Script de Build Desktop
REM Cria executável Windows standalone

echo ========================================
echo ARQV30 Enhanced v3.0 - Desktop Build
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

echo [1/6] Verificando Python...
python --version
echo.

echo [2/6] Instalando/Atualizando dependencias desktop...
python -m pip install --upgrade pip
pip install -r desktop_requirements.txt
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias!
    pause
    exit /b 1
)
echo.

echo [3/6] Limpando builds anteriores...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "ARQV30_Enhanced.spec" del "ARQV30_Enhanced.spec"
echo.

echo [4/6] Instalando drivers do Playwright...
playwright install chromium
echo.

echo [5/6] Baixando modelo Spacy (pt_core_news_sm)...
python -m spacy download pt_core_news_sm
if errorlevel 1 (
    echo [AVISO] Modelo pt_core_news_sm nao instalado. Continuando...
)
echo.

echo [6/6] Construindo executavel com PyInstaller...
echo IMPORTANTE: Este processo pode levar 10-20 minutos!
echo Nao feche esta janela!
echo.
pyinstaller arqv30.spec
if errorlevel 1 (
    echo [ERRO] Falha ao construir executavel!
    pause
    exit /b 1
)
echo.

echo ========================================
echo BUILD CONCLUIDO COM SUCESSO!
echo ========================================
echo.
echo O executavel foi criado em:
echo %CD%\dist\ARQV30_Enhanced\
echo.
echo Para executar:
echo 1. Va ate a pasta dist\ARQV30_Enhanced\
echo 2. Execute ARQV30_Enhanced.exe
echo.
echo IMPORTANTE:
echo - Copie o arquivo .env para a pasta dist\ARQV30_Enhanced\
echo - Configure suas chaves de API no .env
echo.
pause
