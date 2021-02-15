from circle import Circle

if(__name__ == "__main__"):
    first_circle = Circle(4, 4, 5)
    second_circle = Circle(14, 5, 5.1)
    third_circle = Circle(7, 15, 6)
    fourth_circle = Circle(9.35, -0.58, 2.04)

    print(first_circle)
    print(second_circle)
    print(third_circle)
    print(fourth_circle)

    print("First circle area (78.539...): {0}".format(first_circle.area()))
    print("Second circle area (81.712...): {0}".format(second_circle.area()))
    print("Third circle area (113.097...): {0}".format(third_circle.area()))
    print("Fourth circle area (13.074...): {0}".format(fourth_circle.area()))

    print("First circle distance to second circle (10.05): {0}".format(first_circle.distance(second_circle)))
    print("First circle distance to fourth circle (7.04): {0}".format(first_circle.distance(fourth_circle)))

    print("First & second circle overlap (true): {0}".format(first_circle.overlap(second_circle)))
    print("First & third circle overlap (false): {0}".format(first_circle.overlap(third_circle)))
    print("Second & third circle overlap (false): {0}".format(second_circle.overlap(third_circle)))
    print("First & fourth circle overlap (true): {0}".format(first_circle.overlap(fourth_circle)))
    print("Second & fourth circle overlap (false): {0}".format(second_circle.overlap(fourth_circle)))

    print("First circle equals second circle (false): {0}".format(first_circle == second_circle))
    print("First circle equals new same info circle (true): {0}".format(first_circle == Circle(4,4,5)))