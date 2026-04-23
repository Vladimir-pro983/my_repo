
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # 1. Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        wait = WebDriverWait(driver, 20)

        # 2. Дождаться загрузки ВСЕХ картинок.
        #    Здесь мы считаем, что все картинки загружены,
        #    когда в DOM появилось не меньше 4 тегов <img>.
        wait.until(
            lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4
        )

        # 3. После ожидания ещё раз получаем список всех картинок
        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"Картинок на странице после загрузки: {len(images)}")

        # 4. Берём 3-ю картинку (индекс 2)
        third_image = images[2]

        # 5. Читаем значение атрибута src и выводим в консоль
        src_value = third_image.get_attribute("src")
        print(src_value)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
