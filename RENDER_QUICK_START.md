# ?? Быстрая инструкция по деплою FunPayCardinal на Render.com

## ? У вас уже есть:
- ? Настроенный конфиг `configs/_main.cfg` с Golden Key
- ? Telegram Bot Token в конфиге
- ? Все файлы проекта

## ?? Что нужно сделать:

### Шаг 1: Загрузить проект на GitHub

1. Создайте новый репозиторий на [GitHub.com](https://github.com/new)
2. Загрузите ВСЕ файлы проекта в репозиторий (включая папку `configs` с вашим настроенным `_main.cfg`)

**Важно:** Убедитесь, что эти файлы есть в корне:
- `main.py`
- `requirements.txt`
- `Procfile`
- `runtime.txt`
- `start.sh`
- папка `configs/` с файлом `_main.cfg`

### Шаг 2: Создать сервис на Render.com

1. Зайдите на [Render.com](https://render.com) и войдите/зарегистрируйтесь
2. Нажмите **"New +"** ? **"Background Worker"**
3. Подключите ваш GitHub репозиторий
4. Выберите созданный репозиторий

### Шаг 3: Настроить сервис

Заполните поля:

#### Основные настройки:
```
Name: funpay-cardinal
Environment: Python 3
Region: Frankfurt (EU Central) или любой другой
Branch: main
Build Command: pip install -r requirements.txt
Start Command: bash start.sh
```

#### Выбор плана:
- **Free** - 750 часов/месяц (бот будет засыпать при неактивности)
- **Starter** ($7/мес) - РЕКОМЕНДУЕТСЯ для постоянной работы

### Шаг 4: Environment Variables (необязательно)

Добавьте только эти переменные (остальное уже в конфиге):

```bash
PYTHONUNBUFFERED=1
FPC_IS_RUNNIG_AS_SERVICE=1
```

### Шаг 5: Запуск

1. Нажмите **"Create Background Worker"**
2. Render начнет установку зависимостей и запуск бота
3. Следите за логами во вкладке **"Logs"**

### Шаг 6: Проверка работы

1. Откройте вашего Telegram бота (токен из конфига)
2. Отправьте команду `/start`
3. Проверьте, что бот отвечает

## ?? Проверка логов на Render

После запуска проверьте логи:
- Должны увидеть ASCII-арт логотип FunPay Cardinal
- Сообщение "Авторизация прошла успешно"
- Информацию о балансе и лотах

## ?? Важные моменты

### 1. **Golden Key и Telegram Token**
Ваш `_main.cfg` уже содержит:
```
golden_key: nza87nro4lkl9txlflxuvheag1qz4f2n
token: 8579372707:AAGKCHieEi6PHKA3Ot9D6S0H1E5fJFhMkDk
```

?? **ВНИМАНИЕ:** Эти токены видны в репозитории! Рекомендации:
- Сделайте репозиторий **приватным** на GitHub
- Или вынесите токены в переменные окружения (см. раздел ниже)

### 2. **Free план Render**
- Сервис засыпает после 15 минут без HTTP-запросов
- Для круглосуточной работы нужен Starter план ($7/мес)

### 3. **Хранение данных**
- Логи и файлы хранятся только между перезапусками
- При полном редеплое данные теряются
- База пользователей и настройки сохраняются в `storage/`

## ?? (Опционально) Безопасность: вынос токенов в переменные окружения

Если хотите убрать токены из конфига:

### 1. Измените `configs/_main.cfg`:
```ini
[FunPay]
golden_key : ${FUNPAY_GOLDEN_KEY}
...

[Telegram]
token : ${TELEGRAM_BOT_TOKEN}
...
```

### 2. Добавьте переменные на Render:
```bash
FUNPAY_GOLDEN_KEY=nza87nro4lkl9txlflxuvheag1qz4f2n
TELEGRAM_BOT_TOKEN=8579372707:AAGKCHieEi6PHKA3Ot9D6S0H1E5fJFhMkDk
```

### 3. Создайте файл `load_env_config.py`:
```python
import os
import configparser

config = configparser.ConfigParser()
config.read('configs/_main.cfg', encoding='utf-8')

# Заменяем переменные окружения
for section in config.sections():
    for key, value in config[section].items():
        if value.startswith('${') and value.endswith('}'):
            env_var = value[2:-1]
            env_value = os.getenv(env_var, '')
            if env_value:
                config[section][key] = env_value

with open('configs/_main.cfg', 'w', encoding='utf-8') as f:
    config.write(f)
```

### 4. Обновите `start.sh`:
```bash
#!/bin/bash

mkdir -p configs logs storage/cache storage/plugins storage/products plugins
touch configs/auto_delivery.cfg
touch configs/auto_response.cfg

# Загрузка переменных окружения в конфиг
python load_env_config.py

export FPC_IS_RUNNIG_AS_SERVICE=1
export PYTHONUNBUFFERED=1

echo "?? Starting FunPay Cardinal..."
exec python main.py
```

## ?? Типичные проблемы

### Проблема: "ModuleNotFoundError"
**Решение:** Проверьте, что `requirements.txt` присутствует и Build Command = `pip install -r requirements.txt`

### Проблема: Бот не отвечает в Telegram
**Решение:** 
1. Проверьте логи на Render
2. Убедитесь, что Telegram Token правильный
3. Проверьте, что бот не заблокирован в Telegram

### Проблема: "golden_key invalid"
**Решение:**
1. Получите новый Golden Key на FunPay
2. Обновите `configs/_main.cfg` в репозитории
3. Сделайте новый деплой

### Проблема: Сервис постоянно перезапускается
**Решение:** Проверьте логи на критические ошибки. Возможно:
- Неверный Golden Key
- Проблемы с сетью
- Нехватка памяти (перейдите на Starter план)

## ?? Полезные команды Telegram бота

После запуска используйте в Telegram:
- `/start` - Запуск бота
- `/menu` - Главное меню управления
- `/balance` - Проверка баланса FunPay
- `/lots` - Управление лотами
- `/help` - Справка

## ?? Обновление бота

Для обновления кода:
1. Внесите изменения в GitHub репозиторий
2. Render автоматически обнаружит и задеплоит изменения
3. Или вручную: **Manual Deploy** ? **Deploy latest commit**

## ?? Мониторинг

На Render доступны:
- **Logs** - Все логи в реальном времени
- **Metrics** - CPU, память, время работы
- **Events** - История деплоев и ошибок

## ?? Помощь

- [Telegram чат FunPay Cardinal](https://t.me/funpay_cardinal)
- [Официальный репозиторий](https://github.com/sidor0912/FunPayCardinal)
- [Документация Render](https://render.com/docs/background-workers)

---

## ? Чеклист перед деплоем:

- [ ] Репозиторий на GitHub создан (приватный!)
- [ ] Все файлы загружены (включая `configs/_main.cfg`)
- [ ] Файлы `Procfile`, `runtime.txt`, `start.sh` в корне
- [ ] Сервис Background Worker создан на Render
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `bash start.sh`
- [ ] План выбран (Free или Starter)
- [ ] Деплой запущен
- [ ] Логи проверены на ошибки
- [ ] Telegram бот отвечает на `/start`

**Готово! Ваш FunPay Cardinal работает на Render.com! ??**
