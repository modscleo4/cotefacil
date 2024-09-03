# Prova Técnica Desenvolvedor Python - CoteFácil
Repositório criado para armazenar a solução do desafio proposto pela CoteFácil.

## Instruções para execução
### Questão 1
Para executar a questão 1, basta gerar a imagem Docker e executar o container:
```bash
cd Questao1
docker build -t questao1 .
docker run -e LOGIN=12345678 -e PASSWORD=senha123 questao1
```

### Questão 2
Para executar a questão 2, basta gerar a imagem Docker e executar o container:
```bash
cd Questao2
docker build -t questao2 .
docker run -e LOGIN=login@exemplo.com -e PASSWORD=senha123 questao2 [numero-pedido]
```

### Questão 5
Para executar a questão 5, basta executar o arquivo `tests.py`:
```bash
cd Questao5
python tests.py
```

### Questão 7
Para executar a questão 7, basta gerar a imagem Docker e executar o container:
```bash
cd Questao7
docker build -t questao7 .
docker run questao7
```

## Observações
- A questão 1 não tem o login implementado por conta do reCAPTCHA.
- A questão 3 não foi implementada por não ser mais possível acessar o site.
