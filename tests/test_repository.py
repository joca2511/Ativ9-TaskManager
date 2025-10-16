from task_manager.task import Task, Priority, Status
from task_manager.repository import TaskRepository
from datetime import datetime

def test_save_atribui_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc", Priority.BAIXA, Status.PENDENTE, datetime.now())
    
    resultado = repo.save(task)
    
    assert resultado.id == 1
    mock_storage.add.assert_called_once()

def test_save_chama_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc", Priority.BAIXA, Status.PENDENTE, datetime.now())
    
    resultado = repo.save(task)
    
    assert task == resultado

def test_find_id_chama_storage_get(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    
    task = Task(None, "Teste", "Desc", Priority.BAIXA, Status.PENDENTE, datetime.now())
    task_com_id = repo.save(task)
    
    mock_storage.get.return_value = task_com_id
    
    resultado = repo.find_by_id(task_com_id.id)
    
    mock_storage.get.assert_called_once_with(task_com_id.id)
    assert resultado == task_com_id

def test_find_all_retorna_lista(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    
    mock_storage.get_all.return_value = []
    
    resultado = repo.find_all()
    
    mock_storage.get_all.assert_called_once()
    assert isinstance(resultado, list)
