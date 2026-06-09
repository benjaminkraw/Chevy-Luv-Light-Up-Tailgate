# Import Libraries
from manim import *

# Define Functions

# Given an array of x distance and y distance, create an Array of points of path (z = 0 is assumed)
def PathFromDistance(Distance):
     # Initialize PathPoints Array [x, y, z] for size
     PathPoints = np.empty(shape=(len(Distance), 3), dtype='object')

     i = 0
     while i < len(Distance):
          # First Element of DirectionDistance array is starting point for PathPoints
          if i == 0:
               PathPoints[0][0] = Distance[0][0]
               PathPoints[0][1] = Distance[0][1]
               PathPoints[0][2] = 0
          # All other points are distances from previous point
          else:
            PathPoints[i][0] = PathPoints[i - 1][0] + Distance[i][0]
            PathPoints[i][1] = PathPoints[i - 1][1] + Distance[i][1]
            PathPoints[i][2] = 0

          i = i + 1     

     return PathPoints


# Given points for an Outline, and thickness, create a VGroup of lines (Creates closed loop)
def DrawLetterOutline(LetterPoints, LineThickness):
    Letter_Lines = VGroup()
    i = 0
    while i < len(LetterPoints):
        if i < len(LetterPoints) - 1:
            j = i + 1
        else:
            j = 0
        Letter_Lines.add(Line(LetterPoints[i], LetterPoints[j], stroke_width=LineThickness))

        i = i + 1

    return Letter_Lines

# Given an array of pixel locations, create a VGroup of pixels
def DrawPixels(PixelLocations, PixelRadius):
    Pixels = VGroup()
    i = 0
    while i < len(PixelLocations):
        x = PixelLocations[i][0]
        y = PixelLocations[i][1]
        z = PixelLocations[i][2]
        PixelLocation = [x, y, z]
        Pixels.add(Dot(PixelLocation, radius=PixelRadius))
        i = i + 1

    return Pixels

Origin = np.empty(shape=(0, 3), dtype='object')
Origin = np.append(Origin, [0,0], axis = 0)

print(Origin[0])

# An array with direction and distance to travel
# Letters use bottom left corner of "R" as origin
R_Directions = (
    [0, 0],
    [24.8, 0],
    [0, 40],
    [20.2, 0],
    [0, -40],
    [27.5, 0],
    [0, 95.5],
    [-72.5, 0]
)

Rcenter_Directions = (
    [R_Directions[0][0] + 24.8, R_Directions[0][1] + 59],
    [24.2, 0],
    [0, 18.5],
    [-24.2, 0],
)

O_Directions = (
    [R_Directions[0][0] + 100, R_Directions[0][1]],
    [63.5, 0],
    [0, 95.5],
    [-63.5, 0]
)

Ocenter_Directions = (
    [R_Directions[0][0] + 123, R_Directions[0][1] + 30],
    [20, 0],
    [0, 40],
    [-20, 0],
)

L_Directions = (
    [R_Directions[0][0] + 197, R_Directions[0][1]],
    [60, 0],
    [0, 18.5],
    [-35, 0],
    [0, 77],
    [-25, 0]
)

E2_Directions = (
    [R_Directions[0][0] + 267, R_Directions[0][1]],
    [63.5, 0],
    [0, 18.5],
    [-39, 0],
    [0, 21.5],
    [39, 0],
    [0, 19],
    [-39, 0],
    [0, 18.5],
    [39, 0],
    [0, 18],
    [-63.5, 0]
)

T_Directions = (
    [R_Directions[0][0] + 341.0, R_Directions[0][1] + 77.5],
    [27.5, 0],
    [0, -77.5],
    [25.5, 0],
    [0, 77.5],
    [27.5, 0],
    [0, 18],
    [-80.5, 0]
)

C_Directions = (
    [R_Directions[0][0] - 350.0, R_Directions[0][1]],
    [63.5, 0],
    [0, 18.5],
    [-39, 0],
    [0, 59],
    [39, 0],
    [0, 18],
    [-63.5, 0]
)
        
H_Directions = (
    [R_Directions[0][0] - 262.0, R_Directions[0][1]],
    [25, 0],
    [0, 40],
    [29, 0],
    [0, -40],
    [25, 0],
    [0, 95.5],
    [-25, 0],
    [0, -36.5],
    [-29, 0],
    [0, 36.5],
    [-25, 0]
)

E1_Directions = (
    [R_Directions[0][0] - 163.5, R_Directions[0][1]],
    [63.5, 0],
    [0, 18.5],
    [-39, 0],
    [0, 21.5],
    [39, 0],
    [0, 19],
    [-39, 0],
    [0, 18.5],
    [39, 0],
    [0, 18],
    [-63.5, 0]
)

V_Directions = (
    [R_Directions[0][0] - 68.5, R_Directions[0][1]],
    [33.5, 0],
    [25, 95.5],
    [-20.5, 0],
    [-18.3, -77],
    [-1.7, 0],
    [-13.5, 77],
    [-26.5, 0]
)

# Create array of points from path directions
C_points = PathFromDistance(C_Directions)
H_points = PathFromDistance(H_Directions)
E1_points = PathFromDistance(E1_Directions)
V_points = PathFromDistance(V_Directions)
R_points = PathFromDistance(R_Directions)
Rcenter_points = PathFromDistance(Rcenter_Directions)
O_points = PathFromDistance(O_Directions)
Ocenter_points = PathFromDistance(Ocenter_Directions)
L_points = PathFromDistance(L_Directions)
E2_points = PathFromDistance(E2_Directions)
T_points = PathFromDistance(T_Directions)


C_PixelRowHeights = (
    [5.25],
    [13.25],
    [21.25],
    [29.25],
    [37.25],
    [45.25],
    [53.75],
    [63.75],
    [72.75],
    [82.75],
    [90.25]
)

H_PixelRowHeights = (
    [5.25],
    [13.25],
    [21.25],
    [29.25],
    [37.25],
    [45.25],
    [53.75],
    [63.75],
    [72.75],
    [82.75],
    [90.25]
)

E1_PixelRowHeights = H_PixelRowHeights

L_PixelRowHeights = H_PixelRowHeights

E2_PixelRowHeights = H_PixelRowHeights

T_PixelRowHeights = H_PixelRowHeights

C_PixelColumnDistance = (
    [4.5],
    [12.5],
    [20.5],
    [27.8],
    [35.6],
    [43.4],
    [51.2],
    [58.5]
)

H_PixelColumnDistance = (
    [4.5],
    [12.5],
    [20.5],
    [27.8],
    [35.6],
    [43.4],
    [51.2],
    [58.5],
    [66.5],
    [74.5]
)

E1_PixelColumnDistance = H_PixelColumnDistance

L_PixelColumnDistance = (
    [4.5],
    [12.5],
    [20.5],
    [29.25],
    [38.0],
    [46.75],
    [55.5]
)

E2_PixelColumnDistance = H_PixelColumnDistance

T_PixelColumnDistance = (
    [4.5],
    [13.75],
    [23.0],
    [32.0],
    [40.25],
    [48.50],
    [57.50],
    [66.75],
    [76.0]
)

# Build Arrays of Pixel Locations
# Initialize Pixels Array [x, y, z] for size
C_PixelLocations = np.empty(shape=(0, 3), dtype='object')
row = 0
while row < len(C_PixelRowHeights):
    column = 0
    while column < len(C_PixelColumnDistance):
        x = C_points[0][0] + C_PixelColumnDistance[column][0]
        y = C_points[0][1] + C_PixelRowHeights[row][0]
        z = 0
        Pixel = np.array([[x, y, z]])

        if (column < 3):
            C_PixelLocations = np.append(C_PixelLocations, Pixel, axis = 0)
        if (column >= 3 and (row <= 1 or row >= 9)):
            C_PixelLocations = np.append(C_PixelLocations, Pixel, axis = 0)
        column += 1
    row += 1


H_PixelLocations = np.empty(shape=(0, 3), dtype='object')
row = 0
while row < len(H_PixelRowHeights):
    column = 0
    while column < len(H_PixelColumnDistance):
        x = H_points[0][0] + H_PixelColumnDistance[column][0]
        y = H_points[0][1] + H_PixelRowHeights[row][0]
        z = 0
        Pixel = np.array([[x, y, z]])

        if (column < 3 or column > 6):
            H_PixelLocations = np.append(H_PixelLocations, Pixel, axis = 0)
        if (column >= 3 and column <= 6 and row >= 5 and row <= 6):
            H_PixelLocations = np.append(H_PixelLocations, Pixel, axis = 0)
        column += 1
    row += 1


E1_PixelLocations = np.empty(shape=(0, 3), dtype='object')
row = 0
while row < len(E1_PixelRowHeights):
    column = 0
    while column < len(E1_PixelColumnDistance):
        x = E1_points[0][0] + E1_PixelColumnDistance[column][0]
        y = E1_points[0][1] + E1_PixelRowHeights[row][0]
        z = 0
        Pixel = np.array([[x, y, z]])

        if (column < 3):
            E1_PixelLocations = np.append(E1_PixelLocations, Pixel, axis = 0)
        if (column >= 3 and column <= 7 and (row == 0 or row == 1 or row == 5 or row == 6 or row == 9 or row == 10)):
            E1_PixelLocations = np.append(E1_PixelLocations, Pixel, axis = 0)
        column += 1
    row += 1


L_PixelLocations = np.empty(shape=(0, 3), dtype='object')
row = 0
while row < len(L_PixelRowHeights):
    column = 0
    while column < len(L_PixelColumnDistance):
        x = L_points[0][0] + L_PixelColumnDistance[column][0]
        y = L_points[0][1] + L_PixelRowHeights[row][0]
        z = 0
        Pixel = np.array([[x, y, z]])

        if (column < 3):
            L_PixelLocations = np.append(L_PixelLocations, Pixel, axis = 0)
        if (column >= 3 and column <= 7 and (row == 0 or row == 1)):
            L_PixelLocations = np.append(L_PixelLocations, Pixel, axis = 0)
        column += 1
    row += 1

E2_PixelLocations = np.empty(shape=(0, 3), dtype='object')
row = 0
while row < len(E2_PixelRowHeights):
    column = 0
    while column < len(E2_PixelColumnDistance):
        x = E2_points[0][0] + E2_PixelColumnDistance[column][0]
        y = E2_points[0][1] + E2_PixelRowHeights[row][0]
        z = 0
        Pixel = np.array([[x, y, z]])

        if (column < 3):
            E2_PixelLocations = np.append(E2_PixelLocations, Pixel, axis = 0)
        if (column >= 3 and column <= 7 and (row == 0 or row == 1 or row == 5 or row == 6 or row == 9 or row == 10)):
            E2_PixelLocations = np.append(E2_PixelLocations, Pixel, axis = 0)
        column += 1
    row += 1

T_PixelLocations = np.empty(shape=(0, 3), dtype='object')
row = 0
while row < len(T_PixelRowHeights):
    column = 0
    while column < len(T_PixelColumnDistance):
        x = T_points[0][0] + T_PixelColumnDistance[column][0]
        y = T_points[0][1] + T_PixelRowHeights[row][0] - 77.5
        z = 0
        Pixel = np.array([[x, y, z]])

        if (row >= 9):
            T_PixelLocations = np.append(T_PixelLocations, Pixel, axis = 0)
        if (column > 2 and column < 6 and row < 9):
            T_PixelLocations = np.append(T_PixelLocations, Pixel, axis = 0)
        column += 1
    row += 1


class LightUpTailgate(MovingCameraScene):
    def construct(self): 
        OutlineThick = 100

        # Add Lines for Letter Outline
        self.add(DrawLetterOutline(C_points, OutlineThick))
        self.add(DrawLetterOutline(H_points, OutlineThick))
        self.add(DrawLetterOutline(E1_points, OutlineThick))
        self.add(DrawLetterOutline(V_points, OutlineThick))
        self.add(DrawLetterOutline(R_points, OutlineThick))
        self.add(DrawLetterOutline(Rcenter_points, OutlineThick))
        self.add(DrawLetterOutline(O_points, OutlineThick))
        self.add(DrawLetterOutline(Ocenter_points, OutlineThick))
        self.add(DrawLetterOutline(L_points, OutlineThick))
        self.add(DrawLetterOutline(E2_points, OutlineThick))
        self.add(DrawLetterOutline(T_points, OutlineThick))

        # Add Origin Lines
        self.add(Line([0, -200, 0], [0, 200, 0], stroke_width=100, color=RED))
        self.add(Line([-600, 0, 0], [600, 0, 0], stroke_width=100, color=RED))


        PixelRadius = 2

        # Add Pixels from Locations
        self.add(DrawPixels(C_PixelLocations, PixelRadius))
        self.add(DrawPixels(H_PixelLocations, PixelRadius))
        self.add(DrawPixels(E1_PixelLocations, PixelRadius))
        # self.add(DrawPixels(V_PixelLocations, PixelRadius))
        # self.add(DrawPixels(R_PixelLocations, PixelRadius))
        # self.add(DrawPixels(O_PixelLocations, PixelRadius))
        self.add(DrawPixels(L_PixelLocations, PixelRadius))
        self.add(DrawPixels(E2_PixelLocations, PixelRadius))
        self.add(DrawPixels(T_PixelLocations, PixelRadius))

 
        # Animate Scenes
        self.play(self.camera.frame.animate.scale(56)) #56
        self.play(self.camera.frame.animate.move_to([30, 0, 0]))