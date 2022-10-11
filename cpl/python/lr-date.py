import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder

X = np.array([
    [1, '周六', '吃饭', '晴天', '轻松', '清零', '精彩'],
    [2, '周日', '吃饭', '阴天', '轻松', '清零', '精彩'],
    [3, '周日', '吃饭', '晴天', '轻松', '清零', '精彩'],
    [4, '周六', '吃饭', '阴天', '轻松', '清零', '精彩'],
    [5, '周间', '吃饭', '晴天', '轻松', '清零', '精彩'],
    [6, '周六', '逛街', '晴天', '轻松', '平缓', '无聊'],
    [7, '周日', '逛街', '晴天', '适中', '平缓', '无聊'],
    [8, '周日', '逛街', '晴天', '轻松', '平缓', '精彩'],
    [9, '周日', '逛街', '阴天', '适中', '平缓', '精彩'],
    [10, '周六', '学习', '雨天', '轻松', '严峻', '无聊'],
    [11, '周间', '学习', '雨天', '繁重', '严峻', '精彩'],
    [12, '周间', '吃饭', '晴天', '繁重', '严峻', '无聊'],
    [13, '周六', '逛街', '晴天', '适中', '清零', '精彩'],
    [14, '周间', '逛街', '阴天', '适中', '清零', '精彩'],
    [15, '周日', '逛街', '晴天', '轻松', '平缓', '无聊'],
    [16, '周间', '吃饭', '晴天', '繁重', '严峻', '精彩'],
    [17, '周六', '吃饭', '阴天', '适中', '平缓', '精彩'],
])
y = np.array(
    ['是', '是', '是', '是', '是', '是', '是', '是',
     '否', '否', '否', '否', '否', '否', '否', '否', '否']
)

X = OneHotEncoder().fit_transform(X[:, 1:7])
y = LabelBinarizer().fit_transform(y).squeeze()

train_index = [0, 1, 2, 5, 6, 9, 13, 14, 15, 16]
test_index = [3, 4, 7, 8, 10, 11, 12]

X_train, X_test, y_train, y_test = X[train_index, :], X[test_index, :], y[train_index], y[test_index]

clf = LogisticRegression(penalty='none', verbose=True)  # 无正则项 输出日志
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

print(y_test, clf.predict_proba(X_test))