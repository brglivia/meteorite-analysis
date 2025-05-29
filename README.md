# 🌠 Análise de Meteoritos no Mundo
Este projeto apresenta uma análise exploratória de dados sobre meteoritos, com visualizações interativas em **Streamlit** e um notebook Jupyter que detalha a análise e o tratamento dos dados.

---

## 🚀 Sobre o Projeto
- Exploração do dataset de meteoritos: estatísticas, gráficos temporais, histogramas e mapas de localização.
- Dashboard interativo desenvolvido em Streamlit para fácil visualização e análise dos dados.
- Notebook Jupyter contendo o processo de limpeza, tratamento e análise detalhada dos dados.
  
---

## 🔍 Principais Insights
- Aumento no Registro de Meteoritos: Observa-se um crescimento no número de meteoritos registrados a partir da década de 1960, refletindo provavelmente avanços na detecção e registro dos eventos.
- Distribuição de Massa: A maioria dos meteoritos possui massas relativamente baixas. Algumas classes específicas apresentam médias de massa significativamente mais altas, destacando-se pela sua raridade ou características físicas.
- Localização Global: A maior concentração de meteoritos encontrados ocorre em regiões próximas aos polos e desertos, locais onde a detecção é facilitada devido à baixa vegetação e condições climáticas.
- Período Analisado: A análise focou principalmente nos registros entre 1959 e 2012, período com dados mais consistentes e representativos.
- Latitude e Longitude: As distribuições de latitude e longitude mostram que os registros estão espalhados por todo o mundo, sem grandes concentrações em áreas específicas, mas com ligeira predominância em regiões mais monitoradas.

---

## 📂 Conteúdo do Repositório
- `meteorite_landings.xlsx`: Arquivo de dados utilizado na análise.
- `app.py`: Aplicação Streamlit para visualização interativa dos dados.
- `notebook.ipynb`: Notebook com a análise e limpeza dos dados.
- `requirements.txt`: Arquivo com as dependências necessárias para rodar o app.
- `README.md`: Documentação do projeto.

---

## ☁️ Deploy no Streamlit Cloud
O app está hospedado no Streamlit Cloud e pode ser acessado [clicando aqui.](https://meteorite-analysis-u8hjg7zgof4u5nzgbmnldg.streamlit.app/)

---

## 📊 Tecnologias Utilizadas
- Python
- Pandas
- Matplotlib
- Streamlit

---

## 💡 O que Aprendi
- Criação de dashboards interativos para análise de dados.
- Manipulação e visualização de dados com Pandas e Matplotlib.
- Integração de notebooks com apps web para facilitar a apresentação.
- Deploy de aplicações web usando Streamlit Cloud.

---

## ⚙️ Como Rodar Localmente
1. Clone o repositório:
```bash
git clone https://github.com/brglivia/meteorite-analysis.git
cd meteorite-analysis

2. Instale as dependências
pip install -r requirements.txt

3. Rode o app Streamlit:
streamlit run app.py

