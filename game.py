def browse(txt_name='settings.txt'):
    '''функция для получения данных из текстовика в форме словаря
    :return dict'''
    ss = {}
    for line in open(txt_name, 'r'):
        item = line.strip('\n').replace(' ', '').split('=')
        try:
            ss[item[0]] = int(item[1])
        except ValueError:
            ss[item[0]] = item[1]
    return ss





