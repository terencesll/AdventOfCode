#import bfs
import copy

class State:
    def __init__(self, elev, stateVec):
        self.elev = elev
        self.stateVec = stateVec
        self.stateVec.sort()
        self.numMetal = len(stateVec)

    def states1(self, fromFloor, toFloor):
        ret = set()
        for i in range(self.numMetal):
            for j in range(2):
                if self.stateVec[i][j] == fromFloor:
                    newStateVec = copy.deepcopy(self.stateVec)
                    newStateVec[i] = (newStateVec[i][0], toFloor) if j == 1 else (toFloor, newStateVec[i][1])
                    print(newStateVec)
                    newStateVec.sort()
                    ret.add(newStateVec)
        return ret

    def __repr__(self):
        return str(self.elev) + ": " + str(self.stateVec)

thisState = State(1, [(2,1), (3,1)])
print(thisState)
print(thisState.states1(1,2))
