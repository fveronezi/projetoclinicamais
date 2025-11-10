# Passo 3: Análise Lógica

O objetivo é analisar as regras de atendimento da Clínica Vida+. 

**Variáveis Lógicas:**
***A:** Paciente tem agendamento
***B:** Paciente está com documentos em dia
***C:** Há médico disponível
***D:** Paciente está em dia com pagamentos

---

### 1. Expressões Lógicas

***Consulta Normal:** (Tem agendamento E docs OK E médico) OU (Docs OK E médico E pagamentos em dia)
    * `S_normal = (A ∧ B ∧ C) ∨ (B ∧ C ∧ D)`

***Emergência:** (Há médico) E (Tem documentos OU pagamentos em dia)
    * `S_emerg = C ∧ (B ∨ D)`

---

### 2. e 3. Tabela Verdade Completa (16 Linhas)

Aqui está a tabela verdade para todas as 16 combinações possíveis das variáveis A, B, C e D.

| Linha | A | B | C | D | **(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)** <br> **(Consulta Normal)** | **C ∧ (B ∨ D)** <br> **(Emergência)** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | F | F | F | F | F | F |
| 2 | F | F | F | V | F | F |
| 3 | F | F | V | F | F | F |
| 4 | F | F | V | V | F | **V** |
| 5 | F | V | F | F | F | F |
| 6 | F | V | F | V | F | F |
| 7 | F | V | V | F | F | **V** |
| 8 | F | V | V | V | **V** | **V** |
| 9 | V | F | F | F | F | F |
| 10 | V | F | F | V | F | F |
| 11 | V | F | V | F | F | F |
| 12 | V | F | V | V | F | **V** |
| 13 | V | V | F | F | F | F |
| 14 | V | V | F | V | F | F |
| 15 | V | V | V | F | **V** | **V** |
| 16 | V | V | V | V | **V** | **V** |

---

### 4. Análise

* **Consulta Normal:** O paciente pode ser atendido em **3** situações diferentes (Linhas 8, 15 e 16).
* **Emergência:** O paciente pode ser atendido em **6** situações diferentes (Linhas 4, 7, 8, 12, 15 e 16).

---

### 5. Situação Prática

* **Condições:** Sem agendamento $(A=F)$, Documentos OK $(B=V)$, Médico disponível $(C=V)$, Pagamentos atrasados $(D=F)$.
* *Corresponde à Linha 7 da tabela.*

* **Análise Consulta Normal:**
    * `S_normal = (F ∧ V ∧ V) ∨ (V ∧ V ∧ F)`
    * `S_normal = (F) ∨ (F)`
    * **Resultado: FALSO** (Não será atendido)

* **Análise Emergência:**
    * `S_emerg = V ∧ (V ∨ F)`
    * `S_emerg = V ∧ (V)`
    * **Resultado: VERDADEIRO** (Será atendido)

**Conclusão:** O paciente será atendido na modalidade Emergência.