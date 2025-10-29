#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v3.0 - Desktop Application
Interface nativa CustomTkinter moderna e profissional
"""

import os
import sys
import json
import threading
import webbrowser
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.run import create_app

class ARQV30DesktopApp(ctk.CTk):
    """
    ARQV30 Desktop Application com interface CustomTkinter
    Design moderno, arrojado, sobrio e profissional
    """

    def __init__(self):
        super().__init__()

        self.title("ARQV30 Enhanced v3.0 - Market Analysis System")
        self.geometry("1400x900")
        self.minsize(1200, 700)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.server_thread = None
        self.server_running = False
        self.app = None
        self.host = "127.0.0.1"
        self.port = 12000

        self.setup_ui()
        self.setup_styles()

    def setup_styles(self):
        """Configura estilos personalizados"""
        self.colors = {
            'bg_primary': '#1a1a1a',
            'bg_secondary': '#242424',
            'bg_tertiary': '#2d2d2d',
            'accent_blue': '#0d7377',
            'accent_green': '#14a76c',
            'accent_red': '#ff6b6b',
            'text_primary': '#ffffff',
            'text_secondary': '#b0b0b0',
            'border': '#404040'
        }

    def setup_ui(self):
        """Configura interface principal"""

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_content()
        self.create_status_bar()

    def create_sidebar(self):
        """Cria barra lateral de navegação"""

        sidebar = ctk.CTkFrame(self, width=280, corner_radius=0)
        sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        sidebar.grid_rowconfigure(10, weight=1)

        logo_label = ctk.CTkLabel(
            sidebar,
            text="ARQV30 Enhanced",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        logo_label.grid(row=0, column=0, padx=20, pady=(30, 10))

        version_label = ctk.CTkLabel(
            sidebar,
            text="v3.0 Professional",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        version_label.grid(row=1, column=0, padx=20, pady=(0, 30))

        nav_buttons = [
            ("🏠 Dashboard", self.show_dashboard),
            ("🚀 Iniciar Servidor", self.toggle_server),
            ("📊 Nova Análise", self.new_analysis),
            ("📁 Análises Salvas", self.show_analyses),
            ("⚙️ Configurações", self.show_settings),
            ("📖 Documentação", self.show_documentation),
            ("ℹ️ Sobre", self.show_about),
        ]

        for idx, (text, command) in enumerate(nav_buttons, start=2):
            btn = ctk.CTkButton(
                sidebar,
                text=text,
                command=command,
                height=45,
                font=ctk.CTkFont(size=14),
                anchor="w"
            )
            btn.grid(row=idx, column=0, padx=20, pady=8, sticky="ew")

            if "Iniciar" in text:
                self.server_button = btn

        footer_label = ctk.CTkLabel(
            sidebar,
            text="© 2024 ARQV30 Enhanced\nAll Rights Reserved",
            font=ctk.CTkFont(size=10),
            text_color="gray"
        )
        footer_label.grid(row=15, column=0, padx=20, pady=20)

    def create_main_content(self):
        """Cria área de conteúdo principal"""

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self.main_frame, height=80, corner_radius=0)
        header.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        header.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            header,
            text="Dashboard",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=30, pady=20, sticky="w")

        self.content_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.show_dashboard()

    def create_status_bar(self):
        """Cria barra de status"""

        self.status_bar = ctk.CTkFrame(self, height=40, corner_radius=0)
        self.status_bar.grid(row=1, column=1, sticky="ew", padx=0, pady=0)
        self.status_bar.grid_columnconfigure(1, weight=1)

        self.status_indicator = ctk.CTkLabel(
            self.status_bar,
            text="●",
            font=ctk.CTkFont(size=20),
            text_color="#ff6b6b"
        )
        self.status_indicator.grid(row=0, column=0, padx=10)

        self.status_label = ctk.CTkLabel(
            self.status_bar,
            text="Servidor: Desligado",
            font=ctk.CTkFont(size=12)
        )
        self.status_label.grid(row=0, column=1, sticky="w")

        self.time_label = ctk.CTkLabel(
            self.status_bar,
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.time_label.grid(row=0, column=2, padx=20)
        self.update_time()

    def update_time(self):
        """Atualiza hora no status bar"""
        now = datetime.now().strftime("%H:%M:%S")
        self.time_label.configure(text=now)
        self.after(1000, self.update_time)

    def clear_content(self):
        """Limpa área de conteúdo"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        """Mostra dashboard principal"""
        self.clear_content()
        self.title_label.configure(text="Dashboard")

        welcome_frame = ctk.CTkFrame(self.content_frame)
        welcome_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        welcome_frame.grid_columnconfigure(0, weight=1)

        welcome_label = ctk.CTkLabel(
            welcome_frame,
            text="Bem-vindo ao ARQV30 Enhanced v3.0",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        welcome_label.grid(row=0, column=0, padx=30, pady=(30, 10))

        subtitle = ctk.CTkLabel(
            welcome_frame,
            text="Sistema Avançado de Análise de Mercado com IA",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.grid(row=1, column=0, padx=30, pady=(0, 30))

        stats_container = ctk.CTkFrame(self.content_frame)
        stats_container.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        stats_container.grid_columnconfigure((0, 1, 2), weight=1)

        stats = [
            ("Análises Realizadas", "0", "#0d7377"),
            ("Servidor Status", "Desligado", "#ff6b6b"),
            ("Última Atualização", "---", "#14a76c")
        ]

        for idx, (title, value, color) in enumerate(stats):
            stat_card = self.create_stat_card(stats_container, title, value, color)
            stat_card.grid(row=0, column=idx, padx=10, pady=10, sticky="ew")

        features_frame = ctk.CTkFrame(self.content_frame)
        features_frame.grid(row=2, column=0, sticky="ew", pady=(0, 20))
        features_frame.grid_columnconfigure(0, weight=1)

        features_title = ctk.CTkLabel(
            features_frame,
            text="🔥 Recursos Principais",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        features_title.grid(row=0, column=0, padx=30, pady=(20, 10), sticky="w")

        features = [
            "✓ IA com Busca Ativa Real (Gemini 2.0 + OpenAI + Groq)",
            "✓ Análise de Conteúdo Viral Real",
            "✓ Captura Automática de Screenshots",
            "✓ 16 Módulos de Análise Especializados",
            "✓ Rotação Inteligente de APIs",
            "✓ Workflow em 3 Etapas Controladas",
            "✓ Banco de Dados Local Seguro",
            "✓ Interface Web Moderna Integrada"
        ]

        for idx, feature in enumerate(features, start=1):
            feature_label = ctk.CTkLabel(
                features_frame,
                text=feature,
                font=ctk.CTkFont(size=13),
                anchor="w"
            )
            feature_label.grid(row=idx, column=0, padx=50, pady=5, sticky="w")

        quick_start = ctk.CTkFrame(self.content_frame)
        quick_start.grid(row=3, column=0, sticky="ew")
        quick_start.grid_columnconfigure(0, weight=1)

        qs_title = ctk.CTkLabel(
            quick_start,
            text="🚀 Início Rápido",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        qs_title.grid(row=0, column=0, padx=30, pady=(20, 15), sticky="w")

        start_button = ctk.CTkButton(
            quick_start,
            text="Iniciar Servidor e Abrir Interface Web",
            command=self.quick_start,
            height=50,
            font=ctk.CTkFont(size=15, weight="bold")
        )
        start_button.grid(row=1, column=0, padx=30, pady=(0, 30), sticky="ew")

    def create_stat_card(self, parent, title, value, color):
        """Cria card de estatística"""
        card = ctk.CTkFrame(parent)
        card.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        title_label.grid(row=0, column=0, padx=20, pady=(20, 5))

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=color
        )
        value_label.grid(row=1, column=0, padx=20, pady=(0, 20))

        return card

    def toggle_server(self):
        """Liga/desliga servidor"""
        if not self.server_running:
            self.start_server()
        else:
            self.stop_server()

    def start_server(self):
        """Inicia servidor Flask"""
        try:
            self.server_button.configure(text="⏳ Iniciando...")
            self.server_button.configure(state="disabled")

            def run_server():
                try:
                    self.app = create_app()
                    self.server_running = True

                    self.after(100, lambda: self.update_server_status(True))

                    self.app.run(
                        host=self.host,
                        port=self.port,
                        debug=False,
                        use_reloader=False,
                        threaded=True
                    )
                except Exception as e:
                    self.after(100, lambda: self.show_error(f"Erro ao iniciar servidor: {str(e)}"))
                    self.after(100, lambda: self.update_server_status(False))

            self.server_thread = threading.Thread(target=run_server, daemon=True)
            self.server_thread.start()

        except Exception as e:
            self.show_error(f"Erro ao iniciar servidor: {str(e)}")
            self.update_server_status(False)

    def stop_server(self):
        """Para servidor Flask"""
        if self.server_running:
            self.server_running = False
            self.update_server_status(False)
            messagebox.showinfo("Servidor", "Servidor será encerrado.")

    def update_server_status(self, running: bool):
        """Atualiza status do servidor na UI"""
        self.server_running = running

        if running:
            self.server_button.configure(text="🛑 Parar Servidor", state="normal")
            self.status_indicator.configure(text_color="#14a76c")
            self.status_label.configure(text=f"Servidor: Ativo em http://{self.host}:{self.port}")
        else:
            self.server_button.configure(text="🚀 Iniciar Servidor", state="normal")
            self.status_indicator.configure(text_color="#ff6b6b")
            self.status_label.configure(text="Servidor: Desligado")

    def quick_start(self):
        """Início rápido: inicia servidor e abre navegador"""
        if not self.server_running:
            self.start_server()

            def open_browser():
                import time
                time.sleep(2)
                webbrowser.open(f"http://{self.host}:{self.port}")

            threading.Thread(target=open_browser, daemon=True).start()
        else:
            webbrowser.open(f"http://{self.host}:{self.port}")

    def new_analysis(self):
        """Abre interface para nova análise"""
        if not self.server_running:
            response = messagebox.askyesno(
                "Servidor Desligado",
                "O servidor precisa estar ativo para criar uma nova análise.\n\nDeseja iniciar o servidor agora?"
            )
            if response:
                self.quick_start()
        else:
            webbrowser.open(f"http://{self.host}:{self.port}")

    def show_analyses(self):
        """Mostra análises salvas"""
        self.clear_content()
        self.title_label.configure(text="Análises Salvas")

        info_label = ctk.CTkLabel(
            self.content_frame,
            text="Suas análises são armazenadas na pasta 'analyses_data'",
            font=ctk.CTkFont(size=14)
        )
        info_label.grid(row=0, column=0, padx=20, pady=20)

        open_folder_btn = ctk.CTkButton(
            self.content_frame,
            text="📁 Abrir Pasta de Análises",
            command=self.open_analyses_folder,
            height=40
        )
        open_folder_btn.grid(row=1, column=0, padx=20, pady=10)

    def open_analyses_folder(self):
        """Abre pasta de análises"""
        analyses_path = Path("analyses_data")
        if not analyses_path.exists():
            analyses_path.mkdir(exist_ok=True)

        if sys.platform == 'win32':
            os.startfile(str(analyses_path))
        else:
            webbrowser.open(str(analyses_path))

    def show_settings(self):
        """Mostra configurações"""
        self.clear_content()
        self.title_label.configure(text="Configurações")

        settings_frame = ctk.CTkFrame(self.content_frame)
        settings_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        settings_frame.grid_columnconfigure(1, weight=1)

        port_label = ctk.CTkLabel(settings_frame, text="Porta do Servidor:")
        port_label.grid(row=0, column=0, padx=20, pady=15, sticky="w")

        port_entry = ctk.CTkEntry(settings_frame, placeholder_text=str(self.port))
        port_entry.grid(row=0, column=1, padx=20, pady=15, sticky="ew")

        appearance_label = ctk.CTkLabel(settings_frame, text="Tema:")
        appearance_label.grid(row=1, column=0, padx=20, pady=15, sticky="w")

        appearance_menu = ctk.CTkOptionMenu(
            settings_frame,
            values=["Dark", "Light", "System"],
            command=self.change_appearance
        )
        appearance_menu.grid(row=1, column=1, padx=20, pady=15, sticky="ew")
        appearance_menu.set("Dark")

    def change_appearance(self, mode: str):
        """Muda tema da interface"""
        ctk.set_appearance_mode(mode.lower())

    def show_documentation(self):
        """Mostra documentação"""
        self.clear_content()
        self.title_label.configure(text="Documentação")

        docs_text = """
        ARQV30 Enhanced v3.0 - Guia Rápido

        1. INICIAR O SISTEMA
           - Clique em "Iniciar Servidor" na barra lateral
           - Aguarde o servidor inicializar
           - O indicador ficará verde quando pronto

        2. CRIAR NOVA ANÁLISE
           - Com o servidor ativo, clique em "Nova Análise"
           - Ou clique em "Início Rápido" no Dashboard
           - A interface web será aberta no navegador

        3. CONFIGURAR APIs
           - As chaves de API ficam no arquivo .env
           - Configure: GEMINI_API_KEY, OPENAI_API_KEY, GROQ_API_KEY
           - APIs opcionais: SERPER_API_KEY, EXA_API_KEY

        4. ANÁLISES SALVAS
           - Análises ficam em: analyses_data/analyses/
           - Relatórios ficam em: analyses_data/reports/
           - Backups automáticos são criados

        5. SOLUÇÃO DE PROBLEMAS
           - Se o servidor não iniciar, verifique a porta 12000
           - Logs ficam em: analyses_data/logs/
           - Reinicie o aplicativo se necessário
        """

        docs_label = ctk.CTkTextbox(self.content_frame, height=500)
        docs_label.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        docs_label.insert("1.0", docs_text)
        docs_label.configure(state="disabled")

    def show_about(self):
        """Mostra informações sobre o app"""
        self.clear_content()
        self.title_label.configure(text="Sobre")

        about_frame = ctk.CTkFrame(self.content_frame)
        about_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        about_frame.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            about_frame,
            text="ARQV30 Enhanced v3.0",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title.grid(row=0, column=0, pady=(30, 10))

        subtitle = ctk.CTkLabel(
            about_frame,
            text="Market Analysis System",
            font=ctk.CTkFont(size=16),
            text_color="gray"
        )
        subtitle.grid(row=1, column=0, pady=(0, 30))

        info_text = """
        Sistema Avançado de Análise de Mercado

        Desenvolvido com:
        • Python 3.11+
        • Flask + CustomTkinter
        • IA: Gemini 2.0, OpenAI, Groq
        • Selenium + Playwright

        © 2024 ARQV30 Enhanced
        Todos os direitos reservados
        """

        info_label = ctk.CTkLabel(
            about_frame,
            text=info_text,
            font=ctk.CTkFont(size=13),
            justify="center"
        )
        info_label.grid(row=2, column=0, pady=(0, 30))

    def show_error(self, message: str):
        """Mostra mensagem de erro"""
        messagebox.showerror("Erro", message)

    def on_closing(self):
        """Handler para fechar aplicação"""
        if self.server_running:
            response = messagebox.askyesno(
                "Servidor Ativo",
                "O servidor ainda está rodando.\n\nDeseja realmente sair?"
            )
            if response:
                self.server_running = False
                self.destroy()
        else:
            self.destroy()


def main():
    """Função principal"""
    app = ARQV30DesktopApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()


if __name__ == "__main__":
    main()
