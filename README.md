# Projeto final de dados - Curso de Análise de dados - CEPEDI

Nesta pasta estão os arquivos relacionados ao projeto final do curso de análise
de dados usando Python, pelo prof. Breno Otsuka através da CEPEDI.

# Integrantes

- João Pedro Rocha
- Mateus Barbosa

# Estrutura de pastas

Foi usada a estrutura padrão:

```
.
├── datasets
│   └── heart\_attack
│       ├── heart\_attack\_data\_set.pkl
│       └── raw
│           ├── description.md
│           └── heart\_attack\_data\_set.csv
├── environment.yml
├── notebooks
│   ├── edas
│   │   ├── eda\_joaopedro\_heart-attack.ipynb
│   │   ├── \_\_init\_\_.py
│   │   └── tools
│   │       ├── \_\_init\_\_.py
│   │       └── standard\_pipeline.py
│   ├── models.ipynb
│   └── report.ipynb
├── outputs
│   └── best\_model.pkl
└── README.md
```

## Pastas

- datasets: contém os dados brutos e processados usados no projeto.
- notebooks: cadernos jupyter do projeto
- notebooks/edas: analises exploratórias individuais
- notebooks/edas/tools: pacote contendo funcionalidades para o processamento de dados (para ajudar nos cadernos)
- outputs: saídas

## Arquivos

- environment.yml: ambiente virtual utilizado com o conda
- notebooks/models.ipynb: carderno com os experimentos com os modelos
- notebooks/report.ipynb: caderno com a eda combinada
- outputs/best\_model.ipynb: modelo final salvo como pickle
