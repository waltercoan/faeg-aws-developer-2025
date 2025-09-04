# faeg-aws-developer-2025

## Exemplo do [./vscode/launch.json](./vscode/launch.json)

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "AWS_ACCESS_KEY_ID": "",
                "AWS_SECRET_ACCESS_KEY": "",
                "AWS_SESSION_TOKEN": ""
            },
            "envFile": "${workspaceFolder}/.env"
        }
    ]
}
```

## Criando o ambiente Python

- Executar o comando para criar um VENV

```bash
python -m venv venv
```

- Ativar o VENV

```bash
source ./venv/bin/activate
```

- Selecionar o interpretador do Python:

1) Teclar F1
2) Digitar: Python: Select Interpreter
3) Escolher: Enter Interpreter Path...
4) Escolher: Find
5) Escolher: /workspaces/faeg-aws-developer-2025/s3/venv/bin/python3

- Instalar as dependências

```bash
pip install -r ./requirements.txt
```

- Fazer o commit e push para o Github
```bash
git add .
git commit -m "texto explicando as alteracoes"
git push
```