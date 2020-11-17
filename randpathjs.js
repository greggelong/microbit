let x = 0
let y = 0
basic.forever(function () {
    led.plot(x, y)
    basic.pause(200)
    if (x < 4 && y < 4) {
        if (Math.randomBoolean()) {
            x += 1
        } else {
            y += 1
        }
    } else if (x == 4 && y < 4) {
        y += 1
    } else if (y == 4 && x < 4) {
        x += 1
    } else {
        basic.clearScreen()
        x = 0
        y = 0
    }
})
