import importlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

class SimulationChooser(QWidget):
    def __init__(self):
        super().__init__()

        self.simulation_modules = [
            "ampere_simulation",
            "biot_savart_simulation",
            "lorentz_simulation",
            "induction_simulation",
            "inductance_simulation"
        ]

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simulações de Eletromagnetismo')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.radio_buttons = []
        for i, simulation in enumerate(["Lei de Ampère", "Lei de Biot-Savart", "Força de Lorentz", "Indução", "Indutância"]):
            radio_button = QRadioButton(simulation)
            radio_button.setChecked(False)
            radio_button.setFont(QFont("Arial", 12))
            layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)

        execute_button = QPushButton('Executar', self)
        execute_button.clicked.connect(self.on_execute_button_clicked)
        execute_button.setFont(QFont("Arial", 14))
        layout.addWidget(execute_button)

        self.setLayout(layout)

    def on_execute_button_clicked(self):
        selected_simulation = None
        for i, radio_button in enumerate(self.radio_buttons):
            if radio_button.isChecked():
                selected_simulation = i + 1
                break

        if selected_simulation is not None:
            simulation_module = self.simulation_modules[selected_simulation - 1]
            self.run_simulation(simulation_module)
        else:
            self.show_error_message("Opção inválida", "Selecione uma opção válida.")

    def run_simulation(self, simulation_module):
        try:
            # Cria uma nova instância do QApplication
            app_simulation = QApplication([])

            # Importa e executa o módulo da simulação
            importlib.import_module(simulation_module).run_simulation()

            # Executa o loop de eventos da nova aplicação
            app_simulation.exec_()

        except ImportError:
            self.show_error_message("Erro", f"Erro ao importar o módulo {simulation_module}")

    def show_error_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication([])
    window = SimulationChooser()
    window.show()
    app.exec_()
