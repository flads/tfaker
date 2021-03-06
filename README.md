# tfaker
Gere CPF e CNPJ válidos a partir do terminal. <br>
Sem abrir mais uma aba do Chrome e sem Ctrl-C.

### Instalação
Você pode executar o script de instalação ou seguir este passo a passo para instalar o **tfaker**:

1. É necessário que você tenha o gerenciador de pacotes pip instalado. Caso não possua, execute o seguinte comando:
    ```sh
    sudo apt-get install python3-pip -y
    ```

2. Uma vez com o pip instalado, clone o repositório do projeto:
    ```sh
    mkdir -p ~/src && git clone git@github.com:flads/tfaker.git ~/src/tfaker
    ```

3. Entre na pasta do projeto e instale as dependências:
    ```sh
    cd ~/src/tfaker && pip3 install -r requirements.txt
    ```

4. Crie um link para facilitar o uso do tfaker:
    ```sh
    sudo ln -s ~/src/tfaker/tfaker.py /usr/local/bin/tf
    ```

5. Você pode checar se o comando **tf** está funcionando corretamente assim:
    ```sh
    tf --help
    ```

### Utilização
Segue exemplos de utilização do **tfaker**:

- Gerando um CPF:
    ```sh
    tf cpf
    ```

- Gerando um CNPJ:
    ```sh
    tf cnpj
    ```
    
- Para gerar um CPF/CNPJ com os separadores utilize a flag **-s**, por exemplo:
    ```sh
    tf cpf -s
    ```

Licença
----

MIT
