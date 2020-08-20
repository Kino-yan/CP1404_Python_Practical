Code_to_color={"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "black": "#000000", "beige": "#f5f5dc", "blueviolet": "#8a2be2", "burlywood": "#deb887", "coral": "#cd661d", "darkgoldenrod": "#b8860b", "darkgreen": "#006400", "darkorchid": "#9932cc"}

color_name = input("Enter color name: ").lower()
while color_name != "":
    if color_name in Code_to_color:
        print(color_name, "is", Code_to_color[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ")