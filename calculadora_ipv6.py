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
