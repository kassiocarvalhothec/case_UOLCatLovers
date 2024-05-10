SELECT *
FROM `seu_projeto.seu_dataset.cat_facts`
WHERE dh_update BETWEEN TIMESTAMP('2020-08-01') AND TIMESTAMP('2020-08-31 23:59:59');
