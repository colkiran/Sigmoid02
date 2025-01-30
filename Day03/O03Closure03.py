
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

engGrt = outerFun("Hello")

engGrtTgr = engGrt("tiger")

engGrtTgr("Prabhakar")





"""
engGrt = outerFun("Hello")

engGrtSngArw = engGrt("----->")
engGrtDblArw = engGrt("=====>>")

engGrtSngArw("Sachin")
engGrtDblArw("Virat")
"""