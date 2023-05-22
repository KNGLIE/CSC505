import inflect
p = inflect.engine()


def get_dollar_amount():
    dollar_amount = int(input('input dollar amount'))
    return dollar_amount


def get_cent_amount():
    cent_amount = int(input('input cent amount'))
    if cent_amount == 1:
        cent_amount = 'and', cent_amount.__str__(), 'Cent'
    elif 2 <= cent_amount <= 99:
        cent_amount = 'and', cent_amount.__str__(), 'Cents'
    elif cent_amount == 0:
        cent_amount = 'and', cent_amount.__str__(), 'Cents'
    else:
        input('That value is not allowed. ENTER to retry cents')
        get_cent_amount()
    return cent_amount


def dollar_to_string():
    convert = p.number_to_words(get_dollar_amount())
    return convert


def output_check():
    print(str.title(dollar_to_string()), 'Dollars', ' '.join(get_cent_amount()))


output_check()

