import time


def test_product_page_has_add_to_basket_button(browser):
    # Открываем страницу товара
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    # Пауза для визуальной проверки языка кнопки (требование задания)
    time.sleep(30)

    # Ищем кнопку добавления в корзину по уникальному селектору
    add_to_basket_button = browser.find_element(
        'css selector', 'button.btn-add-to-basket'
    )

    # Проверяем, что кнопка существует и видна
    assert add_to_basket_button is not None, \
        'Кнопка добавления в корзину не найдена на странице товара'