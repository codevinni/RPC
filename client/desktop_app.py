import sys
import subprocess
import time
import os
import signal
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class StreamlitDesktop(QMainWindow):

    PORT = "9494"

    def __init__(self):

        super().__init__()
        self.setWindowTitle("RPC Desktop")
        self.resize(1200, 900)

        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.app_path = os.path.join(self.base_dir, "client", "app.py")
        self.port = self.PORT

        # Inicia o Streamlit
        print(f"Iniciando servidor Streamlit na porta {self.port}...")
        self.process = subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", self.app_path, 
             "--server.headless", "true", 
             "--server.port", self.port],
            cwd=self.base_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # Aguarda o servidor iniciar
        time.sleep(5)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(f"http://localhost:{self.port}"))
        self.setCentralWidget(self.browser)

    def closeEvent(self, event):
        """Garante que o servidor Streamlit encerre ao fechar a janela"""

        print("Fechando servidor e encerrando...")

        if self.process:

            self.process.terminate()

            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.kill()

        event.accept()

if __name__ == "__main__":
    
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = StreamlitDesktop()
    window.show()
    sys.exit(app.exec())