from task_manager.task import Task, Priority
from task_manager.repository import TaskRepository
from datetime import datetime
def test_save_atribui_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc",Priority.BAIXA, datetime.now())
    resultado = repo.save(task)
    assert resultado.id == 1
    mock_storage.add.assert_called_once()
def test_save_chama_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc",Priority.BAIXA, datetime.now())
    resultado = repo.save(task)
    assert task == resultado
def test_find_id_chama_storage_get(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc",Priority.BAIXA, datetime.now())
    resultado = repo.save(task)
    assert repo.find_by_id(resultado.id) == resultado
def test_find_all_retorna_lista(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc",Priority.BAIXA, datetime.now())
    resultado = repo.save(task)
    assert type(repo.find_all()) == list
    

    