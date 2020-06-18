from subprocess import CalledProcessError
from subprocess import check_output as run

MYPY_COMMAND = "mypy"

MYPY_INPUTS = ["app.py", "api"]


def pytest_generate_tests(metafunc):
    metafunc.parametrize("folder", MYPY_INPUTS)


def test_mypy(folder):
    """ Run project files files through mypy """
    try:
        run([MYPY_COMMAND, folder])
    except CalledProcessError as e:
        raise AssertionError("mypy has found errors.\n\n" +
                             e.output.decode("utf-8"))
    except OSError:
        raise OSError(
            "Failed to run mypy. Please check that"
            "you have installed it properly."
        )
