# 🏥 Projeto Integrado: Sistema de Gestão (Clínica Vida+)

Este projeto é uma solução para o Projeto Integrado do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O objetivo é desenvolver um protótipo de sistema de gestão para a "Clínica Vida+", aplicando conceitos de programação, lógica e modelagem de sistemas.

## 🚀 Funcionalidades

O sistema principal (`clinica.py`) é um programa de console em Python que permite:

* **Gestão de Pacientes:**
    * Cadastrar pacientes (Nome, CPF, Idade, Telefone).
    * Listar todos os pacientes.
    * Buscar um paciente por nome.
* **Estatísticas:**
    * Calcular o número total de pacientes.
    * Calcular a idade média.
    * Encontrar o paciente mais novo e o mais velho.
* **Gestão da Clínica:**
    * Cadastrar médicos e suas especialidades.
    * Agendar consultas, vinculando pacientes e médicos.
    * Listar todos os agendamentos.

## 🛠️ Componentes do Projeto

Este repositório inclui todas as etapas exigidas no documento do projeto:

1.  **`clinica.py`**: O sistema principal em Python.
2.  **`logica_acesso.md`**: A análise de lógica proposicional e tabelas verdade para o controle de acesso (Passo 3).
3.  **`pseudocodigo_fila.txt`**: O algoritmo em pseudocódigo para a fila de atendimento (Passo 4).
4.  **`diagrama_casos_de_uso.puml`**: O código-fonte PlantUML para o Diagrama de Casos de Uso (Passo 5).

## ⚙️ Como Executar

1.  Certifique-se de ter o [Python](https://www.python.org/) instalado.
2.  Clone este repositório.
3.  No seu terminal, navegue até a pasta do projeto.
4.  Execute o sistema principal:
    ```bash
    python clinica.py
    ```