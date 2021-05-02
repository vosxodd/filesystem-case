# Case-study #10
# Developers:   Aksenov A. (35%),
#               Soloveychik D. (40%),
#               Labuzov A. (46%)

def runCommand(command):
    """
    Определяет по номеру команды command, какую функцию следует выполнить.
    """
def acceptCommand():
    """
    Запрашивает номер команды и в случае если номер команды указан некорректно, выводит сообщение об ошибке. Запрос команд осуществляется до тех пор, пока не введен корректный номер команды. Возвращает корректный номеркоманды.
    """
    a=0
    n=input("Введите номер команды: )
    while a==0:
        try:
            n=int(n)
            break
        except ValueError:
            n=input("Неверный номер команды. Повторите ввод: ")
def moveUp():
    """
    Делает текущим родительский каталог.
    """
def moveDown(currentDir):
    """
    Запрашивает имя подкаталога. Если имя указано корректно делает каталог находящийся в currentDir текущим, иначе выводит сообщение об ошибке.
    """
def countFiles(path):
    """
    Рекурсивная функция подсчитывающая количество файлов в указанном каталоге path. В подсчет включаются все файлы, находящиеся в подкаталогах. Возвращает количество файлов.
    """
def countBytes(path):
    """
    Рекурсивная функция подсчитывающая суммарный объем (в байтах) всех файлов в указанном каталоге path. В подсчет включаются все файлы, находящиеся в подкаталогах. Возвращает суммарное количество байт.
    """
def findFiles(target, path):
    """
    Рекурсивная функция, формирующая список путей к файлам, в имени которых содержится target. В поиск включаются все подкаталоги каталога path. В случае если файлы не найдены, выводит соответствующее сообщение.
    """
def main():
    """
    Основная программа, которая выводит путь к текущему каталогу и меню. Вызывает функцию выполнения команд.
    """
