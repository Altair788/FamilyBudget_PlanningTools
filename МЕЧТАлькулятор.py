    #  МЕЧТАлькулятор

#  Определяет предполагаемую будущую стоимость мечты (с поправкой на инфляцию)
#  и сумму ежемесячных взносов, необходимую для накопления
#  на покупку в течение заданного количества лет"

    #  ФОРМУЛА
#  Стоимость мечты (в б.в.) == целевая стоимость (в н.в.) * (1 + процент инфляции)**количество лет до покупки
#  Размер ежемесячного взноса == Стоимость мечты (в б.в.)/количество лет до покупки/12


def future_purchase_cost(target_value, inflation_rate, years_to_purchase):
    inflation_rate = inflation_rate / 100
    future_cost = target_value * (1 + inflation_rate) ** years_to_purchase
    monthly_installment = future_cost / years_to_purchase / 12
    return future_cost, monthly_installment
