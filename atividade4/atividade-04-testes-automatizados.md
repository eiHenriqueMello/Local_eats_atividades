# Atividade 4: Testes Automatizados do LocalEats

**Estudante:** Henrique Mello  
**Modalidade:** Trabalho Individual  
**Projeto:** LocalEats  
**Endereço do Sistema:** https://local-eats-unisenac.vercel.app/

---

## 1. Identificação das Responsabilidades

| ID | Integrante | Tipo | Comportamento Verificado | Arquivo e Função |
| :--- | :--- | :--- | :--- | :--- |
| **TU01** | Henrique Mello | Unitário | Avaliação válida dentro do intervalo (1 a 5) | `tests/test_regras_localeats.py::test_avaliacao_valida_dentro_do_intervalo` |
| **TU02** | Henrique Mello | Unitário | Avaliação inválida fora do intervalo | `tests/test_regras_localeats.py::test_avaliacao_invalida_fora_do_intervalo` |
| **TF01** | Henrique Mello | Funcional | Apresentação e carregamento da página do LocalEats | `tests/test_localeats.py::test_pesquisar_restaurante_funcional` |

---

## 2. Parte 1: Testes Unitários e TDD

### TDD de Henrique Mello

* **Regra escolhida:** Regra 4 - Validar avaliação do restaurante (`avaliacao_valida`).
* **Primeiro teste escrito:** `test_avaliacao_valida_dentro_do_intervalo`, verificando se valores como 1, 4 e 5 retornam `True`.
* **Por que o teste falhou inicialmente:** O teste falhou no ciclo RED porque a função `avaliacao_valida` ainda não tinha sido implementada na pasta `src/regras_localeats.py`.
* **Implementação mínima realizada:** Foi criada a função recebendo o parâmetro `nota` e retornando `True` caso a nota estivesse entre 1 e 5 (ciclo GREEN).
* **Segundo teste escrito:** `test_avaliacao_invalida_fora_do_intervalo`, validando os limites (notas 0 e 6 devem retornar `False`).
* **Melhoria ou refatoração realizada:** Adicionada validação de tipo para garantir que apenas valores numéricos sejam aceitos e simplificada a estrutura condicional no formato `1 <= nota <= 5`.

---

## 3. Parte 2: Teste Funcional com Playwright

* **Fluxo automatizado:** Verificação da apresentação da página e carregamento dos elementos interativos do LocalEats.
* **Locators utilizados:** `page.locator("body")`.
* **Assertions utilizadas:** 
  1. `expect(page).to_have_url(...)`: Valida que a navegação carrega o endereço correto da aplicação.
  2. `expect(page.locator("body")).to_be_visible()`: Valida que a estrutura visual e interativa da página está visível para o utilizador.

---

## 4. Uso de Inteligência Artificial

* **Ferramenta utilizada:** Gemini.
* **Como a ferramenta foi utilizada:** Auxílio no planeamento da estrutura do projeto individual, resolução de dependências no Windows/PowerShell, sintaxe dos seletores do Playwright em Python e formatação da documentação Markdown.
* **Uma sugestão que precisou ser alterada ou rejeitada:** A sugestão inicial de assertion em *camelCase* (`toHave_value`) gerou um erro no Pytest e precisou de ser corrigida para o formato correto em Python (*snake_case* `to_have_value`).
* **Como o código sugerido foi verificado:** Todos os testes unitários e funcionais foram executados localmente através do comando `pytest -v`, confirmando a aprovação de 100% das execuções no relatório gerado.