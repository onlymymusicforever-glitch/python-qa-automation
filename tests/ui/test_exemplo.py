def validar_status(codigo):
    if codigo in [200, 201]:
        return "Pass"
    else:
        return "Fail"
    
    
def test_validar_status_200():
    assert validar_status(200) == "Pass"

def test_validar_status_201():
    assert validar_status(201) == "Pass"

def test_validar_status_404():
    assert validar_status(404) == "Fail"    