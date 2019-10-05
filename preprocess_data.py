import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np


class PreprocessData:
    """
    probability of default at the moment of application ==> discard all information gathered after loan was granted
    hence ignoring the following columns
    ['grade']
    ['installment']
    ['issue_d']
    ['last_pymnt_d']

    """

    def __init__(self, path_to_data=''):

        self._path_to_data = path_to_data
        self.data = pd.read_csv(self._path_to_data)



    def missing_values(self):
        """
        if the data contains missing values, fill them with median
        :return:
        """
        pass

    def nan_values(self):
        """
        detect nans and substitute them with median
        :return:
        """
        imp = SimpleImputer(missing_values=np.nan, strategy='median')  # because median is not prone to outliers
        # find the columns in which nan values appear
        rows_with_nans = self.data.isna().sum() != 0
        rows_with_nans = rows_with_nans[rows_with_nans==True]
        # fill in the nans appearing in rows with mean value
        for i in range(2):
            table = imp.fit(self.data[rows_with_nans.index[i]].values.reshape(-1, 1))
            self.data[rows_with_nans.index[i]] = table.transform(self.data[rows_with_nans.index[i]].values.reshape(-1, 1))
        return self.data

    def woe(self):  # weight of evidence, to check which values are relevant for the predictions
        pass

    def outliers(self):
        pass

    def bin_data(self):
        pass

    def normalize_data(self):
        """
        normalizes data for credit scoring
        :return:
        """
        pass



if __name__ == '__main__':
    path = '/home/m.lewandows4/Downloads/practice/lending-club-loan-data/loan.csv'
    a = PreprocessData(path)
    tabelka = a.nan_values()
    print(tabelka)

