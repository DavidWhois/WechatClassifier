from numpy import *
from sklearn.naive_bayes import GaussianNB
from WechatClassifier.readdata import read_data, read_dict
import time


def get_classifier():
    # 导入dict文件，此字典和分词使用的字典相同
    dic = read_dict('dict.txt')
    print('dict_words num:', len(dic))
    # 读取数据,构造labels


    data1 = read_data('datas/liu.txt', '刘处')
    labels1 = zeros(len(data1))
    labels1 = list(labels1)
    data2 = read_data('datas/wang.txt', '王绕柱')
    labels2 = ones(len(data2))
    labels2 = list(labels2)
    data = data1+data2
    train_labels = labels1+labels2

    train_features = zeros([len(data), len(dic)])

    # 将dic中的字和字符串中的字匹配，得到的结果放到train_features中
    for i in range(len(dic)):

        for j in range(len(data)):
            # 每个feature的值是dic上该位置的字在样例list中出现的个数
            train_features[j][i] = data[j].count(dic[i])

    # 按照朴素贝叶斯库的格式要求，转成numpy的array格式
    train_features = array(train_features)
    train_labels = array(train_labels)

    # todo:改成svm，用一下那个自动调参数的工具，这样也算调过超参数了嘛！
    # 调用naive_bayes方法训练
    start_time = time.time()
    clf = GaussianNB()
    clf.fit(train_features, train_labels)
    end_time = time.time()
    print('training time: %10.3f ms' % (end_time-start_time))
    return clf
