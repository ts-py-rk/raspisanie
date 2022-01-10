import pytils
import sqlite3
import calendar
import datetime
import logging

def month_from_base():
    # print(f'START month_from_base()')
    # logging.info(f'START month_from_base()')
    conn = sqlite3.connect(r'db.sqlite3')
    cur = conn.cursor()
    # print('читаем базу данных')
    cur.execute("SELECT * FROM duty_month;")
    all_results = cur.fetchall()
    first_day = all_results[0][1]
    first_month = int(first_day.split('-')[1])
    # print(f'{first_month = }')
    conn.close()
    # print(f'STOP month_from_base()')
    # logging.info(f'STOP month_from_base()')
    return first_month

def now_month():
    # print(f'START now_month()')
    # logging.info(f'START now_month()')
    c = calendar.Calendar()
    today = datetime.datetime.now()
    mes = today.month
    # print(f'{mes = }')
    # print(f'STOP now_month()')
    # logging.info(f'STOP now_month()')
    return mes

def check(read_m, now_m):
    # print(f'START check({read_m}, {now_m})')
    # logging.info(f'START check({read_m}, {now_m})')
    if read_m != now_m:
        message = '    НАДО ОБНОВИТЬ РАСПИСАНИЕ!!!'
        print(f'{message}')
        logging.error(f'{message}')
        conn = sqlite3.connect(r'db.sqlite3')
        cur = conn.cursor()
        # print('читаем базу данных')
        cur.execute("SELECT * FROM duty_month;")
        all_results = cur.fetchall()
        # for a_r in all_results:
        #     print(a_r)
        # print(f'{len(all_results) = }')
        last_id = all_results[-1][0]
        # print(f'{last_id = }')
        # print('удаляем лишнее')
        for i in range(0, (last_id + 1)):
            try:
                # print(f'{i = } - пытаюсь удалить')
                cur.execute(f"DELETE FROM duty_month WHERE id='{i}';")
            except:
                print(f'{i = } - фигня вышла')
                logging.error(f'{i = } - фигня вышла')
        # print('читаем базу данных')
        cur.execute("SELECT * FROM duty_month;")
        # all_results = cur.fetchall()
        # for a_r in all_results:
        #     print(a_r)
        c = calendar.Calendar()
        today = datetime.datetime.now()
        god, mes = today.year, today.month
        table = []
        for i in c.itermonthdays(god, mes):
            stro = []
            if i != 0:
                day = datetime.date(god, mes, i)
                dayy = str(day)
                n_d = calendar.weekday(god, mes, i)
                day_of_week = pytils.dt.ru_strftime(
                    u"%a",
                    inflected=True,
                    date=day
                )
                if n_d in range(5):
                    stro.append(i)
                    stro.append(dayy)
                    stro.append(day_of_week)
                    stro.append(36)
                    stro.append(1)
                    stro.append(1)
                    table.append(stro)
                elif n_d == 5:
                    pass
        # print(f'НАДО ЧТО БЫ ВОТ ТАК:')
        # for t in table:
        #     print(t)
        cur.executemany(
            "INSERT INTO duty_month VALUES(?, ?, ?, ?, ?, ?);",
            table
        )
        conn.commit()
        conn.close()
    else:
        pass
        # print(f'ТИПА ВСЕ ОК')
    # print(f'STOP check({read_m}, {now_m})')
    # logging.info(f'STOP check({read_m}, {now_m})')
    return