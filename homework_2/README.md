##Определение абстракций, устойчивых к изменениям требований.

###Описание рвботы

Создан абстрактный класс FlyingObject, имплементирующий в себе общую логику летающих объектов
За повороты и прямолинейное движение отвечяют дополнительные классы Mover и Rotator
Классы SpaceShip и Torpedo являются наследниками FlyingObject


###Тесты

Создан набор юнит тестов, проверяющий различные ситуации с движением и поворотом объектов

###Изменения

В случае изменения требований к движению объектов, достаточно будет изменить только классы Mover и Rotator, оставив без изменений классы FlyingObject, SpaceShip и Torpedo

Тестирование происходит сатоматически с использованием GitActions.