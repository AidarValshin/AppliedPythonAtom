#!/usr/bin/env python
# coding: utf-8
import numpy as np
from sklearn.preprocessing import StandardScaler


class KNNRegressor:
    """
    Построим регрессию с помощью KNN. Классификацию писали на паре
    """

    scaler = StandardScaler()

    def __init__(self, n):
        '''
        Конструктор
        :param n: число ближайших соседей, которые используются
        '''
        self.n = n

    def fit(self, X, y):
        '''
        :param X: обучающая выборка, матрица размерности (num_obj, num_features)
        :param y: целевая переменная, матрица размерности (num_obj, 1)
        :return: None
        '''
        self.x = scaler.fit_transform(X)
        self.x = X
        self.y = y

    def predict(self, X):
        '''
        :param X: выборка, на которой хотим строить предсказания (num_test_obj, num_features)
        :return: вектор предсказаний, матрица размерности (num_test_obj, 1)
        '''
        X = scaler.transform(X)
        self.y = np.array(self.y)
        y = []
        assert len(X.shape) == 2
        for t in X:
            # Посчитаем расстояние от всех элементов в тренировочной выборке
            # до текущего примера -> результат - вектор размерности трейна
            # TODO d =
            d = np.sum(np.sqrt((t - self.x[:]) ** 2), axis=1)

            # Возьмем индексы n элементов, расстояние до которых минимально
            # результат -> вектор из n элементов
            # TODO idx =
            idx = np.argsort(d[:])[:self.n]

            """a,b=0,0
            for inds in idx:
                ind=int(inds)
                a+=((1/d[ind]))*(self.y[ind])
                b+=(1/d[ind])
               # print("idx",idx,d[ind],self.y[ind])
            prediction =np.round(a/b)"""
            prediction = np.average(self.y[idx], weights=1 / d[idx])
            y.append(prediction)
        return y
