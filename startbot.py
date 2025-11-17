import subprocess
import sys
import os
import time
import logging

def install_dependencies():
    """Устанавливает зависимости из requirements.txt"""
    print("📦 Устанавливаю зависимости...")
    
    try:
        # Обновляем pip
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # Устанавливаем зависимости
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ Зависимости установлены успешно")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка установки зависимостей: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def run_cardinal():
    """Запускает main.py в фоновом режиме"""
    
    if not os.path.exists("main.py"):
        print("❌ Файл main.py не найден")
        return False
    
    print("🚀 Запускаю Cardinal...")
    
    try:
        # Для Linux/Mac
        if sys.platform in ["linux", "linux2", "darwin"]:
            process = subprocess.Popen(
                [sys.executable, "main.py"],
                stdout=open("cardinal.log", "w"),
                stderr=subprocess.STDOUT,
                preexec_fn=os.setsid
            )
        # Для Windows
        else:
            process = subprocess.Popen(
                [sys.executable, "main.py"],
                stdout=open("cardinal.log", "w"),
                stderr=subprocess.STDOUT,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        
        # Сохраняем PID для возможности остановки
        with open("cardinal.pid", "w") as f:
            f.write(str(process.pid))
        
        print(f"✅ Cardinal запущен в фоне (PID: {process.pid})")
        print("📝 Логи записываются в cardinal.log")
        print("❌ Этот скрипт можно закрывать")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка запуска Cardinal: {e}")
        return False

def main():
    """Основная функция"""
    print("=" * 50)
    print("🎯 FunPay Cardinal Launcher")
    print("=" * 50)
    
    # Устанавливаем зависимости
    if not install_dependencies():
        print("❌ Не удалось установить зависимости. Выход...")
        time.sleep(5)
        sys.exit(1)
    
    # Запускаем бота
    if not run_cardinal():
        print("❌ Не удалось запустить Cardinal. Выход...")
        time.sleep(5)
        sys.exit(1)
    
    # Проверяем, что процесс запустился
    time.sleep(3)
    if os.path.exists("cardinal.pid"):
        with open("cardinal.pid", "r") as f:
            pid = f.read().strip()
        print(f"🔍 Проверка: Cardinal работает с PID {pid}")
    else:
        print("⚠️  Предупреждение: PID файл не создан")

if __name__ == "__main__":
    main()
