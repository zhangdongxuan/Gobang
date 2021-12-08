from PySide6.QtCore import QRect, Qt, Slot, QPoint, QPointF, QLine
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPen, QPalette, QFont, QMouseEvent, QBrush, QColor, QPainter
import math
import time
import numpy as np

WINDOW_WIDTH = 800

GRID_ITEM_COUNT = 15
GRID_OFFSET = 40
GRID_WIDTH = 720
GRID_HEIGHT = 720

GRID_ITEM_HEIGHT = GRID_HEIGHT / GRID_ITEM_COUNT
GRID_ITEM_WIDTH = GRID_WIDTH / GRID_ITEM_COUNT

CHESSTYEPE_EMPTY = 0
CHESSTYEPE_WHITE = 1
CHESSTYEPE_BLACK = 2

class ChessBoard(QWidget):
    def __init__(self):
        super().__init__()
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("peru"))
        self.setAutoFillBackground(1)
        self.setPalette(palette)
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_WIDTH)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_WIDTH)
        self.setWindowTitle("五子棋")
        self.pieces = np.zeros([GRID_ITEM_COUNT + 1, GRID_ITEM_COUNT + 1])
        self.currentType = CHESSTYEPE_WHITE

    def paintEvent(self, event):
        self.paintGrid()
        self.paintChesspiece()

    def paintGrid(self):
        painter = QPainter(self)  # 定义一个画布
        # painter.begin(self)  # 初始化画布属性
        painter.setPen(QColor.fromRgbF(0, 0, 0, 0.1))
        for i in range(0, GRID_ITEM_COUNT + 1):
            hy = GRID_OFFSET + i * GRID_ITEM_HEIGHT
            horizontal = QLine(GRID_OFFSET, hy, GRID_OFFSET + GRID_WIDTH, hy)
            painter.drawLine(horizontal)

            vx = GRID_OFFSET + i * GRID_ITEM_WIDTH
            vertical = QLine(vx, GRID_OFFSET, vx, GRID_OFFSET + GRID_HEIGHT)
            painter.drawLine(vertical)
        # painter.end()

    def paintChesspiece(self):
        painter = QPainter(self)  # 定义一个画布
        painter.setRenderHint(QPainter.Antialiasing);
        radius = GRID_ITEM_WIDTH / 4
        for i in range(GRID_ITEM_COUNT + 1):
            for j in range(GRID_ITEM_COUNT + 1):
                # print("i:", i, "j:", j)
                if self.pieces[i][j] == CHESSTYEPE_EMPTY : 
                    continue
                elif self.pieces[i][j] == CHESSTYEPE_WHITE : 
                    painter.setPen(QColor("floralwhite"))
                    painter.setBrush(QBrush(QColor("floralwhite")))
                else :
                    painter.setPen(QColor("black"))
                    painter.setBrush(QBrush(QColor("black")))

                x = GRID_ITEM_WIDTH * i + GRID_OFFSET
                y = GRID_ITEM_HEIGHT * j + GRID_OFFSET
                rect = QRect(x - radius, y - radius, radius * 2, radius * 2)
                painter.drawEllipse(rect)

    def mousePressEvent(self, event):
        mouseEvent = QMouseEvent(event)
        point = mouseEvent.localPos()
        row = round((point.x() - GRID_OFFSET) / GRID_ITEM_WIDTH)
        row = min(row, GRID_ITEM_COUNT)
        column = round((point.y() - GRID_OFFSET) / GRID_ITEM_HEIGHT)
        column = min(column, GRID_ITEM_COUNT)

        valueX = (point.x() - GRID_OFFSET) / GRID_ITEM_WIDTH
        valueY = (point.y() - GRID_OFFSET) / GRID_ITEM_HEIGHT
        print("valueX:", valueX, "valueY:", valueY)
        print("point:", point.x(), point.y(), "row:", row, "column:", column, "value:", self.pieces[row][column])

        if self.pieces[row][column] != CHESSTYEPE_EMPTY : 
            return

        if self.currentType == CHESSTYEPE_WHITE:
            self.pieces[row][column] = CHESSTYEPE_WHITE
            self.currentType = CHESSTYEPE_BLACK
        else:
            self.pieces[row][column] = CHESSTYEPE_BLACK
            self.currentType = CHESSTYEPE_WHITE

        self.update()