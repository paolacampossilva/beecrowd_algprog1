import collections
import queue
while True:
    try:
        casos = int(input())
        entrada = collections.deque()
        fila = collections.deque()
        fila_prioridade = queue.PriorityQueue()
        stack = queue_ = priority_queue = True
        estrutura = ""
        for n in range(casos):
            comando, item = map(int,input().split())
            if comando == 1:
                if stack:
                    entrada.append(item)
                if queue_:
                    fila.append(item)
                if priority_queue:
                    fila_prioridade.put(-item)
            else:
                if stack:
                    if len(entrada) == 0 or entrada[-1] != item:
                        stack = False
                    else:
                        entrada.pop()
                if queue_:
                    if len(fila) == 0 or fila[0] != item:
                        queue_ = False
                    else:
                        fila.popleft()
                if priority_queue and (fila_prioridade.empty() or fila_prioridade.get() != -item):
                    priority_queue = False
        verificador = 0
        if stack:
            estrutura = "stack"
            verificador = verificador + 1
        if queue_:
            estrutura = "queue"
            verificador = verificador + 1
        if priority_queue:
            estrutura = "priority queue"
            verificador = verificador + 1
        if verificador == 0:
            estrutura = "impossible"
        if verificador > 1:
            estrutura = "not sure"
        print(estrutura)
    except EOFError:
        break
