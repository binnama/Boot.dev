def should_serve_customer(customer_age, on_break, time):

    if (customer_age >= 21 and on_break == False and time >= 5 and time <= 10):
        # Nome: Paratheses not necessary + only 'and', no need for 'or' at all XD
        return True
    else:
        return False

