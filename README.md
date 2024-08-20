# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите зависимости этой командой

```sh
    pip install -r requirements.txt
```
или
```sh
    python -m pip install -r requirements.txt
```
- Создайте файл с напитками по примеру ниже
- Запустите сайт командой, где path это путь до файла с напитками

```sh
    python main.py -f path
```

- Откройте в браузере полученый index.html

## Пример файла с напитками
```sh
# Белые вина


Название: Белая леди

Сорт: Дамский пальчик

Цена: 399

Картинка: images/belaya_ledi.png

Выгодное предложение
```

## Таблица с винами

| Категория    | Название             | Сорт            | Цена | Картинка                 | Акция                |
|--------------|----------------------|-----------------|------|--------------------------|----------------------|
| Белые вина   | Белая леди           | Дамский пальчик | 399  | belaya_ledi.png          | Выгодное предложение |
| Напитки      | Коньяк классический  |                 | 350  | konyak_klassicheskyi.png |                      |
| Белые вина   | Ркацители            | Ркацители       | 499  | rkaciteli.png            |                      |
| Красные вина | Черный лекарь        | Качич           | 399  | chernyi_lekar.png        |                      |
| Красные вина | Хванчкара            | Александраули   | 550  | hvanchkara.png           |                      |
| Белые вина   | Кокур                | Кокур           | 450  | kokur.png                |                      |
| Красные вина | Киндзмараули         | Саперави        | 550  | kindzmarauli.png         |                      |
| Напитки      | Чача                 |                 | 299  | chacha.png               | Выгодное предложение |
| Напитки      | Коньяк кизиловый     |                 | 350  | konyak_kizilovyi.png     |                      |

Таблица с винами можно [тут](https://lyl.su/EADQ).

Эта таблица нужна для отрисовки самого сайта. Без неё на сайте не будет карточек с винами. Все 5 значения нужно указывать, кроме сорта в напитках.

## Проверь итоговый результат

На сайте должен быть указан правильно, как на картинке:

![картинка](https://dvmn.org/media/business_age.png)

Как должен выглядеть сайт в общем:

![картинка](https://dvmn.org/media/lesson_1_separate_to_types.png)

Как должны выглядеть карточки из раздела Напитки:

![картинка](https://dvmn.org/media/lesson_1_brandies.png)

Как должны выглядеть карточки с выгодным предложением или с самой низкой ценой:

![картинка](https://dvmn.org/media/lesson1_cheapest_wine_card.png)

Как должны выглядеть карточки из разделов Красные вина и Белые вина:

![картинка](https://dvmn.org/media/lesson_1_add_two_wine_cards.png)

**`Между ними должны находится разделы, как на картинке:`**

![картинка](https://dvmn.org/media/lesson_1_separate_to_types.png)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
