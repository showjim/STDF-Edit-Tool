# -*- coding:utf-8 -*-
###################################################
# STDF Viewer Tool                                #
# Version: Beta 0.2                               #
#                                                 #
# Aug. 18, 2020                                   #
# A light STDF viewer and editor Tool               #
###################################################
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from stdf.stdf_reader import Reader
from stdf.stdf_writer import Writer
import logging
import qtawesome as qta
import time
import gzip

__version__ = 'STDF Viewer Beta V0.2'
__author__ = 'zhouchao486@gmail.com'


class Application(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUI()
        self.index_in_same_record = 0
        self.current_row = 0
        self.w = Writer()
        self.position = 0
        self.rec_name = ''
        self.e = ''

    def setupUI(self):
        # Title and window size
        self.setWindowTitle(__version__)
        self.resize(1000, 600)

        self.table = QTableWidget(self)
        self.record_content_table = QTableWidget(self)
        # Load STDF
        self.load_stdf_button = QPushButton(qta.icon('mdi.folder-open', color='blue'), '')
        self.load_stdf_button.clicked.connect(self.load_stdf)
        # Save STDF
        self.save_stdf_button = QPushButton(qta.icon('mdi.content-save', color='blue'), '')
        self.save_stdf_button.clicked.connect(self.save_stdf)
        # Button show next record
        self.show_next_record = QPushButton(qta.icon('mdi.skip-next', color='green'), '')
        self.show_next_record.clicked.connect(self.show_next_content_table)
        # Button show previous record
        self.show_previous_record = QPushButton(qta.icon('mdi.skip-previous', color='red'), '')
        self.show_previous_record.clicked.connect(self.show_previous_content_table)
        # Update modification button
        self.update_mod_record = QPushButton(qta.icon('mdi.arrow-up-bold-box-outline', color='green'), '')
        self.update_mod_record.clicked.connect(self.modify_content_table)
        # increase record button
        self.increase_record = QPushButton(qta.icon('fa.plus-square', color='green'), '')
        self.increase_record.clicked.connect(self.modify_content_table)
        # delete record button
        self.delete_record = QPushButton(qta.icon('fa.minus-square', color='red'), '')
        self.delete_record.clicked.connect(self.modify_content_table)


        row_num = 0  # len(self.stdf_dic)
        col_num = 4

        self.table.setRowCount(row_num)
        self.table.setColumnCount(col_num)
        self.table.setHorizontalHeaderLabels(['Index', 'Records', 'Count', 'Position'])

        self.record_content_table.setRowCount(0)
        self.record_content_table.setColumnCount(3)
        self.record_content_table.setHorizontalHeaderLabels(['Field', 'Type', 'Value'])

        # Config layout
        layout = QGridLayout()
        layout.addWidget(self.load_stdf_button, 0, 0, 1, 1)
        layout.addWidget(self.save_stdf_button, 0, 1, 1, 1)
        layout.addWidget(self.update_mod_record, 0, 2, 1, 1)
        layout.addWidget(self.increase_record, 0, 3, 1, 1)
        layout.addWidget(self.delete_record, 0, 4, 1, 1)
        layout.addWidget(self.table, 1, 0, 32, 18)
        # layout2 = QGridLayout()
        layout.addWidget(self.show_previous_record, 1, 19, 1, 1)
        layout.addWidget(self.show_next_record, 1, 20, 1, 1)
        # self.record_content_table.setLayout(layout2)
        layout.addWidget(self.record_content_table, 2, 19, 31, 12)
        # layout.addWidget(self.record_content_table)
        self.setLayout(layout)

        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellClicked.connect(self.show_content_table)

    def modify_content_table(self):
        data = {}
        for row in range(self.record_content_table.rowCount()):
            tmp_field = self.record_content_table.item(row, 0).text()
            tmp_type = self.record_content_table.item(row, 1).text()
            tmp_val = self.record_content_table.item(row, 2).text()
            if tmp_val == 'N/A': # or tmp_val == ' ': # or tmp_val == '':
                data[tmp_field] = None
            else:
                # long/intger data
                if 'U' in tmp_type or 'I' in tmp_type or 'B' in tmp_type or 'N' in tmp_type:
                    # list data
                    if 'K' in tmp_type:
                        data[tmp_field] = list(
                            map(int, tmp_val.replace('[', '').replace(']', '').replace(' ', '').split(',')))
                    else:
                        data[tmp_field] = int(tmp_val)
                # double data
                elif 'R' in tmp_type:
                    # list data
                    if 'K' in tmp_type:
                        data[tmp_field] = list(
                            map(float, tmp_val.replace('[', '').replace(']', '').replace(' ', '').split(',')))
                    else:
                        data[tmp_field] = float(tmp_val)
                # string data
                elif 'C' in tmp_type:
                    if 'K' in tmp_type:
                        data[tmp_field] = tmp_val.replace('[', '').replace(']', '').replace(' ', '').split(',')
                    else:
                        data[tmp_field] = str(tmp_val)
        # tmp = self.w.pack_record('FAR', data)
        # self.stdf.STDF_IO.seek(self.position)
        # self.stdf.STDF_IO.write(tmp)
        # set the endian
        self.w.e = self.e
        # # This is to overwrite the bytes with same length
        # with open(self.filename, mode='rb+') as fout:
        #     tmp = self.w.pack_record(self.rec_name, data)
        #     fout.seek(self.position)
        #     fout.write(tmp)
        #     # fout.flush()

        # This is to modify/insert bytes into file
        if self.filename.endswith(".std") or self.filename.endswith(".stdf"):
            with open(self.filename, 'rb') as old_buffer, open(self.filename + '_new.stdf', 'wb') as new_buffer:
                # copy until nth byte
                if self.position > 1:
                    tmp = old_buffer.read(self.position)
                    new_buffer.write(tmp)
                # insert new content
                tmp = self.w.pack_record(self.rec_name, data)
                new_buffer.write(tmp)
                # copy the rest of the file
                tmp = old_buffer.read()
                new_buffer.write(tmp)
        elif self.filename.endswith(".gz"):
            with gzip.open(self.filename, 'rb') as old_buffer, gzip.open(self.filename + '_new.std.gz', 'wb') as new_buffer:
                # copy until nth byte
                if self.position > 1:
                    tmp = old_buffer.read(self.position)
                    new_buffer.write(tmp)
                # insert new content
                tmp = self.w.pack_record(self.rec_name, data)
                new_buffer.write(tmp)
                # copy the rest of the file
                tmp = old_buffer.read()
                new_buffer.write(tmp)

    # To show records in stdf file
    def show_table(self):
        row_num = len(self.stdf_dic)
        col_num = 4

        self.table.setRowCount(row_num)
        self.table.setColumnCount(col_num)
        # Fill STDF data to table
        i = 0  # row index
        for key, val in self.stdf_dic.items():
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

    def show_content_table(self, row, col):
        self.index_in_same_record = 0
        self.show_record(row, col, self.index_in_same_record)

    def show_next_content_table(self):
        self.index_in_same_record += 1
        self.show_record(self.current_row, 0, self.index_in_same_record)

    def show_previous_content_table(self):
        self.index_in_same_record -= 1
        self.show_record(self.current_row, 0, self.index_in_same_record)

    # To show fields & data in record
    def show_record(self, row, col, index):
        # Get cell text
        self.current_row = row
        key = self.table.item(row, 0).text() + ' - ' + self.table.item(row, 1).text()
        # Enable STDF record read procedure
        if index < 0 or index > len(self.stdf_dic[key]) - 1:
            index = 0
        self.position = self.stdf_dic[key][index]
        self.stdf.STDF_IO.seek(self.position)
        self.rec_name, header, body = self.stdf.read_record()
        # Refresh the content table
        self.record_content_table.setRowCount(len(body))
        self.record_content_table.setHorizontalHeaderLabels(['Field', 'Type', 'Value'])
        self.record_content_table.setColumnCount(3)
        # Fill the content table
        i = 0
        for k, v in body.items():
            field_item = QTableWidgetItem(str(k))
            type_item = QTableWidgetItem(self.stdf.STDF_TYPE[self.rec_name]['body'][i][1])
            if isinstance(v, list):
                tmp_list = []
                for tmp_v in v:
                    if isinstance(tmp_v, bytes):
                        tmp_list.append(str(bytes.decode(tmp_v)))
                        # val_item = QTableWidgetItem(str(bytes.decode(tmp_v)))
                    else:
                        tmp_list.append(str(tmp_v))
                        # val_item = QTableWidgetItem(str(tmp_v))
                val_item = QTableWidgetItem('[' + ', '.join(tmp_list) + ']')
            else:
                if isinstance(v, bytes):
                    val_item = QTableWidgetItem(str(bytes.decode(v)))
                else:
                    val_item = QTableWidgetItem(str(v))
            self.record_content_table.setItem(i, 0, field_item)
            self.record_content_table.setItem(i, 1, type_item)
            self.record_content_table.setItem(i, 2, val_item)
            print(str(k) + ": " + str(v))
            i += 1

    def load_stdf(self):
        filterboi = 'STDF (*.stdf *.std);;GZ (*.stdf.gz *.std.gz)'
        filepath = QFileDialog.getOpenFileName(
            caption='Open STDF or GZ File', filter=filterboi)
        # Open std file/s
        if len(filepath[0]) == 0:
            pass
        else:
            if len(filepath[0]) > 1:
                self.filename = filepath[0]

                self.stdf = Reader()
                self.stdf.load_stdf_file(stdf_file=self.filename)
                self.stdf_dic = self.get_all_records(self.stdf)
                self.show_table()
                self.setWindowTitle(__version__ + ' - ' + self.filename.split(r'/')[-1])
            else:
                pass

    def save_stdf(self):
        pass

    # Get the records list in stdf file
    def get_all_records(self, stdf):
        stdf.read_rec_list = True
        stdf_dic = {}
        i = 0
        j = 1  # same record cnt
        last_rec = ''
        tmp_list = []
        for rec_name, position in stdf:
            tmp_list = [position]
            if rec_name == last_rec:
                stdf_dic[key] = stdf_dic[key] + tmp_list
            else:
                key = str(i) + ' - ' + rec_name
                stdf_dic[key] = tmp_list
                tmp_list = []
            i += 1
            last_rec = rec_name
        stdf.read_rec_list = False
        self.e = stdf.e
        return stdf_dic


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    app = QApplication(sys.argv)
    viewer = Application()
    viewer.show()
    sys.exit(app.exec_())
