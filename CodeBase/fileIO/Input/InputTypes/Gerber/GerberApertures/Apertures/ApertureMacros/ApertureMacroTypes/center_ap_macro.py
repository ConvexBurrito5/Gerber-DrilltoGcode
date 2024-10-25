from CodeBase.fileIO.Input.InputTypes.Gerber.GerberApertures.Apertures.ApertureMacros.ApertureMacroTypes.ap_macro_parent import \
    APMacroParent


class CenterAPMacro(APMacroParent):
    def __init__(self, exposure, width, start_x, start_y, end_x, end_y, rotation=0):
        super().__init__()
        self.code = 21
        self.exposure = exposure
        self.width = width
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.rotation = rotation  # IN DEGREES CC
        self.common_form = []

        self.to_common_form()

    def to_common_form(self):
        pass

