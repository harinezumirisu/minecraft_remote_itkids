from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #9  house')

mc.setBlocks(-82, param.Y_SEA + 1, -82,   -2, param.AXIS_TOP,    -2,    param.AIR)

def setPyramid(mc=mc, x=0, z=0, size=3, y=param.Y_SEA + 1, blockTypeId=param.GOLD_BLOCK):
    while size > 0:
        mc.setBlocks(x, y, z, x + size - 1, y, z + size - 1, blockTypeId)
        x += 1
        z += 1
        size -= 2
        y += 1
        sleep(0.01)


setPyramid(x=-83, z=-83, y=param.Y_SEA + 17, size=77, blockTypeId=param.IRON_BLOCK)
setPyramid(x=-82, z=-82, y=param.Y_SEA + 17, size=75, blockTypeId=param.SHROOMLIGHT)
setPyramid(x=-81, z=-81, y=param.Y_SEA + 17, size=73, blockTypeId=param.AIR)

mc.setBlocks(-80, param.Y_SEA + 1, -80,   -10, param.Y_SEA+9,    -10,    param.IRON_BLOCK)
mc.setBlocks(-79, param.Y_SEA + 2, -79,   -11, param.Y_SEA+9,    -11,    param.AIR)
mc.setBlocks(-79, param.Y_SEA + 1, -79,   -11, param.Y_SEA+1,    -11,    param.SHROOMLIGHT)
mc.setBlocks(-80, param.Y_SEA + 10, -80,   -10, param.Y_SEA+18,    -10,    param.IRON_BLOCK)
mc.setBlocks(-79, param.Y_SEA + 11, -79,   -11, param.Y_SEA+18,    -11,    param.AIR)
mc.setBlocks(-79, param.Y_SEA + 10, -79,   -11, param.Y_SEA+10,    -11,    param.SHROOMLIGHT)
mc.setBlocks(-71, param.Y_SEA + 19, -71,   -19, param.Y_SEA+27,    -19,    param.IRON_BLOCK)
mc.setBlocks(-70, param.Y_SEA + 20, -70,   -20, param.Y_SEA+27,    -20,    param.AIR)
mc.setBlocks(-79, param.Y_SEA + 19, -79,   -11, param.Y_SEA+19,    -11,    param.SHROOMLIGHT)
mc.setBlocks(-62, param.Y_SEA + 28, -62,   -28, param.Y_SEA+36,    -28,    param.IRON_BLOCK)
mc.setBlocks(-61, param.Y_SEA + 29, -61,   -29, param.Y_SEA+36,    -29,    param.AIR)
mc.setBlocks(-71, param.Y_SEA + 28, -71,   -19, param.Y_SEA+28,    -19,    param.SHROOMLIGHT)
mc.setBlocks(-53, param.Y_SEA + 37, -53,   -37, param.Y_SEA+45,    -37,    param.IRON_BLOCK)
mc.setBlocks(-52, param.Y_SEA + 38, -52,   -38, param.Y_SEA+45,    -38,    param.AIR)
mc.setBlocks(-62, param.Y_SEA + 37, -62,   -28, param.Y_SEA+37,    -28,    param.SHROOMLIGHT)

def setStep(mc=mc, x=0, z=0, size=3, high=3, y=param.Y_SEA + 1, blockTypeId=param.IRON_BLOCK):
    while high > 0:
        mc.setBlocks(x, y, z, x, y, z + size, blockTypeId)
        x -= 1
        high -= 1
        y += 1
        sleep(0.01)

if __name__ == "__main__":
    setStep(x=-16, z=-79,y=param.Y_SEA +2, size=4, high=9, blockTypeId=param.SHROOMLIGHT)
    setStep(x=-20, z=-70,y=param.Y_SEA +11, size=4, high=9, blockTypeId=param.SHROOMLIGHT)
    setStep(x=-29, z=-61,y=param.Y_SEA +20, size=4, high=9, blockTypeId=param.SHROOMLIGHT)
    setStep(x=-38, z=-52,y=param.Y_SEA +29, size=4, high=9, blockTypeId=param.SHROOMLIGHT)

mc.setBlocks(-23, param.Y_SEA + 10, -75,   -11, param.Y_SEA+10,    -79,    param.AIR)
mc.setBlocks(-27, param.Y_SEA + 19, -66,   -20, param.Y_SEA+19,    -70,    param.AIR)
mc.setBlocks(-36, param.Y_SEA + 28, -57,   -29, param.Y_SEA+28,    -61,    param.AIR)
mc.setBlocks(-45, param.Y_SEA + 37, -48,   -38, param.Y_SEA+37,    -52,    param.AIR)

mc.setBlocks(-10, param.Y_SEA + 2, -10,   -11, param.Y_SEA + 3,    -11,    param.AIR)
