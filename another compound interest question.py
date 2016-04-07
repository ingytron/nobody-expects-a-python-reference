def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = float(annual_rate) / periods_per_year
    print rate_per_period
    periods = periods_per_year * years
    value = 0
    for i in periods:
        value += (float(present_value*(1.0+annual_rate))**periods)
        print value
    print "$1000 at 2% compounded daily for 3 years yields $" , value
    print 'checksum' , value 

future_value(500, 0.04, 10, 10)
future_value(1000, 0.02, 365, 3)

