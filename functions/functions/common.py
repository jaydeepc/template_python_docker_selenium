

class Common:

    @classmethod
    def click_on_dropdown_option(self, available_options_in_dropdown, option_to_be_clicked):
        for option in available_options_in_dropdown:
            if option.text == option_to_be_clicked:
                option.click()
