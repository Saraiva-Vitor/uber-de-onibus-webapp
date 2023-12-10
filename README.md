# Necessário para rodar o projeto:

* Instalar bibliotecas (com o terminal na raiz do projeto onde se enconta o arquivo requirements.txt)
```
pip install -r requirements.txt
```

* Iniciar projeto (com o terminal na raiz do projeto onde se enconta o arquivo manage.py)
```
python manage.py runserver
```


# Páginas/Rotas

* /
  
HomePage

* /error, /(outra rota qualquer)

Renderiza as páginas de erro com html: 400.html, 403.html, 404.html e 500.html ou a página PageNotFound.html

* /admin
  
Página de Administrador

* /login
  
Página de Login

* /cadastro
  
Página de Cadastro

* /pesquisa
  
Página de Resultado da Pesquisa de Rotas

* /mapa-de-assentos/rota_id/hora_id
  
Página do Mapa para Seleção do Assento da Rota e Horários Específicos

* /checkout
  
Página de Descrição do Horário Selecionado da Rota

* /pagamento

Página dos Métodos de Pagamento

* /confirmacao-pagamento

Página de Confirmação de Pagamento

* /passagem

Página com o Ticket de Embarque
