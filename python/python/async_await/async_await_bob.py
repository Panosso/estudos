import asyncio
from time import sleep
from datetime import datetime

# class SyncBob:

#     def cook_bread(self):
#         sleep(3)

#     def cook_hamburguer(self):
#         sleep(10)

#     def mount_sanduich(self):
#         sleep(3)

#     def make_milkshake(self):
#         sleep(5)

#     def cook(self):
#         self.cook_bread()
#         self.cook_hamburguer()
#         self.mount_sanduich()
#         self.make_milkshake()

# sync_bob = SyncBob()

# inicio = datetime.now()
# sync_bob.cook()
# fim = datetime.now()
# print(fim - inicio)


#Para usar o sleep em funcoes assincronas é necessário usar o sleep do asyncio
class AsyncBob:

    async def cook_bread(self):
        await asyncio.sleep(3)

    async def cook_hamburguer(self):
        await asyncio.sleep(10)

    async def mount_sanduich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)

    async def make_sanduiche(self):
        await asyncio.gather(self.cook_bread(), self.cook_hamburguer())
        #Foi criado no momento em que as tasks foram executadas
        event_loop = asyncio.get_running_loop()
        #Crio mais uma task dentro do event loop para ser executada
        event_loop.create_task(self.mount_sanduich())

    async def cook(self):
        #Gather: Função que permite que as coroutine sejam engatilhadas para serem executadas.
        await asyncio.gather(self.make_sanduiche(), self.make_milkshake())

async_bob = AsyncBob()

inicio = datetime.now()

#Executa as tasks engatilhadas, e nesse momento é criado também o event_loop
# No nosso exemplo: serão executadas nesse momento as funções engatilhadas no cook e dentre essas funções temos a função make_sanduiche que ao ser executada adiciona a lista de execução de task's a funções mount_sanduich, visto que as funções cook_bread e cook_hamburguer, ja foram executadas e ja tem a resposta pois utilizamos a palavra await, indicando que precisamos esperar essas 2 funções estarem prontas para poder executar a mount_sanduich
asyncio.run(async_bob.cook())

fim = datetime.now()

print(f"Tempo decorrido: {fim - inicio}")