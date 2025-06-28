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
        
        # Calcula quantos blocos de zero precisam ser inseridos
        # Um IPv6 completo tem 8 blocos.
        num_zeros = 8 - (len(blocos_esquerda) + len(blocos_direita))
        
        # Cria os blocos de zeros e junta tudo
        blocos_zeros = ['0000'] * num_zeros
        partes_expandidas = blocos_esquerda + blocos_zeros + blocos_direita
    else:
        # Se não há '::', apenas separamos os blocos existentes
        partes_expandidas = endereco_ipv6.split(':')
        
    return partes_expandidas


