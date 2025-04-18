import sys
import random
from threading import Thread
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QLabel,                             QWidget, QVBoxLayout)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QColor, QPainter, QFont
from main import jarvis  # Your main function

class TransparentTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QTextEdit {
                background: rgba(34, 34, 34, 150);
                color: #00ff99;
                border: none;
                padding: 10px;
                font-family: 'Courier New';
                font-size: 11pt;
            }
        """)
        self.setReadOnly(True)

class JarvisUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("J.A.R.V.I.S SYSTEM")
        self.resize(1280, 720)
        # Set window transparency (0=transparent, 255=opaque)
        self.setWindowOpacity(0.9)
        # Central widget with background
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Background image
        self.background = QLabel(self.central_widget)
        self.background.setPixmap(QPixmap("assets/bg.jpg").scaled(1280, 720))
        self.background.setGeometry(0, 0, 1280, 720)

        # Title
        self.title = QLabel("J.A.R.V.I.S SYSTEM", self.central_widget)
        self.title.setFont(QFont("Orbitron", 22, QFont.Weight.Bold))
        self.title.setStyleSheet("color: #00ffff; background: transparent;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setGeometry(0, 20, 1280, 40)

        # Transparent console
        self.console = TransparentTextEdit(self.central_widget)
        self.console.setGeometry(240, 180, 800, 300)

        # Status bar
        self.status = QLabel("Status: Ready", self.central_widget)
        self.status.setStyleSheet("color: #00ffcc; background: transparent;")
        self.status.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.status.setGeometry(20, 650, 300, 20)

        # Audio visualization
        self.canvas = QLabel(self.central_widget)
        self.canvas.setGeometry(20, 620, 1240, 100)

        # Start animation timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_waves)
        self.timer.start(100)

    def update_waves(self):
        # Create wave visualization
        pixmap = QPixmap(1240, 100)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        painter.setPen(QColor("#00ffcc"))
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        center = 50
        points = []
        for x in range(0, 1240, 5):
            y = center + random.randint(-25, 25)
            points.append((x, y))

        for i in range(len(points) - 1):
            painter.drawLine(points[i][0], points[i][1],
                             points[i + 1][0], points[i + 1][1])

        painter.end()
        self.canvas.setPixmap(pixmap)

    def log_message(self, sender, message):
        self.console.append(f"{sender}: {message}")
        self.console.verticalScrollBar().setValue(
            self.console.verticalScrollBar().maximum()
        )

    def update_status(self, status):
        self.status.setText(f"Status: {status}")


class ConsoleRedirect:
    def __init__(self, ui, sender):
        self.ui = ui
        self.sender = sender

    def write(self, message):
        if message.strip():
            self.ui.log_message(self.sender, message.strip())

    def flush(self):
        pass


def start_ui(jarvis_function):
    app = QApplication(sys.argv)
    ui = JarvisUI()
    ui.show()

    # Redirect stdout
    sys.stdout = ConsoleRedirect(ui,"")

    # Run jarvis in separate thread
    def run_jarvis():
        ui.update_status("Jarvis is running...")
        try:
            jarvis_function()
        except Exception as e:
            ui.log_message("Error", str(e))
        finally:
            ui.update_status("Jarvis stopped")

    Thread(target=run_jarvis, daemon=True).start()
    sys.exit(app.exec())


if __name__ == "__main__":
    start_ui(jarvis)