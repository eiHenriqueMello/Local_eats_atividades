# Responsável: Henrique Mello
import pytest
from src.regras_localeats import avaliacao_valida

def test_avaliacao_valida_dentro_do_intervalo():
    # Teste para comportamento válido/esperado
    assert avaliacao_valida(4) is True
    assert avaliacao_valida(1) is True
    assert avaliacao_valida(5) is True

def test_avaliacao_invalida_fora_do_intervalo():
    # Teste para limite ou comportamento inválido
    assert avaliacao_valida(0) is False
    assert avaliacao_valida(6) is False