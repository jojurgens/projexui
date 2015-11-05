from xqt import QtGui, QtCore
Qt = QtCore.Qt

class Demo(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.widgets = []
        self.buttons = {}

        lay = QtGui.QVBoxLayout(self)
        for name, method, tip in [
            ('CalendarWidget',     self.XCalendarWidget, ''),
            ('ChartWidgetItem',    self.XChartWidgetItem, ''),
            ('GanttWidget',        _gantt_demo, ''),
            ('TreeWidget',         self.XTreeWidget, 'Extends the base QTreeWidget class with additional methods.'),

            ('KeyValueTreeWidget', self.XKeyValueTreeWidget, 'Creates a key/value pair editing tree widget.'),
            ('MultiTagEdit',       self.XMultiTagEdit, 'Defines a multi-taggable widget object, like a magnet board.'),
            ('PopupWidget',        self.XPopupWidget, 'Extends the base QToolButton class to support popup widgets.'),
            ('Menu',               self.XMenu, 'Extends the base QToolButton class to support popup widgets.'),
            ('Image Slider', self.XImageSlider, ''),
            ('Collapsible Logger', self.XCollapsibleLoggerWidget, 'Defines a view for the XViewWidget based on the XConsoleEdit.'),
            ('RatingSlider',       self.XRatingSlider, ''),
            ('SplitButton',        self.XSplitButton, 'Multi-checkable tool button based on QActions and QActionGroups'),
            ('TimerLabel',         self.XTimerLabel, '')]:

            butt = QtGui.QPushButton(name)
            butt.setToolTip(tip)
            butt.clicked.connect(method)
            lay.addWidget(butt)
            self.buttons[name] = butt

    # main widgets

    def XCalendarWidget(self, *x):
        from widgets.xcalendarwidget import XCalendarWidget,XCalendarItem
        widget = XCalendarWidget(None)
        scn = widget.scene()
        it1 = XCalendarItem()
        it1.setDuration(4)
        it1.setBorderColor(QtGui.QColor(22,123,233))
        it1.setDescription('Blah blah blah')
        it1.setTitle('Long Task')
        scn.addItem(it1)
        scn.addItem(XCalendarItem())
        scn.addItem(XCalendarItem())
        widget.resize(1000,900)
        self._show_widget(widget)

    def XChartWidgetItem(self, *x):
        from widgets.xchartwidget.xchartwidget import XChartWidget
        from widgets.xchartwidget.xchartwidgetitem import XChartWidgetItem
        from widgets.xchartwidget.xchartscene import XChartScene

        def make_widget(chartType, twoCharts=True):
            widget = XChartWidget(None)
            scene = widget.scene()
            isinstance(scene, XChartScene)

            item = XChartWidgetItem()
            item.addPoint(1,10)
            item.addPoint(30,20)
            item.addPoint(50,60)
            item.addPoint(60,90)
            item.addPoint(70,10)
            item.addPoint(95,30)
            item.setTitle('lalala')
            scene.addItem(item)

            if twoCharts or 1:
                item2 = XChartWidgetItem()
                item2.addPoint(1,20)
                item2.addPoint(20,50)
                item2.addPoint(30,20)
                item2.addPoint(55,10)
                item2.addPoint(65,80)
                item2.addPoint(95,40)
                item2.setTitle('bobobo')
                scene.addItem(item2)

            scene.setChartType(chartType)
            return widget

        mainWidget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout(mainWidget)
        layout.addWidget(make_widget(XChartScene.Type.Bar))
        layout.addWidget(make_widget(XChartScene.Type.Pie))
        layout.addWidget(make_widget(XChartScene.Type.Line))
        mainWidget.resize(600, 800)
        self._show_widget(mainWidget)

    def XTreeWidget(self, *x):
        from widgets.xtreewidget import XTreeWidget, XTreeWidgetItem

        w = XTreeWidget(None)
        w.setColumns(['First', 'Second', 'Third'])
        item = w.headerItem()
        for i in range(item.columnCount()):
            item.setTextAlignment(i, Qt.AlignBottom | Qt.AlignHCenter)
        t = XTreeWidgetItem
        a,b = t('a'), t('b')
        w.addTopLevelItems([a,b])

        a.addChild(t(a, ['a', 'b', 'c']))
        a.addChild(t(a, ['x', 'y', 'z']))
        a.addChild(t(a, ['1', '2', '3']))

        b.addChild(t(b, ['a', 'b', 'c']))
        b.addChild(t(b, ['x', 'y', 'z']))
        b.addChild(t(b, ['1', '2', '3']))

        a.setExpanded(True)
        w.resize(320, 150)

        self._show_widget(w)


    # smaller windgets

    def XKeyValueTreeWidget(self, *x):
        import widgets.xkeyvaluetreewidget as module
        widget = module.XKeyValueTreeWidget(None)
        widget.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers) # SelectedClicked
        widget.setDictionary(dict(zip(range(26), list('abcdefghijklmnopqrstuvwxyz'))))
        self._show_widget(widget)

    def XMultiTagEdit(self, *x):
        import widgets.xmultitagedit as module
        widget = module.XMultiTagEdit(None)
        self._show_widget(widget)

    def XPopupWidget(self, *x):
        import widgets.xpopupbutton as module
        widget = module.XPopupWidget(self.buttons['PopupWidget'])
##        widget.mapAnchorFrom(self.buttons['PopupWidget'],
##                             QtGui.QCursor.pos())
##        widget.show()
        self._show_widget(widget)

    def XMenu(self):
        import menus.xmenu as module
        menu = module.XMenu(self)
        self.buttons['Menu'].setMenu(menu)

        menu.addSection('Group 1')
        menu.setTitle('Grouping Options')
        menu.setShowTitle(True)
        menu.addAction('Edit Advanced Grouping')

        menu.addSeparator()

        action = menu.addAction('No Grouping')
        action.setCheckable(True)

        action = menu.addAction('Group 2')
        action2 = module.QAction('Action with Advanced Option', menu)
        menu.setAdvancedAction(action, action2)

        menu.addSection('Skrakk')
        action = menu.addAction('Billy')
        action = menu.addAction('Bobby')
        action = menu.addAction('Benny')

        menu.addSearchAction()
        menu.show()

    def XImageSlider(self):
        from widgets.ximageslider import XImageSlider

        widget = XImageSlider()
        widget.setPixmaps([QtGui.QPixmap(r"C:\Users\Public\Pictures\Sample Pictures\Hydrangeas.jpg"),
                           QtGui.QPixmap(r"C:\Users\Public\Pictures\Sample Pictures\Chrysanthemum.jpg"),
                           QtGui.QPixmap(r"C:\Users\Public\Pictures\Sample Pictures\Desert.jpg"),
                           QtGui.QPixmap(r"C:\Users\Public\Pictures\Sample Pictures\Penguins.jpg"),
                           QtGui.QPixmap(r"C:\Users\Public\Pictures\Sample Pictures\Koala.jpg"),
                           QtGui.QPixmap(r"C:\Users\Public\Pictures\Sample Pictures\Jellyfish.jpg"),
                           QtGui.QPixmap(r"C:\Users\Public\Pictures\Sample Pictures\Tulips.jpg")])
        self._show_widget(widget)

    def XCollapsibleLoggerWidget(self):
        from widgets.xcollapsibleloggerwidget import XCollapsibleLoggerWidget
        widget = XCollapsibleLoggerWidget()
        widget.debug('Debug message')
        widget.critical('Critical message')
        widget.error('Error message')
        self._show_widget(widget)



    def XRatingSlider(self, *x):
        import widgets.xratingslider as module
        widget = module.XRatingSlider(None)
        self._show_widget(widget)

    def XSplitButton(self, *x):
        import widgets.xsplitbutton as module
        widget = module.XSplitButton(None)
        widget.addAction('a')
        widget.addAction('b')
        widget.addAction('c')
        self._show_widget(widget)

    def XTimerLabel(self, *x):
        import widgets.xtimerlabel as module
        widget = module.XTimerLabel(None)
        widget.start()
        self._show_widget(widget)

    def _show_widget(self, widget):
        widget.setWindowTitle(str(widget).split('.')[-1].split(' ')[0])
        widget.show()
        widget.raise_()
        self.widgets.append(widget)

    def closeEvent(self, event):
        import sys
        sys.exit(0)



def _gantt_demo(*x):
    from datetime import date, datetime
    from xqt.QtGui import QColor
    from xqt.QtCore import Qt, QDate
    from widgets.xganttwidget import  XGanttWidget, XGanttWidgetItem

    TEST_DATAS = [
        {'kind' : 'booking', 'reference': '001', 'cache_room': 'Habitacion 201', 'cache_accommodation': 'Sencilla', 'state': 'draft', 'cache_party': 'Juan Jimenez', 'start_date': datetime(2014, 6, 7, 11,10), 'end_date': datetime(2014,6,10, 19,50)},
        {'kind' : 'maintenance', 'reference': '', 'cache_room': 'Habitacion 202', 'state': 'draft', 'cache_party': 'Marcos Parra', 'start_date': datetime(2014, 4, 1, 1, 20), 'end_date': datetime(2014, 4, 8, 5, 10)},
        {'kind' : 'booking', 'reference': '002', 'cache_room': 'Habitacion 203', 'cache_accommodation': 'Sencilla', 'state': 'confirmed', 'cache_party': 'Diego Hinestroza', 'start_date': datetime(2014, 4, 11, 15,00), 'end_date': datetime(2014, 4, 12, 13,10)},
        {'kind' : 'booking', 'reference': '038', 'cache_room': 'Habitacion 203', 'cache_accommodation': 'Sencilla', 'state': 'submitted', 'cache_party': 'Francisco Mendieta', 'start_date': datetime(2014, 4, 15, 1, 10), 'end_date': datetime(2014, 4, 18, 22,06)},
        {'kind' : 'maintenance', 'reference': '', 'cache_room': 'Habitacion 204', 'cache_accommodation': '', 'state': 'finished', 'cache_party': 'Gonzalo Castelllanos', 'start_date': datetime(2014, 5, 4, 16, 33), 'end_date': datetime(2014, 5, 13, 9,10)},
        {'kind' : 'booking', 'reference': '017', 'cache_room': 'Habitacion 205', 'cache_accommodation': 'Triple', 'state': 'guaranteed', 'cache_party': 'Ramiro Martinez', 'start_date': datetime(2014, 4, 14, 15, 8), 'end_date': datetime(2014, 4, 17, 14, 40)},
        {'kind' : 'maintenance', 'reference': '', 'cache_room': 'Habitacion 206', 'state': 'confirmed', 'cache_party': 'Cristian Zapata', 'start_date': datetime(2014, 5, 11), 'end_date': datetime(2014, 5, 17)},
    ]

    state2color = {
            'booking': {
                'draft': QColor(210, 230, 230),  #gray
                'confirmed': QColor(150, 250, 85),  #green
                'guaranteed': QColor(20, 210, 250),  #blue
                'submitted': QColor(120, 110, 250),  #blue-dark
                },
            'maintenance': {
                'draft': QColor(255, 200, 80), #orange
                'confirmed': QColor(255, 0, 40), #red
                'finished': QColor(255, 250, 240), #soft-gray
            }}

    trans_state = {
            'draft': 'Borrador',
            'confirmed': 'Confirmada',
            'submitted': 'Ocupada',
            'guaranteed': 'Garantizada',
            'maintenance': 'Mantenimiento',
            'finished': 'Finalizada',
    }

    trans_kind = {
            'booking': 'Reserva',
            'maintenance': 'Mantenimiento',
    }

    class Gantt():

        def __init__(self, datas=None):
            self.gantt_widget = XGanttWidget()
            self.gantt_widget.setWindowTitle('Operations Forecast')
            self.gantt_widget.setWindowFlags(Qt.Dialog)
            self.gantt_widget.show()
            self.itemsList = {}
            if not datas:
                datas = TEST_DATAS
            self.process_data(datas)

        def get_convert_date(self, value):
            if isinstance(value, date):
                return QDate(value.year, value.month, value.day)
            else:
                return date

        def process_data(self, datas):
            target_datas = []

            for data in datas:
                color = state2color[data['kind']][data['state']]
                row = {
                    'name': data['cache_room'],
                    'color': color,
                    'cache_party': data['cache_party'],
                    'start_date': self.get_convert_date(data['start_date']),
                    'end_date': self.get_convert_date(data['end_date']),
                }

                tool_tip_info = [
                        'Clase: %s' % trans_kind[data['kind']],
                        'Habitacion: %s' % data['cache_room'],
                        'Estado: %s' % trans_state[data['state']],
                        'Arribo: %s' % data['start_date'],
                        'Salida: %s' % data['end_date'],
                ]
                if data['kind'] == 'booking':
                    tool_tip_info.insert(1, '# Reserva: %s' % data['reference'])
                    tool_tip_info.insert(3, 'Huesped: %s' % data['cache_party'],)
                    tool_tip_info.insert(5, 'Acomodacion: %s' % data['cache_accommodation'],)

                tool_tip_info = "\n ".join(tool_tip_info)
                info = {'info': tool_tip_info}
                row.update(info)
                target_datas.append(row)
            self.create_graph(target_datas)

        def create_graph(self, datas):
            for data in datas:
                item = None
                if data['name'] not in self.itemsList.keys():
                    item = XGanttWidgetItem(self.gantt_widget)
                    self.gantt_widget.addTopLevelItem(item)
                    item.setName(data['name'])
                    self.itemsList[data['name']] = item
                else:
                    item = self.itemsList[data['name']]
                new_item_view = item.createViewItem()
                item.setDateStart(data['start_date'])
                item.setDateEnd(data['end_date'])
                item.setToolTip(0, data['info'])
    #jj
    ##            new_item_view.setDateStart(data['start_date'])
    ##            new_item_view.setDateEnd(data['end_date'])
    ##            new_item_view.setInfoTip(data['info'])
                if data.get('color'):
                    new_item_view.setColor(data['color'])
    ##            item.addChild(new_item_view)
                item.sync()
                self.gantt_widget.syncView()
                self.gantt_widget.show()

    Gantt()

if __name__=='__main__':
    import sys
    app = QtGui.QApplication([])
    widget = Demo()
    widget.show()
    sys.exit(app.exec_())


"""

if __name__=='__main__':
    from qt import QtGui
    app = QtGui.QApplication([])
    widget = XCalendarWidget(None)
    scn = widget.scene()
    it1 = XCalendarItem()
    it1.setDuration(4)
    it1.setBorderColor(QtGui.QColor(22,123,233))
    it1.setDescription('skdjksjdksjdksj')
    it1.setTitle('knutsen model')
    scn.addItem(it1)
    scn.addItem(XCalendarItem())
    scn.addItem(XCalendarItem())
    widget.resize(1000,900)
    widget.show()
    app.exec_()
"""