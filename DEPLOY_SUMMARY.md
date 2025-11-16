# ?? ИТОГОВАЯ ИНСТРУКЦИЯ: Деплой на Render.com

## ?? Что уже готово у вас:
? Проект FunPayCardinal настроен  
? `configs/_main.cfg` с Golden Key и Telegram Token  
? Все зависимости в `requirements.txt`  

## ?? Новые файлы созданы:
? `Procfile` - указывает Render как запускать бот  
? `runtime.txt` - версия Python  
? `start.sh` - скрипт запуска  
? `RENDER_QUICK_START.md` - подробная инструкция  
? `.gitignore.render` - правильный gitignore для Render  

---

## ?? 3 ПРОСТЫХ ШАГА ДЛЯ ДЕПЛОЯ:

### ШАГ 1: Подготовка GitHub репозитория

```bash
# 1. Переименуйте .gitignore (чтобы configs попал в репозиторий)
переименуйте .gitignore в .gitignore.old
переименуйте .gitignore.render в .gitignore

# 2. Создайте репозиторий на GitHub (ОБЯЗАТЕЛЬНО ПРИВАТНЫЙ!)
# Зайдите на https://github.com/new
# Создайте PRIVATE репозиторий с именем funpay-cardinal

# 3. Загрузите все файлы в репозиторий
git init
git add .
git commit -m "Initial commit for Render deployment"
git branch -M main
git remote add origin https://github.com/ВАШ_USERNAME/funpay-cardinal.git
git push -u origin main
```

**Или просто через GitHub Desktop / веб-интерфейс загрузите все файлы**

---

### ШАГ 2: Создание сервиса на Render.com

1. Зайдите на https://render.com
2. Зарегистрируйтесь / войдите
3. Нажмите **"New +"** ? **"Background Worker"**
4. Подключите GitHub (если не подключен)
5. Выберите ваш репозиторий `funpay-cardinal`

**Настройки сервиса:**
```
Name: funpay-cardinal
Environment: Python 3
Region: Frankfurt (EU Central)
Branch: main

Build Command:
pip install -r requirements.txt

Start Command:
bash start.sh

Instance Type:
? Free (для теста, но бот будет засыпать)
  или
? Starter - $7/мес (РЕКОМЕНДУЕТСЯ для 24/7 работы)
```

**Environment Variables (добавьте 2 переменные):**
```
PYTHONUNBUFFERED = 1
FPC_IS_RUNNIG_AS_SERVICE = 1
```

6. Нажмите **"Create Background Worker"**

---

### ШАГ 3: Проверка работы

1. **Следите за логами** во вкладке "Logs" на Render
2. Дождитесь сообщений:
   ```
   ?? Creating directories...
   ?? Ensuring config files exist...
   ?? Starting FunPay Cardinal...
   [ASCII логотип]
   Авторизация прошла успешно!
   ```

3. **Проверьте Telegram бота:**
   - Найдите бота по токену: `8579372707:AAGKCHieEi6PHKA3Ot9D6S0H1E5fJFhMkDk`
   - Отправьте `/start`
   - Должен ответить!

---

## ?? ВАЖНО: Безопасность

Ваш `configs/_main.cfg` содержит:
- **Golden Key**: `nza87nro4lkl9txlflxuvheag1qz4f2n`
- **Telegram Token**: `8579372707:AAGKCHieEi6PHKA3Ot9D6S0H1E5fJFhMkDk`

?? **ОБЯЗАТЕЛЬНО сделайте репозиторий ПРИВАТНЫМ на GitHub!**

---

## ?? Что делать при проблемах?

### Бот не запускается:
1. Проверьте логи на Render
2. Убедитесь, что все файлы загружены
3. Проверьте Build Command и Start Command

### Бот не отвечает в Telegram:
1. Проверьте, что сервис запущен (зелёная галочка на Render)
2. Посмотрите логи - нет ли ошибок авторизации
3. Убедитесь, что Telegram Token правильный

### "ModuleNotFoundError":
- Build Command должна быть: `pip install -r requirements.txt`

---

## ?? Дополнительные ресурсы:

- ?? Подробная инструкция: `RENDER_QUICK_START.md`
- ?? Telegram чат поддержки: https://t.me/funpay_cardinal
- ?? GitHub проекта: https://github.com/sidor0912/FunPayCardinal

---

## ? Контрольный список:

- [ ] Создан ПРИВАТНЫЙ репозиторий на GitHub
- [ ] Все файлы загружены (включая configs/_main.cfg)
- [ ] Файлы Procfile, runtime.txt, start.sh в корне
- [ ] Создан Background Worker на Render
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `bash start.sh`
- [ ] Environment Variables добавлены
- [ ] Сервис запущен (зелёная галочка)
- [ ] Логи без критических ошибок
- [ ] Telegram бот отвечает на /start

---

## ?? Готово!

Ваш FunPay Cardinal работает на Render.com в облаке 24/7!

**Команды для управления в Telegram:**
- `/start` - Запуск
- `/menu` - Главное меню
- `/balance` - Баланс FunPay
- `/help` - Помощь

Удачи! ??
