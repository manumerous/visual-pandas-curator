__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker"
__license__ = "Apache-2.0"


import pandas as pd
from pandas.core.indexes.base import Index
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from src.main_window import MainWindow


def mavisual_pandas_cropper(data_df, plot_config_dict):
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(data_df, plot_config_dict)
    app.exec_()
    return