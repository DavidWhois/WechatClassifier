import numpy as np
from WechatClassifier.readdata import read_data, read_dict
from WechatClassifier.mainClassfier import get_classifier

dic = read_dict('dict.txt')
testStr = '我在睡觉麻痹我家传统11点前睡觉，7点起床这句没看懂天天发这个表情的必然是我胡大师麻痹从外婆家取大伯家接我爸然后送姨夫回家最后再回家开了将近3个小时车'

test_features = np.zeros([1, len(dic)])
for i in range(len(dic)):
        test_features[0][i] = testStr.count(dic[i])
# 获取分类器
clf = get_classifier()
test_label = clf.predict(test_features)
if test_label[0] == 0:
    print('聊天对象为刘处')
else:
    print('聊天对象为王绕柱')
