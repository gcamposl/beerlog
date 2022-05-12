from beerlog.cli import main
from typer.testing import CliRunner

runner = CliRunner()


def test_add_beer():
    """
        Teste funcional pode ter mais de um assert
        Imita sempre a usabilidade do usuário
    """
    result = runner.invoke(
        main,
        ["add", "Skolzinha", "KornIPA", "--flavor=1", "--image=2", "--cost=3"],
    )
    assert result.exit_code == 0
    assert "Beer added!!!" in result.stdout
