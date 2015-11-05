#!/usr/bin/python

""" Defines a chart widget for use in displaying data. """

# define authorship information
__authors__         = ['Eric Hulser']
__author__          = ','.join(__authors__)
__credits__         = []
__copyright__       = 'Copyright (c) 2012, Projex Software'
__license__         = 'LGPL'

# maintenance information
__maintainer__      = 'Projex Software'
__email__           = 'team@projexsoftware.com'


#------------------------------------------------------------------------------

from projexui.qt.QtCore import Qt
from projexui.qt.QtGui import QGraphicsView

from projexui.widgets.xchartwidget.xchartscene import XChartScene

class XChartWidget(QGraphicsView):
    """ """
    Type = XChartScene.Type
    
    def __getattr__( self, key ):
        """
        Passes along access to the scene properties for this widget.
        
        :param      key | <str>
        """
        return getattr(self.scene(), key)
        
    def __init__( self, parent = None ):
        super(XChartWidget, self).__init__( parent )
        
        # define custom properties
        
        # set default properties
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setScene(XChartScene(self))
        
        # create connections



if __name__=='__main__':
    from projexui.qt import QtGui
    from projexui.widgets.xchartwidget.xchartwidgetitem import XChartWidgetItem
    from projexui.widgets.xchartwidget.xchartscene import XChartScene

    app = QtGui.QApplication([])

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
    mainWidget.show()
    #print 'TOTAL TIME', round(time.time()-tm, 3)
    app.exec_()