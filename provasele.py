'''Selenium test script'''
from time import sleep as timesleep
from selenium.webdriver import Chrome as WebdriverChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options



def main() -> None:
    '''Main function'''
    #marcotognazzi1965dicembre23@gmail.com
    chrome_options: Options = Options()
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("detach", True)
    browser: WebdriverChrome = WebdriverChrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    wait = WebDriverWait(browser, 10)
    print("Browser opened")
    #https://www.oldwildwest.it/fidelitycard/registerwithoutcard
    browser.get("https://www.oldwildwest.it/fidelitycard/registerwithoutcard")
    print("Page loaded")

    cookiesbtn = wait.until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection")))
    cookiesbtn.click()
    print("Cookies accepted")

    first_name = wait.until(EC.visibility_of_element_located((By.ID, "input_Nome")))
    first_name.send_keys("Luca")
    print("Name sent")

    last_name = wait.until(EC.visibility_of_element_located((By.ID, "input_Cognome")))
    last_name.send_keys("Gianni")
    print("Last name sent")

    email = wait.until(EC.visibility_of_element_located((By.ID, "input_email")))
    email.send_keys("your-email@example.com")
    print("Email sent")

    telephone = wait.until(EC.visibility_of_element_located((By.ID, "input_Telefono")))
    telephone.send_keys("+351999888777")
    print("Telephone sent")

    data_nascita = wait.until(EC.visibility_of_element_located((By.ID, "input_DataDiNascita")))
    data_nascita.send_keys("23/12/1965")
    print("Birth date sent")

    sesso_btn = browser.find_element(By.ID, "Input_Sesso_M")
    browser.execute_script("arguments[0].click();", sesso_btn)
    print("Btn sesso clicked")

    comune = wait.until(EC.visibility_of_element_located((By.ID, "input_Comune")))
    comune.send_keys("Trento")
    print("Comune sent")

    cap_field = wait.until(EC.visibility_of_element_located((By.ID, "input_CAP")))
    cap_field.send_keys("38122")
    print("CAP sent")

    password = wait.until(EC.visibility_of_element_located((By.ID, "input_password")))
    password.send_keys("ChiaroPassword.123")
    print("Password sent")

    password_confirm = wait.until(EC.visibility_of_element_located((By.ID, "input_confermaPassword")))
    password_confirm.send_keys("ChiaroPassword.123")
    print("Confirm password sent")

    #agree_privacy = wait.until(EC.element_to_be_clickable((By.ID, "Input_TakeAwayPrivacy")))
    #agree_privacy.click()
    a_element = browser.find_element(By.CSS_SELECTOR, 'a[data-target=".help_fidelityPrivacyAndRegulation"]')
    browser.execute_script('''
    var element = arguments[0];
    $("a[data-target='.help_fidelityPrivacyAndRegulation']").click(function(){
        $($(this).data("target")).show();
        $($(this).data("target")).hide();
    })
    ''', a_element)
    browser.execute_script("arguments[0].click();", a_element)
    close_element = browser.find_element(By.CSS_SELECTOR, 'body > div.fancybox-overlay.fancybox-overlay-fixed > div > div > a')
    browser.execute_script("arguments[0].click();", close_element)
    agree_privacy = browser.find_element(By.ID, "Input_TakeAwayPrivacy")
    browser.execute_script("arguments[0].click();", agree_privacy)
    print("Privacy policy clicked")

    timesleep(100)
    #submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))
    #submit_button.click()
    #print("Registration submitted")

    #wait.until(EC.url_contains("https://www.oldwildwest.it/TakeAway/ConfermaRegistrazione"))
    #print("Registration confirmed")

    browser.quit()


if __name__ == "__main__":
    main()
