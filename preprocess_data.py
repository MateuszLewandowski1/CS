import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np


class PreprocessData:

    def __init__(self, path_to_data=''):

        self._path_to_data = path_to_data
        self.data = pd.read_csv(self._path_to_data)

    def nan_values(self):
        """
        detect nans and missing values and substitute them with median
        :return:
        """
        imp = SimpleImputer(missing_values=np.nan, strategy='median')  # because median is not prone to outliers
        # find the columns in which nan values appear
        rows_with_nans = self.data.isna().sum() != 0
        rows_with_nans = rows_with_nans[rows_with_nans==True]
        # fill in the nans appearing in rows with median value
        for i in range(2):
            table = imp.fit(self.data[rows_with_nans.index[i]].values.reshape(-1, 1))
            self.data[rows_with_nans.index[i]] = table.transform(self.data[rows_with_nans.index[i]].values.reshape(-1, 1))
        return self.data

    def delete_unknown_values_at_the_time_of_application(self):
        """
        deletes columns with data that could only have been collected after the loan is granted, or irrelevant like
        earliest_cr_line
        :return:
        """
        unavailable_data = ['recoveries', 'installment', 'int_rate', 'issue_d', 'last_pymnt_d', 'term',
                            'earliest_cr_line']
        remaining_columns = self.data.columns.drop(unavailable_data)  # list of remaning columns
        self.data = self.data[remaining_columns]  # table of remaining data
        return self.data

    def group_cont_var_into_bins(self):
        """
        grouping grade, sub_grade, annual_inc into 5 bins
        :return:
        """
        self.data['annual_inc'] = pd.qcut(self.data['annual_inc'], 5)  # TODO finish with grade and sub_grade


        pass

    def information_value_woe(self):  # weight of evidence, to check which values are relevant for the predictions
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

