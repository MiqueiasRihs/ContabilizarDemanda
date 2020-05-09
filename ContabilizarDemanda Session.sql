

delete FROM app_produtos where id in (30, 31, 32, 33, 34, 35, 36);
COMMIT;


SELECT * FROM app_produtos;

INSERT INTO app_produtos(id,nome,marca,tamanho,quantidade,tipo) VALUES (01,"Old Skool", "Vans", "34", 1, "C");
INSERT INTO app_produtos(id,nome,marca,tamanho,quantidade,tipo) VALUES (02,"Moletom Supreme", "Supreme", "G", 2, "V");
INSERT INTO app_produtos(id,nome,marca,tamanho,quantidade,tipo) VALUES (03,"CAMISETA PRISON STRIPE WHITE", "Prison", "M", 1, "V");
INSERT INTO app_produtos(id,nome,marca,tamanho,quantidade,tipo) VALUES (04,"CAMISETA PRISON NOTORIOUS JUYCE", "Prison", "P", 1, "V");
INSERT INTO app_produtos(id,nome,marca,tamanho,quantidade,tipo) VALUES (05,"BONÉ ADIDAS ORIGINALS", "ADIDAS", "P", 1, "A");
INSERT INTO app_produtos(id,nome,marca,tamanho,quantidade,tipo) VALUES (06,"MOLETOM ADIDAS CREW NAVY", "ADIDAS", "P", 1, "V");
INSERT INTO app_produtos(id,nome,marca,tamanho,quantidade,tipo) VALUES (07,"TENIS VIBE CREW DARK", "Vibe", "42", 1, "C");
INSERT INTO app_produtos(nome,marca,tamanho,quantidade,tipo) VALUES ("RELÓGIO VINTAGE DOURADO", "CASIO", "P", 1, "A");
COMMIT;