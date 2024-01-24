# Импорт библиотек
from kivymd.app import MDApp

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.fitimage import FitImage
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.uix.image import AsyncImage
from kivy.graphics import Color, Mesh, Ellipse
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.core.text import LabelBase

from plyer import filechooser

from kivy.clock import Clock
import threading

# Импорт киви строки
import kv_text

import config
import date_handler

from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission

    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

# date_handler.update_xl()

date_handler.start_data = date_handler.new_start_data_def()

# Задаем начальные значения цветов у графиков и фона
color_in = (.56, .57, .60, 1)
color_out = (.51, .53, .56, 1)


class Slider_1(ScrollView):
    def __init__(self, **kwargs):
        super(Slider_1, self).__init__(**kwargs)
        self.do_scroll_y = True
        self.size_hint = (.9, .95)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        # self.data = date_handler.Update_Data("example.db").results_data()['slide_1']
        self.data = date_handler.start_data['slide_1']
        self.lay_list = [] ## Список с изменяемыми объектами
        self.generate_slider()
        self.bind(width=self.update_height)

    def update_height(self, instance, width_value): ## Динамическое изменение размеров при запуске приложения и изменении размеров окна
        self.h_s.height = width_value*0.13
        self.MDC_1.height = width_value*(0.5+0.306+0.43)+10*4
        self.MDC_2.height = width_value*(0.12+(len(self.data['hist_1'][list(self.data['hist_1'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_3.height = width_value*(0.12+(len(self.data['hist_2'][list(self.data['hist_2'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_4.height = width_value*(0.12+(len(self.data['hist_3'][list(self.data['hist_3'].keys())[0]].keys())*0.09)+0.22)
        self.layout.height = self.h_s.height+self.MDC_1.height+self.MDC_2.height+self.MDC_3.height+self.MDC_4.height+15*6

    def update_height_1(self, data): ## Динамическое изменение размеров при обновлении данных
        width_value = self.width
        self.h_s.height = width_value*0.13
        self.MDC_1.height = width_value*(0.5+0.306+0.43)+10*4
        self.MDC_2.height = width_value*(0.12+(len(data['hist_1'][list(data['hist_1'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_3.height = width_value*(0.12+(len(data['hist_2'][list(data['hist_2'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_4.height = width_value*(0.12+(len(data['hist_3'][list(data['hist_3'].keys())[0]].keys())*0.09)+0.22)
        self.layout.height = self.h_s.height+self.MDC_1.height+self.MDC_2.height+self.MDC_3.height+self.MDC_4.height+15*6


    def generate_slider(self): ## Добавление виджетов в слайдер
        self.layout = MDBoxLayout(orientation = 'vertical', spacing=15, padding=15, radius = 15,size_hint_y = None, md_bg_color = color_out)
        self.h_s = Head_slider(left_text='ОБЪЕМ', right_text='2023', size_hint=(1, .01))
        self.layout.add_widget(self.h_s)
        self.MDC_1 = MDBoxLayout(orientation='vertical', spacing=10, padding=10,radius=15, md_bg_color=color_in,size_hint_y = None)
        MDC_1_1 = MDBoxLayout(orientation='horizontal', spacing=10, padding=10,radius=15, md_bg_color=color_in)
        MDC_1_1.add_widget(Donut_Chart(size_hint_x=.6, data=[self.data['all'][x] for x in self.data['all'].keys()], color=config.color_volume_bggo,
                    color_in=color_in, color_out=color_in, text_1=self.data['summ'], text_2=self.data['step_numb'], text_3='123/252'))

        MDC_1_1.add_widget(Right_legend(data = self.data['all'], color=config.color_volume, color_in=color_in,size_hint_x = .4))
        self.MDC_1.add_widget(MDC_1_1)
        self.MDC_1.add_widget(Table_type_1(data = self.data['table'], color=config.color_volume, color_in=color_in))
        self.MDC_1.add_widget(Basement_type_1(data = self.data['legend'], color=config.color_volume, color_in=color_in, text_1='Завершено выбором',text_2='Без выбора/Отменено'))
        self.layout.add_widget(self.MDC_1)

        # График 2: Объемы по статусам

        self.MDC_2 = MDBoxLayout(orientation = 'vertical',spacing=10, padding=10, radius = 15, md_bg_color = color_in,size_hint_y = None)
        self.MDC_2.add_widget(Head_in_card(left_text='Объемы по статусам', right_text='123/252', color_in=color_in))
        self.MDC_2.add_widget(Hor_gist_type_1(data=self.data['hist_1'], color_in=color_in, color = config.color_volume_bggo, type = self.data['all_status_L2']))
        self.MDC_2.add_widget(Basement_legend_type_1(color=config.color_volume_bggo, data=['План', 'В работе', 'Завершено', 'Не поступило'], color_in=color_in))

        self.layout.add_widget(self.MDC_2)


        # График 3: В работе по услугам

        self.MDC_3 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in,size_hint_y = None)
        self.MDC_3.add_widget(Head_in_card(left_text='В работе по услугам', right_text='123/252', color_in=color_in))
        self.MDC_3.add_widget(Hor_gist_type_1(data=self.data['hist_2'], color_in=color_in, color = config.color_volume_bggo, type = self.data['all_services_L3']))
        self.MDC_3.add_widget(Basement_legend_type_1(color=config.color_volume_bggo, data=['План', 'В работе', 'Завершено', 'Не поступило'], color_in=color_in))

        self.layout.add_widget(self.MDC_3)

        # График 4: В работе по заказчикам

        self.MDC_4 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in,size_hint_y = None)
        self.MDC_4.add_widget(Head_in_card(left_text='В работе по заказчикам', right_text='123/252', color_in=color_in))
        self.MDC_4.add_widget(Hor_gist_type_1(data=self.data['hist_3'], color_in=color_in, color = config.color_volume_bggo, type = self.data['all_customers']))
        self.MDC_4.add_widget(Basement_legend_type_1(color=config.color_volume_bggo, data=['План', 'В работе', 'Завершено', 'Не поступило'], color_in=color_in))

        self.layout.add_widget(self.MDC_4)

        self.lay_list.append(self.h_s)
        self.lay_list.append(self.MDC_1)
        self.lay_list.append(self.MDC_2)
        self.lay_list.append(self.MDC_3)
        self.lay_list.append(self.MDC_4)


        self.add_widget(self.layout)

    def change_data(self, button_id): ## Определение изменяемых объектов и обновление данных для каждого
        sliter_lay_list = []
        self.data = button_id
        for children in self.lay_list:

            for child in children.children:  # Итерация по дочерним элементам MDBoxLayout
                if isinstance(child, (Donut_Chart, Table_type_1, Basement_type_1, Hor_gist_type_1)):
                    sliter_lay_list.append(child)

                if child.children:
                    for ch in child.children:
                        if isinstance(ch, (Donut_Chart, Table_type_1, Basement_type_1, Hor_gist_type_1)):
                            sliter_lay_list.append(ch)

        sliter_lay_list[0].update_data(button_id['legend'])
        sliter_lay_list[1].update_data(button_id['table'])
        sliter_lay_list[2].update_data([button_id['all'][x] for x in button_id['all'].keys()], button_id['summ'], button_id['step_numb'])
        sliter_lay_list[3].update_data(button_id['hist_1'], button_id['all_status_L2'])
        sliter_lay_list[4].update_data(button_id['hist_2'], button_id['all_services_L3'])
        sliter_lay_list[5].update_data(button_id['hist_3'], button_id['all_customers'])

        self.update_height_1(button_id)





class Slider_2(ScrollView):
    def __init__(self, **kwargs):
        super(Slider_2, self).__init__(**kwargs)
        self.do_scroll_y = True
        self.size_hint = (.9, .95)
        self.data = date_handler.start_data['slide_2']
        self.pos_hint = {"center_x": .5, "center_y": .5}
        self.lay_list = []
        self.generate_slider()
        self.bind(width=self.update_height)

    def update_height(self, instance, width_value):
        self.h_s.height = width_value*0.13
        self.MDC_1.height = width_value*(0.5+0.22)+10*4
        self.MDC_2.height = width_value*0.13
        self.MDC_3.height = width_value*(0.12+0.44)
        self.MDC_4.height = width_value*(0.12+(len(self.data['hist_1'][
                list(self.data['hist_1'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_5.height = width_value*(0.12+(len(self.data['hist_2'][
                list(self.data['hist_2'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_6.height = width_value*(0.12+(len(self.data['hist_3'][
                list(self.data['hist_3'].keys())[0]].keys())*0.09)+0.22)
        self.layout.height = self.h_s.height+self.MDC_1.height+self.MDC_2.height+self.MDC_3.height+self.MDC_4.height+self.MDC_5.height+self.MDC_6.height+15*8


    def update_height_1(self, data):
        width_value = self.width
        self.h_s.height = width_value*0.13
        self.MDC_1.height = width_value*(0.5+0.22)+10*4
        self.MDC_2.height = width_value*0.13
        self.MDC_3.height = width_value*(0.12+0.44)
        self.MDC_4.height = width_value*(0.12+(len(data['hist_1'][
                list(data['hist_1'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_5.height = width_value*(0.12+(len(data['hist_2'][
                list(data['hist_2'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_6.height = width_value*(0.12+(len(data['hist_3'][
                list(data['hist_3'].keys())[0]].keys())*0.09)+0.22)
        self.layout.height = self.h_s.height+self.MDC_1.height+self.MDC_2.height+self.MDC_3.height+self.MDC_4.height+self.MDC_5.height+self.MDC_6.height+15*8


    def generate_slider(self):
        self.layout = MDBoxLayout(orientation='vertical', spacing=15, padding=15, size_hint_y=None, radius=15,md_bg_color=color_out)

        ## Шапка 2 слайдера
        self.h_s = Head_slider(left_text='СВОЕВРЕМЕННОСТЬ', right_text='2023', size_hint_y = None)
        self.layout.add_widget(self.h_s)

        ## График 1: Бубликовая диаграмма

        self.MDC_1 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in,size_hint_y = None)

        MDC_1_1 = MDBoxLayout(orientation='horizontal', spacing=10, padding=10, radius=15, md_bg_color=color_in)
        MDC_1_1.add_widget(Donut_Chart(size_hint_x=.6, data=[self.data['summ'], 100-self.data['summ']] , color=config.colors_grey,color_in=color_in, color_out=color_in, text_1=str(self.data['summ'])+'%', text_2='',text_3=''))
        MDC_1_1.add_widget(Right_legend_type_2(color_in = color_in, data_1 = str(self.data['legend'][0]) + '' + self.data['step_numb'], data_2 = str(self.data['legend'][1]), data_3 = str(self.data['legend'][2]), size_hint_x = .4))

        self.MDC_1.add_widget(MDC_1_1)

        self.MDC_1.add_widget(Basement_type_2(color_in = color_in, color = config.colors_grey, text = ['Завершено выбором','Без выбора/Отменено']))

        self.layout.add_widget(self.MDC_1)

        ## График 2: Процент выполняемости

        self.MDC_2 = Info_Card_type_1(data_1=self.data['fact'][0], data_2=self.data['fact'][1])

        self.layout.add_widget(self.MDC_2)

        ## График 3: Продолжительность (раб.дн)

        self.MDC_3 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in,size_hint_y = None)

        self.MDC_3.add_widget(Head_in_card(left_text='Продолжительность (раб.дн)', right_text='', color_in=color_in))
        self.MDC_3.add_widget(Table_type_2(color_in = color_in, tyte = ['Лот(ов)', 'Факт', 'Н.Факт', 'Цель'], data = self.data['table']))

        self.layout.add_widget(self.MDC_3)

        # График 2: В работе по статусам

        self.MDC_4 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in,size_hint_y = None)

        self.MDC_4.add_widget(Head_in_card(left_text='В работе по по статусам', right_text='123/252', color_in=color_in))
        self.MDC_4.add_widget(Hor_gist_type_1(data=self.data['hist_1'], color_in=color_in, color = config.color_volume_worg, type = self.data['all_status_L2']))
        self.MDC_4.add_widget(Basement_legend_type_1(color=config.color_volume_worg[:-1], data=['Норма','Внимание','Эскалация'], color_in=color_in))

        self.layout.add_widget(self.MDC_4)

        # График 3: В работе по услугам

        self.MDC_5 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in,size_hint_y = None)

        self.MDC_5.add_widget(Head_in_card(left_text='В работе по услугам', right_text='123/252', color_in=color_in))
        self.MDC_5.add_widget(Hor_gist_type_1(data=self.data['hist_2'], color_in=color_in, color = config.color_volume_worg, type = self.data['all_services_L3']))
        self.MDC_5.add_widget(Basement_legend_type_1(color=config.color_volume_worg[:-1], data=['Норма','Внимание','Эскалация'], color_in=color_in))
        self.layout.add_widget(self.MDC_5)

        # График 4: В работе по заказчикам

        self.MDC_6 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y = None)

        self.MDC_6.add_widget(Head_in_card(left_text='В работе по заказчикам', right_text='123/252', color_in=color_in))
        self.MDC_6.add_widget(Hor_gist_type_1(data=self.data['hist_3'], color_in=color_in, color = config.color_volume_worg, type = self.data['all_customers']))
        self.MDC_6.add_widget(Basement_legend_type_1(color=config.color_volume_worg[:-1], data=['Норма','Внимание','Эскалация'], color_in=color_in))

        self.layout.add_widget(self.MDC_6)

        self.lay_list.append(self.h_s)
        self.lay_list.append(self.MDC_1)
        self.lay_list.append(self.MDC_2)
        self.lay_list.append(self.MDC_3)
        self.lay_list.append(self.MDC_4)
        self.lay_list.append(self.MDC_5)
        self.lay_list.append(self.MDC_6)


        self.add_widget(self.layout)


    def change_data(self, button_id):
        sliter_lay_list = []
        self.data = button_id
        for children in self.lay_list:
            for child in children.children:  # Итерация по дочерним элементам MDBoxLayout
                if isinstance(child, (Donut_Chart, Table_type_2, Hor_gist_type_1,Right_legend_type_2)):
                    sliter_lay_list.append(child)
                if child.children:
                    for ch in child.children:
                        if isinstance(ch, (Donut_Chart, Table_type_2, Hor_gist_type_1,Right_legend_type_2)):
                            sliter_lay_list.append(ch)

        self.MDC_2.update_data(button_id['fact'][0],button_id['fact'][0])
        sliter_lay_list[0].update_data(str(button_id['legend'][0]), str(button_id['legend'][1]), str(button_id['legend'][2]))
        sliter_lay_list[1].update_data([button_id['summ'], 100 - button_id['summ']], str(button_id['summ'])+'%', '')
        sliter_lay_list[2].update_data(button_id['table'])
        sliter_lay_list[3].update_data(button_id['hist_1'], button_id['all_status_L2'])
        sliter_lay_list[4].update_data(button_id['hist_2'], button_id['all_services_L3'])
        sliter_lay_list[5].update_data(button_id['hist_3'], button_id['all_customers'])

        self.update_height_1(button_id)




class Slider_3(ScrollView):
    def __init__(self, **kwargs):
        super(Slider_3, self).__init__(**kwargs)
        self.do_scroll_y = True
        self.size_hint = (.9, .95)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        # self.data = date_handler.Update_Data("example.db").results_data()['slide_3']
        self.data = date_handler.start_data['slide_3']
        self.lay_list = []
        self.generate_slider()
        self.bind(width=self.update_height)

    def update_height(self, instance, width_value):
        self.h_s.height = width_value * 0.13
        self.MDC_1.height = width_value * (0.5 + 0.22) + 10 * 4
        self.MDC_2.height = width_value * 0.13
        self.MDC_3.height = width_value * (0.12 + 0.44)
        self.MDC_4.height = width_value * (0.12 + (len(self.data['hist_1'][
                list(self.data['hist_1'].keys())[0]].keys()) * 0.09) + 0.22)
        self.MDC_5.height = width_value * (0.12 + (len(self.data['hist_2'][
                list(self.data['hist_2'].keys())[0]].keys()) * 0.09) + 0.22)
        self.MDC_6.height = width_value * (0.12 + (len(self.data['hist_3'][
                list(self.data['hist_3'].keys())[0]].keys()) * 0.09) + 0.22)
        self.layout.height = self.h_s.height + self.MDC_1.height + self.MDC_2.height + self.MDC_3.height + self.MDC_4.height + self.MDC_5.height + self.MDC_6.height + 15 * 8

    def update_height_1(self, data):
        width_value = self.width
        self.h_s.height = width_value * 0.13
        self.MDC_1.height = width_value * (0.5 + 0.22) + 10 * 4
        self.MDC_2.height = width_value * 0.13
        self.MDC_3.height = width_value * (0.12 + 0.44)
        self.MDC_4.height = width_value * (0.12 + (len(data['hist_1'][
                list(data['hist_1'].keys())[0]].keys()) * 0.09) + 0.22)
        self.MDC_5.height = width_value * (0.12 + (len(data['hist_2'][
                list(data['hist_2'].keys())[0]].keys()) * 0.09) + 0.22)
        self.MDC_6.height = width_value * (0.12 + (len(data['hist_3'][
                list(data['hist_3'].keys())[0]].keys()) * 0.09) + 0.22)
        self.layout.height = self.h_s.height + self.MDC_1.height + self.MDC_2.height + self.MDC_3.height + self.MDC_4.height + self.MDC_5.height + self.MDC_6.height + 15 * 8

    def generate_slider(self):
        self.layout = MDBoxLayout(orientation='vertical', spacing=15, padding=15, size_hint_y=None, radius=15, md_bg_color=color_out)

        ## Шапка 2 слайдера

        self.h_s = Head_slider(left_text='КОНКУРЕНЦИЯ', right_text='2023', size_hint=(1, .02), size_hint_y=None)

        self.layout.add_widget(self.h_s)

        ## График 1: Бубликовая диаграмма

        self.MDC_1 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        MDC_1_1 = MDBoxLayout(orientation='horizontal', spacing=10, padding=10, radius=15, md_bg_color=color_in)

        MDC_1_1.add_widget(Donut_Chart(size_hint_x = .6, data=[self.data['summ'], 100-self.data['summ']], color=config.colors_grey, color_in=color_in, color_out=color_in, text_1=str(self.data['summ'])+'%', text_2='', text_3=''))
        MDC_1_1.add_widget(Right_legend_type_2(size_hint_x = .4, color_in=color_in, data_1= str(self.data['legend'][0]) + '' + self.data['step_numb'], data_2=str(self.data['legend'][1]), data_3=str(self.data['legend'][2])))

        self.MDC_1.add_widget(MDC_1_1)

        self.MDC_1.add_widget(Basement_type_2(color_in=color_in, color=config.colors_grey, text=['Завершено выбором', 'Без выбора/Отменено']))
        self.layout.add_widget(self.MDC_1)

        ## График 2: Процент выполняемости

        self.MDC_2 = Info_Card_type_2(text='Конкуренция\n(итоги тех.оценки)', data=str(self.data['competition']))

        self.layout.add_widget(self.MDC_2)

        ## График 3: Конкуренция по форме закупки

        self.MDC_3 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        self.MDC_3.add_widget(Head_in_card(left_text='Конкуренция по форме закупки', right_text='', color_in=color_in))
        self.MDC_3.add_widget(Table_type_2(color_in=color_in, tyte=['Лот(ов)', 'Конкуренция', 'Ком.'], data=self.data['table']))

        self.layout.add_widget(self.MDC_3)

        # График 2: В работе по статусам

        self.MDC_4 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        self.MDC_4.add_widget(Head_in_card(left_text='В работе по по статусам', right_text='123/252', color_in=color_in))
        self.MDC_4.add_widget(Hor_gist_type_1(data=self.data['hist_1'], color_in=color_in, color = config.color_volume_wog, type = self.data['all_status_L2']))
        self.MDC_4.add_widget(Basement_legend_type_1(color=config.color_volume_wog[:-1], data=['Норма', 'Лоты с низкой конкуренцией'], color_in=color_in))

        self.layout.add_widget(self.MDC_4)

        # График 3: В работе по услугам

        self.MDC_5 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        self.MDC_5.add_widget(Head_in_card(left_text='В работе по услугам', right_text='123/252', color_in=color_in))
        self.MDC_5.add_widget(Hor_gist_type_1(data=self.data['hist_2'], color_in=color_in, color = config.color_volume_wog, type = self.data['all_services_L3']))
        self.MDC_5.add_widget(Basement_legend_type_1(color=config.color_volume_wog[:-1], data=['Норма', 'Лоты с низкой конкуренцией'], color_in=color_in))

        self.layout.add_widget(self.MDC_5)

        # График 4: В работе по заказчикам

        self.MDC_6 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        self.MDC_6.add_widget(Head_in_card(left_text='В работе по заказчикам', right_text='123/252', color_in=color_in))
        self.MDC_6.add_widget(Hor_gist_type_1(data=self.data['hist_3'], color_in=color_in, color = config.color_volume_wog, type = self.data['all_customers']))
        self.MDC_6.add_widget(Basement_legend_type_1(color=config.color_volume_wog[:-1], data=['Норма', 'Лоты с низкой конкуренцией'], color_in=color_in))

        self.layout.add_widget(self.MDC_6)

        self.lay_list.append(self.h_s)
        self.lay_list.append(self.MDC_1)
        self.lay_list.append(self.MDC_2)
        self.lay_list.append(self.MDC_3)
        self.lay_list.append(self.MDC_4)
        self.lay_list.append(self.MDC_5)
        self.lay_list.append(self.MDC_6)

        self.add_widget(self.layout)

    def change_data(self, button_id):
        sliter_lay_list = []
        self.data = button_id
        for children in self.lay_list:
            for child in children.children:  # Итерация по дочерним элементам MDBoxLayout
                if isinstance(child, (Donut_Chart, Table_type_2, Hor_gist_type_1,Right_legend_type_2,Info_Card_type_2)):
                    sliter_lay_list.append(child)
                if child.children:
                    for ch in child.children:
                        if isinstance(ch, (Donut_Chart, Table_type_2, Hor_gist_type_1,Right_legend_type_2,Info_Card_type_2)):
                            sliter_lay_list.append(ch)

        self.MDC_2.update_data(str(button_id['competition']))
        sliter_lay_list[0].update_data(str(button_id['legend'][0]), str(button_id['legend'][1]), str(button_id['legend'][2]))
        sliter_lay_list[1].update_data([button_id['summ'], 100 - button_id['summ']], str(button_id['summ'])+'%','')
        sliter_lay_list[2].update_data(button_id['table'])
        sliter_lay_list[3].update_data(button_id['hist_1'], button_id['all_status_L2'])
        sliter_lay_list[4].update_data(button_id['hist_2'], button_id['all_services_L3'])
        sliter_lay_list[5].update_data(button_id['hist_3'], button_id['all_customers'])

        self.update_height_1(button_id)


class Slider_4(ScrollView):
    def __init__(self, **kwargs):
        super(Slider_4, self).__init__(**kwargs)
        self.do_scroll_y = True
        self.size_hint = (.9, .95)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        # self.data = date_handler.Update_Data("example.db").results_data()['slide_4']
        self.data = date_handler.start_data['slide_4']
        self.lay_list = []
        self.generate_slider()
        self.bind(width=self.update_height)

    def update_height(self, instance, width_value):
        self.h_s.height = width_value*0.13
        self.MDC_1.height = width_value*(0.5+0.22)+10*4
        self.MDC_2.height = width_value*0.13
        self.MDC_3.height = width_value*(0.12+0.44)
        self.MDC_4.height = width_value*(0.3*3+0.12+0.22)
        self.MDC_5.height = width_value*(0.12+(len(self.data['hist_2'][
                list(self.data['hist_2'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_6.height = width_value*(0.12+(len(self.data['hist_3'][
                list(self.data['hist_3'].keys())[0]].keys())*0.09)+0.22)
        self.layout.height = self.h_s.height+self.MDC_1.height+self.MDC_2.height+self.MDC_3.height+self.MDC_4.height+self.MDC_5.height+self.MDC_6.height+15*8

    def update_height_1(self, data):
        width_value = self.width
        self.h_s.height = width_value*0.13
        self.MDC_1.height = width_value*(0.5+0.22)+10*4
        self.MDC_2.height = width_value*0.13
        self.MDC_3.height = width_value*(0.12+0.44)
        self.MDC_4.height = width_value*(0.3*3+0.12+0.22)
        self.MDC_5.height = width_value*(0.12+(len(data['hist_2'][
                list(data['hist_2'].keys())[0]].keys())*0.09)+0.22)
        self.MDC_6.height = width_value*(0.12+(len(data['hist_3'][
                list(data['hist_3'].keys())[0]].keys())*0.09)+0.22)
        self.layout.height = self.h_s.height+self.MDC_1.height+self.MDC_2.height+self.MDC_3.height+self.MDC_4.height+self.MDC_5.height+self.MDC_6.height+15*8


    def generate_slider(self):
        self.axes_list = []
        self.layout = MDBoxLayout(orientation='vertical', spacing=15, padding=15, size_hint_y=None, radius=15, md_bg_color=color_out)
        ## Шапка 2 слайдера

        self.h_s = Head_slider(left_text='ЭФФЕКТИВНОСТЬ', right_text='2023', size_hint=(1, .02), size_hint_y=None)

        self.layout.add_widget(self.h_s)

        ## График 1: Бубликовая диаграмма

        self.MDC_1 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        MDC_1_1 = MDBoxLayout(orientation='horizontal', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint=(1, .6))

        MDC_1_1.add_widget(Donut_Chart(size_hint_x=.6, data=[self.data['summ'], 100-self.data['summ']], color=config.colors_grey, color_in=color_in, color_out=color_in, text_1=str(self.data['summ'])+'%', text_2='', text_3=''))
        MDC_1_1.add_widget(Right_legend_type_2(size_hint_x=.4, color_in=color_in, data_1=str(self.data['legend'][0]) + '' + self.data['step_numb'], data_2=str(self.data['legend'][1]), data_3=str(self.data['legend'][2])))

        self.MDC_1.add_widget(MDC_1_1)

        self.MDC_1.add_widget(Basement_type_2(color_in=color_in, color=config.colors_grey, text=['Завершено выбором', 'Без выбора/Отменено']))

        self.layout.add_widget(self.MDC_1)

        ## График 2: Эффективность

        self.MDC_2 = Info_Card_type_2(text='Эффективность', data=str(self.data['effect']))

        self.layout.add_widget(self.MDC_2)


        ## График 3: Эффективность (ЦП/НМЦ-1)

        self.MDC_3 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        self.MDC_3.add_widget(Head_in_card(left_text='Эффективность (ЦП/НМЦ-1)', right_text='', color_in=color_in))
        self.MDC_3.add_widget(Table_type_2(color_in=color_in, tyte=['Лот(ов)', 'млрд', '%'], data=self.data['table']))

        self.layout.add_widget(self.MDC_3)

        # График 2: В работе по статусам

        self.MDC_4 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        self.MDC_4.add_widget(Head_in_card(left_text='Воронка эффективности\n(по завершенным выбором)', right_text='123/252', color_in=color_in))

        MDC_4_1 = MDBoxLayout(orientation='vertical', spacing=10, padding=10)

        MDC_4_1.add_widget(Trapezoid(trapezoid_sizes=(0.1, 0.9, 0.95, 0.05), text='22', count = '64'))
        MDC_4_1.add_widget(Trapezoid(trapezoid_sizes=(0.15, 0.85, 0.9, 0.1), text = '-12', count = '10'))
        MDC_4_1.add_widget(Trapezoid(trapezoid_sizes=(0.2, 0.8, 0.85, 0.15), text = '-15', count = '5'))

        self.MDC_4.add_widget(MDC_4_1)

        self.MDC_4.add_widget(Basement_legend_type_1(color=config.color_volume_wrg[:-1], data=['Лоты с ЦП > НМЦ', 'Лоты с ЦП < НМЦ'], color_in=color_in))

        self.layout.add_widget(self.MDC_4)

        # График 3: В работе по услугам

        self.MDC_5 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        self.MDC_5.add_widget(Head_in_card(left_text='В работе по услугам', right_text='123/252', color_in=color_in))
        self.MDC_5.add_widget(Hor_gist_type_1(data=self.data['hist_2'], color_in=color_in, color = config.color_volume_wrg, type = self.data['all_services_L3']))
        self.MDC_5.add_widget(Basement_legend_type_1(color=config.color_volume_wrg[:-1], data=['Лоты с ЦП > НМЦ', 'Лоты с ЦП < НМЦ'], color_in=color_in))

        self.layout.add_widget(self.MDC_5)

        # График 4: В работе по заказчикам

        self.MDC_6 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, md_bg_color=color_in, size_hint_y=None)

        self.MDC_6.add_widget(Head_in_card(left_text='В работе по заказчикам', right_text='123/252', color_in=color_in))
        self.MDC_6.add_widget(Hor_gist_type_1(data=self.data['hist_3'], color_in=color_in, color = config.color_volume_wrg, type = self.data['all_customers']))
        self.MDC_6.add_widget(Basement_legend_type_1(color=config.color_volume_wrg[:-1], data=['Лоты с ЦП > НМЦ', 'Лоты с ЦП < НМЦ'], color_in=color_in))

        self.layout.add_widget(self.MDC_6)

        self.lay_list.append(self.h_s)
        self.lay_list.append(self.MDC_1)
        self.lay_list.append(self.MDC_2)
        self.lay_list.append(self.MDC_3)
        self.lay_list.append(self.MDC_4)
        self.lay_list.append(self.MDC_5)
        self.lay_list.append(self.MDC_6)

        self.add_widget(self.layout)


    def change_data(self, button_id):
        sliter_lay_list = []
        self.data = button_id
        for children in self.lay_list:
            for child in children.children:  # Итерация по дочерним элементам MDBoxLayout
                if isinstance(child, (Donut_Chart, Table_type_2, Hor_gist_type_1,Right_legend_type_2,Info_Card_type_2)):
                    sliter_lay_list.append(child)
                if child.children:
                    for ch in child.children:
                        if isinstance(ch, (Donut_Chart, Table_type_2, Hor_gist_type_1,Right_legend_type_2,Info_Card_type_2)):
                            sliter_lay_list.append(ch)

        self.MDC_2.update_data(str(button_id['effect']))
        sliter_lay_list[0].update_data(str(button_id['legend'][0]), str(button_id['legend'][1]), str(button_id['legend'][2]))
        sliter_lay_list[1].update_data([button_id['summ'], 100 - button_id['summ']], str(button_id['summ'])+'%','')
        sliter_lay_list[2].update_data(button_id['table'])
        sliter_lay_list[3].update_data(button_id['hist_2'],button_id['all_services_L3'])
        sliter_lay_list[4].update_data(button_id['hist_3'],button_id['all_customers'])

        self.update_height_1(button_id)


class Head_slider(MDBoxLayout):
    def __init__(self, left_text, right_text, **kwargs):
        super(Head_slider, self).__init__(**kwargs)
        self.left_text = left_text
        self.right_text = right_text
        md_bg_color = (0,0,0,0)
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.13

    def update_widget(self, *args):
        self.layout = MDBoxLayout(orientation='horizontal')
        self.layout.add_widget(
            MDLabel(
                text=self.left_text,
                size_hint_x=0.8,  # Устанавливаем размер виджета в 70% от родительского
                size_hint_min_x=300,  # Минимальный размер, чтобы предотвратить перенос текста
                theme_text_color='Custom',
                halign='left',
                text_color=(1, 1, 1, 1),
                font_style='NewFont26',
            )
        )
        self.layout.add_widget(
            MDLabel(
                text=self.right_text,
                size_hint_x=0.2,  # Устанавливаем размер виджета в 30% от родительского
                theme_text_color='Custom',
                halign='right',
                text_color=(1, 1, 1, 1),
                font_style='NewFont26',
            )
        )

        self.add_widget(self.layout)


class Donut_Chart(MDFloatLayout):
    def __init__(self, color_in, color_out, data,color,text_1,text_2,text_3, **kwargs):
        super(Donut_Chart, self).__init__(**kwargs)
        self.data = data
        self.colors = color
        self.text_1 = text_1
        self.text_2 = text_2
        self.text_3 = text_3
        self.bind(pos=self.update_widget, size=self.update_widget, width=self.update_height)
        self.size_hint_y = None
        self.F_L = MDFloatLayout()
        self.add_widget(self.F_L)
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value

    def update_widget(self, *args):
        total = sum(self.data)
        angle_start = 0
        center = self.width / 2 + self.x, self.height / 2 + self.y
        radius = min(self.width, self.height) / 2.3

        self.F_L.canvas.clear()

        for idx, value in enumerate(self.data):
            if total != 0: angle_end = angle_start + (value / total) * 360
            else: angle_end = 0
            with self.F_L.canvas:
                Color(*self.colors[idx])
                Ellipse(pos=(center[0] - radius, center[1] - radius),
                        size=(radius * 2, radius * 2),
                        angle_start=angle_start,
                        angle_end=angle_end)
            angle_start = angle_end

        inner_radius = radius / 1.3
        with self.F_L.canvas:
            Color(*color_in)
            Ellipse(pos=(center[0] - inner_radius, center[1] - inner_radius),
                    size=(inner_radius * 2, inner_radius * 2))

        self.clear_widgets()
        self.add_widget(self.F_L)

        self.add_widget(MDLabel(text=str(self.text_1), halign="center", pos_hint={'y': 0, 'x': 0}, theme_text_color='Custom',
                                text_color=(1, 1, 1, 1), font_style='NewFont46'))
        self.add_widget(
            MDLabel(text=self.text_2, halign="center", pos_hint={'y': .2, 'x': 0}, theme_text_color='Custom',
                    text_color=(1, 1, 1, 1), font_style='NewFont12'))
        self.add_widget(
            MDLabel(text=self.text_3, halign="center", pos_hint={'y': -.2, 'x': 0}, theme_text_color='Custom',
                    text_color=(1, 1, 1, 1), font_style='NewFont12'))

    def update_data(self,new_data, text_1, text_2):
        self.data = new_data
        self.text_1 = text_1
        self.text_2 = text_2
        self.update_widget()
        self.update_height


class Right_legend(MDBoxLayout):
    def __init__(self, color_in, data,color, **kwargs):
        super(Right_legend, self).__init__(**kwargs)
        self.data = data
        self.color = color
        self.color_in = color_in
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value*1.25

    def update_widget(self, *args):
        self.layout = MDGridLayout(cols=2, spacing=10, padding=10, md_bg_color=self.color_in, size_hint=(1,None),
                                    pos_hint={"center_x": .5, "center_y": .5})
        self.layout.bind(minimum_height=self.layout.setter('height'))
        for i in range(4):
            self.layout.add_widget(
                MDBoxLayout(md_bg_color=self.color[i], size=(50,50), size_hint=(None, None), radius=2))
            self.layout.add_widget(
                MDLabel(text=list(self.data.keys())[i], theme_text_color='Custom', halign='left',font_style='NewFont14',
                        text_color=(1, 1, 1, 1)))

        self.add_widget(self.layout)


class Table_type_1(MDBoxLayout):
    def __init__(self, color_in, data, color, **kwargs):
        super(Table_type_1, self).__init__(**kwargs)
        self.data = data
        self.color = color
        self.color_in = color_in
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.306

    def update_widget(self, *args):
        self.clear_widgets()
        self.layout = MDGridLayout(spacing=10, padding=10, md_bg_color=self.color_in, cols=5, size_hint=(1,1))
        self.layout.add_widget(MDBoxLayout())
        for i in range(4):
            self.layout.add_widget(MDBoxLayout(md_bg_color=self.color[i], radius=3))

        x = [i for i in self.data.keys()]
        # for i in [x[0]]:
        #     self.layout.add_widget(
        #         MDLabel(text=str(i), font_style='NewFont14', theme_text_color='Custom', text_color=(1, 1, 1, 1)))
        #     for j in range(4):
        #         self.layout.add_widget(
        #             MDLabel(text=transform_number_nmc(str(list(self.data[i][p] for p in self.data[i].keys())[j])),
        #                     halign='right', theme_text_color='Custom', text_color=(1, 1, 1, 1),font_style='NewFont14'))
        for i in x:
            self.layout.add_widget(
                MDLabel(text=str(i), font_style='NewFont14', theme_text_color='Custom', text_color=(1, 1, 1, 1)))
            for j in range(4):
                self.layout.add_widget(
                    MDLabel(text=str(list(self.data[i][p] for p in self.data[i].keys())[j]),
                            halign='right', theme_text_color='Custom', text_color=(1, 1, 1, 1), font_style='NewFont14'))

        self.add_widget(self.layout)
    def update_data(self,new_data):
            self.data = new_data
            self.update_widget()


class Table_type_2(MDBoxLayout):
    def __init__(self, color_in, data, tyte, **kwargs):
        super(Table_type_2, self).__init__(**kwargs)
        self.data = data
        self.tyte = tyte
        self.height = 250
        self.color_in = color_in
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.44

    def update_widget(self, *args):
        self.clear_widgets()
        self.layout = MDGridLayout(spacing=10, padding=10, md_bg_color=self.color_in, cols=len(self.tyte)+1)
        self.layout.add_widget(MDBoxLayout())

        for i in self.tyte:
            self.layout.add_widget(MDLabel(text=i, theme_text_color='Custom', halign='center', font_style='NewFont14',
                                     text_color=(1, 1, 1, 1)))

        for i in list(self.data.keys()):
            self.layout.add_widget(MDLabel(text=i, font_style='NewFont14',theme_text_color='Custom', text_color=(1, 1, 1, 1)))
            for j in list(self.data[i].keys()):
                MD_lay = MDBoxLayout(orientation='horizontal', radius=15, spacing=2, padding=2, md_bg_color='#AEAEAE')
                MD_lay_in = MDBoxLayout(orientation='horizontal', radius=15, md_bg_color=self.color_in)

                MD_lay_in.add_widget(
                    MDLabel(text=str(self.data[i][j]),
                            halign='center', theme_text_color='Custom', text_color=(1, 1, 1, 1),font_style='NewFont14'))
                MD_lay.add_widget(MD_lay_in)

                self.layout.add_widget(MD_lay)


        self.add_widget(self.layout)
    def update_data(self,new_data):
            self.data = new_data
            self.update_widget()


class Basement_type_1(MDBoxLayout):
    def __init__(self, color_in, data,color,text_1,text_2, **kwargs):
        super(Basement_type_1, self).__init__(**kwargs)
        self.data = data
        self.color = color
        self.color_in = color_in
        self.text_1 = text_1
        self.text_2 = text_2
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.43

    def update_widget(self, *args):
        self.clear_widgets()
        self.layout = MDGridLayout(spacing=10, padding=10, md_bg_color=self.color_in, cols=2, size_hint=(1,1))
        self.layout.add_widget(
            MDLabel(text=self.text_1, halign='center', theme_text_color='Custom', text_color=(1, 1, 1, 1),font_style='NewFont16'))
        self.layout.add_widget(
            MDLabel(text=self.text_2, halign='center', theme_text_color='Custom', text_color=(1, 1, 1, 1),font_style='NewFont16'))
        for j in self.data:
            self.layout.add_widget(
                MDLabel(text=str(j), halign='center', theme_text_color='Custom', text_color=(1, 1, 1, 1),font_style='NewFont16'))
        self.add_widget(self.layout)

    def update_data(self,new_data):
            self.data = new_data
            self.update_widget()


class Head_in_card(MDBoxLayout):
    def __init__(self, color_in,right_text,left_text,**kwargs):
        super(Head_in_card, self).__init__(**kwargs)
        self.left_text = left_text
        self.right_text = right_text
        self.color_in = color_in
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.12

    def update_widget(self, *args):
        if not self.right_text == '':
            self.layout = MDBoxLayout(orientation='horizontal', md_bg_color=self.color_in, size_hint=(1,1))
            self.layout.add_widget(MDLabel(text=self.left_text, size_hint=(.7, 1), halign='left', theme_text_color='Custom',
                                    text_color=(1, 1, 1, 1),font_style='NewFont20'))


            MDB = MDBoxLayout(radius=15, spacing=2, padding=2, md_bg_color='#AEAEAE', size_hint=(.3, 1))
            MD_lay_1 = MDBoxLayout(md_bg_color=self.color_in, spacing=10, padding=10, radius=15)
            MD_lay_1.add_widget(MDLabel(text=self.right_text, halign='right', theme_text_color='Custom', text_color=(1, 1, 1, 1),font_style='NewFont20'))
            MDB.add_widget(MD_lay_1)

            self.layout.add_widget(MDB)
            self.add_widget(self.layout)
        else:
            self.layout = MDBoxLayout(orientation='horizontal', md_bg_color=self.color_in, size_hint=(1, 1))
            self.layout.add_widget(
                MDLabel(text=self.left_text, size_hint=(1, 1), halign='left', theme_text_color='Custom',
                        text_color=(1, 1, 1, 1),font_style='NewFont20'))
            self.add_widget(self.layout)


class Hor_gist_type_1(MDBoxLayout):
    def __init__(self, color_in, data,color, type, **kwargs):
        super(Hor_gist_type_1, self).__init__(**kwargs)
        self.data = data
        self.color = color
        self.color_in = color_in
        self.type = type
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = len(list(self.data[list(self.data.keys())[0]].keys())) * 0.09 * width_value

    def update_height_1(self, data):
        self.height = len(list(data[list(data.keys())[0]].keys()))*0.09*self.width

    def update_widget(self, *args):
        self.clear_widgets()

        self.layout = MDGridLayout(spacing=10, md_bg_color=self.color_in, cols=3)

        line =[[y,[self.data[x][y] for x in list(self.data.keys())]] for y in list(self.data[list(self.data.keys())[0]].keys())]
        if line !=[]:
            max_line = max([sum(x[1]) for x in line])
            for x in line:

                self.layout.add_widget(MDLabel(text=self.type[x[0]], size_hint=(.4, 1), theme_text_color='Custom', text_color=(1, 1, 1, 1),font_style='NewFont14'))
                self.layout.add_widget(AsyncImage(source='pic/options_fig.png', size_hint=(.1, 2)))
                lay_line = MDBoxLayout(orientation='horizontal', md_bg_color=self.color_in, spacing=10, padding=4)
                if sum(x[1]) != 0:
                    sum_MDB = MDBoxLayout(size_hint=(2.5 * sum(x[1]) / max_line, .95))
                    for i in range(len(list(self.data.keys()))):
                        if x[1][i] != 0:
                            sum_MDB.add_widget(MDBoxLayout(size_hint_x = (x[1][i]/sum(x[1])),md_bg_color= self.color[i]))

                    lay_line.add_widget(sum_MDB)

                lay_line.add_widget(
                    MDLabel(text=str(sum(x[1])), halign='left', theme_text_color='Custom',
                            text_color=(1, 1, 1, 1),font_style='NewFont16'))

                self.layout.add_widget(lay_line)
        self.add_widget(self.layout)

    def update_data(self,new_data,type):
        self.data = new_data
        self.type = type
        self.update_widget()
        self.update_height_1(new_data)


class Basement_legend_type_1(MDBoxLayout):
    def __init__(self, color_in, color,data,**kwargs):
        super(Basement_legend_type_1, self).__init__(**kwargs)
        self.md_bg_color = '#AEAEAE'
        self.spacing = 2
        self.padding = 2
        self.radius = 15
        self.color_in = color_in
        self.color = color
        self.data = data
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.22


    def update_widget(self, *args):
        if len(self.color) >2:
            cols = 2
        else:
            cols = 1
        self.layout = MDGridLayout(cols=cols, spacing=5, padding=5, md_bg_color=self.color_in, radius = 15,pos_hint = {"center_x": .5, "center_y": .5})
        for i in range(len(self.color)):
            BX = MDBoxLayout(spacing=2, padding=2)

            BX.add_widget(
                MDBoxLayout(md_bg_color=self.color[i], size=(50,50), size_hint=(None, None), radius=2, pos_hint={"center_y": .5}))
            BX.add_widget(
                MDLabel(text=self.data[i], size_hint=(.7, .8), theme_text_color='Custom',
                        text_color=(1, 1, 1, 1), halign='left',font_style='NewFont14'))

            self.layout.add_widget(BX)
        self.add_widget(self.layout)


class Right_legend_type_2(MDBoxLayout):
    def __init__(self, color_in, data_1,data_2,data_3,**kwargs):
        super(Right_legend_type_2, self).__init__(**kwargs)
        self.color_in = color_in
        self.data_1 = data_1
        self.data_2 = data_2
        self.data_3 = data_3
        self.update_widget()  # Вызываем метод update_widget
        self.bind(width=self.update_height)
        self.size_hint_y = None

    def update_height(self, instance, width_value):
        instance.height = width_value*1.25

    def update_widget(self, *args):
        self.clear_widgets()
        self.layout = MDGridLayout(cols=1, spacing=5, padding=5, md_bg_color=self.color_in,
                                    pos_hint={"center_x": .5, "center_y": .5})
        self.layout.add_widget(
            MDLabel(text='Завершено выбором', size_hint=(.7, .25), theme_text_color='Custom', halign='center',
                    text_color=(1, 1, 1, 1), font_style='NewFont14'))
        self.layout.add_widget(
            MDLabel(text=self.data_1, size_hint=(.7, .25), theme_text_color='Custom', halign='center',
                    text_color=(1, 1, 1, 1), font_style='NewFont14'))
        self.layout.add_widget(
            MDLabel(text=self.data_2, size_hint=(.7, .25), theme_text_color='Custom', halign='center',
                    text_color=(1, 1, 1, 1), font_style='NewFont14'))
        self.layout.add_widget(
            MDLabel(text=self.data_3, size_hint=(.7, .25), theme_text_color='Custom', halign='center',
                    text_color=(1, 1, 1, 1), font_style='NewFont14'))

        self.add_widget(self.layout)
    def update_data(self,data_1,data_2,data_3):
            self.data_1 = data_1
            self.data_2 = data_2
            self.data_3 = data_3
            self.update_widget()


class Basement_type_2(MDBoxLayout):
    def __init__(self, color_in, color, text,**kwargs):
        super(Basement_type_2, self).__init__(**kwargs)
        self.color_in = color_in
        self.radius =15
        self.spacing = 2
        self.padding = 2
        self.md_bg_color = '#AEAEAE'
        self.color = color
        self.text = text
        self.bind(width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.18

    def update_widget(self, *args):
        self.layout = MDGridLayout(cols=2, spacing=5, padding=5, md_bg_color=self.color_in, radius = 15)
        BX = MDBoxLayout(orientation = 'vertical')
        BX.add_widget(MDBoxLayout(md_bg_color=self.color[0], size=(50,50),size_hint=(None, None), radius=2))
        BX.add_widget(MDBoxLayout(md_bg_color=(0,0,0,0), size_hint=(.9, .1), radius=2))
        self.layout.add_widget(BX)
        BX = MDBoxLayout(orientation='vertical')
        BX.add_widget(MDBoxLayout(md_bg_color=self.color[1], size=(50,50),size_hint=(None, None), radius=2))
        BX.add_widget(MDBoxLayout(md_bg_color=(0, 0, 0, 0), size_hint=(.9, .1), radius=2))
        self.layout.add_widget(BX)
        self.layout.add_widget(MDLabel(text=self.text[0], theme_text_color='Custom', halign='left',
                                       text_color=(1, 1, 1, 1), font_style='NewFont14'))
        self.layout.add_widget(MDLabel(text=self.text[1], theme_text_color='Custom', halign='left',
                                       text_color=(1, 1, 1, 1), font_style='NewFont14'))

        self.add_widget(self.layout)


class Info_Card_type_1(MDBoxLayout):
    def __init__(self, data_1, data_2, **kwargs):
        super(Info_Card_type_1, self).__init__(**kwargs)
        self.data_1 = data_1
        self.data_2 = data_2
        self.radius = 20
        self.orientation = 'horizontal'
        self.md_bg_color = '#00BD1E'
        self.size_hint_y = None
        self.padding = 20
        self.spacing = 20
        self.bind(pos=self.update_widget, size=self.update_widget, width=self.update_height)
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.13

    def update_widget(self, *args):
        self.clear_widgets()
        left_MD = MDBoxLayout(md_bg_color = '#AEAEAE', padding = 2, spacing = 2, radius = 20)
        left_MD_ = MDBoxLayout(md_bg_color='#00BD1E', padding=5, spacing=5, radius=20)
        left_MD_.add_widget(MDLabel(text=str(round(self.data_1))+'% Факт', size_hint_x=.7, theme_text_color='Custom', halign='center', valign='middle', text_color=(1, 1, 1, 1), font_style='NewFont16'))
        left_MD.add_widget(left_MD_)
        self.add_widget(left_MD)

        right_MD = MDBoxLayout(md_bg_color = '#AEAEAE', padding = 2, spacing = 2, radius = 20)
        right_MD_ = MDBoxLayout(md_bg_color='#00BD1E', padding=5, spacing=5, radius=10)
        right_MD_.add_widget(MDLabel(text=str(round(self.data_2))+'% Н.Факт', size_hint_x=.7, theme_text_color='Custom', halign='center', valign='middle', text_color=(1, 1, 1, 1), font_style='NewFont16'))
        right_MD.add_widget(right_MD_)
        self.add_widget(right_MD)

    def update_data(self,data_1, data_2):
            self.data_1 = data_1
            self.data_2 = data_2
            self.update_widget()


class Info_Card_type_2(MDBoxLayout):
    def __init__(self, data, text, **kwargs):
        super(Info_Card_type_2, self).__init__(**kwargs)
        self.data = data
        self.text = text
        self.radius = 20
        self.orientation = 'horizontal'
        self.md_bg_color = '#00BD1E'
        self.size_hint_y = None
        self.padding = 20
        self.spacing = 20
        self.bind(pos=self.update_widget, size=self.update_widget, width=self.update_height)
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.13

    def update_widget(self, *args):
        self.clear_widgets()
        left_MD = MDBoxLayout(md_bg_color = '#AEAEAE', padding = 2, spacing = 2, radius = 20)
        left_MD_ = MDBoxLayout(md_bg_color='#00BD1E', padding=5, spacing=5, radius=20)
        left_MD_.add_widget(MDLabel(text=self.text, size_hint_x=.7, theme_text_color='Custom', halign='center', valign='middle', text_color=(1, 1, 1, 1), font_style='NewFont14'))
        left_MD.add_widget(left_MD_)
        self.add_widget(left_MD)

        right_MD = MDBoxLayout(md_bg_color = '#AEAEAE', padding = 2, spacing = 2, radius = 20)
        right_MD_ = MDBoxLayout(md_bg_color='#00BD1E', padding=5, spacing=5, radius=10)
        right_MD_.add_widget(MDLabel(text=str(self.data), size_hint_x=.7, theme_text_color='Custom', halign='center', valign='middle', text_color=(1, 1, 1, 1), font_style='NewFont14'))
        right_MD.add_widget(right_MD_)
        self.add_widget(right_MD)

    def update_data(self,data):
            self.data = data
            self.update_widget()


class Trapezoid(MDFloatLayout):
    def __init__(self, trapezoid_sizes,text,count, **kwargs):
        super(Trapezoid, self).__init__(**kwargs)
        self.trapezoid_sizes = trapezoid_sizes
        self.text = text
        self.count = count
        self.bind(pos=self.update_widget, size=self.update_widget, width=self.update_height)
        self.size_hint_y = None
        self.update_widget()  # Вызываем метод update_widget

    def update_height(self, instance, width_value):
        instance.height = width_value * 0.25

    def update_widget(self, *args):
        self.canvas.clear()

        with self.canvas:
            if float(self.text)>0:
                Color(*(1, 0, 0, 1))
                text_color = (1,1,1,1)
            else:
                Color(*(1, 1, 1, 1))
                text_color = (0, 0, 0, 1)

            # Вершины трапеции (x1, y1, x2, y2, x3, y3, x4, y4)
            points = [self.x + self.width * self.trapezoid_sizes[0], self.y,
                      self.x + self.width * self.trapezoid_sizes[1], self.y,
                      self.x + self.width * self.trapezoid_sizes[2], self.y + self.height,
                      self.x + self.width * self.trapezoid_sizes[3], self.y + self.height]

            # Рисуем трапецию с помощью Mesh
            Mesh(vertices=[points[0], points[1], 0, 1,
                           points[2], points[3], 0, 1,
                           points[4], points[5], 0, 1,
                           points[6], points[7], 0, 1],
                 indices=[0, 1, 2, 2, 3, 0],
                 mode='triangles')

            # # Рисуем границы трапеции
            # Line(points=[points[0], points[1], points[2], points[3], points[4], points[5], points[6], points[7],
            #              points[0], points[1]], width=1)
            self.add_widget(MDLabel(text=self.text +'% ' + self.count + ' (лот)', theme_text_color='Custom', halign='center',size_hint_y= None,pos_hint= {'x': 0,'center_y':.5}, font_style='NewFont24',
                    text_color=text_color))

    def update_data(self,new_data):
            self.data = new_data
            self.update_widget()


class Contragents_Card(ScrollView):
    def __init__(self, **kwargs):
        super(Contragents_Card, self).__init__(**kwargs)
        self.do_scroll_y = True
        self.data = date_handler.start_data['all_contragents']
        self.pos_hint = {"center_x": .5, "center_y": .5}
        self.md_bg_color = color_out
        self.update_widget()  # Вызываем метод update_widget
        self.bind(width=self.update_height)

    def update_height(self, instance, width_value):
        for child in self.content_layout.children:
            child.height = width_value*0.1 - 10
        self.content_layout.height = width_value * (len(self.data)+1)*0.1

    def update_height_1(self, data):
        for child in self.content_layout.children:
            child.height = self.width*0.1 - 10
        self.content_layout.height = self.width * (len(data)+1)*0.1

    def update_widget(self, *args):
        self.clear_widgets()

        self.content_layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, size_hint_y=None,  md_bg_color=color_out)


        self.content_layout.add_widget(Head_slider(left_text='КОНТРАГЕНТЫ', right_text=''))
        for contr in list(self.data.keys()):
            MD_lay = MDBoxLayout(radius=15, spacing=2, padding=2, md_bg_color='#AEAEAE', size_hint_y=None)
            MD_lay_1 = MDBoxLayout(md_bg_color=color_out, spacing=10, padding=10, radius=15)
            MD_lay_1.add_widget(MDTextButton(
                text=self.data[contr],
                size_hint=(.9, .9),
                theme_text_color='Custom',
                font_style='NewFont20',
                text_color=(1, 1, 1, 1),
                color=(1, 1, 1, 1),
                on_press=lambda y: MDApp.get_running_app().go_to_screen_level_3_1(1510)))
            MD_lay.add_widget(MD_lay_1)
            self.content_layout.add_widget(MD_lay)
        self.add_widget(self.content_layout)

    def update_data(self, button_id):

        self.data = button_id
        self.update_widget()
        self.update_height_1(button_id)



class Current_status(ScrollView):
    def __init__(self, **kwargs):
        super(Current_status, self).__init__(**kwargs)
        self.do_scroll_y = True
        self.do_scroll_x = False
        # self.size_hint = (.9, .95)
        # self.pos_hint = {"center_x": .5, "center_y": .5}
        self.md_bg_color = color_out
        self.color_in = color_out
        self.color = config.color_volume_bggo
        self.type = date_handler.start_data['slide_1']['all_status_L2']
        self.data = date_handler.start_data['slide_1']['hist_1']
        self.update_widget()  # Вызываем метод update_widget
        self.bind(width=self.update_height)

    def update_height(self, instance, width_value):
        for child in self.content_layout.children:
            child.height = width_value*0.15 - 10
        self.content_layout.height = width_value * (len(list(self.data[list(self.data.keys())[0]].keys()))+1)*0.15

    def update_height_1(self, data):
        for child in self.content_layout.children:
            child.height = self.width*0.15 - 10
        self.content_layout.height = self.width * (len(list(data[list(data.keys())[0]].keys()))+1)*0.15


    def update_widget(self, *args):
        level_1_instance = Level_1()
        type_keys_list = list(self.type.keys())
        self.clear_widgets()
        line =[[y,[self.data[x][y] for x in list(self.data.keys())]] for y in list(self.data[list(self.data.keys())[0]].keys())]
        self.content_layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, size_hint_y=None, md_bg_color=color_out)


        self.content_layout.add_widget(Head_slider(left_text='ТЕКУЩИЙ СТАТУС', right_text='123/249'))

        if line !=[]:
            max_line = max([sum(x[1]) for x in line])
            for x in line:
                MD_lay = MDBoxLayout(orientation='horizontal', radius=15, spacing=2, padding=2, md_bg_color='#AEAEAE',
                                     size_hint_y=None)
                MD_lay_1 = MDGridLayout(cols=3, md_bg_color=color_out, spacing=10, padding=10, radius=15)
                MDC = MDBoxLayout(md_bg_color=color_out, size_hint=(.5, 1))
                MDC.add_widget(MDLabel(
                    text=self.type[x[0]],
                    size_hint=(1, .9),
                    theme_text_color='Custom',
                    text_color=(1, 1, 1, 1),
                    color=(1, 1, 1, 1),
                    font_style='NewFont14'))
                lay_line = MDBoxLayout(orientation='horizontal', md_bg_color=self.color_in, spacing=10, padding=4)
                if sum(x[1]) != 0:
                    sum_MDB = MDBoxLayout(size_hint=(2.5 * sum(x[1]) / max_line, .95))
                    for i in range(len(list(self.data.keys()))):
                        if x[1][i] != 0:
                            sum_MDB.add_widget(MDBoxLayout(size_hint_x = (x[1][i]/sum(x[1])),md_bg_color= self.color[i]))

                    lay_line.add_widget(sum_MDB)

                lay_line.add_widget(
                    MDLabel(text=str(sum(x[1])), halign='left', theme_text_color='Custom',
                            text_color=(1, 1, 1, 1),font_style='NewFont16'))

                pict_but = MDIconButton(icon="icons/arrow_sh.png", size_hint=(.1, .5), font_size=30)
                pict_but.bind(
                    on_press=lambda y, x=x[0]: MDApp.get_running_app().go_to_screen_level_3_1(x)
                )

                MD_lay_1.add_widget(MDC)
                MD_lay_1.add_widget(lay_line)
                MD_lay_1.add_widget(pict_but)

                MD_lay.add_widget(MD_lay_1)

                self.content_layout.add_widget(MD_lay)

        self.add_widget(self.content_layout)

    def update_data(self, button_id):

        self.data = button_id['hist_1']
        self.type = button_id['all_status_L2']
        self.update_widget()
        self.update_height_1(button_id['hist_1'])





class HeadGPN(MDGridLayout): ## Шапка приложения
    pass



class FirstScreen(MDScreen):
    pass


class SecondScreen(MDScreen):
    pass


class ThirdScreen(MDScreen):
    pass

class ThirdScreenLevel_1(MDScreen):
    pass

class Level_1(ScrollView):
    def __init__(self, **kwargs):
        super(Level_1, self).__init__(**kwargs)
        self.do_scroll_y = True
        self.pos_hint = {"center_x": .5, "center_y": .5}
        self.color_in = color_out
        self.data = config.card
        self.update_widget()  # Вызываем метод update_widget
        self.bind(width=self.update_height)

    def update_height(self, instance, width_value):
        for child in self.content_layout.children:
            child.height = width_value*0.4 - 10
        self.content_layout.height = width_value * min(20, len(self.data))*0.4

    def update_height_1(self, data):
        for child in self.content_layout.children:
            child.height = self.width*0.1 - 10
        self.content_layout.height = self.width *min(20, len(self.data))*0.4


    def update_widget(self, *args):
        self.clear_widgets()
        print(self.data)
        self.content_layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10, radius=15, size_hint_y=None)
        if self.data != []:
            for card in self.data:
                if len(self.content_layout.children)>20: break
                Gen_Box = MDBoxLayout(orientation='vertical', spacing=5, padding=5, radius=10,  md_bg_color=color_out)
                Gen_Box_in = MDBoxLayout(orientation='vertical', spacing=5, padding=5, radius=10,  md_bg_color=(1,1,1,1))

                Name_Box = MDBoxLayout(orientation='horizontal', spacing=5, size_hint=(1, .2))
                Name_Box.add_widget(MDLabel(text=str(card[0]), halign='left', theme_text_color='Custom',font_style='NewFont20',
                                        text_color=(0, 0, 0, 1),size_hint=(.7, 1)))
                pic_box_1 = MDBoxLayout(orientation='horizontal', spacing=5, size_hint=(.1, 1))
                if int(card[2])>=3:
                    pic_box_1.add_widget(MDIcon(icon='icons/oval_green.png',pos_hint= {"center_x": .5, "center_y": .5}))
                else:
                    pic_box_1.add_widget(MDIcon(icon='icons/oval_red.png', pos_hint={"center_x": .5, "center_y": .5}))

                pic_box_2 = MDBoxLayout(orientation='horizontal', spacing=5, size_hint=(.1, 1))
                if int(card[4])>40:
                    pic_box_2.add_widget(MDIcon(icon='icons/rect_red.png',pos_hint= {"center_x": .5, "center_y": .5}))
                else:
                    pic_box_2.add_widget(MDIcon(icon='icons/rect_green.png', pos_hint={"center_x": .5, "center_y": .5}))

                pic_box_3 = MDBoxLayout(orientation='horizontal', spacing=5, size_hint=(.1, 1))
                if card[5]>0:
                    pic_box_3.add_widget(MDIcon(icon='icons/romb_green.png',pos_hint= {"center_x": .5, "center_y": .5}))
                else:
                    pic_box_3.add_widget(MDIcon(icon='icons/romb_red.png', pos_hint={"center_x": .5, "center_y": .5}))

                Name_Box.add_widget(pic_box_1)
                Name_Box.add_widget(pic_box_2)
                Name_Box.add_widget(pic_box_3)

                Gen_Box_in.add_widget(Name_Box)

                Gen_Box_in.add_widget(MDLabel(
                    text='НСУ  |  '+ str(card[1]) + '  |  ' + str(card[2]),font_style='NewFont18',
                    size_hint=(1, .2), halign='left', theme_text_color='Custom',
                    text_color=(0, 0, 0, 1)))

                if len(str(card[3]))>150:
                    text = str(card[3])[:150] + "..."
                else:
                    text = str(card[3])

                Gen_Box_in.add_widget(MDLabel(text=text,
                                              theme_text_color='Custom',font_style='NewFont14',
                            text_color=(0, 0, 0, 1), size_hint=(1, .6)))

                Gen_Box.add_widget(Gen_Box_in)
                self.content_layout.add_widget(Gen_Box)
        self.add_widget(self.content_layout)

    def update_data(self, button_id):
        self.data = button_id
        self.update_widget()
        self.update_height_1(self.data)


class ItemConfirm(OneLineAvatarIconListItem): ## Диалоговое окно с chekbox для фильтрации
    divider = None


class LoadingScreen(MDScreen):
    pass


# class LoadDialog(BoxLayout):
#     load = ObjectProperty(None)
#     cancel = ObjectProperty(None)


class MainApp(MDApp):
    dialog = None

    slider_1 = None
    slider_2 = None
    slider_3 = None
    slider_4 = None
    cur_stat = None
    contragents = None
    custom_sheet = None
    level_1 = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = MDScreenManager()

    def build(self): ## Определение основных настроек дизайна и определение окнон
        self.theme_cls.material_style = "M3"

        LabelBase.register(name='NewFont', fn_regular='fonts/dinpro_condensedbold.otf')
        self.theme_cls.font_styles.update(
            {"NewFont46": ['NewFont', 46, 'fonts/dinpro_condensedbold.otf'],
             "NewFont26": ['NewFont', 26, 'fonts/dinpro_condensedbold.otf'],
             "NewFont24": ['NewFont', 24, 'fonts/dinpro_condensedbold.otf'],
             "NewFont22": ['NewFont', 22, 'fonts/dinpro_condensedbold.otf'],
             "NewFont20": ['NewFont', 20, 'fonts/dinpro_condensedbold.otf'],
             "NewFont18": ['NewFont', 18, 'fonts/dinpro_condensedbold.otf'],
             "NewFont16": ['NewFont', 16, 'fonts/dinpro_condensedbold.otf'],
             "NewFont14": ['NewFont', 14, 'fonts/dinpro_condensedbold.otf'],
             "NewFont12": ['NewFont', 12, 'fonts/dinpro_condensedbold.otf']}
        )

        root_widget = Builder.load_string(kv_text.KV)

        self.screen_manager = root_widget.ids['screen_manager']


        first_screen = self.screen_manager.get_screen('first')
        second_screen = self.screen_manager.get_screen('second')
        third_screen = self.screen_manager.get_screen('third')
        third_l_1_screen = self.screen_manager.get_screen('third_l_1')
        loading_screen = self.screen_manager.get_screen('loading')

        # Получите ссылку на экземпляр класса Slider_1
        slider_1_instance = first_screen.ids['slider_1']
        slider_2_instance = first_screen.ids['slider_2']
        slider_3_instance = first_screen.ids['slider_3']
        slider_4_instance = first_screen.ids['slider_4']
        cur_stat_insatnce = second_screen.ids['cur_stat']
        contragents_insatnce = third_screen.ids['contragents']
        level_1_insatnce = third_l_1_screen.ids['level_1']

        self.set_slider_1(slider_1_instance)
        self.set_slider_2(slider_2_instance)
        self.set_slider_3(slider_3_instance)
        self.set_slider_4(slider_4_instance)
        self.set_cur_stat(cur_stat_insatnce)
        self.set_contragents(contragents_insatnce)
        self.set_level_1(level_1_insatnce)


        return root_widget

    def change_screen(self,screen):
        self.screen_manager.current = (screen)

    def file_manager_open(self):
        if platform =='android':
            path = "/storage/emulated/0"
        else:
            path = '/'
        filechooser.open_file(on_selection=self.handle_selection, path=path)

    def handle_selection(self, selection):
        if selection:
            file_path = selection[0]
            toast(f"Выбран файл: {file_path}")
            try:
                date_handler.update_xl(file_path = file_path)
            except Exception as e:
                toast("Неверный файл\n" + str(e))
            self.reset_filters()

        else:
            toast("Ничего не выбрано")

    def go_to_screen_level_3_1(self, l2):
        inf = date_handler.Update_Data("example.db").get_by_cards_current_status_l1(l2)
        self.level_1.update_data(button_id=inf)
        self.screen_manager.current='third_l_1'

    def show_example_custom_bottom_sheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        self.custom_sheet.open()

    def show_date_picker_finish(self): ## Открывает окно фильтрации с датоами подведения итогов
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_date_range_selected_finish)
        date_dialog.open()

    def show_date_picker_start(self): ## Открывает окно фильтрации с датами инициации
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_date_range_selected_start)
        date_dialog.open()


    def show_alert_dialog_customers(self):
        # if not self.dialog:
        customers_list = date_handler.Update_Data("example.db",startDate=None, factDateFinish=None, customer=None,
             services_L3=None, procedureYear=None, organizator=None).all_customers()
        items = [ItemConfirm(text=cust[1]) for cust in customers_list]
        self.dialog = MDDialog(
            title="Заказчики",
            type="confirmation",
            items=items,
            buttons=[
                MDFlatButton(
                    text="Отмена",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="Выбрать",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.select_dialog_customers
                ),
            ],
        )
        self.dialog.open()

    def show_alert_dialog_services(self): ## Открывает окно фильтрации и настроек
        # if not self.dialog:
        services_list = date_handler.Update_Data("example.db",startDate=None, factDateFinish=None, customer=None,
             services_L3=None, procedureYear=None, organizator=None).all_services_L3()
        items = [ItemConfirm(text=serv[1]) for serv in services_list]
        self.dialog = MDDialog(
            title="Услуги",
            type="confirmation",
            items=items,
            buttons=[
                MDFlatButton(
                    text="Отмена",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="Выбрать",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.select_dialog_services
                ),
            ],
        )
        self.dialog.open()

    def get_checked_items(self):
        checked_items = []
        for item in self.dialog.items:
            if item.ids.check.active:  # проверка, включен ли чекбокс
                checked_items.append(item.text)
        return checked_items

    def select_dialog_customers(self, *args): ## Открывает окно фильтрации с выбором заказчиков
        checked_items = self.get_checked_items()
        reverse_cust = {cust[1]: cust[0] for cust in date_handler.Update_Data("example.db",startDate=None, factDateFinish=None, customer=None,
                 services_L3=None,
                 procedureYear=None, organizator=None).all_customers()}
        self.get_customers([reverse_cust[cust] for cust in checked_items])
        self.dialog.dismiss()

    def select_dialog_services(self, *args): ## Открывает окно фильтрации с выбором услуг
        checked_items = self.get_checked_items()
        reverse_serv = {serv[1]: serv[0] for serv in date_handler.Update_Data("example.db",startDate=None, factDateFinish=None, customer=None,
                 services_L3=None,
                 procedureYear=None, organizator=None).all_services_L3()}
        self.get_services([reverse_serv[serv] for serv in checked_items])
        self.dialog.dismiss()

    def close_dialog(self, instance): ## Закрывает диалоговое окно
        self.dialog.dismiss()

    def on_date_range_selected_finish(self, instance, today, dates):
        self.get_factDateFinish(today, dates)

    def on_date_range_selected_start(self, instance, today, dates):
        self.get_startDate(today, dates)

    def set_slider_1(self, slider):
        self.slider_1 = slider

    def set_slider_2(self, slider):
        self.slider_2 = slider

    def set_slider_3(self, slider):
        self.slider_3 = slider

    def set_slider_4(self, slider):
        self.slider_4 = slider

    def set_cur_stat(self, slider):
        self.cur_stat = slider

    def set_contragents(self, slider):
        self.contragents = slider

    def set_level_1(self, slider):
        self.level_1 = slider

    def change_data(self, instance, value): ## Обновление данных (новые данные value поступают в каждый метод change_data каждого слайда и экрана)
        self.slider_1.change_data(button_id=value['slide_1'])
        self.slider_2.change_data(button_id=value['slide_2'])
        self.slider_3.change_data(button_id=value['slide_3'])
        self.slider_4.change_data(button_id=value['slide_4'])
        self.cur_stat.update_data(button_id=value['slide_1'])
        self.contragents.update_data(button_id=value['all_contragents'])

    def get_factDateFinish(self, today, factDateFinish): ## Фильтрация по дате подведению итогов
        date_handler.factDateFinish = [factDateFinish[0], factDateFinish[-1]]

        self.screen_manager.current = 'loading'

        def update_and_reset():
            date_handler.start_data = date_handler.new_start_data_def()
            Clock.schedule_once(lambda dt: self.after_update(), 0)

        self.thread = threading.Thread(target=update_and_reset)
        self.thread.start()

    def get_startDate(self, today, startDate): ## Фильтрация по дате инициации
        date_handler.startDate = [startDate[0], startDate[-1]]

        self.screen_manager.current = 'loading'

        def update_and_reset():
            date_handler.start_data = date_handler.new_start_data_def()
            Clock.schedule_once(lambda dt: self.after_update(), 0)

        self.thread = threading.Thread(target=update_and_reset)
        self.thread.start()

    def get_organizators(self, organizatorId): ## Фильтрация по организаторам
        self.screen_manager.current = 'loading'
        date_handler.organizator = organizatorId

        def update_and_reset():
            date_handler.start_data = date_handler.new_start_data_def()
            Clock.schedule_once(lambda dt: self.after_update(), 0)

        self.thread = threading.Thread(target=update_and_reset)
        self.thread.start()

        return date_handler.start_data

    def get_customers(self, customersID): ## Фильтрация по заказчикам
        date_handler.customer = customersID

        self.screen_manager.current = 'loading'

        def update_and_reset():
            date_handler.start_data = date_handler.new_start_data_def()
            Clock.schedule_once(lambda dt: self.after_update(), 0)

        self.thread = threading.Thread(target=update_and_reset)
        self.thread.start()

    def get_services(self, sericesID): ## Фильтрация по услугам
        date_handler.services_L3 = sericesID

        self.screen_manager.current = 'loading'

        def update_and_reset():
            date_handler.start_data = date_handler.new_start_data_def()
            Clock.schedule_once(lambda dt: self.after_update(), 0)

        self.thread = threading.Thread(target=update_and_reset)
        self.thread.start()

    def reset_filters(self): ## Очистка филтров
        date_handler.startDate = None
        date_handler.factDateFinish = None
        date_handler.customer = None
        date_handler.services_L3 = None
        date_handler.procedureYear = None
        date_handler.organizator = None

        self.screen_manager.current = 'loading'

        def update_and_reset():
            date_handler.start_data = date_handler.new_start_data_def()
            Clock.schedule_once(lambda dt: self.after_update(), 0)

        self.thread = threading.Thread(target=update_and_reset)
        self.thread.start()

    def after_update(self): ## Прекращение работы потока
        if self.thread.is_alive():
            # Если поток все еще работает, повторить проверку через 0.1 секунды
            Clock.schedule_once(lambda dt: self.after_update(), 0)
        else:
            # Если поток завершился, изменить экран и обновить данные
            self.screen_manager.current = 'first'
            self.change_data(self, date_handler.start_data)




if __name__ == "__main__":
    MainApp().run()
