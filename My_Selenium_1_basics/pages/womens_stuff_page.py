from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#from selenium.webdriver.common.keys import Keys
#import pytest

#xpath_coockiec_consent = '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/button[1]/p'



class WomensPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url1 = 'https://magento.softwaretestingboard.com/'
        self.main_page_womens_menu_arr_btn = (By.XPATH, '//*[@id="ui-id-4"]/span[1]')
        self.main_page_womens_menu_btn = (By.XPATH, '//*[@id="ui-id-4"]/span[2]')
        self.main_page_womens_bott_menu = (By.XPATH, '//*[@id="ui-id-10"]')
        self.main_page_womens_bott_shrt_menu = (By.XPATH, '//*[@id="ui-id-16"]')

        #parameters style and material
        self.shorts_style_button = (By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[1]')
        self.shorts_style_snug_button = (By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[2]/ol/li[4]/a')
        self.shorts_material_button = (By.XPATH, '//*[@id="narrow-by-list"]/div[6]/div[1]')
        self.shorts_material_org_cotton_button = (By.XPATH, '//*[@id="narrow-by-list"]/div[6]/div[2]/ol/li[7]/a')

        #color check
        self.shorts_erika_run_green = (By.XPATH, '//*[@id="option-label-color-93-item-53"]')
        self.shorts_erika_run_purple = (By.XPATH, '//*[@id="option-label-color-93-item-57"]')

        self.shorts_erika_run_addtocart_btn = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[4]/div/div[1]/form/button/span')

        # erika run shorts detailed site
        self.shorts_erika_run_photo = (By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]')
        self.shorts_erika_run_photo_arr = (By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div')

        self.shorts_erika_run_size_30_btn = (By.XPATH, '//*[@id="option-label-size-143-item-173"]')
        self.shorts_erika_run_red_btn = (By.XPATH, '//*[@id="option-label-color-93-item-58"]')
        self.shorts_erika_run_qty = (By.XPATH, '//*[@id="qty"]')
        self.shorts_erika_run_add_btn = (By.XPATH, '//*[@id="product-addtocart-button"]')

        self.cart_number_button = (By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a/span[2]/span[1]')
        self.view_and_edit_cart_btn = (By.XPATH, '//*[@id="minicart-content-wrapper"]/div[2]/div[5]/div/a/span')

        #================================================================================================================================
        # if adress isn't provided:
        # ===============================================================================================================================
        # self.cart_number_button = (By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a/span[2]/span[1]')
        # self.view_and_edit_cart_btn = (By.XPATH, '//*[@id="minicart-content-wrapper"]/div[2]/div[5]/div/a/span')
        #
        # #proceed to checkout
        # self.proceed_to_checkout_btn = (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/ul/li[1]/button')
        #
        # #adress
        # self.street_adress_field1 = (By.XPATH, '//*[@id="RCSYGD9"]')
        # self.street_adress_field2 = (By.XPATH, '// *[ @ id = "BTJVJ1C"]')
        # self.street_adress_field3 = (By.XPATH, '// *[ @ id = "PI9BHBW"]')
        #
        # pass
        #
        # self.city_field1 = (By.XPATH,
        #
        # self.state_province_list = (By.XPATH)
        # self.zip_postal_field = (By.XPATH)
        #
        # self.country_list = (By.XPATH)
        #
        # self.phone_number_field = (By.XPATH)
        #
        # self.shipping_meth_best = (By.XPATH)
        # self.shipping_meth_flat = (By.XPATH)
        #
        # self.next_button = (By.XPATH)


    def navigate_to_site1(self):
        self.driver.get(self.base_url1)


    def navigate_to_womens_directly(self):
        womens_menu_btn = self.driver.find_element(*self.main_page_womens_menu_btn)
        womens_menu_btn.click()

    def navigate_by_menu_wmn_shorts(self):
        womens_menu_arr_btn = self.driver.find_element(*self.main_page_womens_menu_arr_btn)
        bottom_menu = self.driver.find_element(*self.main_page_womens_bott_menu)
        shorts_menu = self.driver.find_element(*self.main_page_womens_bott_shrt_menu)

        actions = ActionChains(driver=self.driver)
        actions.move_to_element(womens_menu_arr_btn).perform()
        time.sleep(3)
        actions.move_to_element(bottom_menu).perform()
        actions.move_to_element(shorts_menu).perform()
        self.driver.find_element(*self.main_page_womens_bott_shrt_menu).click()
        time.sleep(3)

        self.driver.find_element(*self.shorts_style_button).click()
        time.sleep(2)
        self.driver.find_element(*self.shorts_style_snug_button).click()
        time.sleep(2)
        self.driver.find_element(*self.shorts_material_button).click()
        time.sleep(2)
        self.driver.find_element(*self.shorts_material_org_cotton_button).click()
        time.sleep(2)

        erika_run_green = self.driver.find_element(*self.shorts_erika_run_green)
        time.sleep(2)
        actions.move_to_element(erika_run_green).perform()
        time.sleep(2)
        erika_run_green.click()

        erika_run_purple = self.driver.find_element(*self.shorts_erika_run_purple)
        time.sleep(2.5)
        actions.move_to_element(erika_run_purple).perform()
        time.sleep(1.5)
        erika_run_purple.click()
        time.sleep(2.5)

        self.driver.find_element(*self.shorts_erika_run_addtocart_btn).click()
        self.driver.implicitly_wait(10)

        time.sleep(10)

    def erika_run_shorts_details(self):
        photo = self.driver.find_element(*self.shorts_erika_run_photo)
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(photo).perform()
        time.sleep(2.5)
        photo_arr = self.driver.find_element(*self.shorts_erika_run_photo_arr)
        time.sleep(1)
        actions.move_to_element(photo_arr).perform()
        time.sleep(2)
        photo_arr.click()
        time.sleep(1)
        photo_arr.click()
        time.sleep(2)

        self.driver.find_element(*self.shorts_erika_run_size_30_btn).click()
        time.sleep(2)
        self.driver.find_element(*self.shorts_erika_run_red_btn).click()
        time.sleep(2)

        erika_run_qty = self.driver.find_element(*self.shorts_erika_run_qty)
        erika_run_qty.clear()
        time.sleep(1)
        erika_run_qty.send_keys('3')
        time.sleep(2)
        self.driver.find_element(*self.shorts_erika_run_add_btn).click()
        time.sleep(5)

        self.driver.find_element(*self.cart_number_button).click()
        time.sleep(1.5)
        self.driver.find_element(*self.view_and_edit_cart_btn).click()
        self.driver.implicitly_wait(10)

        #
        # self.driver.find_element(*self.proceed_to_checkout_btn).click
        # self.driver.implicitly_wait(10)
        # time.sleep(3)

        # from selenium.webdriver.common.by import By
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.webdriver.support import expected_conditions as EC

class DiscountCode:
    def __init__(self, driver):
        self.driver = driver

        # Lokalizatory
        self.apply_discount_code_open_shopping_cart = (By.XPATH, '//*[@id="block-discount"]/div[1]')
        self.apply_discount_code_field_shopping_cart = (By.XPATH, '//*[@id="coupon_code"]')
        self.discount_code = '20poff'
        self.apply_discount_code_apply_btn = (By.XPATH, '//*[@id="discount-coupon-form"]/div/div[2]/div/button')
        self.applied_discount_code_confrm_txt = (
            By.XPATH, '//*[@id="cart-totals"]/div/table/tbody/tr[2]/th/span[1]')  # Bez /text()

        # Lokalizator do całkowitej kwoty w koszyku (opcjonalne)
        self.total_amount_txt = (By.XPATH, '//*[@id="cart-totals"]/div/table/tbody/tr[1]/td/span')

    def apply_discount_code(self):
        """
        Otwiera koszyk, wprowadza kod rabatowy i zatwierdza go.
        """
        # Otwórz sekcję z kodem rabatowym
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.apply_discount_code_open_shopping_cart)
        ).click()

        # Wyczyść pole kodu rabatowego i wpisz kod
        discount_code_field_shopping_cart = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.apply_discount_code_field_shopping_cart)
            )
        discount_code_field_shopping_cart.clear()
        discount_code_field_shopping_cart.send_keys(self.discount_code)

        # Zastosuj kod rabatowy
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.apply_discount_code_apply_btn)
        ).click()

    # def get_discount_confirmation_txt(self):
    #     """
    #     Pobiera tekst potwierdzenia po zastosowaniu kodu rabatowego.
    #     """
    #     confirmation_text = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(self.applied_discount_code_confrm_txt)
    #     )
    #     return confirmation_text.text
    #
    # def verify_discount_applied(self, original_price):
    #     """
    #     Sprawdza, czy rabat został poprawnie zastosowany i obniżył cenę o 20%.
    #     """
    #     # Pobierz aktualną kwotę po zastosowaniu rabatu
    #     total_amount_element = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(self.total_amount_txt)
    #     )
    #     total_amount = float(total_amount_element.text.replace('$', ''))
    #
    #     # Oblicz oczekiwaną kwotę po rabacie (20% mniej)
    #     expected_amount = round(original_price * 0.8, 2)
    #
    #     # Porównaj aktualną kwotę z oczekiwaną
    #     assert total_amount == expected_amount, f"Błąd: oczekiwano {expected_amount}, ale otrzymano {total_amount}."
    #     print("Rabat został poprawnie zastosowany!")








        # ================================================================================================================================
        # Shopping Cart:
        # Shipping address provided
        # Discount code applied
        # ===============================================================================================================================

class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver

        # Discount Code Applied !!!

        self.go_get_pushup_grips_add_btn = (By.XPATH, "//div[@class='block crosssell']//div[3]//div[1]//form[1]//button[1]//span[1]")
        self.sprite_foam_yoga_brick_add_btn = (By.XPATH, "//div[@class='block-content content']//div[2]//div[1]//form[1]//button[1]//span[1]")
        #self.quest_lumaflex_band_add_btn = (By.XPATH, '//li[3]//div[1]//div[1]//div[3]//div[1]//form[1]//button[1]//span[1]')



        self.update_shopping_cart_btn = (By.XPATH, '//*[@id="form-validate"]/div[2]/button[2]')

        # self.erika_qty_shopping_cart_field = (By.XPATH, '//*[@id="cart-431978-qty"]')
        # self.go_get_pushup_qty_shopping_cart_field = (By.XPATH, "//input[@data-cart-item-id='24-UG05']")

        self.proceed_to_checkout_btn = (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/ul/li[1]/button/span')

        self.show_order_summary = (By.XPATH, '//*[@id="opc-sidebar"]/div[1]/div/div[1]')
        self.radio_button_bestway = (By.XPATH, '//*[@id="checkout-shipping-method-load"]/table/tbody/tr[1]/td[1]/input')
        self.radio_button_flatrate = (By.XPATH, '//*[@id="checkout-shipping-method-load"]/table/tbody/tr[2]/td[1]/input')
        self.next_button_shipping = (By.XPATH, '//*[@id="shipping-method-buttons-container"]/div/button')

        self.review_order_summary_btn = (By.XPATH, '//*[@id="opc-sidebar"]/div[1]/div/div[1]')
        self.place_to_order_button = (By.XPATH, '//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button/span')


        self.continue_shopping_button = (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div/div/a')




    def shopping_cart_actions(self):

        self.driver.find_element(*self.go_get_pushup_grips_add_btn).click()
        time.sleep(5)
        self.driver.find_element(*self.sprite_foam_yoga_brick_add_btn).click()
        time.sleep(6)
        # quest_lumaflex = self.driver.find_element(*self.quest_lumaflex_band_add_btn)
        # time.sleep(2)
        # quest_lumaflex.click()
        # time.sleep(5)

        # erika_cart_item_qty = self.driver.find_element(*self.erika_qty_shopping_cart_field)
        # time.sleep(2)
        # erika_cart_item_qty.clear()
        # time.sleep(2)
        # erika_cart_item_qty.send_keys('4')  # Zmień ilość na 2
        # time.sleep(2)
        #
        # goget_cart_item_qty = self.driver.find_element(*self.go_get_pushup_qty_shopping_cart_field)
        # time.sleep(2)
        # goget_cart_item_qty.clear()
        # time.sleep(2)
        # goget_cart_item_qty.send_keys('8')
        # time.sleep(2)

        self.driver.find_element(*self.update_shopping_cart_btn).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://magento.softwaretestingboard.com/checkout/cart/")
        )

        print("URL z dostawą załadowany!\n Shiopping section Loaded")

        time.sleep(5)

        self.driver.find_element(*self.proceed_to_checkout_btn).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://magento.softwaretestingboard.com/checkout/#shipping")
        )

        print("URL z platnosciami załadowany!\n Payment section loaded")
        time.sleep(12)


    def shipping_actions(self):

        # Shipping
        # Localize radio button - checked='tablerate_flatrate'

        self.driver.find_element(*self.radio_button_bestway).click()
        time.sleep(4)
        self.driver.find_element(*self.radio_button_flatrate).click()
        time.sleep(4)
        self.driver.find_element(*self.show_order_summary).click()
        time.sleep(5)
        #self.driver.find_element(*self.proceed_to_checkout_btn).click()
        time.sleep(12)

        self.driver.find_element(*self.next_button_shipping).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://magento.softwaretestingboard.com/checkout/#payment")
        )

        print("URL z platnosciami załadowany!\n Payment section loaded")
        time.sleep(12)

        order_summary_rev_btn = self.driver.find_element(*self.review_order_summary_btn)
        time.sleep(2)
        order_summary_rev_btn.click()
        time.sleep(2)
        order_summary_rev_btn.click()
        time.sleep(4)
        order_button = self.driver.find_element(*self.place_to_order_button)
        time.sleep(3)
        order_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://magento.softwaretestingboard.com/checkout/onepage/success/")
        )

        print("URL z success message załadowany!\n success section loaded")

        time.sleep(5)

        shopping_button = self.driver.find_element(*self.continue_shopping_button)
        time.sleep(3)
        shopping_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://magento.softwaretestingboard.com/")
        )

        print("URL bazowy załadowany!\n based url loaded")

        time.sleep(60)
        # change ship options - change city - use 'pencil' icon - button to edit
        # self.ship_to_edit_button = (By.XPATH, '//*[@id="opc-sidebar"]/div[2]/div/div[1]/div[1]/button')
        # self.ship_meth_edit_button = (By.XPATH, '// *[ @ id = "opc-sidebar"] / div[2] / div / div[2] / div[1] / button')
















