import os
import sqlite3
import openpyxl


start_data = {'slide_1': {'all_status_L1': {151: 'План', 152: 'В работе', 153: 'Завершено', 159: 'Не поступило'}, 'all_status_L2': {1510: 'План', 1521: 'Инициация', 1522: 'Прием заявок', 1523: 'Анализ заявок', 1524: 'Оценка ЦП', 1525: 'Подведение итогов', 1531: 'Утверждение ЗК', 1532: 'Завершено выбором', 1539: 'Отменено/Без выбора', 1590: 'План (не поступил)'}, 'all_customers': {}, 'all_services_L3': {},
    'step_numb': 'руб',
  'summ': 0,
  'all': {'План': 0, 'В работе': 0, 'Завершено': 0, 'Не поступило': 0},
  'table': {'НМЦ': {'План': 0,
    'В работе': 0,
    'Завершено': 0,
    'Не поступило': 0},
   'Отб': {'План': 0, 'В работе': 0, 'Завершено': 0, 'Не поступило': 0},
   'Лот(ов)': {'План': 0, 'В работе': 0, 'Завершено': 0, 'Не поступило': 0}},
  'legend': ['0.0 руб', '0.0 руб', 0, 0, 0, 0],
  'hist_1': {151: {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0},
   152: {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0},
   153: {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0},
   159: {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0}},
  'hist_2': {151: {}, 152: {}, 153: {}, 159: {}},
  'hist_3': {151: {}, 152: {}, 153: {}, 159: {}}},
 'slide_2': {'all_status_L1': {151: 'План', 152: 'В работе', 153: 'Завершено', 159: 'Не поступило'}, 'all_status_L2': {1510: 'План', 1521: 'Инициация', 1522: 'Прием заявок', 1523: 'Анализ заявок', 1524: 'Оценка ЦП', 1525: 'Подведение итогов', 1531: 'Утверждение ЗК', 1532: 'Завершено выбором', 1539: 'Отменено/Без выбора', 1590: 'План (не поступил)'}, 'all_customers': {}, 'all_services_L3': {},
     'step_numb': 'руб',
  'summ': 0,
  'legend': ['0.0 руб', 0, 0],
  'fact': [0, 0],
  'table': {'КО (1 этап)': {'lot': 0,
    'fact': None,
    'n_fact': None,
    'cel': None},
   'КО (2 этап)': {'lot': 0, 'fact': None, 'n_fact': None, 'cel': None}},
  'hist_1': {1: {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0},
   2: {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0},
   3: {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0}},
  'hist_2': {1: {}, 2: {}, 3: {}},
  'hist_3': {1: {}, 2: {}, 3: {}}},
 'slide_3': {'all_status_L1': {151: 'План', 152: 'В работе', 153: 'Завершено', 159: 'Не поступило'}, 'all_status_L2': {1510: 'План', 1521: 'Инициация', 1522: 'Прием заявок', 1523: 'Анализ заявок', 1524: 'Оценка ЦП', 1525: 'Подведение итогов', 1531: 'Утверждение ЗК', 1532: 'Завершено выбором', 1539: 'Отменено/Без выбора', 1590: 'План (не поступил)'}, 'all_customers': {}, 'all_services_L3': {},
     'step_numb': 'руб',
  'summ': 0,
  'legend': ['0.0 руб', 0, 0],
  'competition': 0,
  'table': {'ЗКО': {'Лот(ов)': 0, 'Заявки': None, 'Ком.': None},
   'ОКО': {'Лот(ов)': 0, 'Заявки': None, 'Ком.': None}},
  'hist_1': {'Норма': {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0},
   'Лоты с низкой конкуренцией': {1510: 0,
    1521: 0,
    1522: 0,
    1523: 0,
    1524: 0,
    1525: 0,
    1531: 0,
    1532: 0,
    1539: 0,
    1590: 0}},
  'hist_2': {'Норма': {}, 'Лоты с низкой конкуренцией': {}},
  'hist_3': {'Норма': {}, 'Лоты с низкой конкуренцией': {}}},
 'slide_4': {'all_status_L1': {151: 'План', 152: 'В работе', 153: 'Завершено', 159: 'Не поступило'}, 'all_status_L2': {1510: 'План', 1521: 'Инициация', 1522: 'Прием заявок', 1523: 'Анализ заявок', 1524: 'Оценка ЦП', 1525: 'Подведение итогов', 1531: 'Утверждение ЗК', 1532: 'Завершено выбором', 1539: 'Отменено/Без выбора', 1590: 'План (не поступил)'}, 'all_customers': {}, 'all_services_L3': {},
     'step_numb': 'руб',
  'summ': 0,
  'legend': ['0.0 руб', 0, 0],
  'effect': 0,
  'table': {'ЗКО': {'Лот(ов)': 0, 'млрд': 0.0, '%': 0},
   'ОКО': {'Лот(ов)': 0, 'млрд': 0.0, '%': 0}},
  'voronka': [[(0,)], [(0,)], [(0,)]],
  'hist_2': {'Лоты с ЦП > НМЦ': {}, 'Лоты с ЦП < НМЦ': {}},
  'hist_3': {'Лоты с ЦП > НМЦ': {}, 'Лоты с ЦП < НМЦ': {}}},
 'all_status_L1': {151: 'План',
  152: 'В работе',
  153: 'Завершено',
  159: 'Не поступило'},
 'all_status_L2': {1510: 'План',
  1521: 'Инициация',
  1522: 'Прием заявок',
  1523: 'Анализ заявок',
  1524: 'Оценка ЦП',
  1525: 'Подведение итогов',
  1531: 'Утверждение ЗК',
  1532: 'Завершено выбором',
  1539: 'Отменено/Без выбора',
  1590: 'План (не поступил)'},
 'all_customers': {},
 'all_services_L3': {}}


def update_xl(file_path = 'Справочники.xlsx'):
    if os.path.exists('example.db'):
        os.remove('example.db')
        print('удалил')
    else:
        print('не удалил')
        pass
    print(file_path)

    # Определение структуры таблиц
    table_structure = {
        'Organizators': [
            ('ID', 'string', ''),
            ('Name', 'TEXT', 'NOT NULL')
        ],
        'Cutomers': [
            ('ID', 'int', ''),
            ('Name', 'TEXT', 'NOT NULL')
        ],
        'Partners': [
            ('INN', 'char(12)', ''),
            ('KPP', 'char(9)', ''),
            ('Name', 'TEXT', ''),
            ('Address', 'TEXT', ''),
            ('potIndex', 'TEXT', ''),
            ('phone', 'TEXT', '')
        ],
        'Services_L3': [
            ('L3_ID', 'INT', ''),
            ('L3_N', 'INT', ''),
            ('L3_Name', 'TEXT', ''),
            ('L3_Name2', 'TEXT', ''),
            ('L3_Name3', 'TEXT', '')
        ],
        'Services_L4': [
            ('L4_ID', 'INT', ''),
            ('L3_N', 'INT', ''),
            ('L4_Name', 'TEXT', ''),
            ('L4_NameShort', 'TEXT', ''),
            ('L4_Name2', 'TEXT', ''),
            ('L4_P', 'TEXT', '')
        ],

        'Status_L1': [
            ('L1_ID', 'INT', ''),
            ('L1_Name', 'TEXT', ''),
            ('Comments', 'TEXT', '')
        ],
        'Status_L2': [
            ('L2_ID', 'INT', ''),
            ('L1_ID', 'int', ''),
            ('L2_N', 'TEXT', ''),
            ('L2_Name', 'TEXT', '')
        ],
        'Status_L3': [
            ('L3_ID', 'INT', ''),
            ('L2_ID', 'int', ''),
            ('L2_Name', 'TEXT', ''),
            ('L3_N', 'TEXT', ''),
            ('L3_Name', 'TEXT', ''),
            ('Comment', 'TEXT', '')
        ],
        'Status_L4': [
            ('L4_ID', 'INT', ''),
            ('L3_ID', 'TEXT', ''),
            ('L3_N', 'INT', ''),
            ('L4_Name', 'TEXT', '')
        ],

        'Method_L3': [
            ('L3_ID', 'INT', ''),
            ('L3_NameShort', 'TEXT', ''),
            ('L3_PUBFORM', 'TEXT', ''),
            ('L3_PROCFORM', 'TEXT', ''),
            ('ProcFormaN', 'INT', ''),
            ('DurationKPI1', 'TEXT', ''),
            ('L2_ID', 'INT', ''),
            ('MinCompetition', 'INT', '')
        ],

        'Lots': [
            ('lotId', 'TEXT', ''),
            ('procId', 'TEXT', ''),
            ('finishYear', 'INT', ''),
            ('procedureYear', 'INT', ''),
            ('timeliness', 'INT', ''),
            ('timelinessNorm', 'INT', ''),
            ('serviceL4_ID', 'TEXT', ''),
            ('lotDescription', 'TEXT', ''),
            ('procedureDescription', 'TEXT', ''),
            ('customerId', 'INT', ''),
            ('organozatorId', 'INT', ''),
            ('startPrice', 'INT', ''),
            ('countDays', 'INT', ''),
            ('countDaysNorm', 'INT', ''),
            ('statusL3_id', 'INT', ''),
            ('stateCode', 'INT', ''),
            ('startDate', 'DATE', ''),
            ('dateProvide', 'DATE', ''),
            ('planDateFinish', 'DATE', ''),
            ('factDateFinish', 'DATE', ''),
            ('Competition', 'INT', ''),
            ('Competitors', 'TEXT', ''),
            ('round1Rpice', 'INT', ''),
            ('round2Rpice', 'INT', ''),
            ('round3Rpice', 'INT', ''),
            ('finialPrice', 'INT', ''),
            ('offerPrice', 'INT', ''),
            ('purchaser', 'TEXT', ''),
            ('organizator', 'TEXT', ''),
            ('pricingSpec', 'TEXT', ''),
            ('methodL3_id', 'INT', '')
        ],

        'Competitors': [
            ('idLot', 'TEXT', ''),
            ('idKA', 'TEXT', ''),
            ('Status', 'INT', ''),
            ('Position', 'INT', '')
        ]
    }

    sheet_name = list(table_structure.keys())

    workbook = openpyxl.load_workbook(file_path)

    # Создание SQLite базы данных и подключение к ней
    db_path = 'example.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for sh in sheet_name:
        sheet = workbook[sh]
        # Создание таблицы в базе данных
        columns = ', '.join([f"{column[0]} {column[1]} {column[2]}" for column in table_structure[sh]])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {sh} ({columns})"
        cursor.execute(create_table_query)

        # Вставка данных из файла Excel в таблицу базы данных
        for row in sheet.iter_rows(min_row=2, values_only=True):
            cursor.execute(f"INSERT INTO {sh} VALUES ({', '.join(['?' for _ in row])})", row)

    # Фиксация изменений и закрытие подключения к базе данных
    conn.commit()
    conn.close()


startDate = None
factDateFinish = None
customer = None
services_L3 = None
procedureYear = None
organizator = None


def new_start_data_def(
        # startDate = startDate, factDateFinish = factDateFinish, customer = customer, services_L3 = services_L3, procedureYear = procedureYear, organizator = organizator
):
    start_data = Update_Data("example.db",
                                       factDateFinish=factDateFinish,
                                       startDate=startDate,
                                       customer=customer,
                                       services_L3=services_L3,
                                       procedureYear=procedureYear,
                                       organizator=organizator).results_data()
    print(factDateFinish, startDate, customer, services_L3, procedureYear, organizator)

    return start_data




class Update_Data():
    def __init__(self, db_name, startDate=startDate, factDateFinish=factDateFinish, customer=customer,
                 services_L3=services_L3,
                 procedureYear=procedureYear, organizator=organizator):
        self.db_name = db_name
        self.conn, self.cursor = None, None
        self.startDate = startDate
        self.factDateFinish = factDateFinish
        self.procedureYear = procedureYear
        self.customer = customer
        self.services_L3 = services_L3
        self.organizator = organizator

    def _connect(self):
        if self.conn is None or self.cursor is None:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def filtrated_data(self):
        self._connect()
        query = "DROP TABLE IF EXISTS Lots_F;"
        self.cursor.execute(query)

        query = """
            CREATE TABLE Lots_F AS
            SELECT * FROM Lots
            JOIN Services_L4 as SL4 ON Lots.serviceL4_ID = SL4.L4_ID
            JOIN Services_L3 as SL3 ON SL4.L3_N = SL3.L3_N
            WHERE 1
        """

        params = []

        if self.startDate:  # Диапазон дат по дате инициации отбора
            query += " AND Lots.startDate >= DATE(?) AND Lots.startDate <= DATE(?)"
            params.extend(self.startDate)

        if self.factDateFinish:  # Диапазон дат подведения итогов по дате протокола ЗК
            query += " AND Lots.factDateFinish >= DATE(?) AND Lots.factDateFinish <= DATE(?)"
            params.extend(self.factDateFinish)

        if self.procedureYear:
            query += " AND Lots.procedureYear = ?"
            params.append(self.procedureYear)

        if self.customer:
            query += " AND Lots.customerId IN ({})"
            query = query.format(",".join("?" * len(self.customer)))
            params.extend(self.customer)

        if self.services_L3:
            query += " AND SL3.L3_N IN ({})"
            query = query.format(",".join("?" * len(self.services_L3)))
            params.extend(self.services_L3)

        if self.organizator:
            query += " AND Lots.organozatorId = ?"
            params.append(self.organizator)

        self.cursor.execute(query, params)

        self.cursor.execute("SELECT * FROM Lots_F")
        temp_results = self.cursor.fetchall()

        self.conn.commit()

    def all_customers(self):
        self._connect()
        query = """
              SELECT Cutomers.ID, Cutomers.Name
              FROM Lots_F
              JOIN Cutomers ON Lots_F.customerId = Cutomers.ID
              GROUP BY Cutomers.Name
          """

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def all_services_L3(self):
        self._connect()
        query = """
            SELECT Services_L3.L3_N, Services_L3.L3_Name
            FROM Lots_F
            JOIN Services_L4 ON Lots_F.serviceL4_ID = Services_L4.L4_ID
            JOIN Services_L3 ON Services_L4.L3_N = Services_L3.L3_N
            GROUP BY Services_L3.L3_N
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def all_status_L1(self):
        self._connect()
        query = """
            SELECT L1_ID, L1_Name
            FROM Status_L1
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def all_status_L2(self):
        self._connect()
        query = """
            SELECT L2_ID, L2_Name
            FROM Status_L2
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def all_contragents(self):
        self._connect()
        query = """
            SELECT INN, Name
            FROM Partners
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results


    ### Первый слайд
    def get_sum_by_status_l1(self):
        self._connect()
        query = """
            SELECT L1.L1_Name, SUM(startPrice) as total_sum, COUNT(startPrice)
            FROM Lots_F
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            JOIN Status_L1 as L1 ON L2.L1_ID = L1.L1_ID
            GROUP BY L1.L1_ID
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {status_L1[1]: [0, 0] for status_L1 in self.all_status_L1()}

        for row in results:
            L1_Name, SUM, count = row
            result_dict[L1_Name] = [SUM, count]

        return result_dict

    def get_сount_otb_by_status_l1(self):  ## Количесвто Отборов
        self._connect()
        query = """
            SELECT L1.L1_Name, COUNT(startPrice)
            FROM Lots_F
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            JOIN Status_L1 as L1 ON L2.L1_ID = L1.L1_ID
            GROUP BY L1.L1_ID
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {status_L1[1]: 0 for status_L1 in self.all_status_L1()}

        for row in results:
            L1_Name, count = row
            result_dict[L1_Name] = count

        return result_dict

    def get_сount_lots_by_status_l1(self):  ## Количесвто Лотов
        self._connect()
        query = """
            SELECT L1.L1_Name, COUNT(Competitors.idKA)
            FROM Lots_F
            JOIN Competitors ON Lots_F.lotId = Competitors.idLot
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            JOIN Status_L1 as L1 ON L2.L1_ID = L1.L1_ID
            GROUP BY L1.L1_ID
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {status_L1[1]: 0 for status_L1 in self.all_status_L1()}

        for row in results:
            L1_Name, count = row
            result_dict[L1_Name] = count

        return result_dict

    def get_by_status_l2_sum_otb(self):
        self._connect()
        query = """
            SELECT L2.L2_ID, SUM(startPrice), COUNT(startPrice)
            FROM Lots_F
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            GROUP BY L2.L2_ID, L2.L2_Name
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {status_L2[0]: [0, 0] for status_L2 in self.all_status_L2()}

        for row in results:
            L2_ID, SUM, count = row
            result_dict[L2_ID] = [SUM, count]

        return result_dict


    def get_by_status_l2_lots(self):
        self._connect()
        query = """
            SELECT L2.L2_ID, COUNT(Competitors.idKA)
            FROM Lots_F
            JOIN Competitors ON Lots_F.lotId = Competitors.idLot
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            GROUP BY L2.L2_ID
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {status_L2[0]: 0 for status_L2 in self.all_status_L2()}

        for row in results:
            L2_ID, count = row
            result_dict[L2_ID] = count

        return result_dict

    def get_by_status_l2_lots_hist_1(self):
        self._connect()

        query = """
            SELECT L1.L1_ID, L2.L2_ID, COUNT(Competitors.idKA)
            FROM Lots_F
            JOIN Competitors ON Lots_F.lotId = Competitors.idLot
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            JOIN Status_L1 as L1 ON L2.L1_ID = L1.L1_ID
            GROUP BY L1.L1_ID, L2.L2_ID
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {status_L1[0]: {status_L2[0]: 0 for status_L2 in self.all_status_L2()} for status_L1 in
                       self.all_status_L1()}

        for row in results:
            L1_ID, L2_ID, count = row
            result_dict[L1_ID][L2_ID] = count

        return result_dict

    def get_by_v_rabote_po_uclugam(self):
        self._connect()
        query = """
            SELECT SL4.L3_N, SL3.L3_Name, L2.L1_ID, COUNT(serviceL4_ID)
            FROM Lots_F
            JOIN Services_L4 as SL4 ON Lots_F.serviceL4_ID = SL4.L4_ID
            JOIN Services_L3 as SL3 ON SL4.L3_N = SL3.L3_N
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            GROUP BY SL4.L3_N, L2.L1_ID
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {status_L1[0]: {SL3[0]: 0 for SL3 in self.all_services_L3()} for status_L1 in
                       self.all_status_L1()}

        for row in results:
            l3_n, l3_name, l1_id, count = row
            result_dict[l1_id][l3_n] = count

        return result_dict

    def get_by_v_rabote_po_zakaz(self):
        self._connect()
        query = """
            SELECT Cust.ID, Cust.Name, L2.L1_ID, COUNT(customerId)
            FROM Lots_F
            JOIN Cutomers as Cust ON Lots_F.customerId = Cust.ID
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            GROUP BY Cust.ID, L2.L1_ID
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {status_L1[0]: {custid[0]: 0 for custid in self.all_customers()} for status_L1 in
                       self.all_status_L1()}

        for row in results:
            cust_id, cust_name, l1_id, count = row
            result_dict[l1_id][cust_id] = count

        return result_dict

    ### Второй слайд

    def get_by_sv_fact(self):
        self._connect()
        query = """
            SELECT COUNT(timeliness)
            FROM Lots_F
            WHERE timeliness='1'
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        return 100 * results[0][0] / (
                self.get_by_status_l2_sum_otb()[1532][1] + self.get_by_status_l2_sum_otb()[1539][1]) if self.get_by_status_l2_sum_otb()[1539][1] != 0 else 0


    def get_by_sv_N_fact(self):
        self._connect()
        query = """
            SELECT COUNT(timelinessNorm)
            FROM Lots_F
            WHERE timelinessNorm='1'
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        return 100 * results[0][0] / (
                self.get_by_status_l2_sum_otb()[1532][1] + self.get_by_status_l2_sum_otb()[1539][1]) if self.get_by_status_l2_sum_otb()[1539][1] != 0 else 0

    def get_by_table_slider_2(self, L3_ID=(151, 152, 154, 155)):
        self._connect()
        query = """
            SELECT AVG(countDays), AVG(countDaysNorm), AVG(Method_L3.DurationKPI1), COUNT(lotId)
            FROM Lots_F
            JOIN Method_L3 ON Lots_F.methodL3_id = Method_L3.L3_ID
            WHERE Method_L3.L3_ID IN {}
        """.format(L3_ID)

        self.cursor.execute(query)
        results = self.cursor.fetchall()[0]
        return {'lot': results[3], 'fact': round(results[0],1), 'n_fact': round(results[1],1), 'cel': results[2]}

    def get_by_status_l2_slider_2(self):
        self._connect()
        query = """
            SELECT stateCode, L2.L2_ID, COUNT(startPrice)
            FROM Lots_F
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            GROUP BY stateCode, L2.L2_ID
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        s_c = [1, 2, 3]
        result_dict = {sc: {l2_id[0]: 0 for l2_id in self.all_status_L2()} for sc in s_c}

        for row in results:
            stateCode, l2_id, count = row
            result_dict[stateCode][l2_id] = count

        return result_dict

    def get_by_v_rabote_po_uclugam_slider_2(self):
        self._connect()
        query = """
            SELECT stateCode, SL4.L3_N, SL3.L3_Name, COUNT(serviceL4_ID)
            FROM Lots_F
            JOIN Services_L4 as SL4 ON Lots_F.serviceL4_ID = SL4.L4_ID
            JOIN Services_L3 as SL3 ON SL4.L3_N = SL3.L3_N
            GROUP BY stateCode, SL4.L3_N
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        s_c = [1, 2, 3]
        result_dict = {sc: {services_L3_id[0]: 0 for services_L3_id in self.all_services_L3()} for sc in s_c}

        for row in results:
            l3_n, l1_id, l3_name, count = row
            result_dict[l3_n][l1_id] = count

        return result_dict

    def get_by_v_rabote_po_zakaz_slider_2(self):
        self._connect()
        query = """
            SELECT stateCode, Cust.ID, Cust.Name, COUNT(serviceL4_ID)
            FROM Lots_F
            JOIN Cutomers as Cust ON Lots_F.customerId = Cust.ID
            GROUP BY stateCode, Cust.ID
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        s_c = [1, 2, 3]
        result_dict = {sc: {cust_id[0]: 0 for cust_id in self.all_customers()} for sc in s_c}

        for row in results:
            l3_n, l1_id, l3_name, count = row
            result_dict[l3_n][l1_id] = count

        return result_dict

    ### Третий слайд

    def get_by_competition(self):
        self._connect()
        query = """
            SELECT AVG(Competition)
            FROM Lots_F
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        if results[0][0] is not None:
            return results[0][0]
        else:
            return 0

    def get_by_table_slider_3(self, L3_ID=(154, 155, 156)):
        self._connect()
        query = """
            SELECT COUNT(lotId), AVG(Competition), AVG(Method_L3.MinCompetition)
            FROM Lots_F
            JOIN Method_L3 ON Lots_F.methodL3_id = Method_L3.L3_ID
            WHERE Method_L3.L3_ID IN {}
        """.format(L3_ID)

        self.cursor.execute(query)
        results = self.cursor.fetchall()[0]

        return {'Лот(ов)': results[0], 'Конкуренция': round(results[1],1), 'Ком.': results[2]}


    def get_by_status_l2_slider_3(self, comp='>'):
        self._connect()
        query = """
            SELECT L2.L2_ID, COUNT(lotId)
            FROM Lots_F
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            JOIN Method_L3 ON Lots_F.methodL3_id = Method_L3.L3_ID
            WHERE Lots_F.Competition {} Method_L3.MinCompetition
            GROUP BY L2.L2_ID
        """.format(comp)

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {L2_ID[0]: 0 for L2_ID in self.all_status_L2()}

        for row in results:
            L2_ID, count = row
            result_dict[L2_ID] = count

        return result_dict


    def get_by_v_rabote_po_uclugam_slider_3(self, comp='>'):
        self._connect()
        query = """
            SELECT SL3.L3_N, COUNT(lotId)
            FROM Lots_F
            JOIN Services_L4 as SL4 ON Lots_F.serviceL4_ID = SL4.L4_ID
            JOIN Services_L3 as SL3 ON SL4.L3_N = SL3.L3_N
            JOIN Method_L3 ON Lots_F.methodL3_id = Method_L3.L3_ID
            WHERE Lots_F.Competition {} Method_L3.MinCompetition
            GROUP BY SL3.L3_N
        """.format(comp)

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {SL3[0]: 0 for SL3 in self.all_services_L3()}

        for row in results:
            SL3, count = row
            result_dict[SL3] = count

        return result_dict


    def get_by_v_rabote_po_zakaz_slider_3(self, comp='>'):
        self._connect()
        query = """
            SELECT Cust.ID, COUNT(lotId)
            FROM Lots_F
            JOIN Cutomers as Cust ON Lots_F.customerId = Cust.ID
            JOIN Method_L3 ON Lots_F.methodL3_id = Method_L3.L3_ID
            WHERE Lots_F.Competition {} Method_L3.MinCompetition
            GROUP BY Cust.ID
        """.format(comp)

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {cust[0]: 0 for cust in self.all_customers()}

        for row in results:
            cust, count = row
            result_dict[cust] = count

        return result_dict


    ### Четвертый слайд

    def get_by_effect(self):
        self._connect()
        query = """
            SELECT SUM(startPrice), SUM(finialPrice)
            FROM Lots_F
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        if results[0][0] is not None and results[0][1] is not None:
            return 100 * results[0][1] / results[0][0] - 100
        else:
            return 0

    def get_by_table_slider_4(self, L3_ID=(154, 155, 156)):
        self._connect()
        query = """
            SELECT Count(lotId), SUM(finialPrice), SUM(startPrice)
            FROM Lots_F
            JOIN Method_L3 ON Lots_F.methodL3_id = Method_L3.L3_ID
            WHERE Method_L3.L3_ID IN {}
        """.format(L3_ID)

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        lotov = results[0][0]
        mlrd1 = results[0][1] if results[0][1] is not None else 0
        mlrd2 = results[0][2] if results[0][2] is not None else 0
        percent = 100 * mlrd1 / mlrd2 - 100 if mlrd2 != 0 else 0

        return {'Лот(ов)': lotov, 'млрд': round((mlrd1 - mlrd2)/1000000000,2), '%': round(percent,2)}


    def voronka_effect(self, round=1):
        self._connect()
        query = """
            SELECT COUNT(lotId)
            FROM Lots_F
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            WHERE ((round{}Rpice - startPrice) <= 0) AND (L2.L2_ID = 1532)
        """.format(round)

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        return results

    def get_by_v_rabote_po_uclugam_slide_4(self, option='>'):
        self._connect()
        query = """
            SELECT SL4.L3_N, SL3.L3_Name, COUNT(lotId)
            FROM Lots_F
            JOIN Services_L4 as SL4 ON Lots_F.serviceL4_ID = SL4.L4_ID
            JOIN Services_L3 as SL3 ON SL4.L3_N = SL3.L3_N
            WHERE finialPrice {} startPrice
            GROUP BY SL4.L3_N
        """.format(option)

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {SL3[0]: 0 for SL3 in self.all_services_L3()}

        for row in results:
            SL3, l3_name, count = row
            result_dict[SL3] = count

        return result_dict

    def get_by_v_rabote_po_zakaz_slide_4(self, option='>'):
        self._connect()
        query = """
            SELECT Cust.ID, Cust.Name, COUNT(serviceL4_ID)
            FROM Lots_F
            JOIN Cutomers as Cust ON Lots_F.customerId = Cust.ID
            WHERE finialPrice {} startPrice
            GROUP BY Cust.ID
        """.format(option)

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        result_dict = {cust_id[0]: 0 for cust_id in self.all_customers()}

        for row in results:
            cust, cust_name, count = row
            result_dict[cust] = count

        return result_dict

    def get_by_cards_current_status_l1(self, l2):
        self.filtrated_data()
        self._connect()
        query = """
            SELECT Cust.Name, procId, Competition, procedureDescription, 
            (julianday(factDateFinish)- julianday(startDate)), (finialPrice-startPrice)
            FROM Lots_F
            JOIN Cutomers as Cust ON Lots_F.customerId = Cust.ID
            JOIN Status_L3 as L3 ON Lots_F.statusL3_id = L3.L3_ID
            JOIN Status_L2 as L2 ON L3.L2_ID = L2.L2_ID
            WHERE L3.L2_ID == {}
        """.format(l2)

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        return results

    def step_numb(self):
        nmc = [self.get_sum_by_status_l1()[x][0] for x in self.get_sum_by_status_l1().keys()]
        len_ = 3
        numb = nmc[-2]
        for i in range(5):
           if len(str(numb))>len_:
              len_ = len_ + 3
           else:
              break
        slov = {'0':'руб','3':'тыс','6':'млн','9':'млрд','12':'трл','15':'квдрл'}
        return [10**(len_ - 3), slov[str(len_ - 3)]]


    def results_data(self):
        print('ОБНОВЛЕНИЕ !!!')
        self.filtrated_data()
        all_status_L1 = {x[0]: x[1] for x in self.all_status_L1()},
        all_status_L2 = {x[0]: x[1] for x in self.all_status_L2()},
        all_customers = {x[0]: x[1] for x in self.all_customers()},
        all_services_L3 = {x[0]: x[1] for x in self.all_services_L3()}
        all_contragents = {x[0]: x[1] for x in self.all_contragents()}
        results = {
            'slide_1': {
                'all_status_L1': all_status_L1[0],
                'all_status_L2': all_status_L2[0],
                'all_customers': all_customers[0],
                'all_services_L3': all_services_L3,
                'step_numb': self.step_numb()[1],
                'summ': round(sum([self.get_sum_by_status_l1()[x][0] for x in self.get_sum_by_status_l1().keys()])/self.step_numb()[0]),
                'all': {x: (self.get_sum_by_status_l1()[x][1] / (sum([self.get_sum_by_status_l1()[x][1] for x in self.get_sum_by_status_l1().keys()])))
                if sum([self.get_sum_by_status_l1()[x][1] for x in self.get_sum_by_status_l1().keys()]) != 0 else 0 * 100
                        for x in self.get_sum_by_status_l1().keys()},
                'table': {
                    'НМЦ': {x: round(self.get_sum_by_status_l1()[x][0]/self.step_numb()[0]) for x in self.get_sum_by_status_l1().keys()},
                    'Отб': self.get_сount_otb_by_status_l1(),
                    'Лот(ов)': self.get_сount_lots_by_status_l1()
                },
                'legend': [
                    str(round(self.get_by_status_l2_sum_otb()[1532][0]/self.step_numb()[0],1))+' '+self.step_numb()[1],
                    str(round(self.get_by_status_l2_sum_otb()[1539][0]/self.step_numb()[0],1))+' '+self.step_numb()[1],
                    self.get_by_status_l2_sum_otb()[1532][1],
                    self.get_by_status_l2_sum_otb()[1539][1],
                    self.get_by_status_l2_lots()[1532],
                    self.get_by_status_l2_lots()[1539]
                ],
                'hist_1': self.get_by_status_l2_lots_hist_1(),
                'hist_2': self.get_by_v_rabote_po_uclugam(),
                'hist_3': self.get_by_v_rabote_po_zakaz()
            },
            'slide_2': {
                'all_status_L1': all_status_L1[0],
                'all_status_L2': all_status_L2[0],
                'all_customers': all_customers[0],
                'all_services_L3': all_services_L3,
                'step_numb': self.step_numb()[1],
                'summ': round(
                    100 * self.get_by_status_l2_sum_otb()[1532][0] / self.get_by_status_l2_sum_otb()[1539][0])
                    if self.get_by_status_l2_sum_otb()[1539][0] != 0 else 0,
                'legend': [
                    str(round(self.get_by_status_l2_sum_otb()[1532][0]/self.step_numb()[0],1))+' '+self.step_numb()[1],
                    self.get_by_status_l2_sum_otb()[1532][1],
                    self.get_by_status_l2_lots()[1532]
                ],
                'fact': [
                    self.get_by_sv_fact(),
                    self.get_by_sv_N_fact()
                ],
                'table': {
                    'КО (1 этап)': self.get_by_table_slider_2(L3_ID=(151, 152, 154, 155)),
                    'КО (2 этап)': self.get_by_table_slider_2(L3_ID=(153, 156))
                },
                'hist_1': self.get_by_status_l2_slider_2(),
                'hist_2': self.get_by_v_rabote_po_uclugam_slider_2(),
                'hist_3': self.get_by_v_rabote_po_zakaz_slider_2()
            },
            'slide_3': {
                'all_status_L1': all_status_L1[0],
                'all_status_L2': all_status_L2[0],
                'all_customers': all_customers[0],
                'all_services_L3': all_services_L3,
                'step_numb': self.step_numb()[1],
                'summ': round(
                    100 * self.get_by_status_l2_sum_otb()[1532][0] / self.get_by_status_l2_sum_otb()[1539][0])
                    if self.get_by_status_l2_sum_otb()[1539][0] != 0 else 0,
                'legend': [
                    str(round(self.get_by_status_l2_sum_otb()[1532][0]/self.step_numb()[0],1))+' '+self.step_numb()[1],
                    self.get_by_status_l2_sum_otb()[1532][1],
                    self.get_by_status_l2_lots()[1532]
                ],
                'competition': round(self.get_by_competition(),2),
                'table': {
                    'ЗКО': self.get_by_table_slider_3(L3_ID=(154, 155, 156)),
                    'ОКО': self.get_by_table_slider_3(L3_ID=(151, 152, 153))
                },
                'hist_1': {
                    'Норма': self.get_by_status_l2_slider_3(comp='>'),
                    'Лоты с низкой конкуренцией': self.get_by_status_l2_slider_3(comp='<')
                },
                'hist_2': {
                    'Норма': self.get_by_v_rabote_po_uclugam_slider_3(comp='>'),
                    'Лоты с низкой конкуренцией': self.get_by_v_rabote_po_uclugam_slider_3(comp='<')
                },
                'hist_3': {
                    'Норма': self.get_by_v_rabote_po_zakaz_slider_3(comp='>'),
                    'Лоты с низкой конкуренцией': self.get_by_v_rabote_po_zakaz_slider_3(comp='<')
                }
            },
            'slide_4': {
                'all_status_L1': all_status_L1[0],
                'all_status_L2': all_status_L2[0],
                'all_customers': all_customers[0],
                'all_services_L3': all_services_L3,
                'step_numb': self.step_numb()[1],
                'summ': round(
                    100 * self.get_by_status_l2_sum_otb()[1532][0] / self.get_by_status_l2_sum_otb()[1539][0])
                    if self.get_by_status_l2_sum_otb()[1539][0] != 0 else 0,
                'legend': [
                    str(round(self.get_by_status_l2_sum_otb()[1532][0]/self.step_numb()[0],1))+' '+self.step_numb()[1],
                    self.get_by_status_l2_sum_otb()[1532][1],
                    self.get_by_status_l2_lots()[1532]
                ],
                'effect': round(self.get_by_effect(),2),
                'table': {
                    'ЗКО': self.get_by_table_slider_4(L3_ID=(154, 155, 156)),
                    'ОКО': self.get_by_table_slider_4(L3_ID=(151, 152, 153))
                },
                'voronka': [
                    self.voronka_effect(round=1),
                    self.voronka_effect(round=2),
                    self.voronka_effect(round=3)
                ],
                'hist_2': {
                    'Лоты с ЦП > НМЦ': self.get_by_v_rabote_po_uclugam_slide_4(option='>'),
                    'Лоты с ЦП < НМЦ': self.get_by_v_rabote_po_uclugam_slide_4(option='<')
                },
                'hist_3': {
                    'Лоты с ЦП > НМЦ': self.get_by_v_rabote_po_zakaz_slide_4(option='>'),
                    'Лоты с ЦП < НМЦ': self.get_by_v_rabote_po_zakaz_slide_4(option='<')
                }
            },
            'all_status_L1': all_status_L1,
            'all_status_L2': all_status_L2,
            'all_customers': all_customers,
            'all_services_L3': all_services_L3,
            'all_contragents': all_contragents
        }
        self.close_connection()

        return results



