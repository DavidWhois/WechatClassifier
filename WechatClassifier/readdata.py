import jieba


def read_data(filename, username):
    data = []
    with open(filename) as inputs:
        for each_line in inputs:
            if each_line.startswith(username):
                print('-', end='')
            elif each_line=='\n':
                print('-', end='')
            elif each_line.startswith('—————'):
                print('-', end='')
            else:
                data.append(each_line)
    # 每5行一组，成为一个例子
    data_grouped = []
    element = ''
    for i in range(len(data)):
        element = (element+data[i])
        if (i+1) % 5 == 0:
            # 将分好组的字符串分词成一个list，使用jieba分词
            element_list = jieba.lcut(element)
            data_grouped.append(element_list)
            element = ''
    return data_grouped


def read_dict(filename):
    word_dict = []
    with open(filename) as dicts:
        for each_line in dicts:
            word = each_line.split(" ")
            word_dict.append(word[0])
    return word_dict