from numpy import *
from sklearn.naive_bayes import GaussianNB
from WechatClassifier.readdata import read_data, read_dict
import time


def get_classifier():
    # 导入dict文件，此字典和分词使用的字典相同
    dic = read_dict('dict.txt')
    print('dict_words num:', len(dic))
    # 读取数据,构造labels

    # todo：这里需要改成可以选择待分类的人的个数n,在get_classifier中传入待分类人的聊天记录文件
    # todo:装到一个list中读入
    # 实现思路：使用sys.path获取当前目录，再获取datas目录下的所有文件名list，遍历这个list，导入文件
    # n = len(list)就是要分类的个数
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

    # todo:这里最好比较一下svm和NB分类训练时间
    # todo:更进一步的，改用逻辑回归实现在线系统？
    # 调用naive_bayes方法训练
    start_time = time.time()
    clf = GaussianNB()
    clf.fit(train_features, train_labels)
    end_time = time.time()
    print('training time: %10.3f ms' % (end_time-start_time))
    return clf

