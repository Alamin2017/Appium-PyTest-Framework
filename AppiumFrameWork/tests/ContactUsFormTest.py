import pytest

from AppiumFrameWork.base.DriverClass import Driver
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.ContactUsFormPage import ContactForm
import unittest
import pytest
from AppiumFrameWork.pages.ContactUsFormPage import ContactForm
import AppiumFrameWork.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self. cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()

""""
driver1=Driver()
log=cl.customLogger()
driver=driver1.getDriverMethod()
"""
"""
bp=BasePage(driver)
log.info("Launch the app")
bp.screenShot("App")
#element=bp.waitForElement("com.code2lead.kwad:id/ContactUs","id")
#element.click()
element=bp.isDisplayed("com.code2lead.kwad:id/ContactUs","id")
print(element)
bp.clickElement("com.code2lead.kwad:id/ContactUs","id")
bp.sendText("Code2Lead","Enter Name","text")
bp.screenShot("Code 2 Lead")
"""
"""
cf=ContactForm(driver)
cf.clickContactFormButton()
cf.verifyContactPage()
cf.enterName()
cf.enterEmail()
cf.enterAddress()
cf.enterMNumber()
cf.clickSubmitButton()
"""