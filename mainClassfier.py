from readdata import *
from numpy import *
from sklearn.naive_bayes import GaussianNB
#创建字典
dic = ['我','你','嗯','。','天','坐','车','当','年','裤','衣','照','分','牌','子','图',
'吊','影','球','来','王','发','哈','当','对','麻','痹','玩','意','宅','听','曲','果']

#读取数据,构造labels
data1 = readdata('liu.txt','刘处')
labels1 = zeros(len(data1))
labels1 = list(labels1)
data2 = readdata('wang.txt','王绕柱')
labels2 = ones(len(data2))
labels2 = list(labels2)
data=data1+data2

train_labels=labels1+labels2

train_features=zeros([len(data),len(dic)])
#将dic中的字和字符串中的字匹配，得到的结果放到train_features中
for i in range(len(dic)):
    for j in range(len(data)):
        #每个feature的值是dic上该位置的字在样例中出现的个数
        train_features[j][i]=data[j].count(dic[i])

#按照朴素贝叶斯库的格式要求，转成numpy的array格式
train_features = array(train_features)
train_labels = array(train_labels)
#train_labels = reshape(train_labels,(len(train_labels),1))

print(train_features)
print(shape(train_features))
print(train_labels)
print(shape(train_labels))

#调用naive_bayes方法训练
clf = GaussianNB()
clf.fit(train_features,train_labels)

testStr = '我在睡觉麻痹我家传统11点前睡觉，7点起床这句没看懂天天发这个表情的必然是我胡大师麻痹从外婆家取大伯家接我爸然后送姨夫回家最后再回家开了将近3个小时车'
test_features=zeros([1,len(dic)])
for i in range(len(dic)):
        #每个feature的值是dic上该位置的字在样例中出现的个数
        test_features[0][i]=testStr.count(dic[i])

test_label = clf.predict(test_features)
if test_label[0]==0:
    print('聊天对象为刘处')
else:
    print('聊天对象为王绕柱')
