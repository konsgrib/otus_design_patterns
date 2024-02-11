Домашнее задание
Создал сласс EventLoop с очередью событий, возможностью обавления новых и выполнения существующих заданий.
В блоке обработки исключений добавлена логика вывода сообщения об ошибке в лог, в случае, если команда не может быть выполнена более двух раз.
```python
                ExceptionHandler(cmd, e).handle()
                if isinstance(cmd, DoubleRepeatedCommand):
                    print("Double Repeated Command failed writing to the log...")
                    logger_cmd = LoggerCommand(cmd, e)
                    self.add(logger_cmd)
                elif isinstance(cmd, RepeaterCommand):
                    print("Repeated Command failed, creating double...")
                    double_repeated_cmd = DoubleRepeatedCommand(cmd)
                    self.add(double_repeated_cmd)
                else:
                    print("Creating repeater for the command failed first time...")
                    repeater_cmd = RepeaterCommand(cmd)
                    self.add(repeater_cmd)
```
В классе ExceptionHandler в переменной _exceptions содержатся обработчики событий для известных классов и типов ошибок. Исползуя команду add_handler можно добавить новые обработчики. Сохранения на диск не делал, т.к. не требуется по ТЗ
Пункт 8 задания перекрылся пунктом 9, но если нужно- могу отатить, чтобы и это показать.

Тесты находятся в файле test_command.py, test_event_loop.py test_main.py

Добавил тесты для проверки работы команд и обработки исключений.
Также в файле command созданы классы LoggerCommand, RepeaterCommand, DoubleRepeatedCommand

