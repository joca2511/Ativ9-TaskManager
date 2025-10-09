from enum import IntEnum, Enum
from datetime import datetime
class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"
class Task:
    def __init__(self, id,titulo,descricao,prioridade,status,prazo=None,):
        self.id = int(id)
        self.titulo = str(titulo)
        self.descricao = str(descricao)
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status
    def validar(self,titulo,prazo):
        if len(titulo)<3 or prazo == None:
            raise ValueError()
        
    
    