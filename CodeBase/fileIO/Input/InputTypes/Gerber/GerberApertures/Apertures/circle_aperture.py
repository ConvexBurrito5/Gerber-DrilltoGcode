from CodeBase.fileIO.CommonFormat.CFLayer.CFTraces.curves.cf_circle_trace import CFCircleTrace
from CodeBase.fileIO.Input.InputTypes.Gerber.GerberApertures.aperture_parent import ApertureParent


class CircleAperture(ApertureParent):
    def __init__(self, ap_number, center_x, center_y, diameter, unit, inside_hole_diam):
        # See Page 51:
        # https://www.ucamco.com/files/downloads/file_en/456/gerber-layer-format-specification-revision-2023-08_en.pdf

        # For Reference on Gerber to Common Form Conversion see picture here:
        # XXX No Photo Ref. Lazy

        super().__init__()
        self.aperture_type = "c"
        self.aperture_number = ap_number
        self.unit = unit

        # To common form.
        self.to_common_form(center_x, center_y, diameter, inside_hole_diam)

    def to_common_form(self, center_x, center_y, diameter, inside_hole_diam):
        new_common_form = CFCircleTrace(center_x, center_y, (diameter / 2), inside_hole_diam)
        self.common_form.append(new_common_form)
