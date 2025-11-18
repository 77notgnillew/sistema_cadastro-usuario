# Sistema de Cadastro de Usuários

Um sistema completo de cadastro de pessoas com validações, histórico de exclusão e estatísticas, desenvolvido em Python para console.

## 🚀 Funcionalidades

- Cadastro de usuários com validação completa:
  - Nome (apenas letras, mínimo de 2 caracteres)
  - Data de nascimento (formato DD/MM/AAAA, não pode ser no futuro)
  - Cidade (apenas letras, mínimo de 2 caracteres)
  - E-mail (formato válido e não duplicado)
- Cálculo automático da idade a partir da data de nascimento
- Listagem de usuários em ordem alfabética
- Busca por nome, ID e e-mail
- Exclusão de usuário com confirmação e log de exclusões
- Visualização de todos os usuários excluídos, com dados e data/hora da exclusão
- Estatísticas das idades: mínimo, máximo, média, mediana e desvio-padrão
- Menu interativo em linha de comando, mensagens claras ao usuário

## 📦 Como usar

1. **Pré-requisitos:**  
   - Python 3.6 ou superior instalado.

2. **Execução:**
   - Clone ou baixe este repositório.
   - Execute o arquivo principal:
     ```
     python cadastro_usuarios.py
     ```
   - Siga as instruções do menu.

## 📊 Exemplo de menu

|---------- MENU -----------|
| 1 - Cadastrar |
| 2 - Listar |
| 3 - Estatísticas de idade |
| 4 - Buscar por nome |
| 5 - Buscar por E-mail |
| 6 - Excluir usuário |
| 7 - Usuários excluídos |
| 0 - Sair |

## 🛠️ Tecnologias e conceitos

- Python 3
- Listas e dicionários
- Funções modulares
- Expressões regulares (regex)
- Cálculo de estatísticas (média, mediana, desvio-padrão)
- Organização de código e boas práticas
- Tratamento de erros e validações

## 👨‍💻 Autor

- [Wellington Matos da Costa](https://github.com/77notgnillew)
- [LinkedIn](https://www.linkedin.com/in/wellingtonmatos77/)


## 📄 Licença

Este projeto está sob licença MIT. Sinta-se livre para usar, estudar e modificar!

---

⭐ Se este projeto for útil, deixe uma estrela!
