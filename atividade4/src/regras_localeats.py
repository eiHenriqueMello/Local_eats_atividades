# Responsável: Henrique Mello

def avaliacao_valida(nota):
    """
    Regra 4: Valida a avaliação do restaurante.
    - Notas entre 1 e 5 retornam True.
    - Notas abaixo de 1 retornam False.
    - Notas acima de 5 retornam False.
    """
    if not isinstance(nota, (int, float)):
        raise TypeError("A nota deve ser um número.")
    
    if 1 <= nota <= 5:
        return True
    return False