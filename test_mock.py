import pytest
from unittest.mock import Mock


class Posts:
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body


class ExcecaoPostNaoEncontrado(Exception):
    pass


@pytest.fixture
def post():
    p1 = Posts(1, 1, 'A busca por algo', 'O plot nunca achamos nada')
    return p1


@pytest.fixture
def todosPosts():
    p1 = Posts(1, 1, 'A busca por algo', 'O plot nunca achamos nada')
    p2 = Posts(2, 2, 'Algo não achado', 'Encontramos algo que não era achado')
    todos = [p1, p2]
    return todos


def test_busca_por_id(post):
    listaPosts = Mock()
    listaPosts.obter_post.return_value = post
    resultado = listaPosts.obter_post(1)
    print(resultado)

    assert resultado.title == 'A busca por algo'
    assert resultado.userId == 1


def test_id_nao_existe(post):
    listaPosts = Mock()
    listaPosts.obter_post.side_effect = ExcecaoPostNaoEncontrado

    with pytest.raises(ExcecaoPostNaoEncontrado):
        listaPosts.obter_post(3)


def testi_retorna_tudo(todosPosts):
    listaTposto = Mock()
    listaTposto.obter_todos.return_value = todosPosts
    resultado = listaTposto.obter_todos()

    assert len(resultado) == 2
    assert resultado[0].id == 1
    assert resultado[1].id == 2
    assert resultado[0].body == 'O plot nunca achamos nada'
    assert resultado[1].body == 'Encontramos algo que não era achado'
