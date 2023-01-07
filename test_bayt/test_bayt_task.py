import time
from config import EMAIL, PASSWORD
from drivers import driver, CustomWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestBaytSite(CustomWebDriver):
    def choose_from_searchable_dropdown(self, sleep_time, element_id, value, search_xpath, first_element_xpath):
        self.click_on_element_using_id(sleep_time, element_id)
        self.enter_value_using_xpath(3, search_xpath, value)
        self.click_on_element_using_xpath(4, first_element_xpath)

    def test_01_full_registration(self):
        driver.get('https://www.bayt.com/en/jordan/')
        driver.execute_script("window.scrollTo(0, 5000)")
        self.click_on_element_using_xpath(1, '//a[@href="https://www.bayt.com/en/pages/about-us/"]')
        driver.execute_script("window.scrollTo(0, 500)")
        self.click_on_element_using_xpath(2, '//div[@class="row m20y p20y"]'
                                             '//a[@href="/en/pakistan/jobs/ui-ux-designer-4652439/"]')
        # get current window handle
        current_window = driver.current_window_handle
        # get first child window
        first_child_window = driver.window_handles
        for w in first_child_window:
            # switch focus to child window
            if (w != current_window):
                driver.switch_to.window(w)
        self.click_on_element_using_id(3, 'applyButton')
        self.enter_value_using_id(2, 'JsApplicantRegisterForm_firstName', 'Jumana')
        self.enter_value_using_id(0, 'JsApplicantRegisterForm_lastName', 'Thalji')
        self.enter_value_using_id(0, 'JsApplicantRegisterForm_email', EMAIL)
        self.enter_value_using_id(0, 'JsApplicantRegisterForm_password', PASSWORD)
        self.enter_value_using_id(0, 'JsApplicantRegisterForm_mobPhone', '790000000')
        self.click_on_element_using_id(1, 'register')
        time.sleep(5)
        try:
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, '//*[@id="jsApplicantRegisterFormID"]/div[7]/div/div[1]/div/div/iframe')))
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]'))).click()
            driver.switch_to.default_content()
            self.click_on_element_using_id(5, 'register')
        except Exception:
            pass
        finally:
            self.choose_from_searchable_dropdown(5, 'personalInformationForm_birthDay__r', '19',
                                                 '//*[@id="yw0"]/section[2]/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[2]/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div[3]/ul/li')
            self.choose_from_searchable_dropdown(0, 'personalInformationForm_birthMonth__r', 'March',
                                                 '//*[@id="yw0"]/section[2]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[2]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/ul/li')
            self.choose_from_searchable_dropdown(0, 'personalInformationForm_birthYear__r', '1996',
                                                 '//*[@id="yw0"]/section[2]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[2]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/ul/li')
            self.click_on_element_using_xpath(2, '//label[@for="personalInformationForm_gender_1"]')
            self.choose_from_searchable_dropdown(2, 'personalInformationForm_nationalityCitizenAc__r', 'Jordan',
                                                 '//*[@id="yw0"]/section[2]/div[3]/div/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[2]/div[3]/div/div[1]/div/div[1]/div[3]/ul/li[2]')
            driver.execute_script("window.scrollTo(0, 500)")
            self.enter_value_using_xpath(2, '//*[@id="experienceForm_jobTitle"]', 'Quality Assurance')
            self.click_on_element_using_xpath(1, '//*[@id="experienceDetails"]/section/div[1]/div/div[1]/div/div[1]/div[3]/ul/li[1]')
            self.choose_from_searchable_dropdown(0, 'experienceForm_jobRole__r', 'Information Technology',
                                                 '//*[@id="experienceDetails"]/section/div[2]/div/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="experienceDetails"]/section/div[2]/div/div[1]/div/div[1]/div[3]/ul/li[2]')
            self.choose_from_searchable_dropdown(0, 'experienceForm_country__r', 'Jordan',
                                                 '//*[@id="experienceDetails"]/section/div[3]/div/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="experienceDetails"]/section/div[3]/div/div[1]/div/div[1]/div[3]/ul/li')
            self.choose_from_searchable_dropdown(0, 'experienceForm_startMonth__r', 'November',
                                                 '//*[@id="experienceDetails"]/section/div[4]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="experienceDetails"]/section/div[4]/div/div/div[1]/div[1]/div/div[1]/div[3]/ul/li')
            self.choose_from_searchable_dropdown(0, 'experienceForm_startYear__r', '2020',
                                                 '//*[@id="experienceDetails"]/section/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="experienceDetails"]/section/div[4]/div/div/div[2]/div[1]/div/div[1]/div[3]/ul/li')
            driver.execute_script("window.scrollTo(0, 900)")
            self.choose_from_searchable_dropdown(2, 'experienceForm_endMonth__r', 'January',
                                                 '//*[@id="endDateItem"]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="endDateItem"]/div/div/div[1]/div[1]/div/div[1]/div[3]/ul/li')
            self.choose_from_searchable_dropdown(0, 'experienceForm_endYear__r', '2022',
                                                 '//*[@id="endDateItem"]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="endDateItem"]/div/div/div[2]/div[1]/div/div[1]/div[3]/ul/li')
            driver.execute_script("window.scrollTo(0, 700)")
            self.enter_value_using_id(0, 'experienceForm_company', 'test company')
            driver.execute_script("window.scrollTo(0, 700)")
            self.click_on_element_using_id(0, "experienceForm_companyInd__r")
            self.click_on_element_using_xpath(2, '//li[@data-text="Accounting"]')
            driver.execute_script("window.scrollTo(0, 900)")
            self.click_on_element_using_xpath(3, '//label[@for="experienceForm_isJobThroughBayt_0"]')
            driver.execute_script("window.scrollTo(0, 1500)")
            self.choose_from_searchable_dropdown(2, 'EducationForm_degree__r', 'Diploma',
                                                 '//*[@id="yw0"]/section[5]/div[1]/div/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[5]/div[1]/div/div[1]/div/div[1]/div[3]/ul/li')
            self.enter_value_using_id(2, 'EducationForm_institution', 'Harvard university')
            self.click_on_element_using_xpath(2, '//*[@id="yw0"]/section[5]/div[2]/div/div[1]/div/div[1]/div[3]/ul/li')
            self.choose_from_searchable_dropdown(2, 'EducationForm_educationCountry__r', 'United States',
                                                 '//*[@id="yw0"]/section[5]/div[3]/div/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[5]/div[3]/div/div[1]/div/div[1]/div[3]/ul/li')

            self.choose_from_searchable_dropdown(3, 'EducationForm_educationCity__r', 'Massachusetts',
                                                 '//*[@id="yw0"]/section[5]/div[4]/div/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[5]/div[4]/div/div[1]/div/div[1]/div[3]/ul/li')

            self.enter_value_using_xpath(2, '//*[@id="EducationForm_major"]', 'Computer Science And Business Administration')
            self.click_on_element_using_xpath(1, '//*[@id="yw0"]/section[5]/div[6]/div/div[1]/div/div[1]/div[3]/ul/li')

            self.choose_from_searchable_dropdown(2, 'EducationForm_completionMonth__r', 'September',
                                                 '//*[@id="yw0"]/section[5]/div[7]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[5]/div[7]/div/div/div[1]/div[1]/div/div[1]/div[3]/ul/li')
            self.choose_from_searchable_dropdown(0, 'EducationForm_completionYear__r', '2018',
                                                 '//*[@id="yw0"]/section[5]/div[7]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[5]/div[7]/div/div/div[2]/div[1]/div/div[1]/div[3]/ul/li')
            driver.execute_script("window.scrollTo(0, 2000)")
            self.enter_value_using_id(2, 'targetJobForm_positionSought', 'Quality Assurance Engineer')
            self.click_on_element_using_xpath(3, '//*[@id="yw0"]/section[7]/div[1]/div/div[1]/div/div[1]/div[3]/ul/li[1]')
            self.choose_from_searchable_dropdown(2, 'targetJobForm_careerLevel__r', 'Mid Career',
                                                 '//*[@id="yw0"]/section[7]/div[2]/div/div[1]/div/div[1]/div[2]/div/input',
                                                 '//*[@id="yw0"]/section[7]/div[2]/div/div[1]/div/div[1]/div[3]/ul/li')
            self.click_on_element_using_xpath(2, '//footer[@class="form-footer p0b-d"]//input[@name="submit"]') # Submit
            time.sleep(5)

    def test_02_unique_email_validation(self):
        driver.get('https://www.bayt.com/en/jordan/')
        driver.execute_script("window.scrollTo(0, 5000)")
        self.click_on_element_using_xpath(1, '//a[@href="https://www.bayt.com/en/pages/about-us/"]')
        driver.execute_script("window.scrollTo(0, 500)")
        self.click_on_element_using_xpath(2, '//div[@class="row m20y p20y"]'
                                             '//a[@href="/en/saudi-arabia/jobs'
                                             '/tech-licensing-sales-specialist-saas-b2b-sales-4652516/"]')
        # get current window handle
        current_window = driver.current_window_handle
        # get first child window
        first_child_window = driver.window_handles
        for w in first_child_window:
                # switch focus to child window
                if (w != current_window):
                    driver.switch_to.window(w)
        self.click_on_element_using_id(3, 'applyButton')
        self.enter_value_using_id(2, 'JsApplicantRegisterForm_firstName', 'Jumana')
        self.enter_value_using_id(0, 'JsApplicantRegisterForm_lastName', 'Thalji')
        self.enter_value_using_id(0, 'JsApplicantRegisterForm_email', 'test_email_442@test.net')
        self.enter_value_using_id(0, 'JsApplicantRegisterForm_password', PASSWORD)
        self.enter_value_using_id(0, 'JsApplicantRegisterForm_mobPhone', '790000000')
        self.click_on_element_using_id(1, 'register')
        # Check email validation message
        time.sleep(5)
        driver.find_element_by_id('JsApplicantRegisterForm_email_em_').is_displayed()

    def test_03_delete_account(self):
        driver.get('https://www.bayt.com/en/login/')
        self.enter_value_using_id(2, 'LoginForm_username', EMAIL)
        self.enter_value_using_id(0, 'LoginForm_password', PASSWORD)
        self.click_on_element_using_id(1, 'login-button')
        self.click_on_element_using_xpath(3, '//li[@class="popover-owner"][4]')  # 3 dots
        self.click_on_element_using_xpath(2, '//a[@href="https://www.bayt.com/en/jobseeker/my-account/"]')
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        self.click_on_element_using_xpath(2, '//a[@href="/en/jobseeker/my-account/delete-account/"]')
        self.click_on_element_using_xpath(3, '//button[@class="btn is-danger"]')
        self.click_on_element_using_xpath(2, '//button[@class="btn u-expanded-m  is-danger non-aid"]')
        time.sleep(5)
        driver.get('https://www.bayt.com/en/login/')
        self.enter_value_using_id(2, 'LoginForm_username', EMAIL)
        self.enter_value_using_id(0, 'LoginForm_password', PASSWORD)
        self.click_on_element_using_id(1, 'login-button')
        # Verify showing a validation message when login with the deleted account
        time.sleep(5)
        driver.find_element_by_xpath('//ul[@class="list is-basic t-center"]').is_displayed()

    def test_04_mobile(self):
        driver.get('https://www.bayt.com/en/login/')
        driver.set_window_size(400, 800)
        self.click_on_element_using_xpath(3, '/html/body/nav/ul/li[5]/a/i')
        self.click_on_element_using_xpath(3, '//input[@id="search_keyword"]')
        self.enter_value_using_xpath(2, '/html/body/div[5]/div[1]/div[2]/div/input', 'Quality Assurance Engineer')
        self.click_on_element_using_xpath(2, '/html/body/div[5]/div[1]/div[3]/ul/li[2]/a')
        self.choose_from_searchable_dropdown(2, 'country__r', 'United Arab Emirates',
                                             '/html/body/div[5]/div[1]/div[2]/div/input',
                                             '/html/body/div[5]/div[1]/div[3]/ul/li')
        self.click_on_element_using_xpath(2, '//button[@class="btn is-small u-expanded-m m"]')
        self.click_on_element_using_xpath(2, '//*[@id="results_inner_card"]/ul/li[2]/div/div[4]/div[2]/a')
        time.sleep(5)
        actual_url = driver.current_url
        register_link = str(actual_url).split('applicant-register', 1)[0]
        assert register_link == 'https://www.bayt.com/en/register-j/'
