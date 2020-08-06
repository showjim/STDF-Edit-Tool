# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from stdf.stdf_reader import Reader
from stdf.stdf_writer import Writer
import logging
import qtawesome as qta
import time


class Application(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUI()
        self.index_in_same_record = 0
        self.current_row = 0

    def setupUI(self):
        # 设置标题与初始大小
        self.setWindowTitle('STDF Viewer Beta V0.1')
        self.resize(1000, 600)

        self.table = QTableWidget(self)
        self.record_content_table = QTableWidget(self)
        # Button show next record
        self.show_next_record = QPushButton(qta.icon('mdi.skip-next', color='green'), '')
        self.show_next_record.clicked.connect(self.show_next_content_table)

        # Button show previous record
        self.show_previous_record = QPushButton(qta.icon('mdi.skip-previous', color='red'), '')
        self.show_previous_record.clicked.connect(self.show_previous_content_table)

        row_num = len(stdf_dic)
        col_num = 4

        self.table.setRowCount(row_num)
        self.table.setColumnCount(col_num)
        self.table.setHorizontalHeaderLabels(['Index', 'Records', 'Count', 'Position'])

        self.record_content_table.setRowCount(0)
        self.record_content_table.setColumnCount(3)
        self.record_content_table.setHorizontalHeaderLabels(['Field', 'Type', 'Value'])

        # Fill STDF data to table
        i = 0  # row index
        for key, val in stdf_dic.items():
            index_rec_list = key.split(' - ')
            index = index_rec_list[0]
            rec = index_rec_list[1]

            index_item = QTableWidgetItem(index)
            rec_item = QTableWidgetItem(rec)
            cnt_item = QTableWidgetItem(str(len(val)))
            pos_item = QTableWidgetItem(str(val[0]))

            self.table.setItem(i, 0, index_item)
            self.table.setItem(i, 1, rec_item)
            self.table.setItem(i, 2, cnt_item)
            self.table.setItem(i, 3, pos_item)
            i += 1
        # 设置布局
        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout2 = QGridLayout()
        layout2.addWidget(self.show_previous_record, 0,0)
        layout2.addWidget(self.show_next_record, 0, 1)
        self.record_content_table.setLayout(layout2)
        # layout2.addWidget(self.record_content_table, 1, 0)
        layout.addWidget(self.record_content_table)
        self.setLayout(layout)

        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.cellClicked.connect(self.show_content_table)

    def show_content_table(self, row, col):
        self.index_in_same_record = 0
        self.show_record(row, col, self.index_in_same_record)

    def show_next_content_table(self):
        self.index_in_same_record += 1
        self.show_record(self.current_row, 0, self.index_in_same_record)

    def show_previous_content_table(self):
        self.index_in_same_record -= 1
        if self.index_in_same_record < 0:
            self.index_in_same_record = 0
        self.show_record(self.current_row, 0, self.index_in_same_record)

    def show_record(self, row, col, index):
        # Get cell text
        self.current_row = row
        key = self.table.item(row, 0).text() + ' - ' + self.table.item(row, 1).text()
        # Enable STDF record read procedure
        position = stdf_dic[key][index]
        stdf.STDF_IO.seek(position)
        rec_name, header, body = stdf.read_record()
        # Refresh the content table
        self.record_content_table.setRowCount(len(body))
        self.record_content_table.setHorizontalHeaderLabels(['Field', 'Type', 'Value'])
        self.record_content_table.setColumnCount(3)
        # Fill the content table
        i = 0
        for k, v in body.items():
            field_item = QTableWidgetItem(str(k))
            val_item = QTableWidgetItem(str(v))
            self.record_content_table.setItem(i, 0, field_item)
            self.record_content_table.setItem(i, 2, val_item)
            print(str(k) + ": " + str(v))
            i += 1


def get_all_records(stdf):
    stdf.read_rec_list = True
    stdf_dic = {}
    i = 0
    j = 1  # same record cnt
    last_rec = ''
    tmp_list = []
    for rec_name, position in stdf:
        tmp_list.append(position)
        if rec_name == last_rec:
            pass
        else:
            stdf_dic[str(i) + ' - ' + rec_name] = tmp_list
            tmp_list = []
        i += 1
        last_rec = rec_name
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
