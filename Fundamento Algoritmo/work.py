import os # Importar módulo para manipulação de arquivos e diretórios
CODIGO_ADMIN = "ICEFLIXADM" # Constante para o código secreto de cadastro de administrador
def menu_principal(): # Função para exibir o menu principal do programa
    while True: # Loop principal do programa
        print("\n=== BEM VINDO AO ICEFLIX ===")
        print("1 - Cadastrar usuário")
        print("2 - Login usuário")
        print("3 - Cadastrar administrador")
        print("4 - Login administrador")
        print("5 - Sair")
        Resp = input("Escolha: ")
        if Resp == "1":
            cadastrar_usuario()
        elif Resp == "2":
            usuario = login_usuario()
            if usuario:
                menu_usuario(usuario)
        elif Resp == "3":
            cadastrar_admin()
        elif Resp == "4":
            if login_admin():
                menu_admin()
        elif Resp == "5":
            print("Saindo...")
            break # Encerrar o loop e sair do programa
        else:
            print("Opção inválida!")
def cadastrar_usuario():
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    if os.path.exists("usuarios.txt"): # Verificar se o arquivo de usuários já existe
        arquivo = open("usuarios.txt", "r") # Verificar se o usuário já existe
        for linha in arquivo:
            n, s = linha.strip().split(";") # Separar nome e senha
            if nome == n:
                print("Usuário já existe!")
                arquivo.close()
                return
        arquivo.close()
    arquivo = open("usuarios.txt", "a") # Abrir arquivo para adicionar novo usuário
    arquivo.write(nome + ";" + senha + "\n") # Escrever nome e senha no arquivo
    arquivo.close()
    print("Usuário cadastrado com sucesso!")
def login_usuario():
    nome = input("Nome: ")
    senha = input("Senha: ")
    if not os.path.exists("usuarios.txt"): # Verificar se o arquivo de usuários existe
        print("Nenhum usuário cadastrado.")
        return False # Retorna False se não houver usuários cadastrados para evitar erro ao tentar ler o arquivo
    arquivo = open("usuarios.txt", "r") # Abrir arquivo para leitura e verificar se o nome e senha correspondem a algum usuário cadastrado
    for linha in arquivo:
        n, s = linha.strip().split(";") # Separar nome e senha
        if nome == n and senha == s:
            print("Login realizado com sucesso!")
            arquivo.close()
            return nome # Retorna o nome do usuário logado para usar em outras funções
    arquivo.close()
    print("Nome ou senha incorretos!")
    return False
def menu_usuario(usuario):
    while True:
        print("\n=== MENU USUÁRIO ===")
        print("1 - Ver vídeos")
        print("2 - Buscar vídeo")
        print("3 - Curtir vídeo")
        print("4 - Descurtir vídeo")
        print("5 - Gerenciar favoritos")
        print("6 - Voltar")
        Resp = input("Escolha: ")
        if Resp == "1":
             ver_videos()
        elif Resp == "2":
            buscar_video()
        elif Resp == "3":
            curtir_video()
        elif Resp == "4":
            descurtir_video()
        elif Resp == "5":
            menu_favoritos(usuario)
        elif Resp == "6":
            break
        else:
            print("Opção inválida!")
def ver_videos():
    if not os.path.exists("videos.txt"):
        print("Nenhum vídeo cadastrado.")
        return
    arquivo = open("videos.txt", "r") # Abrir arquivo para leitura
    print("\n=== VÍDEOS ===")
    for linha in arquivo:
        nome, tipo, curtidas = linha.strip().split(";") # Separar nome, tipo e curtidas
        print("Nome:", nome)
        print("Tipo:", tipo)
        print("Curtidas:", curtidas)
        print()
    arquivo.close()
def buscar_video():
    busca = input("Digite o nome do vídeo: ").lower() # Converter busca para minúsculas para comparação
    if not os.path.exists("videos.txt"):
        print("Nenhum vídeo cadastrado.")
        return
    arquivo = open("videos.txt", "r")
    encontrado = False # Variável para verificar se o vídeo foi encontrado
    for linha in arquivo:
        nome, tipo, curtidas = linha.strip().split(";") # Separar nome, tipo e curtidas
        if busca in nome.lower():
            print("\nVídeo encontrado!")
            print("Nome:", nome)
            print("Tipo:", tipo)
            print("Curtidas:", curtidas)
            encontrado = True
    arquivo.close()
    if not encontrado:
        print("Vídeo não encontrado.")
def curtir_video():
    if not os.path.exists("videos.txt"):
        print("Nenhum vídeo cadastrado.")
        return
    video = input("Digite o nome do vídeo: ")
    arquivo = open("videos.txt", "r") # Abrir arquivo para leitura
    linhas = arquivo.readlines() # Ler todas as linhas do arquivo e armazenar em uma lista
    arquivo.close()
    arquivo = open("videos.txt", "w") # Abrir arquivo para escrita (sobrescreve o conteúdo)
    encontrado = False # Variável para verificar se o vídeo foi encontrado
    for linha in linhas:
        nome, tipo, curtidas = linha.strip().split(";") # Separar nome, tipo e curtidas
        if nome == video:
            curtidas = int(curtidas) + 1
            arquivo.write(nome + ";" + tipo + ";" + str(curtidas) + "\n") # Escrever a linha atualizada com mais uma curtida
            encontrado = True
        else:
            arquivo.write(linha)
    arquivo.close()
    if encontrado:
        print("Vídeo curtido!")
    else:
        print("Vídeo não encontrado!")
def descurtir_video():
    if not os.path.exists("videos.txt"):
        print("Nenhum vídeo cadastrado.")
        return
    video = input("Digite o nome do vídeo: ")
    arquivo = open("videos.txt", "r") # Abrir arquivo para leitura
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open("videos.txt", "w")
    encontrado = False
    for linha in linhas:
        nome, tipo, curtidas = linha.strip().split(";")
        if nome == video:
            curtidas = int(curtidas) # Converter curtidas para inteiro
            if curtidas > 0:
               curtidas -= 1 # Diminuir uma curtida, mas não deixar negativo
            arquivo.write(nome + ";" + tipo + ";" + str(curtidas) + "\n") # Escrever a linha atualizada com uma curtida a menos
            encontrado = True # Marcar que o vídeo foi encontrado
        else:
            arquivo.write(linha)
    arquivo.close()
    if encontrado:
        print("Vídeo descurtido!")
    else:
        print("Vídeo não encontrado!")
def menu_favoritos(usuario):
    while True:
        print("\n=== FAVORITOS ===")
        print("1 - Criar lista")
        print("2 - Ver lista")
        print("3 - Adicionar vídeo")
        print("4 - Remover vídeo")
        print("5 - Excluir lista")
        print("6 - Voltar")
        Resp = input("Escolha: ")
        if Resp == "1":
            criar_lista(usuario)
        elif Resp == "2":
            ver_lista(usuario)
        elif Resp == "3":
            adicionar_video_lista(usuario)
        elif Resp == "4":
            remover_video_lista(usuario)
        elif Resp == "5":
            excluir_lista(usuario)
        elif Resp == "6":
            break
        else:
            print("Opção inválida!")
def criar_lista(usuario):
    nome_lista = input("Nome da lista: ")
    arquivo = open(usuario + "_" + nome_lista + ".txt", "w") # Criar um arquivo para a lista de favoritos do usuário
    arquivo.close()
    print("Lista criada!")
def ver_lista(usuario):
    nome_lista = input("Nome da lista: ")
    nome_arquivo = usuario + "_" + nome_lista + ".txt" # Construir o nome do arquivo da lista de favoritos do usuário
    if not os.path.exists(nome_arquivo):
        print("Lista não encontrada.")
        return
    arquivo = open(nome_arquivo, "r") # Abrir o arquivo da lista para leitura
    print("\n=== LISTA ===")
    for linha in arquivo:
        print(linha.strip()) # Imprimir cada vídeo da lista, removendo espaços em branco
    arquivo.close()
def adicionar_video_lista(usuario):
    nome_lista = input("Nome da lista: ")
    nome_arquivo = usuario + "_" + nome_lista + ".txt" # Construir o nome do arquivo da lista de favoritos do usuário
    if not os.path.exists(nome_arquivo):
        print("Lista não encontrada.")
        return
    video = input("Nome do vídeo: ")
    arquivo = open(nome_arquivo, "a") # Abrir o arquivo da lista para adição
    arquivo.write(video + "\n")
    arquivo.close()
    print("Vídeo adicionado!")
def remover_video_lista(usuario):
    nome_lista = input("Nome da lista: ")
    nome_arquivo = usuario + "_" + nome_lista + ".txt"
    if not os.path.exists(nome_arquivo):
        print("Lista não encontrada.")
        return
    remover = input("Nome do vídeo: ")
    arquivo = open(nome_arquivo, "r") # Abrir o arquivo da lista para leitura
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open(nome_arquivo, "w") # Abrir o arquivo da lista para escrita (sobrescreve o conteúdo)
    for linha in linhas:
        if linha.strip() != remover: # Escrever apenas as linhas que não correspondem ao vídeo a ser removido
            arquivo.write(linha)
    arquivo.close()
    print("Vídeo removido!")
def excluir_lista(usuario):
    nome_lista = input("Nome da lista: ")
    nome_arquivo = usuario + "_" + nome_lista + ".txt"
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print("Lista excluída!")
    else:
        print("Lista não encontrada.")
def cadastrar_admin():
    codigo = input("Digite o código secreto: ")
    if codigo != CODIGO_ADMIN:
        print("Código incorreto!")
        return
    nome = input("Digite o nome do admin: ")
    senha = input("Digite a senha: ")
    if os.path.exists("admin.txt"):
        arquivo = open("admin.txt", "r")
        for linha in arquivo:
            n, s = linha.strip().split(";")
            if nome == n:
                print("Administrador já existe!")
                arquivo.close()
                return
        arquivo.close()
    arquivo = open("admin.txt", "a")
    arquivo.write(nome + ";" + senha + "\n")
    arquivo.close()
    print("Administrador cadastrado com sucesso!")
def login_admin():
    nome = input("Admin: ")
    senha = input("Senha: ")
    if not os.path.exists("admin.txt"):
        print("Nenhum administrador cadastrado.")
        return False
    arquivo = open("admin.txt", "r")
    for linha in arquivo:
        n, s = linha.strip().split(";")
        if nome == n and senha == s:
            print("Login admin realizado!")
            arquivo.close()
            return True
    arquivo.close()
    print("Dados incorretos!")
    return False # Retorna False se o login falhar
def menu_admin():
    while True:
        print("\n=== MENU ADMINISTRADOR ===")
        print("1 - Cadastrar vídeo")
        print("2 - Excluir vídeo")
        print("3 - Consultar usuários")
        print("4 - Visualizar estatísticas")
        print("5 - Voltar")
        Resp = input("Escolha: ")
        if Resp == "1":
            cadastrar_video()
        elif Resp == "2":
            excluir_video()
        elif Resp == "3":
            consultar_usuarios()
        elif Resp == "4":
            visualizar_estatisticas()
        elif Resp == "5":
            break
        else:
            print("Opção inválida!")
def cadastrar_video():
    nome = input("Nome do vídeo: ")
    tipo = input("Tipo (filme/série): ")
    arquivo = open("videos.txt", "a")
    arquivo.write(nome + ";" + tipo + ";0\n") # Escrever nome, tipo e 0 curtidas no arquivo
    arquivo.close()
    print("Vídeo cadastrado!")
def excluir_video():
    if not os.path.exists("videos.txt"):
        print("Nenhum vídeo cadastrado.")
        return
    excluir = input("Nome do vídeo: ")
    arquivo = open("videos.txt", "r") # Abrir arquivo para leitura
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open("videos.txt", "w") # Abrir arquivo para escrita (sobrescreve o conteúdo)
    encontrado = False # Variável para verificar se o vídeo foi encontrado e excluído
    for linha in linhas:
        nome, tipo, curtidas = linha.strip().split(";")
        if nome != excluir:
            arquivo.write(linha)
        else:
               encontrado = True
    arquivo.close()
    if encontrado:
        print("Vídeo excluído!")
    else:
        print("Vídeo não encontrado!")
def consultar_usuarios():
    if not os.path.exists("usuarios.txt"):
        print("Nenhum usuário cadastrado.")
        return
    arquivo = open("usuarios.txt", "r") # Abrir arquivo para leitura
    print("\n=== USUÁRIOS ===") # Imprimir título da seção de usuários
    for linha in arquivo:
        nome, senha = linha.strip().split(";")
        print(nome)
    arquivo.close()
def visualizar_estatisticas():
    total_usuarios = 0 # Variável para contar o total de usuários
    total_videos = 0
    videos = []
    if os.path.exists("usuarios.txt"):
        arquivo = open("usuarios.txt", "r")
        for linha in arquivo:
            total_usuarios += 1 # Incrementar o contador de usuários para cada linha do arquivo
        arquivo.close()
    if os.path.exists("videos.txt"):
        arquivo = open("videos.txt", "r")
        for linha in arquivo:
            total_videos += 1
            nome, tipo, curtidas = linha.strip().split(";")
            videos.append((nome, int(curtidas))) # Adicionar tupla (nome, curtidas) à lista de vídeos
        arquivo.close()
    print("\n=== ESTATÍSTICAS ===")
    print("Total de usuários:", total_usuarios)
    print("Total de vídeos:", total_videos)
    videos.sort(key=lambda x: x[1], reverse=True) # Ordenar a lista de vídeos por curtidas em ordem decrescente
    print("\nTOP 5 MAIS CURTIDOS:")
    top = 0 # Variável para contar quantos vídeos já foram exibidos no top 5
    for video in videos:
        print(video[0], "-", video[1], "curtidas")
        top += 1
        if top == 5:
            break
menu_principal()