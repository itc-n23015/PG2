#! python3
# readCensusExcel.py - 郡ごとに人口と人口調査標準地域の数を集計する

import openpyxl, pprint
print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

# TODO: county_dataに郡の人口と地域数を格納する
print('行を読み込んでいます...')
for row in range(2, sheet.max_row + 1):
    # スプレットシートの1行に、1つの人口調査標準地域のデータがある
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
