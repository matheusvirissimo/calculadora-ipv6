#biblioteca built-in do Python.
import random

def expandir_ipv6(endereco_ipv6):
    """Expande um endereço IPv6, possivelmente abreviado, para sua forma completa

    Esta função lida com a abreviação '::', preenchendo-a com o número
    correto de blocos de zeros para que o endereço tenha sempre 8 blocos.

    Parâmetros
    ----------
    endereco_ipv6 : str
        O endereço IPv6 a ser expandido. Pode estar em formato completo
        ou abreviado (ex: "2801:390::ff00" ou "::1").

    Retorna
    -------
    list
        Uma lista contendo os 8 blocos (hextetos) do endereço IPv6 expandido.
        Ex: ['2801', '0390', '0000', '0000', '0000', '0000', '0000', 'ff00']
    """
    # Se '::' estiver no endereço, ele está abreviado e precisa ser expandido
    if "::" in endereco_ipv6:
        # Divide o endereço em duas partes, antes e depois de '::'
        parte_esquerda, parte_direita = endereco_ipv6.split('::')
        
        # Filtra blocos vazios que podem surgir se '::' estiver no início ou fim
        blocos_esquerda = [bloco for bloco in parte_esquerda.split(':') if bloco]
        blocos_direita = [bloco for bloco in parte_direita.split(':') if bloco]
        
        # Calcula quantos blocos de zero precisam ser inseridos (IPv6 completo tem 8 blocos)
        num_zeros = 8 - (len(blocos_esquerda) + len(blocos_direita))
        
        # Cria os blocos de zeros e junta tudo
        blocos_zeros = ['0000'] * num_zeros
        partes_expandidas = blocos_esquerda + blocos_zeros + blocos_direita
    else:
        # Se não há '::', já está expandindo, então apenas separamos os blocos existentes
        partes_expandidas = endereco_ipv6.split(':')
        
    return partes_expandidas

def normalizar_ipv6(endereco_ipv6):
    """Normaliza um endereço IPv6 para sua representação completa de 8 blocos de 4 dígitos.

    Primeiro, expande o endereço para garantir que tenha 8 blocos, e depois
    preenche cada bloco com zeros à esquerda (leftmost) até que tenha 4 dígitos

    Parâmetros
    ----------
    endereco_ipv6 : str
        O endereço IPv6, em qualquer formato válido

    Retorna
    -------
    list
        Uma lista de 8 strings, onde cada string é um bloco de 4 dígitos HEXADECIMAIS
        Ex: ['2801', '0390', '0080', '0000', '0100', '0000', '0000', 'ff00']
    """

    # Garante que o endereço está expandido para 8 blocos
    partes_expandidas = expandir_ipv6(endereco_ipv6)

    # Lista que armazena o resultado final normalizado
    partes_normalizadas = []
    
    # Iterar sobre cada bloco do endereço expandido
    for parte in partes_expandidas:
        bloco_normalizado = parte.zfill(4) # zfill() - Preenche o bloco com zeros à esquerda até atingir 4 caracteres
        partes_normalizadas.append(bloco_normalizado)
        
    return partes_normalizadas

def abreviar_ipv6(partes_normalizadas):
    """Abrevia um endereço IPv6 normalizado de acordo com as regras da RFC 4193

    Esta função implementa três regras de abreviação:
    1. Remove zeros à esquerda de cada bloco
    2. Encontra a maior sequência de blocos de zero e a substitui por '::'
    3. Não comete ambiguidade

    Parâmetros
    ----------
    partes_normalizadas : list
        Uma lista com os 8 blocos de 4 dígitos de um endereço IPv6

    Retorna
    -------
    str
        O endereço IPv6 abreviado.
        Ex: "2801:390:80:0:100::ff00"
    """
    # Encontrar a maior sequência de blocos de zero ('0000')
    maior_sequencia_inicio = -1
    maior_sequencia_tamanho = 0
    sequencia_atual_inicio = -1
    sequencia_atual_tamanho = 0

    # Itera pelos blocos para encontrar a sequência mais longa de '0000'
    for i, parte in enumerate(partes_normalizadas):
        if parte == '0000':
            if sequencia_atual_tamanho == 0:
                sequencia_atual_inicio = i
            sequencia_atual_tamanho += 1
        else:
            if sequencia_atual_tamanho > maior_sequencia_tamanho:
                maior_sequencia_tamanho = sequencia_atual_tamanho
                maior_sequencia_inicio = sequencia_atual_inicio
            sequencia_atual_tamanho = 0
    
    # Verifica a última sequência após o loop terminar
    if sequencia_atual_tamanho > maior_sequencia_tamanho:
        maior_sequencia_tamanho = sequencia_atual_tamanho
        maior_sequencia_inicio = sequencia_atual_inicio

    # Remove os zeros à esquerda de cada bloco
    # Ex: '0390' vira '390', '0000' vira '0'
    partes_sem_zeros_esquerda = [parte.lstrip('0') or '0' for parte in partes_normalizadas]

    # Se encontramos uma sequência de zeros com mais de 1 bloco, aplicamos a regra '::'
    if maior_sequencia_tamanho > 1:
        inicio = maior_sequencia_inicio
        fim = inicio + maior_sequencia_tamanho
        
        # Monta o endereço abreviado
        parte_esquerda = partes_sem_zeros_esquerda[:inicio]
        parte_direita = partes_sem_zeros_esquerda[fim:]
        
        # Junta as partes com '::' no meio
        # A lógica `"::".join([...])` lida com casos onde uma das partes é vazia
        # Ex: ::1 (parte_esquerda é vazia) ou 1:: (parte_direita é vazia)
        endereco_abreviado = ":".join(parte_esquerda) + "::" + ":".join(parte_direita)
    else:
        # Se não há sequência de zeros para abreviar, apenas juntamos com ':'
        endereco_abreviado = ":".join(partes_sem_zeros_esquerda)
        
    return endereco_abreviado

def gerar_ipv6_aleatorio():
    """Gera um endereço IPv6 totalmente aleatório

    Cada endereço IPv6 é formado por 8 blocos de 4 dígitos, totalizando 16 bits por bloco.
    Cria 8 blocos, cada um sendo um número hexadecimal aleatório de 4 dígitos

    Parâmetros
    ----------
    Nenhum.

    Retorna
    -------
    str
        Um endereço IPv6 completo e aleatório.
        Ex: "a1b2:c3d4:e5f6:1234:5678:90ab:cdef:1a2b"
    """
    # Lista para guardar os 8 blocos do nosso IPv6
    partes_aleatorias = []
    
    # Um endereço IPv6 tem 8 blocos
    for _ in range(8):
        # Gera um número aleatório entre 0 e 65535 (que é FFFF em hexadecimal)
        bloco_decimal = random.randint(0, 65535)
        
        # Converte o número para hexadecimal e formata para ter 4 dígitos
        # Ex: 255 -> 'ff' -> '00ff'
        bloco_hex = format(bloco_decimal, 'x').zfill(4)
        partes_aleatorias.append(bloco_hex)
    
    # Junta todos os blocos com ':' para formar o endereço completo
    return ":".join(partes_aleatorias)