import smitecalc as sc

df = sc.load_items("SmitePhys.xlsx")
builds = sc.create_builds(df, 3)
efficient_builds_phys = sc.physical_defense_builds_e(df, builds, 10)

df = sc.load_items("SmiteMag.xlsx")
builds = sc.create_builds(df, 3)
efficient_builds_mag = sc.magical_defense_builds_e(df, builds, 10)

sc.print_builds(efficient_builds_phys)
print("------------")
sc.print_builds(efficient_builds_mag)