import requests
import pytest

@pytest.fixture
def chamada_api(request):
    url = request.param
    return requests.get(url, timeout=5)


@pytest.mark.api
@pytest.mark.parametrize("chamada_api", [
    "https://jsonplaceholder.typicode.com/posts/1"
], indirect=True)
def test_devolve_200(chamada_api):
    assert chamada_api.status_code == 200

@pytest.mark.api
@pytest.mark.parametrize("chamada_api", [
    "https://jsonplaceholder.typicode.com/posts/1"
], indirect=True)
def test_post1_pertence_ao_utilizador1(chamada_api):
    dados = (chamada_api.json())
    assert dados["userId"] == 1

@pytest.mark.api
@pytest.mark.parametrize("chamada_api", [
    "https://jsonplaceholder.typicode.com/posts/1"
], indirect=True)
def test_post1_tem_titulo(chamada_api):
    dados = (chamada_api.json())
    assert dados ["title"] != ""

@pytest.mark.api
@pytest.mark.parametrize("chamada_api", [
    "https://jsonplaceholder.typicode.com/posts/99999"
], indirect=True)
def test_posts_devolve_404(chamada_api):
    resposta = (chamada_api)
    assert resposta.status_code == 404




@pytest.mark.api
def test_get_com_header_personalizado():
    headers = {"Accept": "application/json"}
    resposta = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers=headers,
        timeout=5
    )
    assert resposta.status_code == 200

@pytest.mark.api
@pytest.mark.parametrize("chamada_api", [
    "https://jsonplaceholder.typicode.com/posts/1"
], indirect=True)
def test_get_id(chamada_api):
    dados = chamada_api.json()
    assert dados["id"] == 1
    assert dados["userId"] == 1



@pytest.mark.api
@pytest.mark.parametrize("chamada_api", [
    "https://jsonplaceholder.typicode.com/posts/1"
], indirect=True)
def test_get_body(chamada_api):
    dados = chamada_api.json()
    print (dados)
    assert "id" in dados
    assert "userId" in dados
    assert "title" in dados
    assert "body" in dados





@pytest.mark.api
def test_post_new_id():
    payload = {"title": "teste", "body": "conteudo", "userId": 1}
    resposta = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload,
        timeout=5
    )
    assert resposta.status_code == 201
    assert "id" in resposta.json()




@pytest.mark.api
def test_put_atualiza_post():
    payload = {"title": "teste", "body": "conteudo", "userId": 1}
    resposta = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=payload,
        timeout=5
    )
    assert resposta.status_code == 200
    assert "id" in resposta.json()



@pytest.mark.api
def test_delete():
    get = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    assert get.status_code == 200
    print (get.status_code)
    resposta = requests.delete("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    assert resposta.status_code == 200








@pytest.mark.api
def test_post_new_id_2():
    payload = {"title": "teste", "body": "conteudo", "userId": 101}
    resposta = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload, timeout=5)
    id_criado = resposta.json()["id"]
    get = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_criado}", timeout=5)
    assert get.status_code == 404
    assert "id" in resposta.json()



@pytest.mark.api
def test_get_100_posts():
    get = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
    get_posts = get.json()
    assert len(get_posts) == 100



@pytest.mark.api
def test_get_posts_user1():
    resposta = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1},
    timeout=5
    )
    get_posts1 = resposta.json()
    assert len(get_posts1) == 10


@pytest.mark.api
def test_timeout_tratado():
    try:
        resposta = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=0.001)
        assert resposta.status_code == 200
    except requests.exceptions.Timeout:
        pytest.fail("API nao respondeu a tempo - timeout")