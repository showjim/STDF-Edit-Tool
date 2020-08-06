"""The MIT License (MIT)
Copyright (c) 2016 Cahyo Primawidodo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE."""

from stdf.stdf_reader import Reader
from stdf.stdf_writer import Writer
import logging
from pathlib import Path
import time

__author__ = 'Jerry Zhou'

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
    startt = time.time()
    stdf_dic = get_all_records(stdf)
    if stdf_dic:
        with open('output.txt', mode='wt', encoding='utf-8') as fout:
            # for rec_name, header, body in stdf:
            for item in stdf_dic:
                fout.write(item)

                positon = stdf_dic[item]
                stdf.STDF_IO.seek(positon)
                rec_name, header, body = stdf.read_record()
                for k, v in body.items():
                    fout.write('.')
                    fout.write(str(k) + ": " + str(v))
                    fout.write('|')

                fout.write('\n')
    endt = time.time()
    print('读取时间：', endt - startt)