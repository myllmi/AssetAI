KNOW_001 = {
    'description': 'Não foi encontrado target para inserir assinaturas digitalizadas no template.',
    'summary': 'Ao tentar gerar um relatório eu recebo esta mensagem de erro.',
    'solution': 'Verificar se no template do relatório (*.rpt) existe um campo do tito texto com o seguinte conteúdo: #{assinatura}.\n\nEsse campo será substituído pela assinatura digitalizada.',
}

KNOW_002 = {
    'description': 'Response code from TSA server 308 permanent redirect',
    'summary': 'Erro ao tentar gerar o comprovativo de pedido do CESD.',
    'solution': 'Verificar se o MASTER.properties está a apontar para o endereço correto do serv idor de relatórios.\n\n- O endereço correcto é: 127.0.0.1.',
}