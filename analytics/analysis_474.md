### Analysis 474: `is_carnivorous_plant_predator` Trait Implementation

**Завершенные задачи:**
- Добавлен трейт `is_carnivorous_plant_predator` в класс `Entity` (по умолчанию `False`).
- Реализована логика размножения и мутации данного трейта в методе `Universe.tick()`.
- Добавлен боевой множитель: хищники с этим трейтом получают множитель атаки x1.5 при нападении на сущностей с трейтом `is_carnivorous_plant`.
- Обновлен CLI-визуализатор (`CLIVisualizer`) для отображения сущностей с данным трейтом символом `❀`.
- Написаны изолированные тесты в `tests/test_is_carnivorous_plant_predator.py` для проверки множителя урона, мутации и рендеринга.
- Обновлены файлы `agents.md` и `CHANGELOG.md`.

**Технические детали:**
В `tests/test_is_carnivorous_plant_predator.py` мы временно отключили у тестовых объектов свойства (такие как `is_lucky`, `is_evasive`, `is_clairvoyant`, `is_telekinetic`, `is_ethereal` и др.), которые могли влиять на механику уклонения и защиты, чтобы гарантированно изолировать эффект множителя атаки x1.5 от `is_carnivorous_plant_predator`. Прогонка полного набора тестов (`pytest tests/`) подтвердила отсутствие регрессий.
