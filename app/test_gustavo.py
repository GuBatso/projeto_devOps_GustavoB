from app import app


def test_aluno_devolve_dupla_gustavob():
    dados = app.test_client().get("/aluno").get_json()
    assert dados["dupla"] == "gustavob"