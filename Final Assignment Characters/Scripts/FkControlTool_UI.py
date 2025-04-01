from PySide2 import QtWidgets
import maya.cmds as cmds

class FKControlTool(QtWidgets.QWidget):
    def __init__(self):
        super(FKControlTool, self).__init__()
        self.setWindowTitle("FK Control Tool")
        self.setFixedSize(300, 250)

        layout = QtWidgets.QVBoxLayout()

        self.radius_label = QtWidgets.QLabel("Control Radius")
        self.radius_input = QtWidgets.QLineEdit("1.8")
        layout.addWidget(self.radius_label)
        layout.addWidget(self.radius_input)

        self.create_fk_button = QtWidgets.QPushButton("Create FK Control")
        self.create_fk_button.clicked.connect(self.create_fk_control)
        layout.addWidget(self.create_fk_button)

        self.space_switch_button = QtWidgets.QPushButton("Add FK Space Switch")
        self.space_switch_button.clicked.connect(self.setup_fk_space_switch)
        layout.addWidget(self.space_switch_button)

        self.color_label = QtWidgets.QLabel("Change FK Control Color:")
        layout.addWidget(self.color_label)

        self.red_button = QtWidgets.QPushButton("Red")
        self.red_button.clicked.connect(lambda: self.set_color(13))  
        layout.addWidget(self.red_button)

        self.blue_button = QtWidgets.QPushButton("Blue")
        self.blue_button.clicked.connect(lambda: self.set_color(6))  
        layout.addWidget(self.blue_button)

        self.yellow_button = QtWidgets.QPushButton("Yellow")
        self.yellow_button.clicked.connect(lambda: self.set_color(17))  
        layout.addWidget(self.yellow_button)

        self.setLayout(layout)

    def create_fk_control(self):
        """
        Creates an FK control for the selected joint.
        """
        selection = cmds.ls(selection=True)
        if selection:
            joint = selection[0]
            radius = float(self.radius_input.text()) 
            ctrl_name = f"{joint}_FK_Ctrl"
            ctrl = cmds.circle(n=ctrl_name, nr=(1, 0, 0), r=radius, ch=False)[0]
            cmds.matchTransform(ctrl, joint)
            print(f" FK Control created: {ctrl_name}")
        else:
            print(" Select a joint first!")

    def set_color(self, color):
        """
        Sets the override color for the selected FK control.
        """
        selection = cmds.ls(selection=True)
        if selection:
            for ctrl in selection:
                cmds.setAttr(f"{ctrl}.overrideEnabled", 1)
                cmds.setAttr(f"{ctrl}.overrideColor", color)
                print(f" Changed color of {ctrl}")
        else:
            print(" Select a control first!")

    def setup_fk_space_switch(self):
        """
        Adds FK space switch to the selected arm control.
        """
        selection = cmds.ls(selection=True)
        if selection:
            side = "Left" if "Left" in selection[0] else "Right"
            setup_fk_space_switch(side)
            print(f" FK Space Switch added to {side} arm!")
        else:
            print(" Select an arm FK control first!")
app = QtWidgets.QApplication.instance()
if not app:
    app = QtWidgets.QApplication([])
win = FKControlTool()
win.show()
