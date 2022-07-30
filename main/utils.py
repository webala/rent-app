from .models import House


def get_balance(house_id, amount_paid):
    house = House.objects.get(id=house_id)
    current_balance = house.balance
    rent = house.rent

    if current_balance == 0:
        new_balance = rent - amount_paid
    else:
        new_balance = current_balance - amount_paid

    return new_balance
