KV = """        
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MDScreen:
    MDScreenManager:
        id: screen_manager
        FirstScreen:
            name: 'first'
        SecondScreen:
            name: 'second'
        ThirdScreen:
            name: 'third'
        ThirdScreenLevel_1:
            name: 'third_l_1'            
        LoadingScreen:
            name: 'loading'       

<LoadingScreen>:
    name: 'loading'
    FloatLayout:
        MDSpinner:
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            active: True

<ItemForCustomBottomSheet@OneLineIconListItem>
    on_press: app.custom_sheet.dismiss()
    icon: ""

    IconLeftWidget:
        icon: root.icon

<ContentCustomSheet@MDBoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "3000dp"

    MDTopAppBar:
        title: 'Настройки и фильтрация:'

    ScrollView:

        MDGridLayout:
            cols: 1
            adaptive_height: True

            ItemForCustomBottomSheet:
                icon: "map-clock-outline"
                text: "Год"
                font_style: 'NewFont20'

            ItemForCustomBottomSheet:
                icon: "timetable"
                text: "Диапазон дат подведения итогов по дате протокола ЗК"
                font_style: 'NewFont20'
                on_press: app.show_date_picker_finish()
                
            ItemForCustomBottomSheet:
                icon: "clipboard-text-clock-outline"
                text: "Диапазон дат по дате инициации отбора"
                font_style: 'NewFont20'
                on_press: app.show_date_picker_start()
                
            ItemForCustomBottomSheet:
                icon: "face-agent"
                text: "Заказчики"
                font_style: 'NewFont20'
                on_press: app.show_alert_dialog_customers()

            ItemForCustomBottomSheet:
                icon: "toolbox-outline"
                text: "Сектор услуг"
                font_style: 'NewFont20'
                on_press: app.show_alert_dialog_services()
                
            ItemForCustomBottomSheet:
                icon: "layers-off"
                text: "Сбросить фильтры"
                font_style: 'NewFont20'
                on_press: app.reset_filters()

            ItemForCustomBottomSheet:
                icon: "database-arrow-down-outline"
                text: "Обновление данных"
                font_style: 'NewFont20'
                on_press: 
                    app.screen_manager.transition = FadeTransition()
                    app.file_manager_open()
                    # app.screen_manager.current = 'first'

<ItemConfirm>:

    CheckboxLeftWidget:
        id: check
        

<HeadGPN>
    size_hint:  (1, .3)
    cols:1
    radius: 15
    RelativeLayout:
        size_hint:  (1, .2)
        FitImage
            radius: [0,0,25,25]
            source: 'pic/head.jpg'
        AsyncImage:
            source: 'pic/logo-gazprom-neft1.png'
            opacity: 0.5
            allow_stretch:True
            size_hint:
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        FloatLayout:
            size_hint: (1, 1)
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint: (.8, .4)
                md_bg_color: (.9,.9,.9,1)
                radius:10
                pos_hint: {'center_x':.5,'y': -.2} 
                MDTextField:
                    size_hint: (1.3, 1.7)
                    font_size: '16sp'
                    text_color_normal: "blue"
                    icon_left: 'magnify'
                    icon_left_color_normal: "green"
                    pos_hint: {'center_x':.5,'y': -.35} 
                MDFloatingActionButton:
                    type: "small"
                    pos_hint: {'center_x':1,'y':0} 
                    icon: "tune"
                    on_release: app.show_example_custom_bottom_sheet()


    ScrollView:
        do_scroll_x: True
        size_hint_y: .1
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 10
            size_hint_x: None
            width: self.minimum_width
            center_y:100
            MDTextButton:
                custom_color: "black"
                text:'БО РиУ(БЛПС)'
                font_style: 'NewFont20'
                size_hint_x:None 
                on_press: app.change_data(self, app.get_organizators(501))
            MDTextButton:
                custom_color: "black"
                text:'БО РиУ(ДРП)'
                font_style: 'NewFont20'
                size_hint_x:None 
                on_press: app.change_data(self, app.get_organizators(502))
            MDTextButton:
                custom_color: "black"
                text:'БО РиУ(БДР)'
                font_style: 'NewFont20'
                size_hint_x:None 
                on_press: app.change_data(self, app.get_organizators(503))
            MDTextButton:
                custom_color: "black"
                text:'БО РиУ(РОЦО)'
                font_style: 'NewFont20'
                size_hint_x:None 
                on_press: app.change_data(self, app.get_organizators(504))
            MDTextButton:
                custom_color: "black"
                text:'БО РиУ(ДОКЗ)'
                font_style: 'NewFont20'
                size_hint_x:None
                on_press: app.change_data(self, app.get_organizators(505)) 
            MDTextButton:
                custom_color: "black"
                text:'БО РиУ(ГПН-С)'
                font_style: 'NewFont20'
                size_hint_x:None 
                on_press: app.change_data(self, app.get_organizators(506))
                

            # MDTextButton:
            #     custom_color: "black"
            #     text:'БО РиУ(БЛПС)'
            #     size_hint_x:None 
            #     on_press: app.file_manager_open()
            # MDTextButton:
            #     custom_color: "black"
            #     text:'БО РиУ(ДРП)'
            #     size_hint_x:None 
            # MDTextButton:
            #     custom_color: "black"
            #     text:'БО РиУ(БДР)'
            #     size_hint_x:None 
            #     on_press: app.change_data_donut(self, [1, 1, 11, 1])
            # MDTextButton:
            #     custom_color: "black"
            #     text:'БО РиУ(РОЦО)'
            #     size_hint_x:None 
            #     on_press: app.change_data_donut(self, [11, 1, 1, 1])
            # MDTextButton:
            #     custom_color: "black"
            #     text:'БО РиУ(ДОКЗ)'
            #     size_hint_x:None
            #     on_press: app.change_data(self, app.get_sliders()) 
            # MDTextButton:
            #     custom_color: "black"
            #     text:'БО РиУ(ГПН-С)'
            #     size_hint_x:None 
            #     on_press: app.change_data(self, app.get_sliders_r())

<FirstScreen>:
    name: 'first'
    AnchorLayout:
        AsyncImage:
            source: 'pic/w2.jpg'
            allow_stretch: True
            keep_ratio: False

        MDGridLayout:
            cols:1
            radius: 15
            HeadGPN

            MDBoxLayout:
                radius: 30
                pos_hint: {"center_x": .5, "center_y": .5}
                Carousel:
                    direction:'right'
                    Slider_1:
                        id: slider_1
                    Slider_2:
                        id: slider_2   
                    Slider_3:
                        id: slider_3 
                    Slider_4:
                        id: slider_4                                                                                                                     
                                                                                                                              

                                     
            MDBoxLayout:
                size_hint: (1, .10)
                orientation: 'horizontal'
                padding: dp(10), dp(10), dp(10), dp(10)

                MDIconButton:
                    icon: "icons/1_act.png"
                    size_hint_x: 0.5
                    font_size: dp(30)

                MDIconButton:
                    icon: "icons/2.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.transition = FadeTransition()
                        root.manager.current = 'second'

                MDIconButton:
                    icon: "icons/3.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.transition = FadeTransition()
                        root.manager.current = 'third'



<SecondScreen>:
    name: 'second'
    AnchorLayout:
        AsyncImage:
            source: 'pic/w2.jpg'
            allow_stretch: True
            keep_ratio: False


        MDGridLayout:
            cols:1
            radius: 15
            HeadGPN
            MDBoxLayout:
                padding: [40,15,40,15]
                radius: 30
                pos_hint: {"center_x": .5, "center_y": .5}
                Current_status:
                    id: cur_stat
                        
            MDBoxLayout:
                size_hint: (1, .10)
                orientation: 'horizontal'
                padding: dp(10), dp(10), dp(10), dp(10)

                MDIconButton:
                    icon: "icons/1.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.transition = FadeTransition()
                        root.manager.current = 'first'

                MDIconButton:
                    icon: "icons/2_act.png"
                    size_hint_x: 0.5
                    font_size: dp(30)


                MDIconButton:
                    icon: "icons/3.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.transition = FadeTransition()
                        root.manager.current = 'third'

<ThirdScreen>:
    name: 'third'
    AnchorLayout:
        AsyncImage:
            source: 'pic/w2.jpg'
            allow_stretch: True
            keep_ratio: False


        MDGridLayout:
            cols:1
            radius: 15
            HeadGPN
            MDBoxLayout:
                radius: 30
                pos_hint: {"center_x": .5, "center_y": .5}
                padding: [40,15,40,15]
                MDBoxLayout:
                    Contragents_Card:
                        id: contragents
            MDBoxLayout:
                size_hint: (1, .10)
                orientation: 'horizontal'
                padding: dp(10), dp(10), dp(10), dp(10)

                MDIconButton:
                    icon: "icons/1.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.transition = FadeTransition()
                        root.manager.current = 'first'
                MDIconButton:
                    icon: "icons/2.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.transition = FadeTransition()
                        root.manager.current = 'second'

                MDIconButton:
                    icon: "icons/3_act.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    
                
<ThirdScreenLevel_1>:
    name: 'third_l_1'
    AnchorLayout:
        AsyncImage:
            source: 'pic/w2.jpg'
            allow_stretch: True
            keep_ratio: False


        MDGridLayout:
            cols:1
            radius: 15
            HeadGPN
            
            ScrollView:
                do_scroll_x: True
                size_hint_y: .1
                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    padding: 10
                    size_hint_x: None
                    width: self.minimum_width
                    center_y:100
                    MDTextButton:
                        custom_color: "black"
                        text:'Статус 1'
                        font_style: 'NewFont16'
                        size_hint_x:None 
                        on_press: app.change_data(self, app.get_organizators(501))
                    MDTextButton:
                        custom_color: "black"
                        text:'Статус 1'
                        font_style: 'NewFont16'
                        size_hint_x:None 
                        on_press: app.change_data(self, app.get_organizators(501))
                    MDTextButton:
                        custom_color: "black"
                        text:'Статус 2'
                        font_style: 'NewFont16'
                        size_hint_x:None 
                        on_press: app.change_data(self, app.get_organizators(501))
                    MDTextButton:
                        custom_color: "black"
                        text:'Статус 3'
                        font_style: 'NewFont16'
                        size_hint_x:None 
                        on_press: app.change_data(self, app.get_organizators(501))
                    MDTextButton:
                        custom_color: "black"
                        text:'Статус 4'
                        font_style: 'NewFont16'
                        size_hint_x:None 
                        on_press: app.change_data(self, app.get_organizators(501))
            
            MDBoxLayout:
                padding: [40, 15, 40, 15]
                Level_1:
                    id: level_1
            MDBoxLayout:
                size_hint: (1, .10)
                orientation: 'horizontal'
                padding: dp(10), dp(10), dp(10), dp(10)

                MDIconButton:
                    icon: "icons/1.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.transition = FadeTransition()
                        root.manager.current = 'first'
                MDIconButton:
                    icon: "icons/2_act.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.transition = FadeTransition()
                        root.manager.current = 'second'

                MDIconButton:
                    icon: "icons/3.png"
                    size_hint_x: 0.5
                    font_size: dp(30)
                    on_press:
                        root.manager.current = 'third'
                                   """
