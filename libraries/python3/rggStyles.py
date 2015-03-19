'''
rggStyles - for the Random Game Generator project            
By Doctus (kirikayuumura.noir@gmail.com)

Various stylesheets for the application.

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
'''

standard = ''''''

test = '''background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eef, stop: 1 #ccf);'''

celtica = '''
*{ background-image: url(data/styles/bg_celt.png);}

QLineEdit,QTextEdit,QListWidget{ background: #f3f2e5; }

QLabel { background: #f3f2e5; }

QPushButton { background: #e5e2c9; }

QMenu {
     background: #c8c290;
 }
 
QMenu::item:selected {
     background: #625c2e;
 }
 
QMenu::item:pressed {
     background: #f3f2e5;
 }

QMenuBar::item {
     background: #c8c290;
 }

QMenuBar::item:selected {
     background: #f3f2e5;
 }

QMenuBar::item:pressed {
     background: #625c2e;
 }

'''


#Dark stylesheet license:
'''*
 * The MIT License (MIT)
 *
 * Copyright (c) <2013-2014> <Colin Duquesnoy>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:

 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.

 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *'''
dark = '''QProgressBar:horizontal {
    border: 1px solid #3A3939;
    text-align: center;
    padding: 1px;
    background: #201F1F;
}
QProgressBar::chunk:horizontal {
    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));
}

QToolTip
{
    border: 1px solid #3A3939;
    background-color: rgb(90, 102, 117);;
    color: white;
    padding: 1px;
    opacity: 200;
}

QWidget
{
    color: silver;
    background-color: #302F2F;
    selection-background-color:#78879b;
    selection-color: black;
    background-clip: border;
    border-image: none;
    outline: 0;
}

QWidget:item:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
    stop: 0 #78879b, stop: 1 #78879b);
    color: black;
}

QWidget:item:selected
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
    stop: 0 #78879b, stop: 1 #78879b);
}

QMenuBar
{
    background-color: #302F2F;
    color: silver;
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #3A3939;
}

QMenuBar::item:pressed
{
    border: 1px solid #3A3939;
    background-color: #78879b;
    color: black;
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #3A3939;
    color: silver;
    margin: 2px;
}

QMenu::icon
{
    margin: 5px;
}

QMenu::item
{
    padding: 5px 30px 5px 30px;
    margin-left: 5px;
    border: 1px solid transparent; /* reserve space for selection border */
}

QMenu::item:selected
{
    color: black;
}

QWidget:disabled
{
    color: #404040;
    background-color: #302F2F;
}

QAbstractItemView
{
    alternate-background-color: #3A3939;
    color: silver;
    border: 1px solid 3A3939;
    border-radius: 3px;
    padding: 1px;
}

QWidget:focus, QMenuBar:focus
{
    border: 1px solid rgba(48, 86, 111);
}

QTabWidget:focus, QCheckBox:focus, QRadioButton:focus
{
    border: none;
}

QLineEdit
{
    background-color: #201F1F;
    padding: 2px;
    border-style: solid;
    border: 1px solid #3A3939;
    border-radius: 3px;
    color: silver;
}

QGroupBox {
    border:1px solid #3A3939;
    border-radius: 7px;
    margin-top: 2ex;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 10px;
    padding-right: 10px;
}

QAbstractScrollArea
{
    border-radius: 3px;
    border: 1px solid #3A3939;
}

QScrollBar:horizontal
{
    height: 15px;
    margin: 0px 11px 0px 11px;
    border: 1px solid #3A3939;
    border-radius: 6px;
    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,
    stop: 0 #302F2F, stop: 1 #484846);
}

QScrollBar::handle:horizontal
{
    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,
    stop: 0 #605F5F, stop: 1 #787876);
    min-width: 5px;
    border-radius: 5px;
}

QScrollBar::add-line:horizontal
{
    border-image: url(data/styles/right_arrow_disabled.png);
    width: 10px;
    height: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
    border-image: url(data/styles/left_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
{
    border-image: url(data/styles/right_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}


QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
{
    border-image: url(data/styles/left_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
    background: none;
}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar:vertical
{
    background-color: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 0,
    stop: 0 #302F2F, stop: 1 #484846);
    width: 15px;
    margin: 11px 0 11px 0;
    border: 1px solid #3A3939;
    border-radius: 6px;
}

QScrollBar::handle:vertical
{
    background-color: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 0,
    stop: 0 #605F5F, stop: 1 #787876);
    min-height: 5px;
    border-radius: 5px;
}

QScrollBar::sub-line:vertical
{
    border-image: url(data/styles/up_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical
{

    border-image: url(data/styles/down_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
{

    border-image: url(data/styles/up_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
{
    border-image: url(data/styles/down_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
    background: none;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;
}

QTextEdit
{
    background-color: #201F1F;
    color: silver;
    border: 1px solid #3A3939;
}

QPlainTextEdit
{
    background-color: #201F1F;;
    color: silver;
    border-radius: 3px;
    border: 1px solid #3A3939;
}

QHeaderView::section
{
    background-color: #3A3939;
    color: silver;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QCheckBox:disabled
{
    color: #404040;
}

QSizeGrip {
    image: url(data/styles/sizegrip.png);
    width: 12px;
    height: 12px;
}


QMainWindow::separator
{
    background-color: #302F2F;
    color: white;
    padding-left: 4px;
    spacing: 2px;
    border: 1px dashed #3A3939;
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #58677b,
      stop:0.5 #78879b stop:1 #58677b);
    color: white;
    padding-left: 4px;
    border: 1px solid #3A3939;
    spacing: 2px;
}


QMenu::separator
{
    height: 1px;
    background-color: #3A3939;
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}



QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #302F2F;
    border: 1px solid silver;
    border-radius: 5px;
}



QRadioButton::indicator:checked
{
    background-color: qradialgradient(
    cx: 0.5, cy: 0.5,
    fx: 0.5, fy: 0.5,
    radius: 1.0,
    stop: 0.25 #78879b,
    stop: 0.3 #302F2F
    );
}

QCheckBox, QRadioButton
{
    padding: 3px;
    outline: none;
}

QCheckBox::indicator, QGroupBox::indicator, QMenu::indicator:non-exclusive{
    color: #b1b1b1;
    background-color: #302F2F;
    border: 1px solid silver;
}

QCheckBox::indicator, QMenu::indicator:non-exclusive{
    width: 9px;
    height: 9px;
}

QRadioButton::indicator
{
    border-radius: 7px;
    width: 9px;
    height: 9px;
}

QCheckBox::indicator:pressed
{
    border: 1px solid #78879b;
}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
{
    border: 1px solid #78879b;
}

QCheckBox::indicator:checked, QGroupBox::indicator:checked, QMenu::indicator:non-exclusive:checked
{
    image:url(data/styles/checkbox.png);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
{
    border: 1px solid #444;
}

QCheckBox::indicator:indeterminate {
    image: url(data/styles/checkbox_indeterminate.png);
}

QFrame
{
    border-radius: 3px;
}

QStackedWidget
{
    border: none;
}

QToolBar {
    border: 1px solid #393838;
    background: 1px solid #302F2F;
    font-weight: bold;
}

QToolBar::handle:horizontal {
    image: url(data/styles/Hmovetoolbar.png);
}
QToolBar::handle:vertical {
    image: url(data/styles/Vmovetoolbar.png);
}
QToolBar::separator:horizontal {
    image: url(data/styles/Hsepartoolbar.png);
}
QToolBar::separator:vertical {
    image: url(data/styles/Vsepartoolbars.png);
}

QPushButton
{
    color: silver;
    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,
    stop: 0 #302F2F, stop: 1 #484846);
    border-width: 1px;
    border-color: #4A4949;
    border-style: solid;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 5px;
    padding-right: 5px;
    border-radius: 5px;
    outline: none;
}

QPushButton:disabled
{
    background-color: #302F2F;
    border-width: 1px;
    border-color: #3A3939;
    border-style: solid;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
    /*border-radius: 3px;*/
    color: #454545;
}

QComboBox
{
    selection-background-color: #78879b;
    background-color: #201F1F;
    border-style: solid;
    border: 1px solid #3A3939;
    border-radius: 3px;
    padding: 2px;
    min-width: 75px;
}

QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover
{
    border: 1px solid #78879b;
    color: silver;
}

QComboBox:on
{
    background-color: #626873;
    padding-top: 3px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}

QComboBox QAbstractItemView
{
    background-color: #201F1F;
    border-radius: 3px;
    border: 1px solid #3A3939;
    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
      stop: 0 #78879b, stop: 1 #78879b);
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow
{
    image: url(data/styles/down_arrow_disabled.png);
}

QComboBox::down-arrow:on, QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    image: url(data/styles/down_arrow.png);
}

QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
    stop: 0 #302F2F, stop: 1 #484846);
}

QAbstractSpinBox {
    padding-top: 2px;
    padding-bottom: 2px;
    border: 1px solid #3A3939;
    background-color: #201F1F;
    color: silver;
    border-radius: 3px;
    min-width: 75px;
}

QAbstractSpinBox:up-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center right;
}

QAbstractSpinBox:down-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center left;
}

QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {
    image: url(data/styles/up_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::up-arrow:hover
{
    image: url(data/styles/up_arrow.png);
}


QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off
{
    image: url(data/styles/down_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::down-arrow:hover
{
    image: url(data/styles/down_arrow.png);
}


QLabel
{
    border: 0px solid black;
}


QTabWidget::pane {
    border: 1px solid #3A3939;
}

QTabBar
{
    qproperty-drawBase: 0;
    padding-right: 15px;
}

QTabBar:focus
{
    border: 0px transparent black;
}

QTabBar::close-button  {
    image: url(data/styles/close.png);
    background: transparent;
    icon-size: 10px;
    padding: 5px;
}

QTabBar::close-button:hover
{
    background: rgba(255, 255, 255, 20);
    border-radius: 3px;
}

QTabBar::close-button:pressed {
    padding: 5px 4px 4px 5px;
}

/* TOP - BOTTOM TABS */
QTabBar::tab:top {
    color: #b1b1b1;
    border: 1px solid #3A3939;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,
      stop:1 #302F2F, stop:0 #5A5959);
    padding-left: 5px;
    padding-right: 5px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;

    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

QTabBar::tab:bottom {
    color: #b1b1b1;
    border: 1px solid #3A3939;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,
      stop:1 #302F2F, stop:0 #5A5959);
    padding-left: 5px;
    padding-right: 5px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;

    border-bottom-left-radius: 3px;
    border-bottom-right-radius: 3px;
}

QTabBar::tab:top:last, QTabBar::tab:bottom:last
{
    margin-right: 0;
}

QTabBar::tab:top:first:!selected, QTabBar::tab:bottom:first:!selected
{
    margin-left: 0px;
}

QTabBar::tab:top:!selected
{
    color: #b1b1b1;
    margin-top: 3px;
    background-color: #302F2F;
}

QTabBar::tab:top:selected
{
    margin-bottom: 0px;
}

QTabBar::tab:bottom:!selected
{
    color: #b1b1b1;
    margin-bottom: 3px;
    background-color: #302F2F;
}

QTabBar::tab:bottom:selected
{
    margin-top: 0px;
}

/* LEFT - RIGHT TABS */
QTabBar::tab:left {
    color: #b1b1b1;
    border: 1px solid #3A3939;
    background-color: QLinearGradient(x1:1, y1:0, x2:0, y2:0,
      stop:1 #302F2F, stop:0 #5A5959);
    padding-left: 3px;
    padding-right: 2px;
    padding-top: 5px;
    padding-bottom: 5px;
    margin-bottom: -1px;

    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QTabBar::tab:right {
    color: #b1b1b1;
    border: 1px solid #3A3939;
    background-color: QLinearGradient(x1:0, y1:0, x2:1, y2:0,
      stop:1 #302F2F, stop:0 #5A5959);
    padding-left: 3px;
    padding-right: 2px;
    padding-top: 5px;
    padding-bottom: 5px;
    margin-bottom: -1px;

    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
}

QTabBar::tab:left:!selected
{
    color: #b1b1b1;
    margin-right: 3px;
    background-color: #302F2F;
}

QTabBar::tab:left:selected
{
    margin-left: 0px;
}

QTabBar::tab:right:!selected
{
    color: #b1b1b1;
    margin-left: 3px;
        background-color: #302F2F;
}

QTabBar::tab:right:selected
{
    margin-right: 0px;
}

QTabBar QToolButton::right-arrow:enabled {
     image: url(data/styles/right_arrow.png);
 }

 QTabBar QToolButton::left-arrow:enabled {
     image: url(data/styles/left_arrow.png);
 }

QTabBar QToolButton::right-arrow:disabled {
     image: url(data/styles/right_arrow_disabled.png);
 }

 QTabBar QToolButton::left-arrow:disabled {
     image: url(data/styles/left_arrow_disabled.png);
 }


QDockWidget {
    border: 1px solid #403F3F;
    titlebar-close-icon: url(data/styles/close.png);
    titlebar-normal-icon: url(data/styles/undock.png);
}

QDockWidget::close-button, QDockWidget::float-button {
    border: 1px solid transparent;
    border-radius: 3px;
    background: transparent;
    icon-size: 10px;
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    background: rgba(255, 255, 255, 10);
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
    padding: 1px -1px -1px 1px;
    background: rgba(255, 255, 255, 10);
}

QTreeView, QListView
{
    border: 1px solid #78879b;
    background-color: #201F1F;
}

QTreeView:branch:selected, QTreeView:branch:hover
{
    background: url(data/styles/transparent.png);
}

QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(data/styles/transparent.png);
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(data/styles/transparent.png);
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(data/styles/transparent.png);
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    image: url(data/styles/branch_closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    image: url(data/styles/branch_open.png);
}

QTreeView::branch:has-children:!has-siblings:closed:hover,
QTreeView::branch:closed:has-children:has-siblings:hover {
    image: url(data/styles/branch_closed-on.png);
    }

QTreeView::branch:open:has-children:!has-siblings:hover,
QTreeView::branch:open:has-children:has-siblings:hover  {
    image: url(data/styles/branch_open-on.png);
    }

QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {
    background: rgba(0, 0, 0, 0);
    outline: 0;
    color: #FFFFFF
}

QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {
    background: #78879b;;
    color: #FFFFFF;
}

QSlider::groove:horizontal {
    border: 1px solid #3A3939;
    height: 8px;
    background: #201F1F;
    margin: 2px 0;
    border-radius: 4px;
}

QSlider::handle:horizontal {
    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);
    border: 1px solid #3A3939;
    width: 14px;
    height: 14px;
    margin: -4px 0;
    border-radius: 7px;
}

QSlider::groove:vertical {
    border: 1px solid #3A3939;
    width: 8px;
    background: #201F1F;
    margin: 0 0px;
    border-radius: 4px;
}

QSlider::handle:vertical {
    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,
      stop: 0.2 #a8a8a8, stop: 1 #727272);
    border: 1px solid #3A3939;
    width: 14px;
    height: 14px;
    margin: 0 -4px;
    border-radius: 7px;
}

QToolButton {
    background-color: transparent;
    border: 1px solid #3A3939;
    border-radius: 3px;
    margin: 3px;
}

QToolButton:pressed, QToolButton::menu-button:pressed, QToolButton:checked, QToolButton::menu-button:checked {
    background-color: #4A4949;
    border: 1px solid silver;
}

QToolButton:hover, QToolButton::menu-button:hover {
    background-color: #4A4949;
    border: 1px solid gray;
}

QToolButton[popupMode="1"] { /* only for MenuButtonPopup */
 padding-right: 20px; /* make way for the popup button */
}

QToolButton[popupMode="2"] { /* only for MenuButtonPopup */
 padding-right: 10px; /* make way for the popup button */
}

/* the subcontrols below are used only in the MenuButtonPopup mode */
QToolButton::menu-button {
 border: 1px solid #3A3939;
 border-top-right-radius: 6px;
 border-bottom-right-radius: 6px;
 /* 16px width + 4px for border = 20px allocated above */
 width: 16px;
}

QToolButton::menu-arrow {
 image: url(data/styles/down_arrow.png);
}

QToolButton::menu-arrow:open {
 top: 1px; left: 1px; /* shift it a bit */
}

QPushButton::menu-indicator  {
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    left: 8px;
}

QTableView
{
    border: transparent;
    gridline-color: #6c6c6c;
    background-color: #201F1F;
}


QTableView, QHeaderView
{
    border-radius: 0px;
}

QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {
    background: #78879b;
    color: #FFFFFF;
}

QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {
    background: #78879b;
    color: #FFFFFF;
}


QHeaderView
{
    border: 1px transparent;
    margin: 0px;
    padding: 0px;
}

QHeaderView::section  {
    background-color: #3A3939;
    color: silver;
    padding: 4px;
    border: 1px solid #6c6c6c;
    border-radius: 0px;
    text-align: center;
}

QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one
{
    border-top: 1px solid #6c6c6c;
}

QHeaderView::section::vertical
{
    border-top: transparent;
}

QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one
{
    border-left: 1px solid #6c6c6c;
}

QHeaderView::section::horizontal
{
    border-left: transparent;
}


QHeaderView::section:checked
 {
    color: white;
    background-color: #5A5959;
 }

 /* style the sort indicator */
QHeaderView::down-arrow {
    image: url(data/styles/down_arrow.png);
}

QHeaderView::up-arrow {
    image: url(data/styles/up_arrow.png);
}


QTableCornerButton::section {
    background-color: #3A3939;
    border: 1px solid #3A3939;
    border-radius: 0px;
}

QToolBox::tab {
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,
        stop:1 #302F2F, stop:0 #5A5959);
    padding-left: 3px;
    padding-right: 2px;
    padding-top: 5px;
    padding-bottom: 5px;
    margin-bottom: -1px;

    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    color: darkgray;
 }

 QToolBox::tab:selected { /* italicize selected tabs */
     font: italic bold;
     color: white;
 }

QStatusBar::item {
    border: 1px solid #3A3939;
    border-radius: 3px;
 }


 QFrame[height="3"], QFrame[width="3"] {
    background-color: #3A3939;
}'''

sheets = {"Default":standard, "Dark":dark, "Celtic":celtica}