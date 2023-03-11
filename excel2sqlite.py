import sqlite3
import pandas as pd


def excel2sqlite():
    df = pd.read_excel('labels.xlsx')
    print(df)
    labels, english, chinese = df['label值'], df['英文'], df['中文']
    print(labels)

    conn = sqlite3.connect('labels.db')
    cursor = conn.cursor()

    sql = '''DROP TABLE IF EXISTS labels'''
    cursor.execute(sql)
    sql = '''CREATE TABLE labels (labelNumber INTEGER PRIMARY KEY, english varchar(255), chinese varchar(255))'''
    cursor.execute(sql)

    for i in range(0, len(labels)):
        try:
            cursor.execute('INSERT INTO labels(labelNumber, english, chinese) VALUES(?, ?, ?)',
                           (int(labels[i]), english[i], chinese[i]))
        except:
            print('error line data:', labels[i], english[i], chinese[i])

    conn.commit()
    cursor.close()


if __name__ == '__main__':
    excel2sqlite()
