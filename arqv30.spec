# -*- mode: python ; coding: utf-8 -*-
"""
ARQV30 Enhanced v3.0 - PyInstaller Spec File
Arquivo de configuração completo para build do executável Windows
"""

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, collect_dynamic_libs

block_cipher = None

# Diretórios base
project_dir = os.path.abspath(SPECPATH)
src_dir = os.path.join(project_dir, 'src')
external_ai_dir = os.path.join(project_dir, 'external_ai_verifier')

# Coletar todos os dados necessários
datas = []

# Templates Flask
datas += [(os.path.join(src_dir, 'templates'), 'src/templates')]

# Static files (CSS, JS, images)
datas += [(os.path.join(src_dir, 'static'), 'src/static')]

# External AI Verifier configs
datas += [(os.path.join(external_ai_dir, 'config'), 'external_ai_verifier/config')]

# Playwright browsers (se necessário)
try:
    import playwright
    playwright_dir = os.path.dirname(playwright.__file__)
    datas += [(os.path.join(playwright_dir, 'driver'), 'playwright/driver')]
except:
    pass

# Spacy models
datas += collect_data_files('spacy')
datas += collect_data_files('en_core_web_sm', include_py_files=True)
try:
    datas += collect_data_files('pt_core_news_sm', include_py_files=True)
except:
    pass

# NLTK data
try:
    import nltk
    datas += [(nltk.data.path[0], 'nltk_data')]
except:
    pass

# CustomTkinter themes e assets
datas += collect_data_files('customtkinter')

# Selenium drivers
datas += collect_data_files('selenium')
datas += collect_data_files('webdriver_manager')

# Transformers/HuggingFace models (se usar)
try:
    datas += collect_data_files('transformers')
except:
    pass

# Arquivo .env (template)
if os.path.exists(os.path.join(project_dir, '.env.example')):
    datas += [('.env.example', '.')]

# Binaries necessários
binaries = []

# Chromium para Playwright
try:
    binaries += collect_dynamic_libs('playwright')
except:
    pass

# Bibliotecas CUDA (se necessário)
cuda_paths = [
    'C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.8\\bin',
    'C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v12.0\\bin',
]

for cuda_path in cuda_paths:
    if os.path.exists(cuda_path):
        for file in os.listdir(cuda_path):
            if file.endswith('.dll'):
                binaries.append((os.path.join(cuda_path, file), '.'))
        break

# Hidden imports - CRÍTICO para funcionamento
hiddenimports = [
    # Core Python
    'encodings',
    'encodings.utf_8',
    'encodings.cp1252',
    'encodings.latin_1',

    # CustomTkinter
    'customtkinter',
    'tkinter',
    'tkinter.ttk',
    'PIL',
    'PIL._tkinter_finder',

    # Flask e extensões
    'flask',
    'flask.app',
    'flask.templating',
    'flask_cors',
    'flask_socketio',
    'werkzeug',
    'werkzeug.security',
    'jinja2',
    'jinja2.ext',
    'markupsafe',
    'itsdangerous',
    'click',

    # IA e LLMs
    'openai',
    'google.generativeai',
    'google.ai.generativelanguage',
    'groq',
    'huggingface_hub',
    'transformers',
    'transformers.models',
    'transformers.models.auto',

    # HTTP Clients
    'requests',
    'httpx',
    'aiohttp',
    'aiofiles',
    'urllib3',
    'certifi',

    # Web Scraping
    'selenium',
    'selenium.webdriver',
    'selenium.webdriver.chrome',
    'selenium.webdriver.chrome.service',
    'selenium.webdriver.chrome.options',
    'selenium.webdriver.common',
    'selenium.webdriver.support',
    'webdriver_manager',
    'webdriver_manager.chrome',
    'beautifulsoup4',
    'bs4',
    'lxml',
    'lxml.etree',
    'lxml.html',
    'html5lib',
    'readability',
    'newspaper',
    'trafilatura',

    # Playwright
    'playwright',
    'playwright.sync_api',
    'playwright.async_api',

    # NLP
    'spacy',
    'spacy.cli',
    'en_core_web_sm',
    'pt_core_news_sm',
    'textblob',
    'nltk',
    'nltk.data',
    'vaderSentiment',
    'vaderSentiment.vaderSentiment',
    'gensim',

    # Data Science
    'pandas',
    'numpy',
    'numpy.core',
    'numpy.core._multiarray_umath',
    'scikit-learn',
    'sklearn',
    'sklearn.ensemble',
    'sklearn.tree',
    'statsmodels',
    'scipy',
    'scipy.special',
    'scipy.special.cython_special',

    # Time Series
    'prophet',
    'prophet.models',

    # Visualization
    'matplotlib',
    'matplotlib.pyplot',
    'seaborn',
    'plotly',
    'plotly.graph_objs',
    'bokeh',
    'wordcloud',

    # Network
    'networkx',

    # Image Processing
    'PIL',
    'PIL.Image',
    'PIL.ImageTk',
    'pytesseract',
    'cv2',
    'fitz',

    # PDF Processing
    'PyPDF2',
    'pypdf',
    'pdfplumber',

    # Excel/Docs
    'openpyxl',
    'docx',

    # Database
    'supabase',
    'postgrest',
    'psycopg2',

    # APIs
    'exa_py',
    'serpapi',
    'google.auth',
    'googleapiclient',
    'youtube_transcript_api',
    'instaloader',
    'instagram_private_api',
    'instascrape',

    # Report Generation
    'reportlab',
    'reportlab.lib',
    'reportlab.platypus',
    'reportlab.pdfgen',
    'markdown',

    # Scraping avançado
    'scrapy',
    'scrapy.crawler',

    # Redis
    'redis',

    # Utilities
    'tqdm',
    'colorlog',
    'chardet',
    'python-dotenv',
    'dotenv',
    'pydantic',
    'pydantic.fields',
    'yaml',
    'pyyaml',
    'configparser',

    # Async
    'asyncio',
    'async_timeout',

    # Threading
    'threading',
    'multiprocessing',
    'concurrent.futures',

    # External AI Verifier modules
    'external_review_agent',
    'bias_disinformation_detector',
    'confidence_thresholds',
    'contextual_analyzer',
    'llm_reasoning_service',
    'rule_engine',
    'sentiment_analyzer',

    # ARQV30 modules
    'src.database',
    'src.services',
    'src.routes',
    'src.engine',
    'src.utils',
    'src.ubie',
]

# Adicionar submódulos automaticamente
hiddenimports += collect_submodules('flask')
hiddenimports += collect_submodules('werkzeug')
hiddenimports += collect_submodules('jinja2')
hiddenimports += collect_submodules('customtkinter')
hiddenimports += collect_submodules('selenium')
hiddenimports += collect_submodules('playwright')
hiddenimports += collect_submodules('spacy')
hiddenimports += collect_submodules('transformers')
hiddenimports += collect_submodules('sklearn')
hiddenimports += collect_submodules('scipy')
hiddenimports += collect_submodules('pandas')
hiddenimports += collect_submodules('numpy')
hiddenimports += collect_submodules('PIL')
hiddenimports += collect_submodules('reportlab')
hiddenimports += collect_submodules('google.generativeai')
hiddenimports += collect_submodules('openai')
hiddenimports += collect_submodules('groq')

# Analysis - primeira etapa
a = Analysis(
    ['arqv30_desktop.py'],
    pathex=[project_dir, src_dir, external_ai_dir],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib.tests',
        'numpy.tests',
        'pandas.tests',
        'scipy.tests',
        'sklearn.tests',
        'pytest',
        'unittest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# PYZ - archive Python
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

# EXE - executável
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ARQV30_Enhanced',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # GUI application
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
    version_file='version_info.txt' if os.path.exists('version_info.txt') else None,
)

# COLLECT - coleta todos os arquivos
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ARQV30_Enhanced'
)
