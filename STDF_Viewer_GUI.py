import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from stdf.stdf_reader import Reader
from stdf.stdf_writer import Writer
import logging
from pathlib import Path
import time

class Application(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 设置标题与初始大小
        self.setWindowTitle('STDF Viewer Beta V0.1')
        self.resize(500, 300)

        self.table = QTableWidget(self)

        row_num = len(stdf_dic)
        col_num = 4

        self.table.setRowCount(row_num)
        self.table.setColumnCount(col_num)
        self.table.setHorizontalHeaderLabels(['Index', 'Records', 'Count','Position'])

        i = 0 # row index
        j = 1 # same record cnt
        last_rec = ''
        for key, val in stdf_dic.items():
            index_rec_list = key.split(' - ')
            index = index_rec_list[0]
            rec = index_rec_list[1]

            if rec == last_rec:
                j += 1
            else:

                index_item = QTableWidgetItem(index)
                rec_item = QTableWidgetItem(rec)
                cnt_item = QTableWidgetItem(str(j))
                pos_item = QTableWidgetItem(str(val))
                j = 1

                self.table.setItem(i, 0, index_item)
                self.table.setItem(i, 1, rec_item)
                self.table.setItem(i, 2, cnt_item)
                self.table.setItem(i, 3, pos_item)
                i += 1
            last_rec = rec
        self.table.setRowCount(i)
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)


def get_all_records(stdf):
    stdf.read_rec_list = True
    stdf_dic = {}
    i = 0
    for rec_name, position in stdf:
        stdf_dic[str(i) + ' - ' + rec_name] = position
        i += 1
    stdf.read_rec_list = False
    return stdf_dic

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    in_file = r'./sample_stdf/a595.stdf'
    stdf = Reader()
    stdf.load_stdf_file(stdf_file=in_file)
    stdf_dic = get_all_records(stdf)


    app = QApplication(sys.argv)
    viewer = Application()
    viewer.show()
    sys.exit(app.exec_())