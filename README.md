# Formulário de Cadastro Automatizado com Selenium

Projeto de automação desenvolvido para demonstrar o preenchimento automático de formulários web utilizando Selenium WebDriver. O projeto consiste em uma página HTML com um formulário de cadastro e um script Python que automatiza seu preenchimento.

## Requisitos

Antes de rodar o código, você precisa ter alguns pré-requisitos instalados:

1. **Python** (versão 3.x)
2. **Selenium**: Biblioteca para automação de navegadores.
3. **GeckoDriver ou ChromeDriver**: Dependendo do navegador que você escolheu (Firefox ou Chrome).
4. **Servidor HTTP Local**: Para servir o arquivo HTML do formulário (utilizando `python -m http.server`).

## Instalação

1. **Instale as dependências necessárias**:
   ```properties
   pip install -r requirements.txt
   ```
2. Baixe o Driver apropriado:
   - Firefox: geckodriver
   - Chrome: chromedriver
     
3. Adicione o driver ao PATH do sistema ou especifique seu caminho no código:
   ```properties
   gecko_driver_path = r"caminho/para/seu/driver"
   ```
## Execução do Servidor Local

1. Inicie o servidor local para hospedar o arquivo HTML:
   ```properties
   python -m http.server
   ```
   Isso irá iniciar um servidor HTTP na URL http://localhost:8000

2. Acesse http://localhost:8000/index.html para visualizar o formulário.

## Execução do Código

1. Execute o arquivo main.py

## Como funciona o Código

- O código usa o Selenium para abrir o navegador e acessar o formulário HTML.
- Ele espera que os elementos (como os campos de entrada de texto) se tornem clicáveis antes de interagir com eles.
- O preenchimento dos campos é feito utilizando o método send_keys(), que simula o envio de texto.
- O código faz uso da biblioteca WebDriverWait para garantir que o elemento esteja pronto para a interação
