# 📘 MANUAL DE INSTALAÇÃO - ARQV30 Enhanced v3.0

## Guia Completo para Usuários Finais (Sem Experiência Técnica)

---

## 📋 ÍNDICE

1. [Introdução](#introdução)
2. [Requisitos do Sistema](#requisitos-do-sistema)
3. [Instalação Passo a Passo](#instalação-passo-a-passo)
4. [Configuração Inicial](#configuração-inicial)
5. [Como Usar o Sistema](#como-usar-o-sistema)
6. [Solução de Problemas](#solução-de-problemas)
7. [Perguntas Frequentes](#perguntas-frequentes)

---

## 🎯 INTRODUÇÃO

Bem-vindo ao **ARQV30 Enhanced v3.0**!

Este é um sistema profissional de análise de mercado que usa Inteligência Artificial para coletar e analisar informações detalhadas sobre qualquer nicho ou produto.

### O que o sistema faz?
- ✅ Analisa mercados e nichos de forma automática
- ✅ Coleta informações reais da internet
- ✅ Gera relatórios profissionais completos
- ✅ Identifica tendências e oportunidades
- ✅ Funciona 100% no seu computador (offline após instalação)

---

## 💻 REQUISITOS DO SISTEMA

### Requisitos Mínimos
- **Sistema Operacional:** Windows 10 ou Windows 11 (64-bit)
- **Processador:** Intel Core i5 ou AMD Ryzen 5 (ou superior)
- **Memória RAM:** 8 GB mínimo (16 GB recomendado)
- **Espaço em Disco:** 10 GB livres
- **Placa de Vídeo:** NVIDIA com suporte CUDA (opcional, mas recomendado)
- **Internet:** Conexão estável para uso das APIs de IA

### O que NÃO é necessário
- ❌ Conhecimento de programação
- ❌ Instalação do Python (faremos isso juntos)
- ❌ Experiência com linha de comando
- ❌ Configurações avançadas de sistema

---

## 🚀 INSTALAÇÃO PASSO A PASSO

### ETAPA 1: Instalar o Python 3.11

#### 1.1 - Baixar o Python
1. Abra seu navegador (Chrome, Edge, Firefox)
2. Acesse: [https://www.python.org/downloads/](https://www.python.org/downloads/)
3. Clique no botão amarelo **"Download Python 3.11.x"**
4. Salve o arquivo (python-3.11.x-amd64.exe)

#### 1.2 - Instalar o Python
1. Localize o arquivo baixado (geralmente na pasta Downloads)
2. Clique duas vezes no arquivo para executar
3. **⚠️ IMPORTANTE:** Marque a caixa **"Add Python to PATH"** na primeira tela
4. Clique em **"Install Now"**
5. Aguarde a instalação (pode levar alguns minutos)
6. Clique em **"Close"** quando terminar

#### 1.3 - Verificar a Instalação
1. Pressione as teclas `Windows + R` juntas
2. Digite: `cmd` e pressione Enter
3. Na janela preta que abrir, digite: `python --version`
4. Deve aparecer: `Python 3.11.x`
5. Se aparecer, está correto! Feche a janela.

---

### ETAPA 2: Baixar e Extrair o ARQV30

#### 2.1 - Baixar o Sistema
1. Baixe o arquivo `ARQV30_Enhanced_v3.zip` fornecido
2. Salve em uma pasta de fácil acesso (ex: `C:\ARQV30`)

#### 2.2 - Extrair os Arquivos
1. Vá até a pasta onde salvou o arquivo
2. Clique com botão direito no arquivo `.zip`
3. Selecione **"Extrair Tudo..."**
4. Escolha o destino: `C:\ARQV30`
5. Clique em **"Extrair"**

#### 2.3 - Verificar os Arquivos
Dentro da pasta `C:\ARQV30`, você deve ver:
```
📁 C:\ARQV30\
  📄 install.bat
  📄 run.bat
  📄 arqv30_desktop.py
  📄 requirements.txt
  📄 .env (arquivo de configuração)
  📁 src\
  📁 external_ai_verifier\
  📁 analyses_data\
```

---

### ETAPA 3: Instalar as Dependências

#### 3.1 - Executar o Instalador Automático
1. Navegue até `C:\ARQV30`
2. Localize o arquivo **`install.bat`**
3. Clique com botão direito nele
4. Selecione **"Executar como administrador"**
5. Se aparecer uma tela de segurança, clique em **"Sim"**

#### 3.2 - Aguardar a Instalação
- Uma janela preta (Terminal) irá abrir
- Você verá muitas mensagens passando (isso é normal!)
- **⏱️ IMPORTANTE:** Este processo pode levar de 15 a 30 minutos
- **Não feche a janela durante a instalação!**
- Quando terminar, aparecerá: `"Instalação concluída com sucesso!"`
- Pressione qualquer tecla para fechar

#### 3.3 - O que está sendo instalado?
O sistema instala automaticamente:
- ✓ Todas as bibliotecas Python necessárias
- ✓ Drivers para navegadores (Chrome)
- ✓ Modelos de IA para análise de texto
- ✓ Ferramentas de processamento de dados
- ✓ Interface gráfica moderna

---

### ETAPA 4: Instalar CUDA (Opcional - para NVIDIA)

#### 4.1 - Verificar se você tem placa NVIDIA
1. Pressione `Windows + R`
2. Digite: `dxdiag` e pressione Enter
3. Clique na aba **"Display"** ou **"Exibição"**
4. Veja o nome da sua placa de vídeo
5. Se tiver "NVIDIA" no nome, prossiga. Caso contrário, pule esta etapa.

#### 4.2 - Baixar e Instalar CUDA
1. Acesse: [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
2. Selecione: Windows → x86_64 → 11 → exe (local)
3. Baixe e execute o instalador
4. Siga as instruções (instalação Express)
5. Reinicie o computador quando solicitado

**NOTA:** CUDA é opcional e só melhora a performance se você tiver placa NVIDIA.

---

## ⚙️ CONFIGURAÇÃO INICIAL

### ETAPA 5: Configurar as Chaves de API

Para que o sistema funcione, você precisa configurar as chaves das IAs.

#### 5.1 - Obter as Chaves de API

**GEMINI (Google) - OBRIGATÓRIA**
1. Acesse: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em **"Create API Key"**
4. Copie a chave gerada

**OPENAI (Opcional, mas recomendado)**
1. Acesse: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Crie uma conta ou faça login
3. Clique em **"Create new secret key"**
4. Copie a chave (ela começa com `sk-`)

**GROQ (Opcional, mas recomendado)**
1. Acesse: [https://console.groq.com/keys](https://console.groq.com/keys)
2. Crie uma conta ou faça login
3. Clique em **"Create API Key"**
4. Copie a chave gerada

#### 5.2 - Configurar o Arquivo .env

1. Vá até `C:\ARQV30`
2. Localize o arquivo **`.env`**
3. Clique com botão direito e selecione **"Editar"** ou **"Abrir com Bloco de Notas"**
4. Cole suas chaves nos locais indicados:

```env
# IA - PRINCIPAL (OBRIGATÓRIO)
GEMINI_API_KEY=sua_chave_gemini_aqui

# IA - COMPLEMENTARES (OPCIONAL)
OPENAI_API_KEY=sua_chave_openai_aqui
GROQ_API_KEY=sua_chave_groq_aqui

# DEIXE O RESTANTE COMO ESTÁ
```

5. Salve o arquivo (Ctrl + S)
6. Feche o Bloco de Notas

**⚠️ IMPORTANTE:** Nunca compartilhe suas chaves de API com ninguém!

---

## 🎮 COMO USAR O SISTEMA

### ETAPA 6: Iniciar o Sistema

#### 6.1 - Primeira Execução
1. Vá até `C:\ARQV30`
2. Localize o arquivo **`run.bat`**
3. Clique duas vezes nele
4. Uma janela com interface gráfica moderna irá abrir

#### 6.2 - Tela Principal
Você verá uma interface com:
- **Barra Lateral Esquerda:** Menu de navegação
- **Área Central:** Dashboard com informações
- **Barra Inferior:** Status do sistema

#### 6.3 - Iniciar o Servidor
1. No menu lateral, clique em **"🚀 Iniciar Servidor"**
2. Aguarde alguns segundos
3. O indicador na barra inferior ficará **VERDE**
4. Aparecerá: `Servidor: Ativo em http://127.0.0.1:12000`

#### 6.4 - Abrir Interface Web
1. Clique em **"📊 Nova Análise"** no menu lateral
2. Seu navegador padrão abrirá automaticamente
3. Você verá a interface web completa do sistema

---

### ETAPA 7: Criar Sua Primeira Análise

#### 7.1 - Preencher Informações Básicas
1. **Nome do Nicho/Produto:** Digite o que você quer analisar
   - Exemplo: "Cursos online de marketing digital"
   - Exemplo: "Produtos para pets"

2. **Descrição (opcional):** Detalhes adicionais
   - Exemplo: "Quero entender o mercado de cursos para iniciantes"

3. **Escolha o Tipo de Análise:**
   - **Análise Completa:** Mais detalhada (recomendado)
   - **Análise Rápida:** Mais rápida, menos detalhes

#### 7.2 - Configurar Análise
1. **Profundidade da Pesquisa:**
   - Alta: Mais completa (pode levar 30-60 min)
   - Média: Balanceada (15-30 min)
   - Baixa: Mais rápida (5-15 min)

2. Clique em **"Iniciar Análise"**

#### 7.3 - Acompanhar o Progresso
- Você verá uma barra de progresso
- Mensagens indicando cada etapa
- Logs em tempo real do que está sendo feito

**ETAPAS DA ANÁLISE:**
1. 🔍 Coleta de Dados (40%)
   - Busca informações na internet
   - Coleta conteúdos relevantes

2. 🧠 Análise com IA (30%)
   - Processa dados coletados
   - Identifica padrões e tendências

3. 📊 Geração de Relatório (30%)
   - Cria relatório completo
   - Organiza informações

#### 7.4 - Visualizar Resultados
Quando terminar:
1. Aparecerá um botão **"Ver Relatório"**
2. Clique nele para abrir o relatório completo
3. Você poderá:
   - Ler todas as análises
   - Baixar em PDF
   - Salvar para consulta futura

---

### ETAPA 8: Gerenciar Análises

#### 8.1 - Análises Salvas
1. No menu lateral, clique em **"📁 Análises Salvas"**
2. Você verá todas as suas análises anteriores
3. Clique em **"Abrir Pasta de Análises"**

#### 8.2 - Localização dos Arquivos
Suas análises ficam em: `C:\ARQV30\analyses_data\`

**Estrutura:**
```
📁 analyses_data\
  📁 analyses\     (dados das análises)
  📁 reports\      (relatórios em PDF)
  📁 progress\     (progresso salvo)
  📁 logs\         (logs do sistema)
```

---

## 🔧 SOLUÇÃO DE PROBLEMAS

### Problema 1: "Python não é reconhecido como comando"

**Solução:**
1. Desinstale o Python
2. Reinstale marcando **"Add Python to PATH"**
3. Reinicie o computador

---

### Problema 2: "Erro ao instalar dependências"

**Solução:**
1. Abra o Prompt de Comando como Administrador:
   - Pressione `Windows + X`
   - Clique em **"Prompt de Comando (Admin)"** ou **"Windows PowerShell (Admin)"**

2. Execute os comandos:
```cmd
cd C:\ARQV30
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Aguarde terminar e tente novamente

---

### Problema 3: "Servidor não inicia"

**Possíveis Causas:**
- Porta 12000 já está em uso

**Solução:**
1. Feche todos os programas
2. Reinicie o computador
3. Tente novamente

OU

1. Abra o arquivo `.env`
2. Mude a linha: `PORT=12000` para `PORT=13000`
3. Salve e tente novamente

---

### Problema 4: "API Key inválida"

**Solução:**
1. Verifique se copiou a chave completa (sem espaços)
2. Gere uma nova chave no site da API
3. Cole novamente no arquivo `.env`
4. Reinicie o sistema

---

### Problema 5: "Análise trava ou não avança"

**Solução:**
1. Verifique sua conexão com internet
2. Verifique se as chaves de API estão corretas
3. Clique em **"Cancelar"** e tente novamente
4. Se persistir, reinicie o sistema

---

### Problema 6: "Interface não abre no navegador"

**Solução:**
1. Verifique se o servidor está rodando (indicador verde)
2. Abra manualmente o navegador
3. Digite na barra de endereço: `http://127.0.0.1:12000`
4. Pressione Enter

---

## ❓ PERGUNTAS FREQUENTES

### 1. O sistema funciona sem internet?
**NÃO.** O sistema precisa de internet para:
- Acessar as APIs de IA (Gemini, OpenAI, Groq)
- Buscar informações na web
- Baixar dados em tempo real

Após a análise ser concluída, você pode visualizar os relatórios offline.

---

### 2. Posso usar em múltiplos computadores?
**SIM.** Você pode instalar em quantos computadores quiser.
Apenas repita o processo de instalação em cada máquina.

---

### 3. As chaves de API são pagas?
- **Gemini (Google):** Tem plano gratuito generoso
- **OpenAI:** Requer créditos pagos (mas valores baixos)
- **Groq:** Tem plano gratuito limitado

Você pode começar usando apenas Gemini (gratuito).

---

### 4. Meus dados ficam salvos?
**SIM.** Todas as análises são salvas localmente em:
`C:\ARQV30\analyses_data\`

Nada é enviado para servidores externos (exceto as consultas às APIs de IA).

---

### 5. Posso fazer backup das análises?
**SIM.** Basta copiar a pasta `analyses_data` para outro local:
- Pendrive
- HD externo
- Nuvem (Google Drive, Dropbox, etc.)

---

### 6. Como atualizar o sistema?
Quando uma nova versão for lançada:
1. Faça backup da pasta `analyses_data`
2. Baixe a nova versão
3. Extraia em uma nova pasta
4. Copie sua pasta `analyses_data` antiga para a nova instalação
5. Copie seu arquivo `.env` (com as chaves) para a nova pasta

---

### 7. O sistema pode ser detectado como vírus?
Alguns antivírus podem dar falso positivo porque:
- O sistema faz scraping (coleta de dados web)
- Usa automação de navegadores
- Executa scripts Python

**É seguro.** Você pode adicionar a pasta à lista de exceções do seu antivírus.

---

### 8. Quantas análises posso fazer?
**ILIMITADAS.** Você pode fazer quantas análises quiser.
O único limite é o espaço em disco e os limites das APIs gratuitas.

---

### 9. O sistema funciona em Mac ou Linux?
Esta versão foi otimizada para **Windows**.
Para Mac/Linux, seria necessário ajustes na instalação.

---

### 10. Preciso manter o sistema aberto durante a análise?
**SIM.** Não feche o programa enquanto uma análise estiver em andamento.
O progresso é salvo, mas é melhor deixar concluir.

---

## 📞 SUPORTE

### Onde obter ajuda?

**Documentação Interna:**
- No sistema, clique em **"📖 Documentação"** no menu lateral

**Logs do Sistema:**
- Vá em: `C:\ARQV30\analyses_data\logs\`
- Abra o arquivo mais recente para ver detalhes de erros

**Informações do Sistema:**
- No sistema, clique em **"ℹ️ Sobre"** no menu lateral

---

## ✅ CHECKLIST FINAL

Antes de começar, certifique-se:

- [ ] Windows 10/11 64-bit instalado
- [ ] Python 3.11 instalado e no PATH
- [ ] ARQV30 extraído em `C:\ARQV30`
- [ ] Dependências instaladas via `install.bat`
- [ ] CUDA instalado (se tiver NVIDIA)
- [ ] Chave Gemini configurada no `.env`
- [ ] Outras chaves (OpenAI, Groq) configuradas (opcional)
- [ ] Conexão estável com internet
- [ ] Pelo menos 10 GB de espaço livre
- [ ] Antivírus configurado (exceção se necessário)

---

## 🎉 PARABÉNS!

Você está pronto para usar o **ARQV30 Enhanced v3.0**!

### Próximos Passos:
1. Execute `run.bat`
2. Inicie o servidor
3. Crie sua primeira análise
4. Explore os recursos

### Dicas Finais:
- 💡 Comece com análises rápidas para testar
- 💡 Use descrições detalhadas para melhores resultados
- 💡 Salve seus relatórios importantes
- 💡 Faça backup regular da pasta `analyses_data`

---

**Desenvolvido com 💙 pela equipe ARQV30**

**© 2024 ARQV30 Enhanced - Todos os direitos reservados**

---

## 📝 HISTÓRICO DE VERSÕES

### v3.0 (Atual)
- Interface Desktop CustomTkinter
- Suporte completo Windows
- Build via PyInstaller
- CUDA otimizado
- Manual completo para usuários finais

---

**FIM DO MANUAL**
