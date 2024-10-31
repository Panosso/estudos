#Biblioteca que permite a programção assincrona no python
import asyncio
import random

#Funcao assincrona
async def sum(a, b):
    return a+b

#Await: Indica para o código que a task assyncrona seja executada nesse momento.
async def print_sum(a, b):
    result = await sum(a, b)
    print(f'Resultado igual a: {result}')

#Result sem o await retorna esse obj.
# <coroutine object sum at 0x000001D105D2CAC0>
coro = sum(2, 3)
print(coro)

#Event Loop: Basicamente, ele que orquestra e executa as tarefas assincronas.
event_loop = asyncio.new_event_loop()

#Nesse momento pedimos ou event loop que execute as nossas funções assyncronas
result1 = event_loop.run_until_complete(coro)
event_loop.run_until_complete(print_sum(2, 3))
print(result1)


#Mais exemplos
async def coroutine_task(iteraction):

    print(f'Iniciando a task: {iteraction}')
    process_time = random.randint(1, 10)
    await asyncio.sleep(process_time)
    print(f'Iteracao {iteraction}, tempo ocorrido: {process_time}')

async def coroutine_task_01():

    tasks = []

    for iteraction in range(10):
        #Criação das tasks
        tasks.append(asyncio.create_task(coroutine_task(iteraction)))

    #Execução das tasks
    print('Vou iniciar as tasks')
    await asyncio.gather(*tasks)
    print('Finalizei todas as task')

async def coroutine_task_02():

    for interaction in range(10):
        task = asyncio.ensure_future(coroutine_task(interaction))
        await task

asyncio.run(coroutine_task_01())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine_task_01())
# loop.close()