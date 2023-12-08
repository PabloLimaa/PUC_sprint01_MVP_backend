# Como executar a API


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

(1) Para isso, utilizar os comandos abaixo no terminal da IDE (por convenção adotamos 'env' para o nome do ambiente virtual).

```
python -m venv env 
```

O comando a seguir é para ativar o ambinete virtual no windows.

```
.\env\scripts\activate
```

(2) Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

```
(env)$ pip install -r requirements.txt
```

(3) Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

## Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: Pablo Henrique Costa de Lima  
E-mail: pablo.henriquelima07@gmail.com  
LinkedIn: https://www.linkedin.com/in/pablo-henrique-lima-542300164/    
Agradeço pela sua visita!
