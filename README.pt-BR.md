# NeruBrain

Kit inicial reprodutível para morfologia neuronal: consulta direta aos metadados do NeuroMorpho.org, arquivos SWC padronizados com proveniência por registro, leitor SWC sem dependências, resumos, testes e notebook. O código é MIT; os dados mantêm suas próprias licenças e atribuições.

## Dados incluídos

`data/raw/` contém uma amostra limitada (até 50) de neurônios humanos com correspondência de tipo piramidal, em formato **CNG SWC padronizado pelo NeuroMorpho.org**, acompanhada de metadados. Não são os arquivos originais enviados pelos laboratórios. Cada JSON lateral/manifesto registra o registro da API, URL e SHA-256. Leia [proveniência](docs/DATA_PROVENANCE.md) e [metodologia](docs/METHODOLOGY.md), e confirme termos e citações antes de reutilizar.

## Uso rápido (Python 3.10+)

Sem dependências de execução. Nesta pasta:

```sh
PYTHONPATH=src python examples/quickstart.py
PYTHONPATH=src python -m nerubrain.cli data/raw --output data/processed/morphology_summary.csv
PYTHONPATH=src python -m unittest discover -s tests -v
```

Os testes também funcionam com pytest se ele já estiver disponível; não é dependência do projeto.

Para atualizar dados, com acesso à internet:

```sh
PYTHONPATH=src python -m nerubrain.dataset --root . --limit 50 --species human --cell-type pyramidal --pause 0.5
```

O resumo calcula contagens, limites por eixo e soma de distâncias euclidianas pai-filho nas unidades originais. É uma ferramenta básica, não um pipeline científico validado.

## Licença e atribuição

Código: MIT (`LICENSE`). Os dados do NeuroMorpho.org são regidos por seus termos e atribuições das fontes; eles não são relicenciados sob MIT. Cite NeuroMorpho.org e os artigos/autores aplicáveis. Detalhes: `docs/DATA_PROVENANCE.md`.
