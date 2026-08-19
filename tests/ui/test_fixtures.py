import pytest
import tests.ui.test_exemplo as test_exemplo

from tests.ui.test_exemplo import validar_status

@pytest.fixture
def codigos_exemplo():
    return [200, 404, 201, 500]

def test_lista_tem_quatro_codigos(codigos_exemplo):
    assert len(codigos_exemplo) == 4

  

def test_todos_os_status_sao_validos(respostas_api):
    for resposta in respostas_api:
        codigo = resposta["status"]
        assert codigo in [200, 201, 404, 500]



@pytest.mark.parametrize("codigo, esperado", [
    (200, "Pass"),
    (201, "Pass"),
    (404, "Fail"),
    (500, "Fail"),
])
def test_validar_status(codigo, esperado):
    assert validar_status(codigo) == esperado




def test_validar_status_com_mensagem():
    resultado = validar_status(999)
    assert resultado == "Pass", f"Esperava Pass para o codigo 999, mas recebi {resultado}"