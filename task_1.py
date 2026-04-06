import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {
            "чипсы": 50,
            "кола": 100,
            "печенье": 45,
            "молоко": 55,
            "кефир": 70,
        }
        self.__tax_rate = {
            "чипсы": 20,
            "кола": 20,
            "печенье": 20,
            "молоко": 10,
            "кефир": 10,
        }

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):

        if len(name) <= 0 or len(name) > 40:
            raise ValueError(
                "Нельзя добавить товар, если в его названии нет символов или их больше 40"
            )
        if name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError("Позиция отсутствует в чеке")
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            if item in self.__item_price:
                total.append(self.__item_price[item])

        total_sum = sum(total)

        if len(self.__name_items) > 10:
            total_sum = total_sum * 0.9

        return total_sum

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

        total_nds = 0
        for price in total:
            if len(self.__name_items) > 10:
                price *= 0.9
            total_nds = total_nds + price * 0.2

        return total_nds

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        total_nds = 0
        for price in total:
            if len(self.__name_items) > 10:
                price *= 0.9
            total_nds = total_nds + price * 0.1

        return total_nds

    def total_tax(self):
        return (
            self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        )

    @staticmethod
    def get_telephone_number(telephone_number):

        if type(telephone_number) is not int:
            raise ValueError(f"Необходимо ввести цифры")

        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f"+7{telephone_number}"
