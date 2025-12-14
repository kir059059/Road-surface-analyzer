Програмный анализатор качества дорожного покрытия - это модуль на машину, который с помощью бинокулярного зрения строит карту высот по данным о расстоянии между дорогой и камерами.

Что бы запустить программу вам потребуется 2 камеры, подключенные к компьютеру и установленные библиотеки opencv и matplot

Что бы их установить нужно:

1. Создать виртуальное окружение
2. 
python -m venv venv

3. Активировать его
   
venv\Scripts\activate # Windows

source venv/bin/activate # Linux

Если выводит ошибку:
.\venv\Scripts\activate : Невозможно загрузить файл C:\path\venv\Scripts\activate.ps1, так как выполнение сценариев отключено в этой системе. 
Для получения дополнительных сведений см. about_Execution_Policies по адресу http://go.microsoft.com/fwlink/?LinkID=135170.
строка:1 знак:1
.\venv\Scripts\activate

CategoryInfo          : Ошибка безопасности: (:) [], PSSecurityException
FullyQualifiedErrorId : UnauthorizedAccess

То вот решение проблемы:
- Открываем терминал PowerShell от админа.
- Вставляем и запускаем - Set-ExecutionPolicy RemoteSigned
- На вопрос отвечаем - A

3. Прописать в терминал среды разработки
pip install opencv-python matplot
