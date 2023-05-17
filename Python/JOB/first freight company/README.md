# Решение задания

### Описание задачи:
Нам требовалось создать сервис (функцию api_call), который получает список вагонов из сервиса дислокации, формирует список накладных тех вагонов, у которых отсутствует дата прибытия, отправляет этот список в сервис предсказания даты прибытия, у всех вагонов без даты прибытия выставляет предсказанную дату прибытия и возвращает список с обновленными данными.

### Решение
```
@timing
def api_call():
    locations = get_current_dislocation()

    # Сформировать список уникальных накладных из текущей дислокации только по тем вагонам,
    # у которых arrivale_date = None
    invoices = list({loc["invoice"] for loc in locations if loc["arrivale_date"] is None})

    predicted_data = get_predicted_date_by_invoices(invoices)

    # Создать словарь для быстрого доступа к предсказанным датам
    predicted_dates_dict = {data["invoice"]: data["predicted_date"] for data in predicted_data}

    # Обновить оригинальный список вагонов данными, которые прислал сервис get_predicted_dates().
    # Заменить вагоны, где arrivale_date = None на соответствующее поле predicted_date.
    for loc in locations:
        if loc["arrivale_date"] is None:
            loc["arrivale_date"] = predicted_dates_dict.get(loc["invoice"], None)

    return locations

```



