import simple_draw as sd

point = sd.get_point (100,150)
sd.circle(center_position = point, radius = 100, color = sd.COLOR_WHITE, width = 0 )
sd.circle(center_position = sd.get_point (100, 320), radius = 80, color = sd.COLOR_WHITE, width = 0 )
sd.circle(center_position = sd.get_point (100, 450), radius = 50, color = sd.COLOR_WHITE, width = 0 )
sd.circle(center_position = sd.get_point (80, 450), radius = 5, color = sd.COLOR_BLACK, width = 0 )
sd.circle(center_position = sd.get_point (120, 450), radius = 5, color = sd.COLOR_BLACK, width = 0 )
sd.polygon(point_list = (sd.get_point(100,450), sd.get_point(100,425), sd.get_point(120,420)), color = sd.COLOR_ORANGE, width = 0)
sd.lines(point_list = (sd.get_point (80,420), sd.get_point(105,410), sd.get_point(120,420)), color = sd.COLOR_BLACK, closed = False, width = 1)

sd.pause ()
