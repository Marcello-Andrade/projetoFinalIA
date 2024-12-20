# projetoFinalIA
Projeto referente a matéria de Inteligência Artificial.

## Descrição

O projeto **Consulta de Clima** é uma aplicação web que permite ao usuário consultar as condições climáticas atuais de uma cidade específica, bem como visualizar uma previsão estendida para os próximos dias. A interface foi projetada para ser simples e intuitiva, permitindo acesso rápido às informações climáticas.

## Funcionalidades

- Consulta das condições climáticas atuais com base no nome da cidade fornecido.
    
- Exibição de uma previsão estendida para os próximos dias, incluindo temperatura e descrição.
    
- Interface responsiva e moderna com gradiente de fundo.
    

## Tecnologias Utilizadas

- **HTML5** e **CSS3**: Para estrutura e estilização da página.
    
- **Python (Flask)**: Para lógica de backend e integração com a API de clima.
    
- **API de Clima**: Utilizada para buscar as informações climáticas atuais e futuras.
    
- **Gemini AI**: Parte do projeto para fornecer visualizações mais detalhadas nas previsões estendidas.
    

## Como Funciona o Gemini AI

O **Gemini AI** é descrito no projeto como uma ferramenta adicional para melhorar a experiência do usuário. Sua função seria:

- Realizar análises detalhadas das previsões para os próximos dias.
    
- Exibir insights como “tendências climáticas” e “análises por hora” de forma intuitiva.
    
- Fornecer visualizações gráficas interativas para complementar as informações exibidas.
    

## Estrutura do Projeto

```
/
|-- app.py
|-- /templates
    |-- index.html
```

- **app.py**: Contém a lógica de backend e integrações com a API de clima.
    
- **/templates/index.html**: Contém a estrutura principal da página e inclui estilos CSS embutidos.
    

## Como Executar

1. Clone este repositório:
    
    ```
    git clone <URL_DO_REPOSITORIO>
    ```
    
2. Navegue até o diretório do projeto:
    
    ```
    cd projeto-clima
    ```
    
3. Instale as dependências necessárias:
    
    ```
    pip install -r requirements.txt
    ```
    
4. Inicie o servidor local:
    
    ```
    python app.py
    ```
    
5. Acesse o aplicativo no navegador em `http://localhost:5000`.
     

## Observações

- Certifique-se de que a API de clima esteja configurada corretamente para funcionar com o endpoint esperado no arquivo `app.py`.
    
- Validar a KEY e endpoint utilizada do Gemini AI, pois a mesma é de uso único e imutável.
    

## Captura de Tela (Opcional)

- Dando inicio ao servidor e realizando requisições de previsão.
![image](https://github.com/user-attachments/assets/8023dcee-5810-4d30-b98c-f84e7f80c07a)

- Page inicial da página
![image](https://github.com/user-attachments/assets/1de3690a-ffe2-4190-a57a-fc0fd67a09e9)

- Realizando busca, onde vai mostrar a do dia referente a API Weather e prolongada de 5 dias posteriores onde é trabalhada pelo GeminiAI.
![image](https://github.com/user-attachments/assets/100e8bb1-6c9f-421c-a85a-db1f533e327b)
![image](https://github.com/user-attachments/assets/9e41ded9-bfd5-4334-871b-024b51ed34aa)

- Também possui tratamento de dados inválidos
![image](https://github.com/user-attachments/assets/ae099b1b-3683-43e7-ac5e-26bbf5f6aac4)
