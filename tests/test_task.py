import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

def test_task_valida():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Estudar", "Python", Priority.ALTA, Status.PENDENTE, prazo)
    
    task.validar(task.titulo, task.prazo)
    
    assert task.titulo == "Estudar"

def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, Status.PENDENTE, prazo)
    
    with pytest.raises(ValueError):
        task.validar(task.titulo, task.prazo)

def test_prazo_passado():
    prazo = datetime.now() - timedelta(days=1) 
    task = Task(None, "Rapaaaaaaiz", "Ta losco", Priority.MEDIA, Status.PENDENTE, prazo)
    
    with pytest.raises(ValueError):
        task.validar(task.titulo, task.prazo)
