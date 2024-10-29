import asyncio
import random
import time

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

def main():
    asyncio.run(coroutine_task_01())

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(coroutine_task_01())
    # loop.close()

if __name__ == '__main__':
    main()