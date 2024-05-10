

SELECT texto, dh_criacao, dh_update
FROM `seu_projeto.seu_dataset.cat_facts`
ORDER BY RAND()
LIMIT 100;

/* APÓS RODAR A QUERY
PARA SALVAR VIA TERMINAL DO BQ, BASTA APENAS CLICAR NA OPÇAO DE SALVAR 
E DEPOIS EXPORTAR PARA UM CSV.
*/


EXPORT DATA OPTIONS(
  uri='gs://seu_bucket/nome_do_arquivo.csv',
  format='CSV',
  overwrite=true
) AS
SELECT texto, dh_criacao, dh_update
FROM `seu_projeto.seu_dataset.cat_facts`
ORDER BY RAND()
LIMIT 100;

/* SE CASO QUERIAM UMA QUERY QUE EXPORT AUTOMATICAMENTE APÓS A EXECUÇÃO, PODERÍAMOS MOSTRAR
A OPÇÃO DO EXPORT.
APÓS RODAR A QUERY
O ARQUIVO CSV IRÁ AUTOMATICAMENTE PARA O BUCKET INFERENCIADO NO EXPORT.
*/