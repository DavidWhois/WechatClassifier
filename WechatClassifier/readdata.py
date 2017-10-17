import jieba

# todo：这里需要改成可以选择待分类的人的个数n,在get_classifier中传入待分类人的聊天记录文件
# todo:装到一个list中读入
# 实现思路：使用sys.path获取当前目录，再获取datas目录下的所有文件名list，遍历这个list，导入文件
# n = len(list)就是要分类的个数

# todo:def read_all() 调用readdata(),return data,target(m*n)
# target = np.zeros((m,n))
# 在第j类的target[:,j]=1


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