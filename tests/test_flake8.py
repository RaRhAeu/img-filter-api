from subprocess import CalledProcessError
from subprocess import check_output as run

FLAKE8_COMMAND = "flake8"

FLAKE8_INPUTS = ["app.py", "api", "tests"]


def pytest_generate_tests(metafunc):
    metafunc.parametrize("folder", FLAKE8_INPUTS)


def test_flake8(folder):
    """ Run project files files through flake8 """
    try:
        run([FLAKE8_COMMAND, folder])
    except CalledProcessError as e:
        raise AssertionError("flake8 has found errors.\n\n" +
                             e.output.decode("utf-8"))
    except OSError:
        raise OSError(
            "Failed to run flake8. Please check that"
            " you have installed it properly."
        )
