"""PySide6 port of the Dynamic Spline example from Qt v5.x"""
import sys

from PySide6.QtCharts import QChart, QChartView
from PySide6.QtWidgets import QApplication, QMainWindow
from chessboard import ChessBoard

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chessboard = ChessBoard()
    chessboard.show()
    sys.exit(app.exec())