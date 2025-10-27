from Colour_sensor import ColourSensor   # adjust filename to match your .py file name
from PiicoDev_Unified import sleep_ms

#left front 1
#right front 3
#right bin 4

left_front_sensor = ColourSensor(channel=1)  # create sensor instance
right_front_sensor = ColourSensor(channel=3)
right_bin_sensor = ColourSensor(channel=4)

while True:
    rgb1 = left_front_sensor.readRGB()    
    rgb2 = right_front_sensor.readRGB()
    rgb3 = right_bin_sensor.readRGB()     # returns a dict like {'red': 123, 'green': 456, 'blue': 789}
       # extract the green component
   
    print('left front', rgb1)
    print('right front',rgb2)
    print('right bin', rgb3)

    sleep_ms(5000)
# left front {'red': 535, 'green': 561, 'blue': 203, 'white': 2793, 'als': 141.19248000000002, 'cct': 3552.5842819308064}
# right front {'red': 713, 'green': 683, 'blue': 273, 'white': 3221, 'als': 171.89744000000002, 'cct': 3423.625219949778}
# right bin {'red': 5573, 'green': 5093, 'blue': 2033, 'white': 18579, 'als': 1281.8062400000001, 'cct': 3242.838616349687}

# right on green
# left front {'red': 481, 'green': 505, 'blue': 207, 'white': 2348, 'als': 127.09840000000001, 'cct': 3842.3838047825047}
# right front {'red': 2409, 'green': 2575, 'blue': 987, 'white': 9043, 'als': 648.076, 'cct': 3738.037364851727}
# right bin {'red': 8332, 'green': 7439, 'blue': 3258, 'white': 22466, 'als': 1872.2475200000001, 'cct': 3331.80180353223}

# left on green
# left front {'red': 1523, 'green': 1723, 'blue': 597, 'white': 6549, 'als': 433.64464000000004, 'cct': 3714.42470118417}
# right front {'red': 970, 'green': 919, 'blue': 406, 'white': 3765, 'als': 231.29392, 'cct': 3618.767884986531}
# right bin {'red': 7531, 'green': 6762, 'blue': 2851, 'white': 21475, 'als': 1701.8601600000002, 'cct': 3275.076580814971}

# purple on right
# left front {'red': 604, 'green': 625, 'blue': 251, 'white': 2709, 'als': 157.3, 'cct': 3730.5411744232056}
# right front {'red': 1293, 'green': 1153, 'blue': 673, 'white': 5971, 'als': 290.18704, 'cct': 4804.023801747323}
# right bin {'red': 5535, 'green': 4870, 'blue': 2145, 'white': 15283, 'als': 1225.6816000000001, 'cct': 3280.2451923493613}

# purple on left
# left front {'red': 1033, 'green': 1013, 'blue': 595, 'white': 5018, 'als': 254.95184, 'cct': 5897.240093742249}
# right front {'red': 1598, 'green': 1685, 'blue': 680, 'white': 5569, 'als': 424.0808, 'cct': 3816.3035158035373}
# right bin {'red': 6768, 'green': 6095, 'blue': 2899, 'white': 17535, 'als': 1533.9896, 'cct': 3600.877742008359}

#yellow on right bin(yellow bin)
# left front {'red': 1366, 'green': 1319, 'blue': 735, 'white': 7818, 'als': 331.96592000000004, 'cct': 5039.826770727015}
# right front {'red': 1903, 'green': 1823, 'blue': 777, 'white': 7645, 'als': 458.81264000000004, 'cct': 3570.0165048409067}
# right bin {'red': 5439, 'green': 4973, 'blue': 1997, 'white': 15350, 'als': 1251.60464, 'cct': 3255.1688527256665}

#pink on right bin (red bin)
# left front {'red': 1329, 'green': 1281, 'blue': 702, 'white': 7654, 'als': 322.40208, 'cct': 4857.454232716443}
# right front {'red': 1795, 'green': 1699, 'blue': 697, 'white': 7106, 'als': 427.60432000000003, 'cct': 3431.132395312456}
# right bin {'red': 5539, 'green': 4659, 'blue': 2149, 'white': 14518, 'als': 1172.5771200000001, 'cct': 3177.3024608466053}