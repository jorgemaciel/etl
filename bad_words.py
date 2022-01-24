bad_words = ['INSERT', 'INTO']
# INSERT INTO geren849_ciweb.aluguel_equipamentos (numero,nome,descricao,acessorio,valor_real,valor_dolar,valor_aluguel,valor_alugado,data_aquisicao,data_locacao,data_garantia,tipo_id,situacao_id,fornecedor_id,orgao_id,created_at,updated_at,deleted_at) VALUES

with open('SQL/aluguel_equipamentos_202201151156.sql') as oldfile, open('SQL/equipamentos_clean.sql', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)

