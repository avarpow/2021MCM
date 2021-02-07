import numpy as np
import pandas
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
df_train = pandas.read_csv('data_rat.csv', usecols=[
                           'avar_temperture', 'water_per_capit', 'rain_height', 'grain_yield'])
print(df_train, len(df_train))
pca = PCA(n_components=2)  # 选取3个主成分
low_d = pca.fit_transform(df_train)  # 用他来降低维度
pca.inverse_transform(low_d)  # 恢复降维之前的数据
print(pca.components_)  # 返回模型的各个特征向量
print(pca.explained_variance_ratio_)  # 返回各个成分各自的方差百分比
plt.scatter(low_d[:, 0], low_d[:, 1])
plt.show()
# X = np.array([[-1, 2, 66, -1], [-2, 6, 58, -1], [-3, 8, 45, -2],
#               [1, 9, 36, 1], [2, 10, 62, 1], [3, 5, 83, 2]])  # 导入数据，维度为4
# pca = PCA(n_components=2)  # 降到2维
# pca.fit(X)  # 训练
# newX = pca.fit_transform(X)  # 降维后的数据
# # PCA(copy=True, n_components=2, whiten=False)
# print(pca.explained_variance_ratio_)  # 输出贡献率
# print(newX)  # 输出降维后的数据
