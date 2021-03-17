import pymol as p


class PLIP_modifier:
    def __init__(self, file: str, ligand_residue: str):
        self.file = file
        self.ligand_residue = ligand_residue

    def customize_plip_pse(self) -> bool:
        try:
            print(f"Opening the file {self.file}")
            p.cmd.load(self.file)
            p.cmd.show(representation="sticks", selection=f" resn {self.ligand_residue}")
            p.cmd.show(representation="spheres", selection=f" resn {self.ligand_residue}")
            p.cmd.color(color='gray85', selection=f"resn {self.ligand_residue} and elem C")
            p.cmd.color(color='red', selection=f"resn {self.ligand_residue} and elem O")
            p.cmd.color(color='slate', selection=f"resn {self.ligand_residue} and elem N")
            p.cmd.color(color='gray85', selection=f"resn {self.ligand_residue} and elem H")
            p.cmd.set('stick_color', 'black', f'resn {self.ligand_residue}')
            p.cmd.set('stick_radius', '.01', f'resn {self.ligand_residue}')
            p.cmd.set('ray_texture', '2')
            p.cmd.set('antialias', '3')
            p.cmd.set('sphere_scale', '.25')
            p.cmd.set('ambient', '0.5')
            p.cmd.set('sphere_scale', '.13', 'elem H ')
            p.cmd.set('spec_count', '5')
            p.cmd.set('bg_rgb', '[1, 1, 1]')
            p.cmd.set('shininess', '50')
            p.cmd.set('stick_quality', '50')
            p.cmd.set('specular', '1')
            p.cmd.set('sphere_quality', '4')
            p.cmd.set('reflect', ' .1')
            p.cmd.set('ray_trace_mode', '1')
            p.cmd.set('dash_gap', '0.2')
            p.cmd.set('dash_color', 'blue')
            p.cmd.set('dash_gap', '.3')
            p.cmd.set('dash_length', '.05')
            p.cmd.set('dash_round_ends', '0')
            p.cmd.color("grey", f"resn {self.ligand_residue} and e. C")
            p.cmd.label2("visible and polymer and n. ca", "%s:%s" % ('resn', 'resi'))
            p.cmd.set("label_color", "black")
            p.cmd.set("label_position", "(0,0,5)")
            p.cmd.set("label_font_id", "7")
            p.cmd.set("label_size", "-0.7")
            p.cmd.bg_color("white")
            p.cmd.set('ray_opaque_background', '1')
            p.cmd.save(f"{self.file}_customized.png")
            p.cmd.save(f"{self.file}_customized.pse")
            print(f"File {self.file} successfully converted and saved as _customized")
            return 1
        except Exception as e:
            print(e)
            pass
            return 0
