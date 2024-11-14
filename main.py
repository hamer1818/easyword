import sys
import time
import itertools
from PyQt6 import QtWidgets, QtCore  # QtCore eklendi

class WordlistGenerator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Wordlist Oluşturucu")
        self.setGeometry(100, 100, 400, 250)  # Yükseklik arttırıldı

        # Layout
        layout = QtWidgets.QVBoxLayout()

        # Hane sayısı
        self.length_label = QtWidgets.QLabel("Hane sayısını girin:")
        self.length_input = QtWidgets.QSpinBox()
        self.length_input.setMinimum(1)
        self.length_input.setMaximum(10)
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)

        # Dosya adı
        self.name_label = QtWidgets.QLabel("Wordlist ismini yazın:")
        self.name_input = QtWidgets.QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Oluştur butonu
        self.generate_button = QtWidgets.QPushButton("Wordlist Oluştur")
        self.generate_button.clicked.connect(self.generate_wordlist)
        layout.addWidget(self.generate_button)

        # Durum mesajı
        self.status_label = QtWidgets.QLabel("")
        layout.addWidget(self.status_label)

        # Geliştirici bilgisi
        self.developer_label = QtWidgets.QLabel("Hamza ORTATEPE tarafından geliştirildi")
        self.developer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.developer_label)

        # Geliştirici bilgisi ve GitHub linki
        self.developer_label = QtWidgets.QLabel('<a href="https://github.com/hamer1818/easyword">Proje GitHub Sayfası</a>')
        self.developer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.developer_label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.developer_label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.developer_label.setOpenExternalLinks(True)
        layout.addWidget(self.developer_label)

        self.setLayout(layout)

    def generate_wordlist(self):
        length = self.length_input.value()
        name = self.name_input.text()

        if not name.endswith('.txt'):
            name += '.txt'  # '.txt' eki ekleniyor

        self.status_label.setText("Wordlist oluşturuluyor, lütfen bekleyin...")
        QtWidgets.QApplication.processEvents()

        start_time = time.perf_counter()

        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890!@#$%^&*"

        with open(name, "w") as file:
            for combination in itertools.product(characters, repeat=length):
                file.write(''.join(combination) + "\n")

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        self.status_label.setText(f"Tamamlandı, {elapsed_time:.2f} saniye sürdü.\n'{name}' dosyasını kontrol edin.")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WordlistGenerator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()