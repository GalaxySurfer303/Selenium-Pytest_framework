import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")  # Jedna instancja WebDrivera na całą sesję testową
def driver():
    # Konfiguracja opcji dla Chrome
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Włączenie trybu incognito
    chrome_options.add_argument("--start-maximized")  # Maksymalizacja okna przeglądarki
    chrome_options.add_argument("--disable-popup-blocking")  # Opcjonalnie: wyłącz blokowanie wyskakujących okien

    # Inicjalizacja WebDrivera z opcjami
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)  # Implicit wait dla stabilności testów

    yield driver  # Udostępnij WebDriver do testów
    driver.quit()  # Zamknij WebDriver po zakończeniu sesji

