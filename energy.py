DEFAULT_WATTS = 200
PRICE_PER_KWH = 2.5  

def calc_kwh(watts, hours):
    return (watts * hours) / 1000

def calc_cost(kwh):
    return kwh * PRICE_PER_KWH