import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_image_path():
    while True:
        path = input("Введіть шлях до файлу зображення (наприклад, photo.jpg): ").strip()
        if os.path.exists(path):
            return path
        else:
            print(">> Помилка: Файл не знайдено. Спробуйте ще раз.")

def process_image(img_path):
    try:
        with Image.open(img_path) as img:
            print(f"Зображення завантажено. Розмір: {img.size}, Формат: {img.format}")

            img = img.convert("RGB") 
            target_size = (800, 600)
            img = img.resize(target_size)
            print(f">> Зображення змінено до розміру {target_size}")

            print("\nОберіть ефект:")
            print("1 - Розмиття (Blur)")
            print("2 - Підвищення чіткості (Detail)")
            print("3 - Без ефектів")
            choice = input("Ваш вибір (1-3): ")

            if choice == '1':
                img = img.filter(ImageFilter.BLUR)
                print(">> Застосовано фільтр розмиття.")
            elif choice == '2':
                img = img.filter(ImageFilter.DETAIL)
                print(">> Застосовано фільтр чіткості.")

            draw = ImageDraw.Draw(img)
            width, height = img.size

            border_margin = 20
            draw.rectangle(
                [(border_margin, border_margin), (width - border_margin, height - border_margin)],
                outline="red",
                width=5
            )

            user_text = input("\nВведіть текст привітання: ")
            if not user_text:
                user_text = "Вітаємо!" 

            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except IOError:
                print(">> Системний шрифт не знайдено, використовується стандартний.")
                font = ImageFont.load_default()

            bbox = draw.textbbox((0, 0), user_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            x = (width - text_width) / 2
            y = (height - text_height) / 2

            draw.text((x + 2, y + 2), user_text, font=font, fill="black")
            draw.text((x, y), user_text, font=font, fill="white")
            print(">> Текст додано.")

            out_filename = input("\nВведіть ім'я файлу для збереження (наприклад, card.jpg): ").strip()
            if not out_filename:
                out_filename = "result_card.jpg"
            
            if not out_filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                out_filename += ".jpg"

            img.save(out_filename)
            print(f"\n[Успіх] Листівку збережено як '{out_filename}'")

    except OSError as e:
        print(f"\n[Критична помилка] Не вдалося обробити зображення. Деталі: {e}")
    except Exception as e:
        print(f"\n[Помилка] Щось пішло не так: {e}")

def main():
    print("=== Генератор персоналізованих листівок ===")
    image_path = get_image_path()
    process_image(image_path)
    print("=== Роботу програми завершено ===")

if __name__ == "__main__":
    main()