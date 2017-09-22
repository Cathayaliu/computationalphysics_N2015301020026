import os
import time
#windows console width
width = 79
#
printedMessage = ["*      ***  *   *  ***   ***  *   *  ***  *   *   *** *   *  *** ",
                  "*       *   *   * *   *   *   *   * *   * *  *   *  * *   * *   *",
                  "*       *   *   * *   *   *   **  * *     * *   *   * **  * *    ",
                  "*       *   *   * *   *   *   * * * *     **    *   * * * * *    ",
                  "*       *   *   * *   *   *   *   * *  ** * *   ***** *   * *  **",
                  "*       *   *   *  ***    *   *   * *   * *  *  *   * *   * *   *",
                  "*****  ***   ***      *  ***  *   *  ***  *   * *   * *   *  *** ",]
#
offset = width
#
while True:
    os.system("cls")
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):width - offset])
        #
    offset -= 1
    if offset <= len(printedMessage[0]) * -1:
        offset = width
    #
    time.sleep(0.05)
    #