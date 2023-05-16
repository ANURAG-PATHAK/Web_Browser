import sys
from qtpy.QtCore import QUrl
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLineEdit, QVBoxLayout, QWidget, QPushButton
from qtpy.QtWebEngineWidgets import QWebEngineView

# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a web view
        self.web_view = QWebEngineView(self)
        self.setCentralWidget(self.web_view)

        # Create navigation buttons (back, forward, reload)
        self.back_button = QPushButton(QIcon.fromTheme("go-previous"), "next", self)
        self.back_button.clicked.connect(self.web_view.back)
        self.forward_button = QPushButton(QIcon.fromTheme("go-next"), "previous", self)
        self.forward_button.clicked.connect(self.web_view.forward)
        self.reload_button = QPushButton(QIcon.fromTheme("view-refresh"), "Reload", self)
        self.reload_button.clicked.connect(self.web_view.reload)

        # Create a search bar and a Search button
        self.search_bar = QLineEdit(self)
        self.search_bar.returnPressed.connect(self.search)
        self.search_button = QPushButton(QIcon.fromTheme("edit-find"), "Search", self)
        self.search_button.clicked.connect(self.search)

        # Add the address bar, Go button, and navigation buttons to a toolbar
        toolbar = QToolBar("Navigation")
        self.addToolBar(toolbar)
        toolbar.addWidget(self.back_button)
        toolbar.addWidget(self.forward_button)
        toolbar.addWidget(self.reload_button)

        # Add the search bar and the Search button to another toolbar
        search_toolbar = QToolBar("Search")
        self.addToolBar(search_toolbar)
        search_toolbar.addWidget(self.search_bar)
        search_toolbar.addWidget(self.search_button)

        # Set the initial window size and position
        self.setGeometry(100, 100, 800, 600)

    def search(self):
        query = self.search_bar.text()
        if query.endswith(".com"):
            url = "https://www." + query
        else:
            url = "https://www.google.com/search?q=" + query
        self.web_view.load(QUrl(url))

if __name__ == "__main__":
    # Create a Qt application instance
    app = QApplication(sys.argv)

    # Create the main window
    main_window = MainWindow()
    main_window.show()

    # Run the event loop
    sys.exit(app.exec_())
