# Анализ изменений: Генерация сверхмассивных черных дыр (Supermassive Black Holes)

## Обзор
Был добавлен новый класс `SupermassiveBlackHole`, который представляет сверхмассивную черную дыру.
Также в класс `Galaxy` был добавлен метод `generate_supermassive_black_holes`, позволяющий процедурно генерировать сверхмассивные черные дыры.
Написан соответствующий тест в `tests/test_galaxy.py`, который подтверждает корректность создания объектов и их атрибутов.

## Выполненные задачи
- Добавлен класс `SupermassiveBlackHole`
- Добавлен атрибут `supermassive_black_holes` в конструктор `Galaxy`
- Реализован метод `generate_supermassive_black_holes` для класса `Galaxy`
- Написан изолированный тест `test_supermassive_black_hole_generation`
- Обновлены `agents.md` и `CHANGELOG.md`
