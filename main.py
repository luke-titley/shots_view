import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QTableView, QScrollArea, QVBoxLayout, QHeaderView
from PySide6.QtGui import QStandardItemModel, QPixmap, QImage, QStandardItem, QPainter
from PySide6.QtCore import Qt, QSize

SHOTS = [
    {"name": "Shot 1", "start": 1001, "end": 1100, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 2", "start": 1101, "end": 1200, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 3", "start": 1201, "end": 1300, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 4", "start": 1301, "end": 1400, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 5", "start": 1401, "end": 1500, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 6", "start": 1501, "end": 1600, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 7", "start": 1601, "end": 1700, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 8", "start": 1701, "end": 1800, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 9", "start": 1801, "end": 1900, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 10", "start": 1901, "end": 2000, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 11", "start": 2001, "end": 2100, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 12", "start": 2101, "end": 2200, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 13", "start": 2201, "end": 2300, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 14", "start": 2301, "end": 2400, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 15", "start": 2401, "end": 2500, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 16", "start": 2501, "end": 2600, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 17", "start": 2601, "end": 2700, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 18", "start": 2701, "end": 2800, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
    {"name": "Shot 19", "start": 2801, "end": 2900, "thumbnail": "/Users/luke/src/shots_view/shots/shot_001.jpg"},
]

THUMBNAILS_PER_ROW = 4
THUMBNAIL_HEIGHT = 100
BORDER = 4
FUDGE = 4

def load_thumbnail(shot_name, file_path):

    double_border = BORDER * 2
    shot_thumbnail = QPixmap(QImage(file_path)).scaledToHeight(THUMBNAIL_HEIGHT-double_border)

    annotated_thumbnail_width = shot_thumbnail.width() + double_border
    annotated_thumbnail_height = THUMBNAIL_HEIGHT + 12
    annotated_thumbnail = QPixmap(annotated_thumbnail_width, annotated_thumbnail_height)
    annotated_thumbnail.fill(Qt.GlobalColor.gray)
    painter = QPainter(annotated_thumbnail)
    painter.drawPixmap(BORDER, BORDER, shot_thumbnail)
    painter.drawText(annotated_thumbnail.rect(), Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom, shot_name)
    painter.end()
    
    return annotated_thumbnail

def build_model():
    model = QStandardItemModel(0, THUMBNAILS_PER_ROW)

    for i, shot in enumerate(SHOTS):
        row = i / THUMBNAILS_PER_ROW
        col = i % THUMBNAILS_PER_ROW

        pixmap = load_thumbnail(shot["name"].lower(), shot["thumbnail"])
        item = QStandardItem()
        item.setData(pixmap, Qt.ItemDataRole.DecorationRole)
        item.setSizeHint(pixmap.size()+QSize(FUDGE, FUDGE))
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)

        model.setItem(row, col, item)

    return model

def build_ui(model):
    shots_window = QWidget()
    shots_window.setWindowTitle("Shots")
    shots_window.setGeometry(100, 100, 400, 200)

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    table_view = QTableView()
    table_view.setModel(model)
    table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    table_view.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    #table_view.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignHCenter)
    table_view.horizontalHeader().hide()
    table_view.verticalHeader().hide()

    scroll_area.setWidget(table_view)

    shots_window_layout = QVBoxLayout()
    shots_window_layout.addWidget(scroll_area)
    shots_window.setLayout(shots_window_layout)

    return shots_window


app = QApplication(sys.argv)
shots_window = build_ui(build_model())
shots_window.show()
app.exec()
