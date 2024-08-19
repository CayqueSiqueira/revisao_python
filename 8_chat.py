# o python os possui as ferramentas
# os.getcwd() #retorna o diretório atual
# os.chdir() #muda o diretório atual
# os.listdir() #retorna uma lista com os arquivos do diretório atual
# os.mkdir() #cria um diretório
# os.rmdir() #remove um diretório
# os.remove() #remove um arquivo
# os.rename() #renomeia um arquivo
# os.path.exists() #verifica se um arquivo ou diretório existe
# os.path.isfile() #verifica se é um arquivo
# os.path.isdir() #verifica se é um diretório
# os.path.join() #junta dois caminhos
# os.path.split() #separa o caminho do arquivo
# os.path.splitext() #separa o nome do arquivo da extensão
# os.path.getsize() #retorna o tamanho de um arquivo
# os.path.abspath() #retorna o caminho absoluto
# os.path.basename() #retorna o nome do arquivo
# os.path.dirname() #retorna o caminho do arquivo
# os.path.isabs() #verifica se é um caminho absoluto
# os.path.relpath() #retorna o caminho relativo
# os.path.commonpath() #retorna o caminho comum
# os.path.commonprefix() #retorna o prefixo comum
# os.path.normpath() #normaliza o caminho
# os.path.normcase() #normaliza o caminho
# os.path.expanduser() #expande o caminho
# os.path.expandvars() #expande as variáveis de ambiente
# os.path.samefile() #verifica se é o mesmo arquivo
# os.path.sameopenfile() #verifica se é o mesmo arquivo aberto
# os.path.samestat() #verifica se é o mesmo arquivo aberto
# os.path.realpath() #retorna o caminho real
# os.path.relpath() #retorna o caminho relativo
# os.path.walk() #percorre o caminho
# os.path.walktree() #percorre a árvore de diretórios
# os.path.walkfiles() #percorre os arquivos
# os.path.walkdirs() #percorre os diretórios
# os.path.walk() #percorre o caminho


import os

mensagens = []

nome = input("Nome: ")

while True:

    #limpa o termianl
    os.system("cls")

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_________________________")

    #obtendo texto
    texto = input("Mensagem: ")
    if texto == "sair":
        break

    #adicionando a mensagem
    mensagens.append({
        'nome': nome,
        'texto': texto
    })