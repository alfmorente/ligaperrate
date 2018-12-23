from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time

url = 'http://195.81.204.155/kimai/'
login_url = 'index.php?a=logout'
user = 'RaRoMo'
password = 'jaramago'



class AutoKimai:
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.implicitly_wait(10)

    def __init__(self, start_date=None,
                 end_date=None,
                 test=True):
        if start_date:
            self.start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
        else:
            self.start_date=None
        if end_date:
            self.end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y')
        else:
            self.end_date = datetime.datetime.today() + datetime.timedelta(days=-1)
        self.holidays = []
        for date in holidays:
            self.holidays.append(datetime.datetime.strptime(date, '%d/%m/%Y'))
        self.vacations = []
        for date in vacations:
            self.vacations.append(datetime.datetime.strptime(date, '%d/%m/%Y'))
        self.test = test

    def login(self):
        self.driver.get(url + login_url)
        user_elem = self.driver.find_element_by_name('name')
        user_elem.send_keys(user)
        password_elem = self.driver.find_element_by_name('password')
        password_elem.send_keys(password)
        login_elem = self.driver.find_element_by_tag_name('button')
        login_elem.send_keys(Keys.RETURN)

    def get_start_date(self):
        """
        Habria que conseguirla del entorno
        :return:
        """
        self.start_date = datetime.datetime.strptime("09/10/2018", '%d/%m/%Y')
        return self.start_date


    def add_entry(self, date_day, project_searched=default_project ,task_searched =default_task):
        add_elem = self.driver.find_element_by_xpath('//*[@id="zef_head"]/div/a')
        add_elem.click()
        time.sleep(1.5)
        found=False
        project_form = self.driver.find_element_by_id('add_edit_zef_pct_ID')
        for option in project_form.find_elements_by_tag_name('option'):
            if project_searched.lower() in option.text.lower():
                option.click()
                found=True
        if not found:
            raise Exception("No se ha encontrado el proyecto {}".format(project_searched))
        found=False
        time.sleep(1.5)
        task_form = self.driver.find_element_by_id('add_edit_zef_evt_ID')
        for option in task_form.find_elements_by_tag_name('option'):
            if task_searched.lower() in option.text.lower():
                option.click()
                found=True
                time.sleep(1)
        if not found:
            raise Exception("No se ha encontrado la tarea {}".format(task_searched))
        day_start = self.driver.find_element_by_id('edit_in_day')
        day_end = self.driver.find_element_by_id('edit_out_day')
        time_start = self.driver.find_element_by_id('edit_in_time')
        time_end = self.driver.find_element_by_id('edit_out_time')
        string_date = date_day.strftime('%d.%m.%Y')

        self.driver.execute_script("$(arguments[0]).val('{}');".format(string_date), day_start)
        self.driver.execute_script("$(arguments[0]).val('{}');".format(string_date), day_end)
        self.driver.execute_script("$(arguments[0]).val('09:00');", time_start)
        self.driver.execute_script("$(arguments[0]).val('17:00');", time_end)
        time.sleep(.5)

        if self.test:
            ok = self.driver.find_element_by_xpath('//*[@id="formbuttons"]/input[1]')
        else:
            ok = self.driver.find_element_by_xpath('//*[@id="formbuttons"]/input[2]')
        ok.click()


    def get_project_task(self,date):
        for k, v in projects.items():
            str_date=date.strftime('%d/%m/%Y')

            if str_date in v["worked_days"]:
                return v["name"], v["task"]
        return default_project,default_task

    def run(self):
        self.login()
        if self.start_date:
            date = self.start_date
        else:
            date=self.get_start_date()
        while date <= self.end_date:
            if date.weekday() not in [5, 6] and date not in self.holidays:
                if date in self.vacations:
                    self.add_entry(date,vacations_project,vacations_task)
                else:
                    p,t=self.get_project_task(date)
                    self.add_entry(date, p, t)

            date += datetime.timedelta(days=1)
        self.driver.close()


bot = AutoKimai(test=False)

if __name__ == "__main__":
    bot.run()
