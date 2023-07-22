canvas = Canvas(root, width = 990, height=490, bg = "white", highlightbackground="gray")
fillcolou=["green","yellow","red", "blue"]
colour_dropdown = ttk.Combobox(root, state="readonly", values = fillcolour, width = 10)
startxLabel(root,text="startx")
d1 = ttk.COmbobox(root,state="readonly" ,values = coordinates_values, width = 10)
coordinates_values = [10,50,100,200,300,400,500,600,800,900]