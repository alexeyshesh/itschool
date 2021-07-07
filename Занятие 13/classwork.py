# На занятии обсуждались основы асинхронного программирования и параллельной
# обработки данных. Для лучшего понимания рекомендуется посмотреть запись занятия

# Пример асинхронных функция: одна печатает числа, другая выводит, сколько прошло
# времени. Как сделать так, чтобы они работали одновременно?

import asyncio  # библиотека, необходимая для асинхронной работы


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.2)  # функция сообщает, что сейчас она спит


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        await asyncio.sleep(1)  # аналогично print_nums


async def main():
    task1 = asyncio.create_task(print_nums())  # создаем task - задачу, которая 
                                               # будет крутиться в очереди
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)  # формируем очередь


if __name__ == '__main__':
    asyncio.run(main())  # запускаем